import os, hashlib
from pyrom.auxiliaries import uniq as _uniq
from . import genesis, snes, nes

_parsers = {'bin': genesis,
            'smd': genesis,
            'md': genesis,
            'smc': snes,
            'nes': nes
            }

_parse_attempts = 0

def parse(f):
    ext = os.path.splitext(f.name)[1][1:]
    first_parser = _parsers.get(ext.lower(), None)
    parser_list = _parsers.values()

    if first_parser:
        parser_list.insert(0, first_parser)

    global _parse_attempts
    _parse_attempts = 0

    data = f.read()
    for p in _uniq(parser_list):
        _parse_attempts += 1
        try:
            rom = p.parse(data)
            if not rom.name:
                rom.name = os.path.basename(f.name)
            rom.hsh = hashlib.sha1(data).hexdigest()
            return rom
        except ValueError:
            pass
    else:
        raise ValueError('%s is not a supported ROM type' % f.name)
