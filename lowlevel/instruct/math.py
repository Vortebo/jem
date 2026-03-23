import lowlevel.registers as rg
from lowlevel.memory import memory
from lowlevel.timer import timer
from lowlevel.rom_handler import rom

hex_index = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

# 8-bit math
# I am probably going to get screwed over if I don't allow for signed immediately, buttttttt
def add8(val1,val2,carry=False):
    '''
    Takes hex values :)
    Assumes eight bits in each val
    '''
    val1_last = val1[-1]
    val2_last = val2[-1]
    if hex_index[val1_last] + hex_index[val2_last] >= 16:
        rg.hFlag = True

    val1 = int(val1,16)
    val2 = int(val2,16)
    val1 = val1 + val2
    if val1 > 255:
        if val1 == 256:
            rg.zFlag = True
        val1 = val1 - 255
        if carry:
            rg.cFlag = True
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
def add_a_reg():
    print('lol')

def add_a_val():
    print('lol')

def icecream():
    value=bin(rg.HL.hi.iget())
    # print(value)
    # value = value + 0b1
    # print(value)

    binary_add('0b1111','0b1')
    raise Exception