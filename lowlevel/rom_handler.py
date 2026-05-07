import lowlevel.registers as rg
from lowlevel.hex_ops import HexValue

class ROM:
    '''
    Documentation
    '''

    def __init__(self):
        self.bank = 0

    def load_rom(self, rom):
        self.rom = rom

    def getNext(self):
        # TODO: adjust pc to point to the correct bank
        result = self.rom[rg.pc.iget():rg.pc.iget()+1].hex()
        rg.pc.inc()
        return result

    def getrange(self, length):
        result=''
        for i in range(length):
            result += self.getNext()
        return result
    
    def get(self, address):
        address = address.iget()
        return HexValue(self.rom[(address):address+1].hex())
    
rom=ROM()