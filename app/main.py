import os
from warnings import catch_warnings

os.remove("file.txt")


class CleanUpFile:
    def __init__(self, path: str) -> None:
        self.path = path

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self) -> None:
        try:
            os.remove(self.path)
        except FileNotFoundError:
            return
