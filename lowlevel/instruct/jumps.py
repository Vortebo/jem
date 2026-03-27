import lowlevel.registers as rg
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.memory import memory

# Jumps
def jp_addr():
    dest1 = memory.get(rg.pc.iget())
    rg.pc.inc()
    dest2 = memory.get(rg.pc.iget())
    rg.pc.inc()
    dest = dest1 + dest2
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()
