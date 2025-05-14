from abc import abstractmethod
from pathlib import Path
from typing import Any


class FileManager:
    """
    A class to manage file operations such as reading and writing files.
    """

    def __init__(self, *, file_path: Path) -> None:
        """
        Initializes the FileManager with a file path.

        :param file_path: The path to the file to be managed.
        """
        self._file_path = self.__set_file_path(file_path=file_path)

    @abstractmethod
    def read_file(self) -> list[dict]:
        """
        Abstract method to read the file.

        :return: The content of the file.
        """
        pass

    @abstractmethod
    def write_file(self, *, content: Any) -> None:
        """
        Abstract method to write to the file.

        :param content: The content to be written to the file.
        """
        pass

    @property
    def file_path(self) -> Path:
        """
        Property to get the file path.

        :return: The file path.
        """
        return self._file_path

    @staticmethod
    def __set_file_path(*, file_path: Path) -> Path:
        """
        Sets the file path.

        :param file_path: The path to the file to be managed.
        :return: The file path.
        """
        if not file_path.exists():
            file_path.touch()
        return file_path
