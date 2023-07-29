import json
import subprocess

from app.common.logger import _logger

DEFAULT_ENCODING = "utf8"


def save_to(data, filepath):
    """Save content to filepath."""

    with open(filepath, "w+", encoding=DEFAULT_ENCODING) as file:
        file.write(data)


def abort_if_false(ctx, _, value):
    """Confirm: Abort if false."""

    if not value:
        ctx.abort()


def run_external_command(cmd, **kwargs):
    """Run system command and return result."""

    result = kwargs.pop("result", True)

    if isinstance(cmd, str):
        cmd = cmd.split(" ")

    try:
        if result:
            res = subprocess.check_output(cmd, **kwargs)
        else:
            subprocess.call(cmd, **kwargs)
            res = True
    except FileNotFoundError as error:
        _logger.error(error)
        return False

    return res


def nested_set(dic, keys, value):
    """Update nested dict."""
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def dict_merge(dct, merge_dct):
    """Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    for key, _ in merge_dct.items():
        if (
            key in dct
            and isinstance(dct[key], dict)
            and isinstance(merge_dct[key], dict)
        ):  # noqa
            dict_merge(dct[key], merge_dct[key])
        else:
            dct[key] = merge_dct[key]


def convert_stdout_to_json(content):
    """Convert stdout bytes to json array."""

    try:
        data = json.loads(content)
    except json.decoder.JSONDecodeError:
        content = content.decode("utf8")
        content = content.strip().rstrip().lstrip()
        content = f"[{content}]"
        content = content.replace("}", "},").replace("},]", "}]")

        data = json.loads(content)

    return data
