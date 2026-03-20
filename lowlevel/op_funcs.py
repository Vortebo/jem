import lowlevel.registers as rg
from lowlevel.hex_ops import HexValue, Register
from lowlevel.memory import memory

def jp(dest):
    rg.pc.set(dest)
def jr(dest):
    jp(dest)