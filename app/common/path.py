import os

from platformdirs import PlatformDirs

from app.common.logger import _logger
from app.common.meta import SingletonMeta

APP_NAME = "App"
AUTHOR = "Aurelien ROY"
CONFIG_FILENAME = "config.json"
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = False


class Path(metaclass=SingletonMeta):
    def __init__(self, app_name, author, config_filename):
        self._dirs = PlatformDirs(app_name, author)
        self.config_filename = config_filename

        self._make_dirs()

    @property
    def root_dir(self):
        """Root directory."""

        return os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

    @property
    def config_dir(self):
        """Configuration directory."""

        return self._dirs.user_data_dir

    @property
    def config_filepath(self):
        """Configuration filepath."""

        return os.path.join(self.config_dir, self.config_filename)

    def _make_dirs(self):
        os.makedirs(self.config_dir, exist_ok=True)
        _logger.debug("Config dir: %s", self.config_dir)


path = Path(APP_NAME, AUTHOR, CONFIG_FILENAME)
