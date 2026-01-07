from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# Конкретный обработчик 1: Первая линия (простые вопросы)
class FirstLevelSupport(Handler):
    def handle(self, request):
        if request == "simple_issue":
            return f"Первая линия: Решен простой баг '{request}'."
        else:
            return super().handle(request)

# Конкретный обработчик 2: Вторая линия (сложные баги)
class SecondLevelSupport(Handler):
    def handle(self, request):
        if request == "complex_bug":
            return f"Вторая линия: Исправлен сложный баг '{request}'."
        else:
            return super().handle(request)

# Конкретный обработчик 3: Менеджер (финансовые вопросы)
class ManagerSupport(Handler):
    def handle(self, request):
        if request == "refund_request":
            return f"Менеджер: Одобрен возврат средств для '{request}'."
        else:
            return f"Менеджер: Не могу решить проблему '{request}', передано выше (некуда)."

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Цепочка обязанностей ---")
    
    # Создаем цепочку: First -> Second -> Manager
    first = FirstLevelSupport()
    second = SecondLevelSupport()
    manager = ManagerSupport()

    first.set_next(second).set_next(manager)

    requests = ["simple_issue", "complex_bug", "refund_request", "unknown_issue"]
    
    for req in requests:
        print(f"Запрос: {req} -> {first.handle(req)}")
    print("\n")
    