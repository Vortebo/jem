# Josh's Cool Gameboy Emulator
# import numpy as np
# from lowlevel.hex_ops import HexValue, Register
import registers as rg
from lowlevel.rom_handler import rom
from bootrom.bootrom import boot_rom

def main():
    # load rom
    with open('pokegold.gbc',mode='rb') as file:
        rom.load_rom(file.read())

    boot_flags = boot_rom(rom)

if __name__ == "__main__":
    main()