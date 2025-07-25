


class FileLoader:
    def __init__(self):
        self.line_length = None
    def validate_insruction(self, line: str) -> str | None:
        try:
            instruction = int(line)
            stripped_line = line.strip()
            for character in ["+","-","\n"]:
                stripped_line = stripped_line.replace(character, "")
            if self.line_length is None:
                self.line_length = len(stripped_line)
                if self.line_length not in [4,6]:
                    return f"Length of operations must either 4 or 6, not {self.line_length}"
            else:
                if len(stripped_line) != self.line_length:
                    return "Length of operations is mismatched, please use either 4 or 6 length operations for the whole program"

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
                validated_instructions.append(instruction.strip())
                if len(validated_instructions) > 250:
                    return None, "Program exceeds max length of 250 lines, please shorten it."
                    
        return validated_instructions, None
