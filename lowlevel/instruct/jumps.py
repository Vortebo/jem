import lowlevel.registers as rg
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.memory import memory

# Jumps
def jp_addr():
    dest = memory.getNext() + memory.getNext()
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()
