# Josh's Cool Gameboy Emulator
# import numpy as np
from lowlevel.hex_ops import HexValue
from lowlevel.rom_handler import ROM
from bootrom.bootrom import boot_rom

def main():
    # load rom
    rom = None
    with open('pokegold.gbc',mode='rb') as file:
        rom = ROM(file.read())

    pc = HexValue('0')
    pc, boot_flags = boot_rom(rom, pc)

if __name__ == "__main__":
    main()