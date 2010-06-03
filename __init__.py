import os, auxiliaries
from parsers import genesis, snes

_parsers = {'bin': genesis,
            'smd': genesis,
            'md': genesis,
            'smc': snes
            }

def parse(path):
    dontcare, ext = os.path.splitext(path)
    first_parser = _parsers.get(ext.lower(), None)
    parser_list = _parsers.values()

    if first_parser:
        parser_list.insert(0, first_parser)

    for p in auxiliaries.uniq(parser_list):
        r = p.parse(path)
        if r:
            return r

    raise ValueError('Path is not a support ROM type')
