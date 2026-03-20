import lowlevel.registers as rg
from lowlevel.hex_ops import HexValue, Register
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

def jp(dest):
    rg.pc.set(dest)
def jr(dest):
    jp(dest)

def ld_addr_a(dest,inc=0,elaps=8): # ld [bc], a
    addr = dest.hi.hget() + dest.lo.hget()
    memory.set(addr,rg.AF.hi.hget())
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(elaps)
def ld_a_addr(dest,inc=0,elaps=8): # ld a, [bc]
    addr = dest.hi.hget() + dest.lo.hget()
    rg.AF.hi.set(memory.get(addr))
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(elaps)
def ld_reg_arg(dest,elaps=8):          # ld b, n8
    src = rom.get()
    dest.set(src)
    timer.tick(elaps)
def ld_addr_arg(): # ld [bc], a
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    src = rom.get()
    memory.set(addr,src)
    timer.tick(12)