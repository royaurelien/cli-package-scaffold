import click

from app.core.settings import get_settings

settings = get_settings()  # pylint: disable=C0413

import app.cli.group_1 as gp1  # noqa: E402

if not settings.is_ready and settings.ask_to_user:
    click.echo("Please fill configuration to continue :")
    settings.user_prompt()


@click.group()
def cli():
    """CLI App"""


@click.group()
def group_1():
    """Group 1"""


group_1.add_command(gp1.command_1)
group_1.add_command(gp1.command_2)

cli.add_command(group_1)
