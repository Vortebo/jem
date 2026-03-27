# Josh's Cool Gameboy Emulator
# import numpy as np
# from lowlevel.hex_ops import HexValue, Register
import lowlevel.registers as rg
from lowlevel.rom_handler import rom
from bootrom.bootrom import boot_rom
from lowlevel.op_codes import optable

def main():
    # load rom
    with open('Tetris.gb',mode='rb') as file:
        rom.load_rom(file.read())

    boot_flags = boot_rom()

    print(rg.pc.value)
    for i in range(300):
        optable[rom.getNext()]()
        print(rg.pc.value)

if __name__ == "__main__":
    main()