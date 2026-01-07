from collections.abc import Iterator, Iterable

# Конкретный Итератор
class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration

# Агрегат (Коллекция)
class WordsCollection(Iterable):
    def __init__(self):
        self._collection = []

    def add_item(self, item):
        self._collection.append(item)

    def __iter__(self):
        return AlphabeticalOrderIterator(self._collection)

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Итератор ---")
    collection = WordsCollection()
    collection.add_item("Первый")
    collection.add_item("Второй")
    collection.add_item("Третий")

    print("Перебор элементов:")
    for item in collection:
        print(item)
    print("\n")
    