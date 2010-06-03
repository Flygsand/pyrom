"""
Due to copyright restrictions, the ROMs used for
these tests cannot be distributed with the source.
A table of these ROMs is provided below.

| Filename  | ROM name                     | ROM type    |
|-----------+------------------------------+-------------|
| sc4.smc   | Super Castlevania IV (E) [!] | SNES LoROM  |
| smk.SMC   | Super Mario Kart (U) [!]     | SNES HiROM  |
| sonic3.bin | Sonic the Hedgehog 3 (J) [!] | Genesis RAW |
| sonic3.smd | Sonic the Hedgehog 3 (J) [!] | Genesis SMD |
| sonic3.md | Sonic the Hedgehog 3 (J) [!] | Genesis MD  |
"""

import unittest, fixtures, pyrom

class TestParse(unittest.TestCase):
    def testparse(self):
        for fname, exp in fixtures.ROMS.iteritems():
            got = pyrom.parse('test/data/%s' % fname)
            self.assertEqual(got.name, exp['name'])
            self.assertEqual(got.rom_size, exp['rom_size'])
            self.assertEqual(got.country, exp['country'])
            self.assertEqual(got.region, exp['region'])
            self.assertEqual(got.version, exp['version'])
        
