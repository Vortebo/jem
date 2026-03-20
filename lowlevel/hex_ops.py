class HexValue:
    '''
    Class for easily working with hex values
    '''

    def __init__(self, value:str):
        self.value = value

    def set(self, value:str):
        ''' In hex '''
        self.value = value

    def inc(self):
        '''
        Safely increments a variable holding what's meant to
        be a hex value by one
        '''

        self.value = hex(int(str(self.value),16)+1)
    
    def iget(self):
        '''
        Returns value in integer form
        '''

        return int(str(self.value),16)
    
    def hget(self):
        '''
        Returns value in hex form (string)
        '''

        return self.value
    
class Register(HexValue):
    '''
    Class for holding registers
    '''

    def __init__(self):
        self.hi = HexValue('00000000')
        self.lo = HexValue('00000000')
    
    def inc(self): # Only HL can be increased this way
        addr=self.hi.hget()+self.lo.hget()
        new_addr=HexValue(addr).inc()
        self.hi.set(new_addr[0:9])
        self.lo.set(new_addr[9:16])