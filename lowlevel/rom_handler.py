import lowlevel.registers as rg

class ROM:
    '''
    Documentation
    '''

    def __init__(self):
        self.bank = 0

    def load_rom(self, rom:bytearray):
        self.rom = rom

    def get(self):
        # TODO: adjust pc to point to the correct bank
        result = self.rom[rg.pc.iget():rg.pc.iget()+1].hex()
        rg.pc.inc()
        return result

    def getrange(self, length):
        result=''
        for i in range(length):
            result += self.get()
        return result
    
rom=ROM()