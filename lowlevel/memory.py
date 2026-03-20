from lowlevel.hex_ops import HexValue, Register

#memory class, handles converting memory addresses to what my arrays understand
class Membank:
    def __init__(self):
        bank0size = 16383
        bank0 = bytearray(bank0size)

        bankNsize = 16383
        bankN = bytearray(bankNsize)

        vramsize = 8191 # switchable bank 0/1  in CGB
        vram = bytearray(vramsize)

        eramsize = 8191
        eram = bytearray(eramsize)

        wram1size = 4095
        wram1 = bytearray(wram1size)

        wram2size = 4095 # switchable bank 1 - 7 in CGB
        wram2 = bytearray(wram2size)

        # echo ram goes here

        oamsize = 159
        oam = bytearray(oamsize)

        # not usable

        ioregsize = 127
        ioreg = bytearray(ioregsize)

        hramsize = 126
        hram = bytearray(hramsize)

        iesize = 1
        ie = bytearray(iesize)

        self.sizes = [bank0size,bankNsize,vramsize,eramsize,wram1size,wram2size,oamsize,ioregsize,hramsize,iesize]
        self.banks = [bank0,bankN,vram,eram,wram1,wram2,oam,ioreg,hram,ie]

    def address_adjust(self, address):
        loc = HexValue(address).iget()
        start=0
        for i in range(len(self.sizes)):
            if start <= loc < self.sizes[i]:
                return loc - start, i
            start = self.sizes[i]
        return -1
    
    def get(self, address):
        loc, bank = self.address_adjust(address)
        return HexValue(self.banks[bank][loc])

    def set(self, address, value):
        loc, bank = self.address_adjust(address)
        self.banks[bank][loc] = value

memory = Membank()
