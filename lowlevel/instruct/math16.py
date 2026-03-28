import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

def inc_reg(reg):
    reg.inc()
    timer.tick(8)
def dec_reg(reg):
    reg.dec()
    timer.tick(8)