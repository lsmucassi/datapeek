import sys
import json
from colors import Colors

class Printer:
    colors = Colors()
    message_types = [
        "ERROR",
        "WARN",
        "INFO",
        "GENERAL"
    ]
    data_types = [
        "list",
        "str",
        "tuple",
        "bool",
        "memoryview",
        "bytearray",
        "bytes",
        "frozenset",
        "dict",
        "range",
        "complex",
        "float",
        "int"
    ]

    def print_data(self, data):
        try:
            if type(data) in self.data_types:
                if isinstance(data, memoryview):
                    return str(list(data))
                elif isinstance(data, bytearray):
                    return str(data.hex)
                elif isinstance(data, bytes):
                    x = bytes.fromhex(data)
                    return str(sys.stdout.buffer.write(x))
                elif isinstance(data, dict):
                    parsed = json.loads(data)
                    return json.dumps(parsed, indent=4, sort_keys=True)
                elif isinstance(data, range):
                    return str(list(data))
                else:
                    return str(data)
            else:
                return str(data)
        except TypeError as e:
            print(f"\x1b[{self.colors.get_cformat(self.message_types[3])}m {message_type} \x1b[0m: {message}\n {e}")

    def log_message(self, message_type, message, data=""):
        try:
            message = str(message)
            if message_type in self.message_types:
                print(f"\x1b[{self.colors.get_cformat(message_type)}m {message_type} \x1b[0m: {message} {self.print_data(data)}")
            else:
                print(f"\x1b[{self.colors.get_cformat(self.message_types[3])}m {message_type} \x1b[0m: {message} {self.print_data(data)}")
        except TypeError as e:
            print(f"\x1b[{self.colors.get_cformat(self.message_types[3])}m {message_type} \x1b[0m: {message}\n {e}")