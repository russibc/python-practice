class Person:
    def __init__(self, age, name):
        self.speaking = False
        self.eating = False
        self.age = age
        self.name = name

    def stopSpeaking(self):
        self.speaking = False

    def stopEating(self):
        self.eating = False

    def toSpeak(self):
        self.stopEating()
        self.speaking = True

    def toEat(self):
        self.stopSpeaking()
        self.eating = True

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def isSpeaking(self):
        if(self.speaking == True):
            print('Person is speaking!')
        else:
            print('Person is not speaking!')

    def isEating(self):
        if(self.eating == True):
            print('Person is eating!')
        else:
            print('Person is not eating!')
