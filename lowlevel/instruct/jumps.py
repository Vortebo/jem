import lowlevel.registers as rg
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

# Jumps
def jp_addr():
    dest = rom.get() + rom.get()
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()
