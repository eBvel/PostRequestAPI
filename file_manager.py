

class FileManager:
    @staticmethod
    def write(file_path: str, data: str, encoding: str = "UTF-8") -> None:
        try:
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(data)
        except FileNotFoundError as e:
            print(f"ERROR: File not found. \n{e}")

    @staticmethod
    def read_line_by_line(file_path: str,
                          encoding: str = "UTF-8") -> list[str] | None:
        try:
            result = []
            with open(file_path, 'r', encoding=encoding) as file:
                for line in file:
                    result.append(line.strip())
            return result
        except FileNotFoundError as e:
            print(f"ERROR: File not found. \n{e}")
            return None