class HexValue:
    '''
    Class for easily working with hex values
    '''

    def __init__(self, value:str):
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