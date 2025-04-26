# Copyright (c) 2025 LXIX. Licensed under MIT.

import tkinter as tk
from tkinter import font as tkfont
import time
import threading
from PIL import Image, ImageTk
import ctypes
import webbrowser
from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui

# Настройка иконки для Windows
myappid = 'lxix.timerbombcs2.2.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class BombTimer:
    def __init__(self, root):
        self.root = root
        self.model = YOLO('best.pt')  # Загружаем обученную модель
        self.setup_ui()
        self.setup_state()
        self.setup_threads()
        self.root.after(10, self.update_ui)

    def setup_ui(self):
        self.root.title("Timer By LXIX v2.0 (YOLO Edition)")
        self.root.geometry("400x350")
        self.root.configure(bg="#1A1A2E")
        self.root.resizable(False, False)

        try:
            icon = Image.open("icon.png")
            photo = ImageTk.PhotoImage(icon)
            self.root.iconphoto(False, photo)
        except:
            print("Иконка не найдена (icon.png)")

        self.title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        self.timer_font = tkfont.Font(family="Courier New", size=26, weight="bold")
        self.status_font = tkfont.Font(family="Arial", size=20, weight="bold")
        self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")

        self.title_label = tk.Label(self.root, text="TimerByLXIX (YOLO)", font=self.title_font, fg="#E94560", bg="#1A1A2E")
        self.title_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=self.status_font, fg="#E94560", bg="#1A1A2E")
        self.status_label.pack(pady=(5, 0))

        self.circle_frame = tk.Frame(self.root, bg="#1A1A2E", width=140, height=140)
        self.circle_frame.pack(pady=10)
        self.circle_frame.pack_propagate(False)

        self.progress_canvas = tk.Canvas(self.circle_frame, width=140, height=140, bg="#1A1A2E", bd=0, highlightthickness=0)
        self.progress_canvas.place(x=0, y=0)

        self.timer_label = tk.Label(self.circle_frame, text="", font=self.timer_font, fg="#E94560", bg="#1A1A2E")
        self.timer_label.place(relx=0.5, rely=0.5, anchor="center")

        self.setup_buttons()

    def setup_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1A1A2E")
        button_frame.pack(pady=20)

        telegram_icon = self.load_icon("telegram_icon.png")
        if telegram_icon:
            btn = tk.Button(
                button_frame, text=" Telegram", image=telegram_icon, compound="left",
                font=self.button_font, fg="white", bg="#16213E",
                activebackground="#0F3460", activeforeground="white",
                bd=0, padx=15, pady=5,
                command=lambda: webbrowser.open("https://t.me/LXIXdev")
            )
            btn.image = telegram_icon
            btn.pack(side="left", padx=10)

        github_icon = self.load_icon("github_icon.png")
        if github_icon:
            btn = tk.Button(
                button_frame, text=" GitHub", image=github_icon, compound="left",
                font=self.button_font, fg="white", bg="#16213E",
                activebackground="#0F3460", activeforeground="white",
                bd=0, padx=15, pady=5,
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
                screenshot = pyautogui.screenshot()
                frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                
                results = self.model(frame, conf=0.7)  # Детекция с уверенностью >70%
                
                red_bomb_detected = False
                green_bomb_detected = False
                
                for result in results:
                    for box in result.boxes:
                        class_id = int(box.cls)
                        if class_id == 0:  # red_bomb
                            red_bomb_detected = True
                        elif class_id == 1:  # green_bomb
                            green_bomb_detected = True

                with self.lock:
                    if not self.running and not self.defused and red_bomb_detected:
                        self.running = True
                        self.start_time = time.perf_counter()
                        self.remaining = 40
                    elif self.running and not self.defused and green_bomb_detected:
                        self.defused = True
                        self.running = False
                        self.reset_timer_time = time.time() + 3

            except Exception as e:
                print(f"Ошибка детекции: {e}")
            time.sleep(0.1)

    def draw_progress_circle(self, progress, color):
        self.progress_canvas.delete("all")

        if progress <= 0 or progress > 1:
            return

        self.progress_canvas.create_oval(10, 10, 130, 130, outline="#2C2C54", width=4)
        self.progress_canvas.create_arc(
            10, 10, 130, 130,
            start=-90,
            extent=progress * 360,
            style=tk.ARC,
            outline=color,
            width=6
        )

    def update_ui(self):
        now = time.perf_counter()
        timer_text = ""
        status_text = ""
        color = "#E94560"
        show_circle = False

        with self.lock:
            if self.running:
                time_passed = now - self.start_time
                self.remaining = max(0, 40 - time_passed)

                if self.remaining <= 0:
                    self.running = False
                else:
                    show_circle = True
                    if self.remaining <= 5:
                        color = "#E94560"
                    elif self.remaining <= 10:
                        color = "#FFA500"
                    else:
                        color = "#00FFAB"

                    if self.remaining > 11:
                        timer_text = f"{int(self.remaining)}"
                    else:
                        ms = int((self.remaining % 1) * 100)
                        timer_text = f"{int(self.remaining)}.{ms:02d}"

            elif self.defused:
                status_text = "Раздефано!"
                color = "#00FF00"
                if time.time() >= self.reset_timer_time:
                    self.defused = False
            else:
                status_text = "Жду Бомбу!"

        self.status_label.config(text=status_text, fg=color)
        self.timer_label.config(text=timer_text, fg=color)
        self.progress_canvas.delete("all")

        if show_circle:
            self.draw_progress_circle(self.remaining / 40, color)

        self.root.after(16, self.update_ui)

if __name__ == "__main__":
    root = tk.Tk()
    app = BombTimer(root)
    root.mainloop()