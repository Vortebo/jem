import registers as rg

class ROM:
    '''
    Documentation
    '''

    def __init__(self, rom:bytearray):
        self.rom = rom
        self.bank = 0

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