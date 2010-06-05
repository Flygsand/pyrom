from pyrom.entities import ROM as _ROM
from pyrom.auxiliaries import sub as _sub, unpack as _unpack

def _deinterleave_bytes(data):
    data_len = len(data)
    middle = data_len/2
    deinterleaved = [0]*data_len
    for i in xrange(middle):
        deinterleaved[i*2+1] = data[i]
    for i in xrange(middle, data_len):
        deinterleaved[(i-middle)*2] = data[i]

    return ''.join(deinterleaved)

def _deinterleave_smd(data):
    block_count = len(data) / 16384
    blocks = [_deinterleave_bytes(_sub(data, i*16384, 16384)) for i in xrange(block_count)]
    return ''.join(blocks)

def _valid_rom_info(data):
    console = _sub(data, 0x100, 16).strip()
    return console == 'SEGA MEGA DRIVE' or console == 'SEGA GENESIS'

def parse(data):
    
    if not _valid_rom_info(data):
        if len(data) % 16384 != 0:
            # SMD, omit 512B external header and deinterleave first block
            data = data[512:]
            data = _deinterleave_smd(data)    
        else:
            # MD, deinterleave entire ROM
            data = _deinterleave_bytes(data)
            
        if not _valid_rom_info(data):
            raise ValueError

    name = ' '.join(_sub(data, 0x150, 48).split())
    version = _sub(data, 0x182, 12).replace(' ', '')
    rom_start = _unpack(_sub(data, 0x1a0, 4))
    rom_end = _unpack(_sub(data, 0x1a4, 4))
    ram_start = _unpack(_sub(data, 0x1b4, 4))
    ram_end = _unpack(_sub(data, 0x1b8, 4))
    country = _sub(data, 0x1f0, 16).strip()
    return _ROM(name,
                rom_size=(rom_end-rom_start+1)/1024,
                ram_size=(ram_end-ram_start+1)/1024,
                country=country,
                version=version)
  
