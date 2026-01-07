from abc import ABC, abstractmethod

# Реализация: Интерфейс устройства
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Конкретная реализация 1: ТВ
class TV(Device):
    def turn_on(self):
        print("Телевизор включен")

    def turn_off(self):
        print("Телевизор выключен")

# Конкретная реализация 2: Радио
class Radio(Device):
    def turn_on(self):
        print("Радио включено")

    def turn_off(self):
        print("Радио выключено")

# Абстракция: Пульт
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        # В реальности тут сложнее логика, но для примера просто включаем
        print("Пульт: Нажата кнопка питания")
        self.device.turn_on()

# Расширенная абстракция: Пульт с регулировкой громкости
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Пульт: Включен режим беззвучия")

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Мост ---")
    
    tv = TV()
    radio = Radio()

    remote = RemoteControl(tv)
    remote.toggle_power()

    adv_remote = AdvancedRemoteControl(radio)
    adv_remote.toggle_power()
    adv_remote.mute()
    print("\n")
    