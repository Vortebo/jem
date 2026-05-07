# Josh's Cool Gameboy Emulator
# import numpy as np
# from lowlevel.hex_ops import HexValue, Register
import lowlevel.registers as rg
from lowlevel.rom_handler import rom
from bootrom.bootrom import boot_rom
from lowlevel.op_codes import optable
from lowlevel.memory import memory

def main():
    # load rom
    with open('Tetris.gb',mode='rb') as file:
        rom.load_rom(file.read())

    # boot_flags = boot_rom()
    rg.pc.set('0100')

    for i in range(20):
        print(f'getting opcode from 0x{rg.pc.value}')
        op = memory.get(rg.pc).hget()
        rg.pc.inc()
        print('retrieved opcode is ',op)
        optable[op]()

if __name__ == "__main__":
    main()