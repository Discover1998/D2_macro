# Destiny 2 Macro
Destiny 2 Macro Controller is a lightweight Python-based desktop tool designed to automate character-specific actions (such as Hunter’s shatter skate or Warlock movement combos) in Destiny 2.

### windows
```bash
pip install keyboard
```

```bash
pip install mouse
```

```bash
pip install pystray
```

```bash
pip install pillow
```

```bash
pip install pyinstaller
```

---

Note run the following in CMD (replace "username" with your actual Windows username):
```bash
pyinstaller --onefile --windowed "C:\Users\username\Desktop\macro_app.py"
```

This will generate a .exe file inside the dist/ folder.

# How to Use

### Select your character in the GUI (Hunter / Warlock)
| Key       | Action                     |
|-----------|----------------------------|
| `F10`     | Arm the macro              |
| `F11`     | Disarm the macro           |
| `5`       | Execute **Edge** macro     |
| `6`       | Execute **Ground** macro   |

