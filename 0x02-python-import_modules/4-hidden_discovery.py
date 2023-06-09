#!/usr/bin/python3
import types
import hidden_4

if __name__ == "__main__":
    names = [name for name, value in vars(hidden_4).items()
             if not name.startswith("__") and
             not isinstance(value, types.ModuleType)]
    for name in names:
        print(name)
