import lowlevel.instruct.loads as ld
import lowlevel.instruct.jumps as jp
import lowlevel.instruct.math as mt

import lowlevel.registers as rg
from functools import partial
from lowlevel.timer import timer

optable = {
    '00': partial(timer.tick,4),
    # '02': #
    # '12': 
    ####### 8-bit load instructions
    '02': partial(ld.ld_addr_reg,rg.BC,rg.AF.hi),
    '06': partial(ld.ld_reg_arg,rg.BC.hi),
    '0a': partial(ld.ld_reg_addr,rg.AF.hi,rg.BC),
    '0e': partial(ld.ld_reg_arg,rg.BC.lo),
    '12': partial(ld.ld_addr_reg,rg.DE,rg.AF.hi),
    '16': partial(ld.ld_reg_arg,rg.DE.hi),
    '1a': partial(ld.ld_reg_addr,rg.AF.hi,rg.DE),
    '1e': partial(ld.ld_reg_arg,rg.DE.lo),
    '22': partial(ld.ld_addr_reg,rg.HL,rg.AF.hi,inc=1),
    '26': partial(ld.ld_reg_arg,rg.HL.hi),
    '2a': partial(ld.ld_reg_addr,rg.AF.hi,rg.HL,inc=1),
    '2e': partial(ld.ld_reg_arg,rg.HL.lo),
    '32': partial(ld.ld_addr_reg,rg.HL,rg.AF.hi,inc=-1),
    '36': partial(ld.ld_addr_arg,rg.HL,elaps=12),
    '3a': partial(ld.ld_reg_addr,rg.AF.hi,rg.HL,inc=-1),
    '3e': partial(ld.ld_reg_arg,rg.AF.hi),
    #
    '40': partial(ld.ld_reg_reg,rg.BC.hi,rg.BC.hi),
    '41': partial(ld.ld_reg_reg,rg.BC.hi,rg.BC.lo),
    '42': partial(ld.ld_reg_reg,rg.BC.hi,rg.DE.hi),
    '43': partial(ld.ld_reg_reg,rg.BC.hi,rg.DE.lo),
    '44': partial(ld.ld_reg_reg,rg.BC.hi,rg.HL.hi),
    '45': partial(ld.ld_reg_reg,rg.BC.hi,rg.HL.lo),
    '46': partial(ld.ld_reg_addr,rg.BC.hi),
    '47': partial(ld.ld_reg_reg,rg.BC.hi,rg.AF.hi),
    #
    '48': partial(ld.ld_reg_reg,rg.BC.lo,rg.BC.hi),
    '49': partial(ld.ld_reg_reg,rg.BC.lo,rg.BC.lo),
    '4a': partial(ld.ld_reg_reg,rg.BC.lo,rg.DE.hi),
    '4b': partial(ld.ld_reg_reg,rg.BC.lo,rg.DE.lo),
    '4c': partial(ld.ld_reg_reg,rg.BC.lo,rg.HL.hi),
    '4d': partial(ld.ld_reg_reg,rg.BC.lo,rg.HL.lo),
    '4e': partial(ld.ld_reg_addr,rg.BC.lo),
    '4f': partial(ld.ld_reg_reg,rg.BC.lo,rg.AF.hi),
    #
    '50': partial(ld.ld_reg_reg,rg.DE.hi,rg.BC.hi),
    '51': partial(ld.ld_reg_reg,rg.DE.hi,rg.BC.lo),
    '52': partial(ld.ld_reg_reg,rg.DE.hi,rg.DE.hi),
    '53': partial(ld.ld_reg_reg,rg.DE.hi,rg.DE.lo),
    '54': partial(ld.ld_reg_reg,rg.DE.hi,rg.HL.hi),
    '55': partial(ld.ld_reg_reg,rg.DE.hi,rg.HL.lo),
    '56': partial(ld.ld_reg_addr,rg.DE.hi),
    '57': partial(ld.ld_reg_reg,rg.DE.hi,rg.AF.hi),
    #
    '58': partial(ld.ld_reg_reg,rg.DE.lo,rg.BC.hi),
    '59': partial(ld.ld_reg_reg,rg.DE.lo,rg.BC.lo),
    '5a': partial(ld.ld_reg_reg,rg.DE.lo,rg.DE.hi),
    '5b': partial(ld.ld_reg_reg,rg.DE.lo,rg.DE.lo),
    '5c': partial(ld.ld_reg_reg,rg.DE.lo,rg.HL.hi),
    '5d': partial(ld.ld_reg_reg,rg.DE.lo,rg.HL.lo),
    '5e': partial(ld.ld_reg_addr,rg.DE.lo),
    '5f': partial(ld.ld_reg_reg,rg.DE.lo,rg.AF.hi),
    #
    '60': partial(ld.ld_reg_reg,rg.HL.hi,rg.BC.hi),
    '61': partial(ld.ld_reg_reg,rg.HL.hi,rg.BC.lo),
    '62': partial(ld.ld_reg_reg,rg.HL.hi,rg.DE.hi),
    '63': partial(ld.ld_reg_reg,rg.HL.hi,rg.DE.lo),
    '64': partial(ld.ld_reg_reg,rg.HL.hi,rg.HL.hi),
    '65': partial(ld.ld_reg_reg,rg.HL.hi,rg.HL.lo),
    '66': partial(ld.ld_reg_addr,rg.HL.hi),
    '67': partial(ld.ld_reg_reg,rg.HL.hi,rg.AF.hi),
    #
    '68': partial(ld.ld_reg_reg,rg.HL.lo,rg.BC.hi),
    '69': partial(ld.ld_reg_reg,rg.HL.lo,rg.BC.lo),
    '6a': partial(ld.ld_reg_reg,rg.HL.lo,rg.DE.hi),
    '6b': partial(ld.ld_reg_reg,rg.HL.lo,rg.DE.lo),
    '6c': partial(ld.ld_reg_reg,rg.HL.lo,rg.HL.hi),
    '6d': partial(ld.ld_reg_reg,rg.HL.lo,rg.HL.lo),
    '6e': partial(ld.ld_reg_addr,rg.HL.lo),
    '6f': partial(ld.ld_reg_reg,rg.HL.lo,rg.AF.hi),
    #
    '70': partial(ld.ld_addr_reg,rg.HL,rg.BC.hi),
    '71': partial(ld.ld_addr_reg,rg.HL,rg.BC.lo),
    '72': partial(ld.ld_addr_reg,rg.HL,rg.DE.hi),
    '73': partial(ld.ld_addr_reg,rg.HL,rg.DE.lo),
    '74': partial(ld.ld_addr_reg,rg.HL,rg.HL.hi),
    '75': partial(ld.ld_addr_reg,rg.HL,rg.HL.lo),
    '76': partial(print,'HALLLLTTTT'),
    '77': partial(ld.ld_addr_reg,rg.HL,rg.AF.hi),
    #
    '78': partial(ld.ld_reg_reg,rg.AF.hi,rg.BC.hi),
    '79': partial(ld.ld_reg_reg,rg.AF.hi,rg.BC.lo),
    '7a': partial(ld.ld_reg_reg,rg.AF.hi,rg.DE.hi),
    '7b': partial(ld.ld_reg_reg,rg.AF.hi,rg.DE.lo),
    '7c': partial(ld.ld_reg_reg,rg.AF.hi,rg.HL.hi),
    '7d': partial(ld.ld_reg_reg,rg.AF.hi,rg.HL.lo),
    '7e': partial(ld.ld_reg_addr,rg.AF.hi),
    '7f': partial(ld.ld_reg_reg,rg.AF.hi,rg.AF.hi),
    #
    'e0': partial(ld.ldh_addr_a),
    'f0': partial(ld.ldh_a_addr), # show ya moves
    'e2': partial(ld.ldh_c_a),
    'f2': partial(ld.ldh_a_c),
    'ea': partial(ld.ld_addr_a), # it's in the game
    'fa': partial(ld.ld_a_addr),

    # yump
    'c3': partial(jp.jp_addr),

    ####### 8-bit math
    ### inc
    '04': partial(mt.inc_reg,rg.BC.hi),
    '0c': partial(mt.inc_reg,rg.BC.lo),
    '14': partial(mt.inc_reg,rg.DE.hi),
    '1c': partial(mt.inc_reg,rg.DE.lo),
    '24': partial(mt.inc_reg,rg.HL.hi),
    '2c': partial(mt.inc_reg,rg.HL.lo),
    '34': partial(mt.inc_addr),
    '3c': partial(mt.inc_reg,rg.AF.hi),
    ### add
    '70': partial(mt.add_a_reg,rg.BC.hi),
    '71': partial(mt.add_a_reg,rg.BC.lo),
    '72': partial(mt.add_a_reg,rg.DE.hi),
    '73': partial(mt.add_a_reg,rg.DE.lo),
    '74': partial(mt.add_a_reg,rg.HL.hi),
    '75': partial(mt.add_a_reg,rg.HL.lo),
    '76': partial(mt.add_a_addr),
    '77': partial(mt.add_a_reg,rg.AF.hi),
    'c6': partial(mt.add_a_arg),
}