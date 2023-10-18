import json

class FileHandler:
    def __init__(self, input_path: str, output_file: str) -> None:
        self.file_path = input_path
        self.output_file = output_file
        self.data = self.load_data()

    def load_data(self) -> dict:
        with open(self.file_path, 'r') as f:  data = json.load(f)
        return data

    def save(self, data) -> None:
        with open(self.output_file, 'w') as f: json.dump(data, f,indent=4)