import lowlevel.registers as rg
from lowlevel.hex_ops import HexValue, Register
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

# Jumps
def jp_addr():
    dest = rom.get() + rom.get()
    rg.pc.set(dest)
    timer.tick(16)
def jr():
    jp_addr()

# 8-bit loads
def ld_addr_reg(dest,src,inc=0): # ld [bc], a
    addr = dest.hi.hget() + dest.lo.hget()
    memory.set(addr,src.hget())
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_addr(dest,src,inc=0): # ld a, [bc]
    addr = src.hi.hget() + src.lo.hget()
    dest.set(memory.get(addr))
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_arg(dest):          # ld b, n8
    src = rom.get()
    dest.set(src)
    timer.tick(8)
def ld_addr_arg(): 
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    src = rom.get()
    memory.set(addr,src)
    timer.tick(12)
def ld_reg_reg(dest,src):          # ld b, b
    dest.set(src.hget())
    timer.tick(4)
def ld_addr_a():
    addr = rom.get() + rom.get()
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(16)
def ld_a_addr():
    addr = rom.get() + rom.get()
    rg.AF.hi.set(memory.get(addr))
    timer.tick(16)
def ldh_addr_a():
    addr = 'FF' + rom.get()
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(12)
def ldh_a_addr():
    addr = 'FF' + rom.get()
    rg.AF.hi.set(memory.get(addr))
    timer.tick(12)
def ldh_c_a():
    addr = 'FF' + rg.BC.lo.hget()
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(8)
def ldh_a_c():
    addr = 'FF' + rg.BC.lo.hget()
    rg.AF.hi.set(memory.get(addr))
    timer.tick(8)
