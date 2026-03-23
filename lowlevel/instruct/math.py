import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

# 8-bit math
# I am probably going to get screwed over if I don't allow for signed immediately, buttttttt
def add8(val1,val2,carry=False):
    '''
    Takes hex values :)
    Assumes eight bits in each val
    '''
    rg.hFlag = True if int(val1[-1],16) + int(val2,16) >= 16 else False
    val1 = int(val1,16) + int(val2,16)
    val1 = hex(val1)
    if carry:
        rg.cFlag = True if val1[-3] == '1' else False
    if val1[-3] == '1':
        val1 = val1[-2:]
        rg.zFlag = True if val1 == '00' else False
    rg.nFlag = False
    return val1
def inc_reg(reg):
    '''
    Incs a reg
    '''
    reg.set(add8(reg.hget(),'1'))
    timer.tick(4)
def inc_addr():
    '''
    Increment the byte pointed to by [HL] by 1 (oops, that's the same wording as the rgbds docs)
    '''
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    memory.set(addr,add8(memory.get(addr),'1'))
    timer.tick(12)
def add_a_reg(reg):
    rg.AF.hi.set(add8(rg.AF.hi.hget(),reg.hget(),True))
    timer.tick(4)
def add_a_addr():
    addr = rg.HL.hi.hget() + rg.HL.lo.hget()
    rg.AF.hi.set(add8(rg.AF.hi.hget(),memory.get(addr),True))
    timer.tick(8)
def add_a_arg():
    src = rom.get()
    rg.AF.hi.set(add8(rg.AF.hi.hget(),src,True))
    timer.tick(8)
