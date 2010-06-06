from pyrom.auxiliaries import sub as _sub, unpack as _unpack
from pyrom.entities import ROM as _ROM

def parse(data):
    if _sub(data, 0x0, 4) != 'NES\x1a':
        raise ValueError

    if len(data) % 8192 != 16:
        name = _sub(data, len(data)-128, 128).replace('\x00', '')
    else:
        name = None

    num_rom_banks = _unpack(_sub(data, 0x4, 1))
    num_vrom_banks = _unpack(_sub(data, 0x5, 1))
    rom_size = 16*num_rom_banks + 8*num_vrom_banks
    num_ram_banks = _unpack(_sub(data, 0x8, 1))
    ram_size = 8*num_ram_banks

    return _ROM(name,
                'NES',
                rom_size=rom_size,
                ram_size=ram_size)
                    
