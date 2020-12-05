from typing import List
from pathlib import Path

class Parser:
    extensions = []

    def __init__(extensions: List[str]):

    def valid_extension(extension):
        return extension in self.extensions

    def parse(path, source, dest):
        raise NotImplementedError

    def read(path):
        with open(path, 'r') as file:
            return file.read()

    def write(path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext)
        with open(full_path, 'w') as file:
            file.write(content)