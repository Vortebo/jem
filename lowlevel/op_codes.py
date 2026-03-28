import lowlevel.instruct.loads as ld
import lowlevel.instruct.jumps as jp
import lowlevel.instruct.math8 as mt
import lowlevel.instruct.math16 as mh

import lowlevel.registers as rg
from functools import partial
from lowlevel.timer import timer

optable = {
    ####### misc
    '00': partial(timer.tick,4), # NOP
    '76': partial(print,'HALLLLTTTT'), # HALT

    ####### 8-bit ld
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
    # see misc
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
    '04': partial(mt.mod_reg,mt.add8,rg.BC.hi),
    '0c': partial(mt.mod_reg,mt.add8,rg.BC.lo),
    '14': partial(mt.mod_reg,mt.add8,rg.DE.hi),
    '1c': partial(mt.mod_reg,mt.add8,rg.DE.lo),
    '24': partial(mt.mod_reg,mt.add8,rg.HL.hi),
    '2c': partial(mt.mod_reg,mt.add8,rg.HL.lo),
    '34': partial(mt.mod_addr,mt.add8),
    '3c': partial(mt.mod_reg,mt.add8,rg.AF.hi),
    ### add
    '80': partial(mt.mod_a_reg,mt.add8,rg.BC.hi),
    '81': partial(mt.mod_a_reg,mt.add8,rg.BC.lo),
    '82': partial(mt.mod_a_reg,mt.add8,rg.DE.hi),
    '83': partial(mt.mod_a_reg,mt.add8,rg.DE.lo),
    '84': partial(mt.mod_a_reg,mt.add8,rg.HL.hi),
    '85': partial(mt.mod_a_reg,mt.add8,rg.HL.lo),
    '86': partial(mt.mod_a_addr,mt.add8),
    '87': partial(mt.mod_a_reg,mt.add8,rg.AF.hi),
    'c6': partial(mt.mod_a_arg,mt.add8),
    ### adc
    '88': partial(mt.mod_a_reg,mt.add8,rg.BC.hi,True),
    '89': partial(mt.mod_a_reg,mt.add8,rg.BC.lo,True),
    '8a': partial(mt.mod_a_reg,mt.add8,rg.DE.hi,True),
    '8b': partial(mt.mod_a_reg,mt.add8,rg.DE.lo,True),
    '8c': partial(mt.mod_a_reg,mt.add8,rg.HL.hi,True),
    '8d': partial(mt.mod_a_reg,mt.add8,rg.HL.lo,True),
    '8e': partial(mt.mod_a_addr,mt.add8,True),
    '8f': partial(mt.mod_a_reg,mt.add8,rg.AF.hi,True),
    'ce': partial(mt.mod_a_arg,mt.add8,True),
    ### dec
    '05': partial(mt.mod_reg,mt.sub8,rg.BC.hi),
    '0d': partial(mt.mod_reg,mt.sub8,rg.BC.lo),
    '15': partial(mt.mod_reg,mt.sub8,rg.DE.hi),
    '1d': partial(mt.mod_reg,mt.sub8,rg.DE.lo),
    '25': partial(mt.mod_reg,mt.sub8,rg.HL.hi),
    '2d': partial(mt.mod_reg,mt.sub8,rg.HL.lo),
    '35': partial(mt.mod_addr,mt.sub8),
    '3d': partial(mt.mod_reg,mt.sub8,rg.AF.hi),
    ### sub
    '90': partial(mt.mod_a_reg,mt.sub8,rg.BC.hi),
    '91': partial(mt.mod_a_reg,mt.sub8,rg.BC.lo),
    '92': partial(mt.mod_a_reg,mt.sub8,rg.DE.hi),
    '93': partial(mt.mod_a_reg,mt.sub8,rg.DE.lo),
    '94': partial(mt.mod_a_reg,mt.sub8,rg.HL.hi),
    '95': partial(mt.mod_a_reg,mt.sub8,rg.HL.lo),
    '96': partial(mt.mod_a_addr,mt.sub8),
    '97': partial(mt.mod_a_reg,mt.sub8,rg.AF.hi), # TODO: check flags
    'd6': partial(mt.mod_a_arg,mt.sub8),
    ### sbc
    '98': partial(mt.mod_a_reg,mt.sub8,rg.BC.hi,True),
    '99': partial(mt.mod_a_reg,mt.sub8,rg.BC.lo,True),
    '9a': partial(mt.mod_a_reg,mt.sub8,rg.DE.hi,True),
    '9b': partial(mt.mod_a_reg,mt.sub8,rg.DE.lo,True),
    '9c': partial(mt.mod_a_reg,mt.sub8,rg.HL.hi,True),
    '9d': partial(mt.mod_a_reg,mt.sub8,rg.HL.lo,True),
    '9e': partial(mt.mod_a_addr,mt.sub8,True),
    '9f': partial(mt.mod_a_reg,mt.sub8,rg.AF.hi,True), # TODO: check flags
    'de': partial(mt.mod_a_arg,mt.sub8,True),
    ### and
    'a0': partial(mt.and_reg,rg.BC.hi),
    'a1': partial(mt.and_reg,rg.BC.lo),
    'a2': partial(mt.and_reg,rg.DE.hi),
    'a3': partial(mt.and_reg,rg.DE.lo),
    'a4': partial(mt.and_reg,rg.HL.hi),
    'a5': partial(mt.and_reg,rg.HL.lo),
    'a6': partial(mt.and_addr),
    'a7': partial(mt.and_reg,rg.AF.hi),
    'e6': partial(mt.and_arg),
    ### xor
    'a8': partial(mt.xor_reg,rg.BC.hi),
    'a9': partial(mt.xor_reg,rg.BC.lo),
    'aa': partial(mt.xor_reg,rg.DE.hi),
    'ab': partial(mt.xor_reg,rg.DE.lo),
    'ac': partial(mt.xor_reg,rg.HL.hi),
    'ad': partial(mt.xor_reg,rg.HL.lo),
    'ae': partial(mt.xor_addr),
    'af': partial(mt.xor_reg,rg.AF.hi), # TODO: check flags
    'ee': partial(mt.xor_arg),
    ### or
    'b0': partial(mt.or_reg,rg.BC.hi),
    'b1': partial(mt.or_reg,rg.BC.lo),
    'b2': partial(mt.or_reg,rg.DE.hi),
    'b3': partial(mt.or_reg,rg.DE.lo),
    'b4': partial(mt.or_reg,rg.HL.hi),
    'b5': partial(mt.or_reg,rg.HL.lo),
    'b6': partial(mt.or_addr),
    'b7': partial(mt.or_reg,rg.AF.hi),
    'f6': partial(mt.or_arg),
    ### cp
    'b8': partial(mt.mod_a_reg,mt.sub8,rg.BC.hi,comp=True),
    'b9': partial(mt.mod_a_reg,mt.sub8,rg.BC.lo,comp=True),
    'ba': partial(mt.mod_a_reg,mt.sub8,rg.DE.hi,comp=True),
    'bb': partial(mt.mod_a_reg,mt.sub8,rg.DE.lo,comp=True),
    'bc': partial(mt.mod_a_reg,mt.sub8,rg.HL.hi,comp=True),
    'bd': partial(mt.mod_a_reg,mt.sub8,rg.HL.lo,comp=True),
    'be': partial(mt.mod_a_addr,mt.sub8,comp=True),
    'bf': partial(mt.mod_a_reg,mt.sub8,rg.AF.hi,comp=True), # TODO: check flags
    'fe': partial(mt.mod_a_arg,mt.sub8,comp=True),
    ### misc
    '27': partial(mt.daa), # daa
    '2f': partial(mt.cpl), # cpl
    '37': partial(mt.scf), # scf
    '3f': partial(mt.ccf), # ccf

    ####### 16-bit math
    ### inc
    '03': partial(mh.inc_reg,rg.BC),
    '13': partial(mh.inc_reg,rg.DE),
    '23': partial(mh.inc_reg,rg.HL),
    '33': partial(mh.inc_reg,rg.SP),
    ### dec
    '0b': partial(mh.dec_reg,rg.BC),
    '1b': partial(mh.dec_reg,rg.DE),
    '2b': partial(mh.dec_reg,rg.HL),
    '3b': partial(mh.dec_reg,rg.SP),
}
