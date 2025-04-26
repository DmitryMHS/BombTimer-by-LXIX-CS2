# 💣 TimerByLXIX — CS2 Bomb Timer v2.0 (YOLO Edition)

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
  <img src="https://img.shields.io/badge/AI-YOLOv8-red?logo=openai" alt="YOLOv8">
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License">
</div>

<br>

## 🎯 Что делает программа?

**TimerByLXIX YOLO Edition** — это усовершенствованная версия утилиты с автоматическим таймером бомбы для CS2.  
Теперь программа использует нейросеть YOLOv8 для точного определения бомбы на экране и запускает обратный отсчёт (40 секунд) до взрыва.

---

## 🌟 Новое в версии 2.0
- 🧠 ИИ-детекция бомбы через YOLOv8 (точность до 95%)
- ⚡ Оптимизированная работа с видеокартами NVIDIA
- 🔧 Поддержка кастомного обучения модели
- 🖥️ Улучшенный интерфейс с сохранением фирменного стиля

## 🧠 Основные функции

- 🖥️ Современный GUI на Tkinter с минималистичным стилем
- 🧠 **Автообнаружение бомбы через YOLOv8** (вместо шаблонов)
- ⏱️ **Цветной таймер**: от Зелёного до Красного в зависимости от оставшегося времени
- 📷 Иконки и ссылки на Telegram/GitHub прямо в интерфейсе
- ⚡ Работает в фоне с высокой точностью

---

## 📷 Интерфейс

![TimerByLXIX GUI](https://sun9-32.userapi.com/impg/HEHDXRwbiw-8Y22pWp7PFZ6aoiyRcjYPrP2k4Q/QVJc1eYNByg.jpg?size=401x381&quality=95&sign=b740849ebd013fb4e370fdce381556a2&type=album)

## 🌀 Работа в действии

![Demo GIF](https://github.com/DmitryMHS/BombTimer-by-LXIX-CS2/raw/main/DEMO.gif)

---

## 📦 Установка

1. Клонируйте проект:
   ```bash
   git clone https://github.com/DmitryMHS/BombTimer-by-LXIX-CS2.git
   cd TimerByLXIX-YOLO
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. (Обученная модель `best.pt` должна быть в папке с программой)

---

## 🚀 Запуск

```bash
python main.py
```

---

## 👨‍🏫 Как это работает

1. Программа использует YOLOv8 для сканирования экрана
2. При обнаружении бомбы (класс 0) - запускает отсчёт 40 секунд
3. Меняет цвет текста в зависимости от времени:
   - 🟢 >10 сек
   - 🟠 5-10 сек
   - 🔴 <5 сек
4. При обнаружении обезвреженной бомбы (класс 1) - показывает "Раздефано!"

---

## 🛠 Используемые технологии

- **Python 3.10+** — основной язык
- **Tkinter** — графический интерфейс
- **YOLOv8** — детекция объектов
- **OpenCV** — обработка изображений
- **PyAutoGUI** — работа с экраном

---

## 📜 Лицензия

Проект распространяется под лицензией **MIT**  
Подробности в [LICENSE](LICENSE)

---

<div align="center">
  <strong>Создано с ❤️ для игроков CS2</strong><br>
  ✉️ TG: @LXIX_DEVELOPER | 💼 GitHub: DmitryMHS
</div>