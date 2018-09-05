from bearlibterminal import terminal as blt
import tcod as libtcod

from colors import Color
from components.fighter import Fighter
from death_functions import kill_monster, kill_player
from entity import Entity, get_blocking_entities_at_location
from fov_functions import initialize_fov, recompute_fov
from game_messages import MessageLog
from game_states import GameStates
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, Console, render_all, RenderOrder


def main():
    screen_width: int = 80
    screen_height: int = 35

    bar_width: int = 20
    panel_height: int = 7
    panel_y: int = screen_height - panel_height
    ui_layer = 10

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 80
    map_height = 28
    max_monsters_per_room = 3

    con = Console(x=0, y=0, width=screen_width, height=screen_height)
    panel = Console(0, panel_y, screen_width, panel_height, layer=ui_layer)

    title = "Rogue Alchemist"
    font = "mplus-1p-regular.ttf"

    fighter_component = Fighter(hp=30, defense=2, power=5)
    player = Entity(x=0, y=0, char='@', color=Color.BLACK, name='Player', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component)
    entities = [player]

    game_map = GameMap(map_width, map_height)
    game_map.generate_dungeon(player, entities, max_monsters_per_room)
    # game_map.generate_dungeon(map_width, map_height, cave=True)
    start_room = game_map.dungeon.rooms[0]

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    colors = {
        "dark_wall": Color.DARK_SLATE_GRAY,
        "dark_ground": Color.DIM_GRAY,
        "light_wall": Color.LIGHT_SLATE_GRAY,
        "light_ground": Color.LIGHT_GRAY,
        "dark_door": Color.SADDLE_BROWN,
        "light_door": Color.BROWN,
        "test": Color.GOLD,
    }

    fov_recompute = True
    fov_map = initialize_fov(game_map)

    message_log = MessageLog(message_x, message_width, message_height)

    key = None

    blt.open()  # initializes BearLib Terminal instance with default parameters
    terminal_options = f"window: title={title}, size={str(screen_width)}x{str(screen_height)}; font:{font}, size=12"
    blt.set(terminal_options)

    game_state = GameStates.PLAYERS_TURN

    while True:
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, colors)
        blt.refresh()

        fov_recompute = False

        # remove player's previous position
        clear_all(entities)

        if blt.has_input():  # if no inputs, don't wait
            key = blt.read()

        action = handle_keys(key)
        key = None

        movement = action.get("move")
        exit_game = action.get("exit")

        player_turn_results = []

        if movement and game_state == GameStates.PLAYERS_TURN:
            dx, dy = movement
            destination_x = player.x + dx
            destination_y = player.y + dy

            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)

                if target:
                    attack_results = player.fighter.attack(target)
                    player_turn_results.extend(attack_results)
                else:
                    player.move(*movement)

                    fov_recompute = True

                game_state = GameStates.ENEMY_TURN

        if exit_game:
            blt.close()
            return True

        for player_turn_result in player_turn_results:
            message = player_turn_result.get("message")
            dead_entity = player_turn_result.get("dead")

            if message:
                message_log.add_message(message)

            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)

                message_log.add_message(message)

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                visible = libtcod.map_is_in_fov(fov_map, entity.x, entity.y)
                if entity.ai:
                    enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)

                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get("message")
                        dead_entity = enemy_turn_result.get("dead")

                        if message:
                            message_log.add_message(message)

                        if dead_entity:
                            if dead_entity == player:
                                message, game_state = kill_player(dead_entity)
                            else:
                                message = kill_monster(dead_entity)

                            message_log.add_message(message)

                            if game_state == GameStates.PLAYER_DEAD:
                                break

            if game_state == GameStates.PLAYER_DEAD:
                break

            game_state = GameStates.PLAYERS_TURN


if __name__ == "__main__":
    main()
