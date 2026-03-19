# Josh's Cool Gameboy Emulator
# import numpy as np
from hex_ops import HexValue
from bootrom.bootrom import boot_rom

pc = HexValue('0')

def main():
    # load rom
    rom = None
    with open('pokegold.gbc',mode='rb') as file:
        rom = file.read()

    global pc
    boot_flags = boot_rom(rom)

if __name__ == "__main__":
    main()