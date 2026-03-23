from lowlevel.hex_ops import HexValue, Register

AF = Register()
BC = Register()
DE = Register()
HL = Register()
pc = HexValue('0')

zFlag = False
nFlag = False
hFlag = False
cFlag = False
