class Television:

    def __init__(self, id):
        self.isOn = False
        self.channel = 3
        self.id = id

    def setChannel(self, channel):
        self.channel = channel

    def turnON(self):
        if(self.isOn == True):
            print(f'The TV {self.id} is already ON!')
        else:
            print(f'TV {self.id} is now ON')
            self.isOn = True

    def turnOFF(self):
        if(self.isOn == False):
            print(f'The TV {self.id} is already OFF!')
        else:
            self.isOn = False
            print(f'TV {self.id} is now OFF')

    def setSize(self, size):
        self.size = size

    def getChannel(self):
        return self.channel

    def getSize(self):
        return self.size

    def isTVOn(self):
        if(self.isOn == True):
            print(f'TV {self.id} is ON!')
        else:
            print(f'TV {self.id} is OFF.')
