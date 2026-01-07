from abc import ABC, abstractmethod

class Browser(ABC):
    @abstractmethod
    def create_browser_window(self): pass
    @abstractmethod
    def create_search_toolbar(self): pass

class Messenger(ABC):
    @abstractmethod
    def create_messenger_window(self): pass

class VanillaBrowser(Browser):
    def create_browser_window(self): print("Vanilla browser window")
    def create_search_toolbar(self): print("Vanilla search toolbar")

class VanillaMessenger(Messenger):
    def create_messenger_window(self): print("Vanilla messenger window")

class SecureBrowser(Browser):
    def create_browser_window(self): print("Secure browser window")
    def create_search_toolbar(self): print("Secure search toolbar")

class SecureMessenger(Messenger):
    def create_messenger_window(self): print("Secure messenger window")
