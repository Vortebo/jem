from lowlevel.hex_ops import HexValue, Register
from lowlevel.rom_handler import rom

#memory class, handles converting memory addresses to what my arrays understand
class Membank:
    def __init__(self):
        bank0size = 16384
        bank0 = None#bytearray(bank0size)

        bankNsize = 16384
        bankN = None#bytearray(bankNsize)

        vramsize = 8192 # switchable bank 0/1  in CGB
        vram = bytearray(vramsize)

        eramsize = 8192
        eram = bytearray(eramsize)

        wram1size = 4096
        wram1 = bytearray(wram1size)

        wram2size = 4096 # switchable bank 1 - 7 in CGB
        wram2 = bytearray(wram2size)

        echosize = 7680 # TODO: make it actually echo

        oamsize = 160
        oam = bytearray(oamsize)

        nousesize = 96

        ioregsize = 128
        ioreg = bytearray(ioregsize)

        hramsize = 127
        hram = bytearray(hramsize)

        iesize = 1
        ie = bytearray(iesize)

        self.sizes = [bank0size,bankNsize,vramsize,eramsize,wram1size,wram2size,echosize,oamsize,nousesize,ioregsize,hramsize,iesize]
        self.banks = [bank0,bankN,vram,eram,wram1,wram2,None,oam,None,ioreg,hram,ie]

    def address_adjust(self, address):
        loc = address.iget()
        print(f'Translated address is {loc}')
        start=0
        for i in range(len(self.sizes)):
            # print(f'Bank {i} starts at {start}')
            if start <= loc < self.sizes[i] + start:
                return loc - start, i
            start += self.sizes[i]
        return -1
    
    def get(self, address: HexValue):
        loc, bank = self.address_adjust(address)
        # print(f'Equivalent is {loc} in bank {bank}')
        if bank < 2:
            return rom.get(address)
        return HexValue(self.banks[bank][loc:loc+1].hex())
    
    def getrange(self, length):
        return rom.getrange(length)

    def set(self, address: HexValue, value: int):
        print(f'Attempting to set {value} at address 0x{address}')
        loc, bank = self.address_adjust(address)
        self.banks[bank][loc] = value

memory = Membank()
