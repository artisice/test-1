from singleton import Singleton
from abstract_factory import VanillaProductsFactory, SecureProductsFactory
from builder import ComputerBuilder
from factory_method import SeaLogistics, LandLogistics, AirLogistics


# Singleton
print('\nSingleton:\n')
print(Singleton())
print(Singleton())
s1 = Singleton("A"); s2 = Singleton("B")
print(s1 is s2)

# Abstract Factory
print("\nAbstract factory:\n")
for factory in (VanillaProductsFactory(), SecureProductsFactory()):
    browser = factory.create_browser()
    messenger = factory.create_messenger()
    browser.create_browser_window()
    messenger.create_messenger_window()

# Factory method
print("\nFactory method:\n")
print(SeaLogistics().deliver_order())
print(LandLogistics().deliver_order())
print(AirLogistics().deliver_order())

# Builder
print('\nBuilder:\n')
computer = (ComputerBuilder()
            .set_cpu("AMD Ryzen 9")
            .set_ram_gb(32)
            .set_storage_gb(1024)
            .build())
print(computer)
