class phone1:
    def call(self):
        print("Calling...")

class phone2(phone1): #single inheritance
    """def call(self):
        print("Calling...")"""

    def message(self):
        print("Messaging...")

class phone3(phone1):
    def browse_internet(self):
        print("Browsing the internet...")

class phone4(phone2):
    def take_photo(self):
        print("Taking a photo...")

class phone5(phone2, phone3): #multiple inheritance
    def play_music(self):
        print("Playing music...")

obj1 = phone1()

obj2 = phone2()

obj3 = phone3()

obj4 = phone4()

obj5 = phone5()






