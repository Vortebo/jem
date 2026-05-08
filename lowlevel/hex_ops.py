class HexValue:
    '''
    Class for easily working with hex values
    '''

    def __init__(self, value:str):
        self.value = value
        self._sanitize()

    def set(self, value:str):
        ''' In hex '''
        self.value = value
        self._sanitize()

    def _sanitize(self):
        negative = self.value[0]=='-'
        self.value = self.value.split('x')[1] if 'x' in self.value else self.value
        if negative:
            self.value = '-'+self.value

    def _pad(self,pad):
        padding=''
        for _ in range(pad-len(self.value)):
            padding=padding+'0'
        self.value=padding+self.value

    def inc(self,keep_length=False):
        '''
        Safely increments a variable holding what's meant to
        be a hex value by one

        Args:
            keep_length (bool): Preserves number of digits (useful for (16-bit?) addresses)
        '''

        current_length=len(self.value)
        self.set(hex(int(str(self.value),16)+1).split('x')[1])
        if keep_length:
            self._pad(current_length)

    def dec(self,keep_length=False):
        '''
        Safely decrements a variable holding what's meant to
        be a hex value by one

        Args:
            keep_length (bool): Preserves number of digits (useful for (16-bit?) addresses)
        '''

        current_length=len(self.value)
        self.set(hex(int(str(self.value),16)-1).split('x')[1])
        if keep_length:
            self._pad(current_length)
    
    def bget(self):
        '''
        Returns value in binary form
        '''

        result=bin(int(str(self.value),16)).split('b')[1]
        padding=''
        for _ in range(8-len(result)):
            padding=padding+'0'
        return padding+result
    
    
    def iget(self):
        '''
        Returns value in integer form
        '''

        return int(str(self.value),16)
    
    def hget(self,two=False):
        '''
        Returns value in hex form (string)

        Args:
            two (bool): For if you want to force an address-friendly two-digit value
        '''

        padding=''
        if two:
            for _ in range(2-len(self.value)):
                padding=padding+'0'
        return padding+self.value
    
class Register(HexValue):
    '''
    Class for holding registers
    '''

    def __init__(self):
        self.hi = HexValue('00')
        self.lo = HexValue('00')
    
    def inc(self):
        new_addr=self.address()
        new_addr.inc(True)
        self.hi.set(new_addr.hget()[0:1])
        self.lo.set(new_addr.hget()[2:3])

    def dec(self):
        new_addr=self.address()
        new_addr.dec(True)
        self.hi.set(new_addr.hget()[0:1])
        self.lo.set(new_addr.hget()[2:3])

    def address(self): #TODO: confirm if my endians are correct
        addr=self.hi.hget(True)+self.lo.hget(True)
        return(HexValue(addr))
    