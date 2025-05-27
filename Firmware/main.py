print("Starting")

# Basic imports
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.statusled import statusLED

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # Pins connected to each key
        self.matrix = [
            KeysScanner(
                pins=[
                    board.GP1,   # Key 1 -> KC.N1
                    board.GP6,   # Key 2 -> KC.N2
                    board.GP27,  # Key 3 -> KC.N3
                    board.GP2,   # Key 4 -> KC.N4
                    board.GP7,   # Key 5 -> KC.N5
                    board.GP28,  # Key 6 -> KC.N6
                    board.GP4,   # Key 7 -> KC.N7
                    board.GP0,   # Key 8 -> KC.N8
                    board.GP29,  # Key 9 -> KC.N9
                    board.GP26,  # Key 0 -> KC.N0
                ]
            )
        ]

        # Assign key positions in numpad layout order
        self.coord_mapping = list(range(10))

        # One layer: numpad
        self.keymap = [
            [
                KC.N7, KC.N8, KC.N9,   # Keys 7, 8, 9
                KC.N4, KC.N5, KC.N6,   # Keys 4, 5, 6
                KC.N1, KC.N2, KC.N3,   # Keys 1, 2, 3
                KC.N0,                # Key 0
            ]
        ]

keyboard = MyKeyboard()

# Macros (optional, in case you expand)
macros = Macros()
keyboard.modules.append(macros)

# Optional: Add LED indicator logic if you want
# status_leds = statusLED(led_pins=[board.GP22])  # example
# keyboard.extensions.append(status_leds)

if __name__ == '__main__':
    keyboard.go()
