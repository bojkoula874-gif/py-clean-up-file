import os
os.remove("file.txt")


class CleanUpFile:
    def __init__(self, path: str) -> None:
        self.path = path

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self) -> None:
        os.remove(f"{self.path}")
