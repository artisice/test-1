from abc import ABC, abstractmethod
from products import *

class AbstractFactory(ABC):
    @abstractmethod
    def create_browser(self): pass
    @abstractmethod
    def create_messenger(self): pass

class VanillaProductsFactory(AbstractFactory):
    def create_browser(self): return VanillaBrowser()
    def create_messenger(self): return VanillaMessenger()

class SecureProductsFactory(AbstractFactory):
    def create_browser(self): return SecureBrowser()
    def create_messenger(self): return SecureMessenger()
