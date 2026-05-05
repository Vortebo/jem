import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom
from lowlevel.hex_ops  import HexValue

# 8-bit math
# I am probably going to get screwed over if I don't allow for signed immediately, buttttttt
def add8(val1,val2,cflag=False,pluscarry=False):
    '''
    Takes HexValues :)
    Assumes eight bits in each val
    '''
    rg.hFlag = True if int(val1.hget()[-1],16) + val2.iget() >= 16 else False
    carry = 1 if pluscarry else 0
    val1 = hex(val1.iget() + val2.iget() + carry)
    if cflag:
        rg.cFlag = True if val1[-3] == '1' else False
    if val1[-3] == '1':
        val1 = val1[-2:]
        rg.zFlag = True if val1 == '00' else False
    rg.nFlag = False
    return HexValue(val1)
def sub8(val1,val2,cflag=False,pluscarry=False):
    val1 = val1.bget()
    val2 = val2.bget()
    rg.hFlag = True if int(val1[-4:],2) < int(val2[:-4],2) else False
    carry = 1 if pluscarry else 0
    minus = int(val2,16) + carry
    if cflag:
        rg.cFlag = True if minus > int(val1,16) else False
    val1 = int(val1,16) - minus
    rg.zFlag = True if val1 == 0 else False #TODO: this all seems inefficient
    rg.nFlag = True
    val1 = 256 + val1 if val1 < 0 else val1
    val1 = hex(val1)
    return HexValue(val1)
def mod_reg(func,reg):
    '''
    Mods a reg
    '''
    reg.set(func(reg,HexValue(hex(1))).hget())
    timer.tick(4)
def mod_addr(func):
    '''
    Modcrement the byte pointed to by [HL] by 1
    '''
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    memory.set(addr,func(memory.get(addr),HexValue(hex(1))))
    timer.tick(12)
def mod_a_reg(func,reg,pluscarry=False,comp=False):
    new_val = func(rg.AF.hi,reg,True,pluscarry)
    if not comp:
        rg.AF.hi.set(new_val)
    timer.tick(4)
def mod_a_addr(func,pluscarry=False,comp=False):
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    new_val = func(rg.AF.hi,memory.get(addr),True,pluscarry)
    if not comp:
        rg.AF.hi.set(new_val)
    timer.tick(8)
def mod_a_arg(func,pluscarry=False,comp=False):
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    new_val = func(rg.AF.hi,src,True,pluscarry)
    if not comp:
        rg.AF.hi.set(new_val)
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
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    rg.AF.hi.set(hex(rg.AF.hi.iget() & src.iget()))
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
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    rg.AF.hi.set(hex(rg.AF.hi.iget() ^ src.iget()))
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
    src = memory.get(rg.pc.iget())
    rg.pc.inc()
    rg.AF.hi.set(hex(rg.AF.hi.iget() | src.iget()))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = False
    timer.tick(8)

def daa():
    adjust = 0
    flagStates = [rg.nFlag, rg.cFlag]
    if rg.nFlag:
        if rg.hFlag:
            adjust = adjust + 6
        if rg.cFlag:
            adjust = adjust + int('60',16)
        rg.AF.hi.set(sub8(rg.AF.hi,HexValue(hex(adjust)),False,False))
    else:
        if rg.hFlag or (rg.AF.hi.iget() & int('F',16))>9:
            adjust = adjust + 6
        if rg.cFlag or rg.AF.hi.iget() > int('99',16):
            adjust = adjust + int('60',16)
            flagStates[1] = True
        rg.AF.hi.set(add8(rg.AF.hi,HexValue(hex(adjust)),False,False))
    rg.zFlag = True if rg.AF.hi.iget() == 0 else False
    rg.nFlag = flagStates[0]
    rg.hFlag = False
    rg.cFlag = flagStates[1]
    timer.tick(4)
def cpl():
    rg.AF.hi.set(hex(~(rg.AF.hi.iget())))
    rg.nFlag = True
    rg.hFlag = True
    timer.tick(4)
def scf():
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = True
    timer.tick(4)
def ccf():
    rg.nFlag = False
    rg.hFlag = False
    rg.cFlag = not rg.cFlag
    timer.tick(4)
