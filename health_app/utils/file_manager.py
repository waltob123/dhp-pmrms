import json
import os

class FileManager:
    """
    Handles file operations such as reading and writing JSON data.
    """
    def __init__(self, file_path):
        """Initialize file manager and ensure file exists."""
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def read_data(self):
        """Read data from JSON file."""
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def write_data(self, data):
        """Write data to JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)