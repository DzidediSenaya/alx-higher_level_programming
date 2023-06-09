#!/usr/bin/python3
import dis

if __name__ == "__main__":
    def print_hidden_names():
        with open("hidden_4.pyc", "rb") as file:
            magic = file.read(4)
            timestamp = file.read(4)
            dis_header_size = file.read(4)

            while True:
                op = file.read(2)
                if not op:
                    break

                arg = file.read(4)
                arg_value = int.from_bytes(arg, byteorder="little")

                if op == b"\x01\x00":  # LOAD_CONST opcode
                    const = dis.get_instructions("", b"\x01\x00" + arg)
                    const_op = next(const)
                    const_value = const_op.argval

                    if isinstance(const_value, str) and not const_value.startswith("__"):
                        print(const_value)

    print_hidden_names()
