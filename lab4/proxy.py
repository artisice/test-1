from abc import ABC, abstractmethod
import time

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Реальный объект (тяжелый ресурс)
class RealVideo(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.load_video_from_disk()

    def load_video_from_disk(self):
        print(f"Загрузка видео {self.filename} с диска... (это занимает время)")
        time.sleep(1) # Имитация задержки

    def request(self):
        print(f"Воспроизведение видео {self.filename}")

# Прокси (заглушка)
class VideoProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self._real_video = None

    def request(self):
        if self._real_video is None:
            print("Прокси: Видео еще не загружено, инициализируем...")
            self._real_video = RealVideo(self.filename)
        self._real_video.request()

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Прокси ---")
    proxy = VideoProxy("lesson_01.mp4")
    
    # Первый вызов - загрузка происходит
    print("Пользователь нажал Play:")
    proxy.request()

    # Второй вызов - загрузки нет
    print("\nПользователь нажал Play снова:")
    proxy.request()
    print("\n")
    