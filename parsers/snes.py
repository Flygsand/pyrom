from pyrom.entities import ROM as _ROM
from pyrom.auxiliaries import unpack as _unpack, sub as _sub

_countries = ['Japan', 'USA', 'Australia, Europe, Oceania and Asia',
               'Sweden', 'Finland', 'Denmark', 'France', 'Holland',
               'Spain', 'Germany, Austria and Switzerland', 'Italy',
               'Hong Kong and China', 'Indonesia', 'Korea']

def _country_and_region(code):
    if code == 0x0 or code == 0x1 or code == 0xd:
        return (_countries[code], 'NTSC')
    elif code >= 0x2 and code <= 0xc:
        return (_countries[code], 'PAL')
    else:
        return ('Invalid', 'Invalid')

def _checksum_heuristic(data, hdr):
    chksum_cpl = _unpack(_sub(data, hdr+0x1c, 2))
    chksum = _unpack(_sub(data, hdr+0x1e, 2))
    return chksum_cpl ^ chksum == 0xffff

def _has_lorom_makeup(data, hdr):
    l_nibble = _unpack(_sub(data, hdr+0x15, 1)) & 0xf
    return l_nibble % 2 == 0

def _find_header_address(data):
    hdr = 0x7fc0
    if _checksum_heuristic(data, hdr):
        # either original LoROM or interleaved HiROM
        return hdr
    
    hdr = 0xffc0
    if _checksum_heuristic(data, hdr) and \
        not _has_lorom_makeup(data, hdr):
         # original HiROM
         return hdr

    hdr = len(data) / 65536 # middle 32KB block
    if _checksum_heuristic(data, hdr) and \
        _has_lorom_makeup(data, hdr):
        # interleaved LoROM
        return hdr

    raise ValueError
 
def parse(data):
        
    # omit 512B external header
    if len(data) % 32768 != 0:
        data = data[512:]
            
    # find 64B internal header address
    hdr = _find_header_address(data)
                
    name = _sub(data, hdr, 21).strip()
    rom_byte = ord(data[hdr+0x17])
    rom_size = 1 << rom_byte if rom_byte > 0 else 0
    ram_byte = ord(data[hdr+0x18])         
    ram_size = 1 << ram_byte if ram_byte > 0 else 0
    ccode = ord(data[hdr+0x19])
    country, region = _country_and_region(ccode)
    version = '1.%d' % ord(data[hdr+0x1b])        
    return _ROM(name,
                'SNES',
                rom_size=rom_size,
                ram_size=ram_size,
                country=country,
                region=region,
                version=version)
