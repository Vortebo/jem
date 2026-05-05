import lowlevel.registers as rg
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.memory import memory

# Jumps
def jp_addr():
    dest1 = memory.get(rg.pc.hget())
    rg.pc.inc()
    dest2 = memory.get(rg.pc.hget())
    rg.pc.inc()
    dest = dest1.hget() + dest2.hget()
    print('destination is',dest)
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()
