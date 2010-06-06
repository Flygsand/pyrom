class ROM(object):
    def __init__(self, name, console, **kwargs):
        self.name = name
        self.console = console
        self.hsh = kwargs.pop('hsh', None)
        self.rom_size = kwargs.pop('rom_size', None)
        self.ram_size = kwargs.pop('ram_size', None)
        self.country = kwargs.pop('country', None)
        self.region = kwargs.pop('region', None)
        self.version = kwargs.pop('version', None)
        if kwargs:
            raise ValueError('Unknown parameter(s): %s' % ''.join(kwargs.keys()))
