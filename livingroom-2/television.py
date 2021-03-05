class Television:

    def __init__(self, id, cMin, cMax, channel):
        self.isOn = False
        self.channel = channel
        self.id = id
        self.cMin = cMin
        self.cMax = cMax

    def changeChannelHigher(self):
        if(self.channel+1 <= self.cMax):
            self.channel += 1

    def changeChannelLower(self):
        if(self.channel-1 >= self.cMin):
            self.channel -= 1

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
