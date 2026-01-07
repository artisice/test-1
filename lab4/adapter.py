# Целевой интерфейс (то, что использует клиент)
class MediaPlayer:
    def play(self, audio_type, filename):
        pass

# Адаптируемый класс (чужой код с другим интерфейсом)
class AdvancedMediaLibrary:
    def play_mp4(self, filename):
        print(f"Воспроизведение MP4 файла: {filename}")

    def play_vlc(self, filename):
        print(f"Воспроизведение VLC файла: {filename}")

# Адаптер: делает AdvancedMediaLibrary совместимым с MediaPlayer
class MediaAdapter(MediaPlayer):
    def __init__(self):
        self.advanced_library = AdvancedMediaLibrary()

    def play(self, audio_type, filename):
        if audio_type == "mp4":
            self.advanced_library.play_mp4(filename)
        elif audio_type == "vlc":
            self.advanced_library.play_vlc(filename)

# Класс клиента, который хочет просто вызывать play()
class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = MediaAdapter()

    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print(f"Встроенный плеер: Воспроизведение MP3 файла: {filename}")
        elif audio_type in ["mp4", "vlc"]:
            # Делегирование адаптеру
            self.media_adapter.play(audio_type, filename)
        else:
            print(f"Неподдерживаемый формат: {audio_type}")

# Пример использования
if __name__ == "__main__":
    print("--- Паттерн Адаптер ---")
    player = AudioPlayer()

    player.play("mp3", "song.mp3")
    player.play("mp4", "movie.mp4")
    player.play("vlc", "clip.vlc")
    player.play("avi", "video.avi") # Ошибка
    print("\n")
    