import lowlevel.op_funcs as op
import lowlevel.registers as rg
from functools import partial
from lowlevel.timer import timer

optable = {
    '00': partial(timer.tick,4),
    # '02': #
    # '12': 
    ####### 8-bit load instructions
    '02': partial(op.ld_addr_reg,rg.BC,rg.AF.hi),
    '06': partial(op.ld_reg_arg,rg.BC.hi),
    '0a': partial(op.ld_reg_addr,rg.AF.hi,rg.BC),
    '0e': partial(op.ld_reg_arg,rg.BC.lo),
    '12': partial(op.ld_addr_reg,rg.DE,rg.AF.hi),
    '16': partial(op.ld_reg_arg,rg.DE.hi),
    '1a': partial(op.ld_reg_addr,rg.AF.hi,rg.DE),
    '1e': partial(op.ld_reg_arg,rg.DE.lo),
    '22': partial(op.ld_addr_reg,rg.HL,rg.AF.hi,inc=1),
    '26': partial(op.ld_reg_arg,rg.HL.hi),
    '2a': partial(op.ld_reg_addr,rg.AF.hi,rg.HL,inc=1),
    '2e': partial(op.ld_reg_arg,rg.HL.lo),
    '32': partial(op.ld_addr_reg,rg.HL,rg.AF.hi,inc=-1),
    '36': partial(op.ld_addr_arg,rg.HL,elaps=12),
    '3a': partial(op.ld_reg_addr,rg.AF.hi,rg.HL,inc=-1),
    '3e': partial(op.ld_reg_arg,rg.AF.hi),
    #
    '40': partial(op.ld_reg_reg,rg.BC.hi,rg.BC.hi),
    '41': partial(op.ld_reg_reg,rg.BC.hi,rg.BC.lo),
    '42': partial(op.ld_reg_reg,rg.BC.hi,rg.DE.hi),
    '43': partial(op.ld_reg_reg,rg.BC.hi,rg.DE.lo),
    '44': partial(op.ld_reg_reg,rg.BC.hi,rg.HL.hi),
    '45': partial(op.ld_reg_reg,rg.BC.hi,rg.HL.lo),
    '46': partial(op.ld_reg_addr,rg.BC.hi),
    '47': partial(op.ld_reg_reg,rg.BC.hi,rg.AF.hi),
    #
    '48': partial(op.ld_reg_reg,rg.BC.lo,rg.BC.hi),
    '49': partial(op.ld_reg_reg,rg.BC.lo,rg.BC.lo),
    '4a': partial(op.ld_reg_reg,rg.BC.lo,rg.DE.hi),
    '4b': partial(op.ld_reg_reg,rg.BC.lo,rg.DE.lo),
    '4c': partial(op.ld_reg_reg,rg.BC.lo,rg.HL.hi),
    '4d': partial(op.ld_reg_reg,rg.BC.lo,rg.HL.lo),
    '4e': partial(op.ld_reg_addr,rg.BC.lo),
    '4f': partial(op.ld_reg_reg,rg.BC.lo,rg.AF.hi),
    #
    '50': partial(op.ld_reg_reg,rg.DE.hi,rg.BC.hi),
    '51': partial(op.ld_reg_reg,rg.DE.hi,rg.BC.lo),
    '52': partial(op.ld_reg_reg,rg.DE.hi,rg.DE.hi),
    '53': partial(op.ld_reg_reg,rg.DE.hi,rg.DE.lo),
    '54': partial(op.ld_reg_reg,rg.DE.hi,rg.HL.hi),
    '55': partial(op.ld_reg_reg,rg.DE.hi,rg.HL.lo),
    '56': partial(op.ld_reg_addr,rg.DE.hi),
    '57': partial(op.ld_reg_reg,rg.DE.hi,rg.AF.hi),
    #
    '58': partial(op.ld_reg_reg,rg.DE.lo,rg.BC.hi),
    '59': partial(op.ld_reg_reg,rg.DE.lo,rg.BC.lo),
    '5a': partial(op.ld_reg_reg,rg.DE.lo,rg.DE.hi),
    '5b': partial(op.ld_reg_reg,rg.DE.lo,rg.DE.lo),
    '5c': partial(op.ld_reg_reg,rg.DE.lo,rg.HL.hi),
    '5d': partial(op.ld_reg_reg,rg.DE.lo,rg.HL.lo),
    '5e': partial(op.ld_reg_addr,rg.DE.lo),
    '5f': partial(op.ld_reg_reg,rg.DE.lo,rg.AF.hi),
    #
    '60': partial(op.ld_reg_reg,rg.HL.hi,rg.BC.hi),
    '61': partial(op.ld_reg_reg,rg.HL.hi,rg.BC.lo),
    '62': partial(op.ld_reg_reg,rg.HL.hi,rg.DE.hi),
    '63': partial(op.ld_reg_reg,rg.HL.hi,rg.DE.lo),
    '64': partial(op.ld_reg_reg,rg.HL.hi,rg.HL.hi),
    '65': partial(op.ld_reg_reg,rg.HL.hi,rg.HL.lo),
    '66': partial(op.ld_reg_addr,rg.HL.hi),
    '67': partial(op.ld_reg_reg,rg.HL.hi,rg.AF.hi),
    #
    '68': partial(op.ld_reg_reg,rg.HL.lo,rg.BC.hi),
    '69': partial(op.ld_reg_reg,rg.HL.lo,rg.BC.lo),
    '6a': partial(op.ld_reg_reg,rg.HL.lo,rg.DE.hi),
    '6b': partial(op.ld_reg_reg,rg.HL.lo,rg.DE.lo),
    '6c': partial(op.ld_reg_reg,rg.HL.lo,rg.HL.hi),
    '6d': partial(op.ld_reg_reg,rg.HL.lo,rg.HL.lo),
    '6e': partial(op.ld_reg_addr,rg.HL.lo),
    '6f': partial(op.ld_reg_reg,rg.HL.lo,rg.AF.hi),
    #
    '70': partial(op.ld_addr_reg,rg.HL,rg.BC.hi),
    '71': partial(op.ld_addr_reg,rg.HL,rg.BC.lo),
    '72': partial(op.ld_addr_reg,rg.HL,rg.DE.hi),
    '73': partial(op.ld_addr_reg,rg.HL,rg.DE.lo),
    '74': partial(op.ld_addr_reg,rg.HL,rg.HL.hi),
    '75': partial(op.ld_addr_reg,rg.HL,rg.HL.lo),
    '76': partial(print,'HALLLLTTTT'),
    '77': partial(op.ld_addr_reg,rg.HL,rg.AF.hi),
    #
    '78': partial(op.ld_reg_reg,rg.AF.hi,rg.BC.hi),
    '79': partial(op.ld_reg_reg,rg.AF.hi,rg.BC.lo),
    '7a': partial(op.ld_reg_reg,rg.AF.hi,rg.DE.hi),
    '7b': partial(op.ld_reg_reg,rg.AF.hi,rg.DE.lo),
    '7c': partial(op.ld_reg_reg,rg.AF.hi,rg.HL.hi),
    '7d': partial(op.ld_reg_reg,rg.AF.hi,rg.HL.lo),
    '7e': partial(op.ld_reg_addr,rg.AF.hi),
    '7f': partial(op.ld_reg_reg,rg.AF.hi,rg.AF.hi),
    #
    'e0': partial(op.ldh_addr_a),
    'f0': partial(op.ldh_a_addr), # show ya moves
    'e2': partial(op.ldh_c_a),
    'f2': partial(op.ldh_a_c),
    'ea': partial(op.ld_addr_a), # it's in the game
    'fa': partial(op.ld_a_addr),

    'c3': partial(op.jp_addr),
}