import board
# print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

# Encoder setup
encoder_handler = EncoderHandler()
encoder_handler.divisor = 2
encoder_handler.pins = (
    (board.GP15, board.GP14, board.GP29, False),
    (board.GP7, board.GP6, board.GP0, False),
)

# keyboard setup
keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP4, board.GP5, board.GP8, board.GP9)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keyboard extentions
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.D, KC.F, KC.E, KC.D,
        KC.A, KC.B, KC.C, KC.D,
        KC.A, KC.B, KC.C, KC.D,
        KC.A, KC.B, KC.C, KC.D,
    ]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.VOLD, KC.VOLU, KC.MUTE)),
]

if __name__ == "__main__":
    keyboard.go()
