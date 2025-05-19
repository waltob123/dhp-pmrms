import json
import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def read_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def write_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

