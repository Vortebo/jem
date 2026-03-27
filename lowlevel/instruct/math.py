import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

# 8-bit math
# I am probably going to get screwed over if I don't allow for signed immediately, buttttttt
def add8(val1,val2,cflag=False,pluscarry=False):
    '''
    Takes hex values :)
    Assumes eight bits in each val
    '''
    rg.hFlag = True if int(val1[-1],16) + int(val2,16) >= 16 else False
    carry = 1 if pluscarry else 0
    val1 = int(val1,16) + int(val2,16) + carry
    val1 = hex(val1)
    if cflag:
        rg.cFlag = True if val1[-3] == '1' else False
    if val1[-3] == '1':
        val1 = val1[-2:]
        rg.zFlag = True if val1 == '00' else False
    rg.nFlag = False
    return val1
def sub8(val1,val2,cflag=False,pluscarry=False):
    val1 = val1.split('x')[1] if 'x' in val1 else val1
    val2 = val2.split('x')[1] if 'x' in val2 else val2
    rg.hFlag = True if int(val1[-4:],16) < int(val2[:-4],16) else False
    carry = 1 if pluscarry else 0
    minus = int(val2,16) + carry
    if cflag:
        rg.cFlag = True if minus > int(val1,16) else False
    val1 = int(val1,16) - minus
    rg.zFlag = True if val1 == 0 else False #TODO: this all seems inefficient
    rg.nFlag = True
    val1 = 256 + val1 if val1 < 0 else val1
    val1 = hex(val1)
    return val1
def mod_reg(func,reg):
    '''
    Mods a reg
    '''
    reg.set(func(reg.hget(),'1'))
    timer.tick(4)
def mod_addr(func):
    '''
    Modcrement the byte pointed to by [HL] by 1
    '''
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    memory.set(addr,func(memory.get(addr).hget(),'1'))
    timer.tick(12)
def mod_a_reg(func,reg,pluscarry=False):
    rg.AF.hi.set(func(rg.AF.hi.hget(),reg.hget(),True,pluscarry))
    timer.tick(4)
def mod_a_addr(func,pluscarry=False):
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    rg.AF.hi.set(func(rg.AF.hi.hget(),memory.get(addr).hget(),True,pluscarry))
    timer.tick(8)
def mod_a_arg(func,pluscarry=False):
    src = rom.get()
    rg.AF.hi.set(func(rg.AF.hi.hget(),src,True,pluscarry))
    timer.tick(8)

def and_reg(reg):
    rg.AF.hi.set(hex(rg.AF.hi.iget() & reg.iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = True
    rg.cFlag = False
    timer.tick(4)
def and_addr():
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    rg.AF.hi.set(hex(rg.AF.hi.iget() & memory.get(addr).iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = True
    rg.cFlag = False
    timer.tick(8)
def and_arg():
    src = rom.get()
    rg.AF.hi.set(hex(rg.AF.hi.iget() & int(src,16)))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = True
    rg.cFlag = False
    timer.tick(8)
def xor_reg(reg):
    rg.AF.hi.set(hex(rg.AF.hi.iget() ^ reg.iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(4)
def xor_addr():
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    rg.AF.hi.set(hex(rg.AF.hi.iget() ^ memory.get(addr).iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(8)
def xor_arg():
    src = rom.get()
    rg.AF.hi.set(hex(rg.AF.hi.iget() ^ int(src,16)))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(8)
def or_reg(reg):
    rg.AF.hi.set(hex(rg.AF.hi.iget() | reg.iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(4)
def or_addr():
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    rg.AF.hi.set(hex(rg.AF.hi.iget() | memory.get(addr).iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(8)
def or_arg():
    src = rom.get()
    rg.AF.hi.set(hex(rg.AF.hi.iget() | int(src,16)))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(8)
