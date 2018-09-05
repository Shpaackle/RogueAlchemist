import tcod as libtcod

from colors import Color
from game_messages import Message
from game_states import GameStates
from render_functions import RenderOrder


def kill_player(player):
    player.char = "%"
    player.color = Color.DEEP_PINK

    return Message('You died', "red"), GameStates.PLAYER_DEAD


def kill_monster(monster)->Message:
    death_message: Message = Message(f"{monster.name.capitalize()} is dead!", "orange")

    monster.char = "%"
    monster.color = Color.DEEP_PINK
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = f"remains of {monster.name}"
    monster.render_order = RenderOrder.CORPSE

    return death_message
