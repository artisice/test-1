from abc import ABC, abstractmethod

# Стратегия: Интерфейс способа оплаты
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Конкретная стратегия 1: Оплата картой
class CreditCardPayment(PaymentStrategy):
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Оплачено {amount}$ используя кредитную карту {self.card_number} ({self.name}).")

# Конкретная стратегия 2: Оплата PayPal
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount: float):
        print(f"Оплачено {amount}$ используя PayPal аккаунт {self.email}.")

# Контекст: Корзина покупок
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item_name, price):
        self.items.append({'name': item_name, 'price': price})
        print(f"Добавлен товар: {item_name}")

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        if not self.payment_strategy:
            print("Не выбран способ оплаты!")
            return
        total_amount = sum(item['price'] for item in self.items)
        self.payment_strategy.pay(total_amount)

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Стратегия ---")
    cart = ShoppingCart()
    cart.add_item("Книга", 20)
    cart.add_item("Флешка", 10)

    # Оплата картой
    cart.set_payment_strategy(CreditCardPayment("Иван Иванов", "1234-5678-9012"))
    cart.checkout()

    # Оплата PayPal
    cart.set_payment_strategy(PayPalPayment("ivan@example.com"))
    cart.checkout()
    print("\n")
    