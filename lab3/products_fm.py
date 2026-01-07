from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Доставка грузовиком по суше"

class Ship(Transport):
    def deliver(self):
        return "Доставка кораблем по морю"

class Airplane(Transport):
    def deliver(self):
        return "Доставка самолетом по воздуху"
