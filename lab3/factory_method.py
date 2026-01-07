from abc import ABC, abstractmethod
from products_fm import *

class LogisticsCreator(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def deliver_order(self):
        transport = self.create_transport()
        return transport.deliver()

class SeaLogistics(LogisticsCreator):
    def create_transport(self):
        return Ship()

class LandLogistics(LogisticsCreator):
    def create_transport(self):
        return Truck()

class AirLogistics(LogisticsCreator):
    def create_transport(self):
        return Airplane()
