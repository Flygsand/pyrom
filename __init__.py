from parsers import parse as _parse

def read(path):
    with open(path) as f:
        return _parse(f)

