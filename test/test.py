"""
Due to copyright restrictions, the ROMs used for
these tests cannot be distributed with the source.
A table of these ROMs is provided below.

| Filename   | ROM name                     | ROM type    | SHA1              |
|------------+------------------------------+-------------+-------------------|
| sc4.smc    | Super Castlevania IV (E) [!] | SNES LoROM  | 554e22380e25a5... |
| smk.SMC    | Super Mario Kart (U) [!]     | SNES HiROM  | 47e103d8398cf5... |
| sonic3.bin | Sonic the Hedgehog 3 (J) [!] | Genesis RAW | 7b98b21b727423... |
| sonic3.smd | Sonic the Hedgehog 3 (J) [!] | Genesis SMD | f6d76027eab012... |
| sonic3.md  | Sonic the Hedgehog 3 (J) [!] | Genesis MD  | 42c1d364b50dd7... |
| smb        | Super Mario Bros. (JU) [o1]  | NES iNES    | 77fb3f0c2d2179... |
| mm2.nes    | Mega Man 2 (E) [!]           | NES iNES    | a9daff94a80062... |
"""

import sys, os, unittest, fixtures, pyrom

class TestParse(unittest.TestCase):
    def test_valid_roms(self):
        for fname, exp in fixtures.ROMS.iteritems():
            ext = os.path.splitext(fname)[1][1:]
            got = pyrom.read('test/data/%s' % fname)
            self.assertEqual(got.name, exp['name'])
            self.assertEqual(got.rom_size, exp['rom_size'])
            self.assertEqual(got.country, exp['country'])
            self.assertEqual(got.region, exp['region'])
            self.assertEqual(got.version, exp['version'])
            self.assertTrue(ext == '' or pyrom.parsers._parse_attempts == 1)
            sys.stderr.write('%sOK\n' % fname.ljust(30))

    def test_invalid_rom(self):
        # test/data/random_crap is just data from /dev/urandom
        self.assertRaises(ValueError, pyrom.read, 'test/data/random_crap')
