import lowlevel.op_funcs as op
import lowlevel.registers as rg
from functools import partial
from lowlevel.timer import timer

optable = {
    '00': partial(timer.tick,4),
    # '02': #
    # '12': 
    '02': partial(op.ld_addr_a,rg.BC),
    '06': partial(op.ld_reg_arg,rg.BC.hi),
    '0a': partial(op.ld_a_addr,rg.BC),
    '0e': partial(op.ld_reg_arg,rg.BC.lo),
    '12': partial(op.ld_addr_a,rg.DE),
    '16': partial(op.ld_reg_arg,rg.DE.hi),
    '1a': partial(op.ld_a_addr,rg.DE),
    '1e': partial(op.ld_reg_arg,rg.DE.lo),
    '22': partial(op.ld_addr_a,rg.HL,inc=1),
    '26': partial(op.ld_reg_arg,rg.HL.hi),
    '2a': partial(op.ld_a_addr,rg.HL,inc=1),
    '2e': partial(op.ld_reg_arg,rg.HL.lo),
    '32': partial(op.ld_addr_a,rg.HL,inc=-1),
    '36': partial(op.ld_addr_arg,rg.HL,elaps=12),
    '3a': partial(op.ld_a_addr),
    '3e': partial(op.ld_reg_arg,rg.AF.hi),

    'c3': partial(op.jp_addr),
}