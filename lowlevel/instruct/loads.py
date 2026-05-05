import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

# 8-bit loads
def ld_addr_reg(dest,src,inc=0): # ld [bc], a
    addr = dest.hi.hget(True) + dest.lo.hget(True)
    memory.set(addr,src.hget())
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_addr(dest,src,inc=0): # ld a, [bc]
    addr = src.hi.hget(True) + src.lo.hget(True)
    dest.set(memory.get(addr))
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_arg(dest):          # ld b, n8
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    dest.set(src)
    timer.tick(8)
def ld_addr_arg(): 
    addr = rg.HL.hi.hget(True) + rg.HL.lo.hget(True)
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    memory.set(addr,src)
    timer.tick(12)
def ld_reg_reg(dest,src):          # ld b, b
    dest.set(src.hget())
    timer.tick(4)
def ld_addr_a():
    addr1 = memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    addr2 = memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    addr = addr1 + addr2
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(16)
def ld_a_addr():
    addr1 = memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    addr2 = memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    addr = addr1 + addr2
    rg.AF.hi.set(memory.get(addr))
    timer.tick(16)
def ldh_addr_a():
    addr = 'FF' + memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(12)
def ldh_a_addr():
    addr = 'FF' + memory.get(rg.pc.iget()).hget(True)
    rg.pc.inc()
    rg.AF.hi.set(memory.get(addr))
    timer.tick(12)
def ldh_c_a():
    addr = 'FF' + rg.BC.lo.hget().hget(True)
    memory.set(addr,rg.AF.hi.hget())
    timer.tick(8)
def ldh_a_c():
    addr = 'FF' + rg.BC.lo.hget().hget(True)
    rg.AF.hi.set(memory.get(addr))
    timer.tick(8)
