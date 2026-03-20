class SystemClock:
    def __init__(self):
        self.time = 0
        self.time_since_x = 0 # not sure how many events or interrupts or whatever I'll need to keep track of

    def tick(self,elaps):
        self.time += elaps
        # if time > whatever, call interrupt, save pc location, etc

timer = SystemClock()