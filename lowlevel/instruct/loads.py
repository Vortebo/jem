import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.hex_ops import HexValue, Register

# 8-bit loads
def ld_addr_reg(dest: Register,src,inc=0): # ld [bc], a
    addr = dest.address()
    memory.set(addr,src.iget())
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_addr(dest,src: Register,inc=0): # ld a, [bc]
    addr = src.address()
    dest.set(memory.get(addr))
    if inc==1:
        rg.HL.inc()
    elif inc==-1:
        rg.HL.dec()
    timer.tick(8)
def ld_reg_arg(dest):          # ld b, n8
    src = memory.get(rg.pc)
    rg.pc.inc()
    dest.set(src.hget())
    timer.tick(8)
def ld_addr_arg(): 
    addr = rg.HL.address()
    src = memory.get(rg.pc)
    rg.pc.inc()
    memory.set(addr,src.iget())
    timer.tick(12)
def ld_reg_reg(dest,src):          # ld b, b
    dest.set(src.hget())
    timer.tick(4)
def ld_addr_a():
    addr1 = memory.get(rg.pc).hget(True)
    rg.pc.inc()
    addr2 = memory.get(rg.pc).hget(True)
    rg.pc.inc()
    addr = HexValue(addr1 + addr2)
    memory.set(addr,rg.AF.hi.iget())
    timer.tick(16)
def ld_a_addr():
    addr1 = memory.get(rg.pc).hget(True)
    rg.pc.inc()
    addr2 = memory.get(rg.pc).hget(True)
    rg.pc.inc()
    addr = HexValue(addr1 + addr2)
    rg.AF.hi.set(memory.get(addr).hget())
    timer.tick(16)
def ldh_addr_a():
    addr = HexValue('FF' + memory.get(rg.pc).hget(True))
    rg.pc.inc()
    memory.set(addr,rg.AF.hi.iget())
    timer.tick(12)
def ldh_a_addr():
    addr = HexValue('FF' + memory.get(rg.pc).hget(True))
    rg.pc.inc()
    rg.AF.hi.set(memory.get(addr).hget())
    timer.tick(12)
def ldh_c_a():
    addr = HexValue('FF' + rg.BC.lo.hget(True))
    memory.set(addr,rg.AF.hi.iget())
    timer.tick(8)
def ldh_a_c():
    addr = HexValue('FF' + rg.BC.lo.hget(True))
    rg.AF.hi.set(memory.get(addr).hget())
    timer.tick(8)

# 16-bit loads
def ld16_reg_val(reg):
    val1 = memory.get(rg.pc)
    rg.pc.inc()
    val2 = memory.get(rg.pc)
    rg.pc.inc()
    reg.hi.set(val2.hget()) # little endian?
    reg.lo.set(val1.hget())
    timer.tick(12)
def pop_reg(reg:Register):
    addr = rg.SP.address()
    reg.lo.set(memory.get(addr).hget())
    rg.SP.inc()
    addr = rg.SP.address()
    reg.hi.set(memory.get(addr).hget())
    rg.SP.inc()
    timer.tick(12)
def pop_af():
    addr = rg.SP.address()
    flags=memory.get(addr)
    rg.AF.lo.set(flags.hget())
    rg.SP.inc()
    addr = rg.SP.address()
    rg.AF.hi.set(memory.get(addr).hget())
    rg.SP.inc()
    flags=flags.bget()
    rg.zFlag = int(flags[-1])
    rg.nFlag = int(flags[-2])
    rg.hFlag = int(flags[-3])
    rg.cFlag = int(flags[-4])
    timer.tick(12)
def push_reg(reg:Register): #TODO: the RGBDS docs have weird example code for AF that another source doesn't back up shrug
    rg.SP.dec()
    addr =  rg.SP.address()
    memory.set(addr,reg.hi.iget())
    rg.SP.dec()
    addr =  rg.SP.address()
    memory.set(addr,reg.lo.iget())
    timer.tick(16)
