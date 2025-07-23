


class FileLoader:
    @staticmethod
    def validate_insruction(line: str) -> str | None:
        try:
            instruction = int(line)
            if instruction > 999999 or instruction < -999999:
                raise Exception
            return None
        except:
            return f"Invalid instruction {line}, must be a value between -999999 and +999999"

    def load_file(self, path: str) -> tuple[list[int], str]:
        validated_instructions = []
        with open(path, "r") as file:
            for instruction in file.readlines():
                error = self.validate_insruction(instruction)
                if error:
                    return None, error
                validated_instructions.append(int(instruction))
                if len(validated_instructions) > 250:
                    return None, "Program exceeds max length of 250 lines, please shorten it."
                    
        return validated_instructions, None
