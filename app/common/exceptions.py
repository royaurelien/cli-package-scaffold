class ExternalDependenciesMissing(Exception):
    """Exception raised for system package missing ."""

    def __init__(self, name):
        self.name = name
        self.message = f"System package missing, please install {name} first."
        super().__init__(self.message)


class CommandNotImplemented(NotImplementedError):
    """Exception raised for CLI command not implemented."""

    def __init__(self, name):
        self.name = name
        self.message = f"The {name} command is not yet implemented."
        super().__init__(self.message)
