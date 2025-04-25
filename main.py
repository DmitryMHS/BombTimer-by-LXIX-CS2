import tkinter as tk
from tkinter import font as tkfont
import pyautogui
import time
import threading
from PIL import Image, ImageTk
import ctypes
import webbrowser

# Настройка иконки для Windows
myappid = 'lxix.timerbombcs2.0.6'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class BombTimer:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.setup_state()
        self.setup_threads()
        self.root.after(10, self.update_ui)

    def setup_ui(self):
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

        self.title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        self.timer_font = tkfont.Font(family="Courier New", size=48, weight="bold")
        self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")

        self.title_label = tk.Label(
            self.root, text="TimerByLXIX", font=self.title_font,
            fg="#E94560", bg="#1A1A2E"
        )
        self.title_label.pack(pady=10)

        self.timer_label = tk.Label(
            self.root, text="Жду Бомбу!", font=self.timer_font,
            fg="#E94560", bg="#1A1A2E"
        )
        self.timer_label.pack(pady=20)

        self.setup_buttons()

    def setup_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1A1A2E")
        button_frame.pack(pady=20)

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
        try:
            icon = Image.open(filename).resize(size)
            return ImageTk.PhotoImage(icon)
        except:
            print(f"Иконка не найдена ({filename})")
            return None

    def setup_state(self):
        self.bomb_visible = False
        self.start_time = 0
        self.remaining = 40
        self.running = False
        self.defused = False
        self.reset_timer_time = 0
        self.lock = threading.Lock()

    def setup_threads(self):
        self.scan_thread = threading.Thread(target=self.bomb_scanner, daemon=True)
        self.scan_thread.start()

    def bomb_scanner(self):
        while True:
            try:
                if not self.running and not self.defused:
                    bomb = pyautogui.locateOnScreen('bomb.png', confidence=0.7)
                    if bomb:
                        with self.lock:
                            self.running = True
                            self.start_time = time.perf_counter()
                            self.remaining = 40
                elif self.running and not self.defused:
                    green = pyautogui.locateOnScreen('green_bomb.png', confidence=0.7)
                    if green:
                        with self.lock:
                            self.defused = True
                            self.running = False
                            self.reset_timer_time = time.time() + 3  # через 3 секунды сброс
            except Exception as e:
                print(f"Ошибка сканирования: {e}")
            time.sleep(0.1)

    def update_ui(self):
        now = time.perf_counter()
        display_text = "Жду Бомбу!"
        color = "#E94560"

        with self.lock:
            if self.running:
                time_passed = now - self.start_time
                self.remaining = max(0, 40 - time_passed)

                if self.remaining <= 0:
                    self.running = False
                else:
                    if self.remaining <= 5:
                        color = "#E94560"
                    elif self.remaining <= 10:
                        color = "#FFA500"
                    else:
                        color = "#00FFAB"

                    if self.remaining > 11:
                        display_text = f"{int(self.remaining)}"
                    else:
                        ms = int((self.remaining % 1) * 100)
                        display_text = f"{int(self.remaining)}.{ms:02d}"

            elif self.defused:
                display_text = "Раздефано!"
                color = "#00FF00"
                if time.time() >= self.reset_timer_time:
                    self.defused = False

        self.timer_label.config(text=display_text, fg=color)
        self.root.after(16, self.update_ui)

if __name__ == "__main__":
    root = tk.Tk()
    app = BombTimer(root)
    root.mainloop()
