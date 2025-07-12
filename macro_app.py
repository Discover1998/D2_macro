import tkinter as tk
import threading, keyboard, mouse, sys, pystray
from time import sleep
from PIL import Image, ImageDraw
from functools import partial


def hunter_edge():
    keyboard.press('3')
    sleep(0.2)
    keyboard.release('3')
    sleep(0.257)
    mouse.press(button='right')
    sleep(0.05)
    keyboard.press('space')
    sleep(0.038)        
    keyboard.press('c')
    sleep(0.078)        
    mouse.release(button='right')
    sleep(0.015)
    keyboard.release('space')
    sleep(0.024)
    keyboard.release('c')
     
def hunter_ground():
    keyboard.press('3')
    sleep(0.001)
    keyboard.release('3')
    sleep(0.500)
    keyboard.press('space')
    sleep(0.005)
    keyboard.release('space')
    sleep(0.020)
    mouse.press(button='left')
    sleep(0.001)
    mouse.release(button='left')
    sleep(0.010)
    keyboard.press('space')
    sleep(0.005)
    keyboard.release('space')
    sleep(0.010)
    keyboard.press('c')
    sleep(0.025)
    keyboard.release('c')
    
def warlock_edge():
    keyboard.press('3')
    sleep(0.2)
    keyboard.release('3')
    sleep(0.257)
    mouse.press(button='right')
    sleep(0.05)
    keyboard.press('space')
    sleep(0.038)        
    keyboard.press('f')
    sleep(0.078)        
    mouse.release(button='right')
    sleep(0.015)
    keyboard.release('space')
    sleep(0.024)
    keyboard.release('f')

def warlock_ground():
    keyboard.press('3')
    sleep(0.5)
    keyboard.release('3')
    keyboard.press('space')
    sleep(0.01)
    keyboard.release('space')
    sleep(0.01)
    mouse.press(button='left')
    sleep(0.05)
    mouse.release(button='left')
    sleep(0.01)
    keyboard.press('space')
    sleep(0.01)
    keyboard.release('space')   
    sleep(0.01)
    keyboard.press('f')
    sleep(0.01)
    keyboard.release('f') 


class MacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Discover1998 Macro")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        self.character_choice = tk.StringVar(value="Hunter")
        tk.Label(root, text="Choose Character:", font=("Arial", 14), fg="black").pack(pady=5)
        self.character_menu = tk.OptionMenu(root, self.character_choice, "Hunter", "Warlock")
        self.character_menu.pack()
        self.status_label = tk.Label(root, text="Macro: DISARMED", font=("Arial", 14), fg="red")
        self.status_label.pack(pady=10)
        self.macro_armed = False
        threading.Thread(target=self.listen_keys, daemon=True).start()
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

    def listen_keys(self):
        keyboard.on_press_key('f10', lambda e: self.arm_macro(True))
        keyboard.on_press_key('f11', lambda e: self.arm_macro(False))
        keyboard.on_press_key('5', lambda e: self.run_macro('5'))
        keyboard.on_press_key('6', lambda e: self.run_macro('6'))
        keyboard.wait('esc')

    def arm_macro(self, armed):
        self.macro_armed = armed
        if armed:
            self.update_status("ARMED", "green")
        else:
            self.update_status("DISARMED", "black")

    def run_macro(self, key):
        if not self.macro_armed:
            self.update_status("NOT ARMED", "red")
            return
        self.update_status("RUNNING...", "blue")
        threading.Thread(target=self.execute_macro, args=(key,), daemon=True).start()

    def execute_macro(self, key):
        choice = self.character_choice.get().lower()
        if choice == "hunter":
            if key == '5':
                hunter_edge()
            else:
                hunter_ground()
        elif choice == "warlock":
            if key == '5':
                warlock_edge()
            else:
                warlock_ground()
        else:
            self.update_status("INVALID CHARACTER", "red")
            return
        self.update_status("EXECUTED", "orange")

    def update_status(self, text, color):
        self.status_label.config(text=f"Macro: {text}", fg=color)

    def hide_window(self):
        self.root.withdraw()
        threading.Thread(target=self.setup_tray_icon, daemon=True).start()

    def show_window(self, icon=None, item=None):
        self.root.deiconify()
        if icon:
            icon.stop()

    def quit_app(self, icon=None, item=None):
        icon.stop()
        self.root.destroy()
        sys.exit()

    def setup_tray_icon(self):
        image = Image.new("RGB", (64, 64), "black")
        draw = ImageDraw.Draw(image)
        draw.ellipse((16, 16, 48, 48), fill="green")

        menu = pystray.Menu(
            pystray.MenuItem("Show", self.show_window),
            pystray.MenuItem("Exit", self.quit_app)
        )

        icon = pystray.Icon("MacroApp", image, "Macro Controller", menu)
        icon.run()


if __name__ == "__main__":
    root = tk.Tk()
    app = MacroApp(root)
    root.mainloop()
