class Counter:
    counter = 0 
    @classmethod
    def addcounter(self):
        self.counter += 1
    
    @classmethod
    def get_counter(self):
        return self.counter

    @classmethod
    def set_counter(self):
        self.counter = 0