


class FileLoader:
    @staticmethod
    def validate_insruction(line: str) -> None:
        try:
            instruction = int(line)
            if instruction > 9999 or instruction < -9999:
                raise Exception
        except:
            raise ValueError(f"Invalid instruction {line}, must be a value between -9999 and +9999")

    def load_file(self, path: str) -> list[int]:
        validated_instructions = []
        with open(path, "r") as file:
            for instruction in file.readlines():
                self.validate_insruction(instruction)
                validated_instructions.append(int(instruction))
                    

        return validated_instructions
