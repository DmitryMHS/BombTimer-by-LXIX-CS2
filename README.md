
# 💣 TimerByLXIX — CS2 Bomb Timer

---

## 💖 Благодарности

Особая благодарность нашим спонсорам, которые помогают развивать проект:

| Спонсор          | Поддержка с       | Уровень       |
|------------------|-------------------|---------------|
| [Пусто](https://github.com/DmitryMHS) | Апрель 2025       | 💎 «СПОНСОР» 💎       |

---

## ☕ Поддержка
Если проект вам помог, можно [поддержать меня и стать нашим спонсором!](https://boosty.to/dmitrymhs/donate)

---

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green?logo=python" alt="Tkinter">
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License">
</div>

<br>

## 🎯 Что делает программа?

**TimerByLXIX** — это утилита с автоматическим таймером бомбы для CS2.  
Она определяет момент установки бомбы и запускает обратный отсчёт (40 секунд) до взрыва.

---

## 🧠 Основные функции

- 🖥️ Современный GUI на Tkinter с минималистичным стилем
- 🧠 Автообнаружение **иконки бомбы** на экране
- ⏱️ **Цветной таймер**: от Зелёного до Красного в зависимости от оставшегося времени
- 📷 Иконки и ссылки на Telegram/GitHub прямо в интерфейсе
- ⚡ Работает в фоне, обновляется ~60 FPS

---

## 📷 Интерфейс

![TimerByLXIX GUI](https://sun9-32.userapi.com/impg/HEHDXRwbiw-8Y22pWp7PFZ6aoiyRcjYPrP2k4Q/QVJc1eYNByg.jpg?size=401x381&quality=95&sign=b740849ebd013fb4e370fdce381556a2&type=album)

## 🌀 Работа в действии

![TimerByLXIX Demo](https://i.imgur.com/TrWaeL1.gif)

---


## 📦 Установка

1. Клонируйте проект:
   ```bash
   git clone https://github.com/DmitryMHS/BombTimer-by-LXIX-CS2.git
   cd TimerByLXIX
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   Пример содержимого `requirements.txt`:
   ```
   pyautogui
   pillow
   ```

---

## 🚀 Запуск

```bash
python main.py
```

Перед первым запуском убедитесь, что у вас есть:
- `bomb.png` и `green_bomb.png` — иконки бомбы из CS2 (для автоопределения на экране)
- `icon.png` — иконка приложения
- `telegram_icon.png` и `github_icon.png` — иконки для кнопок

---

## 👨‍🏫 Как это работает

1. Программа сканирует экран на наличие иконки `bomb.png`
2. Если находит — запускает отсчёт (40 секунд)
3. Меняет цвет текста в зависимости от времени:
   - 🟢 >10 сек
   - 🟠 5-10 сек
   - 🔴 <5 сек
4. Если бомба исчезает с экрана или находится `green_bomb.png` — таймер сбрасывается

---

## 🛠 Используемые технологии

- **Python 3.10+** — основной язык
- **Tkinter** — графический интерфейс
- **PyAutoGUI** — определение бомбы на экране
- **Pillow** — работа с изображениями

---

## 📜 Лицензия

Проект распространяется под лицензией **MIT**  
Подробности в [LICENSE](LICENSE)

---

<div align="center">
  <strong>Создано с ❤️ для игроков CS2</strong><br>
  ✉️ TG: @LXIX_DEVELOPER | 💼
</div>
