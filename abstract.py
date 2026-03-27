from abc import ABC, abstractmethod

class phone(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def message(self):
        pass

class samsung(phone):
    def call(self):
        print("Calling from samsung phone")

    def message(self):
        print("Messaging from samsung phone")

obj = samsung()
