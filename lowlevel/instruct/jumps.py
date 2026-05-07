import lowlevel.registers as rg
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.memory import memory

# Jumps
def jp_addr():
    dest1 = memory.get(rg.pc)
    rg.pc.inc()
    dest2 = memory.get(rg.pc)
    rg.pc.inc()
    dest = dest2.hget(True) + dest1.hget(True) # little endian.
    print('destination is',dest)
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()
