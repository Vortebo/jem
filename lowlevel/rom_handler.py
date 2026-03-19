from lowlevel.hex_ops import HexValue

class ROM:
    '''
    Documentation
    '''

    def __init__(self, rom:bytearray):
        self.rom = rom
        self.bank = 0

    def get(self, pc):
        # TODO: adjust pc to point to the correct bank
        result = self.rom[pc.iget():pc.iget()+1].hex()
        pc.inc()
        return result

    def getrange(self, pc, length):
        result=''
        for i in range(length):
            result += self.get(pc)
            # pc.inc()
        return result