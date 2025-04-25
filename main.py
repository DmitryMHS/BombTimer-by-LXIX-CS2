import tkinter as tk
from tkinter import font as tkfont
import pyautogui
import time
import threading
from PIL import Image, ImageTk
import ctypes
import webbrowser

# Настройка иконки для Windows
myappid = 'lxix.timerbombcs2.0.4'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class BombTimer:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.setup_state()
        self.setup_threads()
        self.last_update_time = time.perf_counter()
        self.root.after(10, self.update_ui)

    def setup_ui(self):
        """Инициализация графического интерфейса"""
        self.root.title("TimerByLXIX")
        self.root.geometry("400x300")
        self.root.configure(bg="#1A1A2E")
        self.root.resizable(False, False)

        try:
            icon = Image.open("icon.png")
            photo = ImageTk.PhotoImage(icon)
            self.root.iconphoto(False, photo)
        except:
            print("Иконка не найдена (icon.png)")

        # Шрифты
        self.title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        self.timer_font = tkfont.Font(family="Courier New", size=48, weight="bold")
        self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")

        # Заголовок
        self.title_label = tk.Label(
            self.root, text="TimerByLXIX", font=self.title_font,
            fg="#E94560", bg="#1A1A2E"
        )
        self.title_label.pack(pady=10)

        # Таймер
        self.timer_label = tk.Label(
            self.root, text="Жду Бомбу!", font=self.timer_font,
            fg="#E94560", bg="#1A1A2E"
        )
        self.timer_label.pack(pady=20)

        # Кнопки
        self.setup_buttons()

    def setup_buttons(self):
        """Инициализация кнопок"""
        button_frame = tk.Frame(self.root, bg="#1A1A2E")
        button_frame.pack(pady=20)

        # Telegram кнопка
        telegram_icon = self.load_icon("telegram_icon.png")
        if telegram_icon:
            btn = tk.Button(
                button_frame,
                text=" Telegram",
                image=telegram_icon,
                compound="left",
                font=self.button_font,
                fg="white",
                bg="#16213E",
                activebackground="#0F3460",
                activeforeground="white",
                bd=0,
                padx=15,
                pady=5,
                command=lambda: webbrowser.open("https://t.me/LXIXdev")
            )
            btn.image = telegram_icon
            btn.pack(side="left", padx=10)

        # GitHub кнопка
        github_icon = self.load_icon("github_icon.png")
        if github_icon:
            btn = tk.Button(
                button_frame,
                text=" GitHub",
                image=github_icon,
                compound="left",
                font=self.button_font,
                fg="white",
                bg="#16213E",
                activebackground="#0F3460",
                activeforeground="white",
                bd=0,
                padx=15,
                pady=5,
                command=lambda: webbrowser.open("https://github.com/DmitryMHS")
            )
            btn.image = github_icon
            btn.pack(side="left", padx=10)

    def load_icon(self, filename, size=(20, 20)):
        """Загрузка иконок"""
        try:
            icon = Image.open(filename).resize(size)
            return ImageTk.PhotoImage(icon)
        except:
            print(f"Иконка не найдена ({filename})")
            return None

    def setup_state(self):
        """Инициализация состояния"""
        self.bomb_visible = False
        self.start_time = 0
        self.remaining = 40
        self.running = False
        self.lock = threading.Lock()
        self.last_bomb_seen = 0
        self.grace_period = 2  # 2 секунды "льготного периода"

    def setup_threads(self):
        """Запуск рабочих потоков"""
        # Поток для поиска бомбы
        self.scan_thread = threading.Thread(target=self.bomb_scanner, daemon=True)
        self.scan_thread.start()

    def bomb_scanner(self):
        """Поиск бомбы в отдельном потоке"""
        while True:
            try:
                found = pyautogui.locateOnScreen('bomb.png', confidence=0.7) is not None
                current_time = time.time()
                
                with self.lock:
                    if found:
                        self.last_bomb_seen = current_time
                        if not self.running:
                            self.running = True
                            self.start_time = time.perf_counter()
                            self.remaining = 40
                    else:
                        # Если бомба не видна дольше grace_period - останавливаем таймер
                        if current_time - self.last_bomb_seen > self.grace_period and self.running:
                            self.running = False
            except Exception as e:
                print(f"Ошибка поиска: {e}")
            
            time.sleep(0.1)

    def update_ui(self):
        """Обновление интерфейса"""
        now = time.perf_counter()
        
        with self.lock:
            running = self.running
            if running:
                time_passed = now - self.start_time
                self.remaining = max(0, 40 - time_passed)
                if self.remaining <= 0:
                    running = False
                    self.running = False

        if running:
            if self.remaining > 11:
                display_text = f"{int(self.remaining)}"
            else:
                milliseconds = int((self.remaining % 1) * 100)
                display_text = f"{int(self.remaining)}.{milliseconds:02d}"

            # Цвета
            if self.remaining <= 5:
                color = "#E94560"  # Красный
            elif self.remaining <= 10:
                color = "#FFA500"  # Оранжевый
            else:
                color = "#00FFAB"  # Голубой
        else:
            display_text = "Жду Бомбу!"
            color = "#E94560"

        self.timer_label.config(text=display_text, fg=color)
        self.root.after(16, self.update_ui)  # ~60 FPS

if __name__ == "__main__":
    root = tk.Tk()
    app = BombTimer(root)
    root.mainloop()