from bearlibterminal import terminal as blt

from observer.events import Event
from observer.subscriber import Subscriber


def handle_keys(key)->dict:
    # Movement keys
    if key in [blt.TK_UP, blt.TK_K]:
        return {"move": (0, -1)}
    elif key in [blt.TK_DOWN, blt.TK_J]:
        return {"move": (0, 1)}
    elif key in [blt.TK_LEFT, blt.TK_H]:
        return {"move": (-1, 0)}
    elif key in [blt.TK_RIGHT, blt.TK_L]:
        return {"move": (1, 0)}
    elif key == blt.TK_Y:
        return {"move": (-1, -1)}
    elif key == blt.TK_U:
        return {"move": (1, -1)}
    elif key == blt.TK_B:
        return {"move": (-1, 1)}
    elif key == blt.TK_N:
        return {"move": (1, 1)}

    # if key.vk == libtcod.KEY_ENTER and key.lalt:
    #     # Alt + Enter: toggle full screen
    #     return {"fullscreen": True}

    elif key in (blt.TK_Q, blt.TK_CLOSE, blt.TK_ESCAPE):
        # Exit the game
        return {"exit": True}

    # No key was pressed
    return {}


class InputHandler(Subscriber):
    def __init__(self, name="InputHandler"):
        """
        needs to know about the following events:
            input
        :param name:
        """
        super().__init__(name)

    def update(self, key):
        print("successful subclass")
        action = handle_keys(key)
