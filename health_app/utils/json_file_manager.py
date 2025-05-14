import json
from pathlib import Path

from health_app.utils.file_manager import FileManager


class JSONFileManager(FileManager):
    """
    A class to manage JSON file operations such as reading and writing JSON files.

    (FileManager) This class inherits from the FileManager class and implements the abstract methods
    """

    def __init__(self, *, file_path: Path) -> None:
        """
        Initializes the JSONFileManager with a file path.

        :param file_path: The path to the JSON file to be managed.
        """
        super().__init__(file_path=file_path)

    def read_file(self) -> list[dict]:
        """
        Reads the JSON file and returns its content.

        :return: The content of the JSON file.
        """
        with open(self._file_path, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return []


    def write_file(self, *, content: list[dict]) -> None:
        """
        Writes the content to the JSON file.

        :param content: The content to be written to the JSON file.
        :return:
        """
        with open(self._file_path, "w") as file:
            json.dump(content, file, indent=4)  # type: ignore
