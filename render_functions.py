from bearlibterminal import terminal as blt
from enum import Enum
from map_objects import dungeonGenerator as dungeon
import tcod as libtcod


class RenderOrder(Enum):
    BACKGROUND = 0
    CORPSE = 1
    ITEM = 2
    ACTOR = 3


class Console:
    def __init__(self, x: int, y: int, width: int, height: int, layer: int=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.layer = layer

        self.back_color = "transparent"


def render_bar(layer: int, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    blt.layer(layer)
    last_bg = blt.state(blt.TK_BKCOLOR)
    blt.bkcolor(blt.color_from_name(back_color))
    blt.clear_area(x, y, total_width, 1)
    blt.bkcolor(last_bg)

    if bar_width > 0:
        last_bg = blt.state(blt.TK_BKCOLOR)
        blt.bkcolor(blt.color_from_name(bar_color))
        blt.clear_area(x, y, bar_width, 1)
        blt.bkcolor(last_bg)

    text: str = f"{name}: {value}/{maximum}"
    x_centered = x + int((total_width - len(text)) / 2)
    blt.color("white")
    blt.puts(x_centered, y, text)


def render_all(entities: list, player, game_map, fov_map, fov_recompute: bool, message_log, screen_width: int, screen_height: int, bar_width: int, panel_height: int, panel_y: int, colors):
    blt.layer(0)
    if fov_recompute:
        if game_map.dungeon:
            for x, y, tile in game_map.dungeon:
                visible: bool = libtcod.map_is_in_fov(fov_map, x, y)
                if visible:
                    if tile in [dungeon.FLOOR, dungeon.CORRIDOR]:
                        blt.bkcolor(blt.color_from_name(colors.get("light_ground", "#FF1493")))
                    elif tile == dungeon.DOOR:
                        blt.bkcolor(blt.color_from_name(colors.get("light_door", "#FF1493")))
                    elif tile == dungeon.WALL:
                        blt.bkcolor(blt.color_from_name(colors.get("light_wall", "#FF1493")))

                    # mark tile as explored
                    game_map.tiles[x][y].explored = True

                elif game_map.tiles[x][y].explored:
                    if tile in [dungeon.FLOOR, dungeon.CORRIDOR]:
                        blt.bkcolor(blt.color_from_name(colors.get("dark_ground", "#FF1493")))
                    elif tile == dungeon.DOOR:
                        blt.bkcolor(blt.color_from_name(colors.get("dark_door", "#FF1493")))
                    elif tile == dungeon.WALL:
                        blt.bkcolor(blt.color_from_name(colors.get("dark_wall", "#FF1493")))
                elif tile == dungeon.CAVE:
                    blt.bkcolor(blt.color_from_name("light brown"))
                    blt.put(x, y, ' ')
                else:
                    blt.bkcolor(blt.color_from_name("black"))
                blt.put(x, y, ' ')

            for de in game_map.dungeon.deadends:
                x, y = de
                visible: bool = libtcod.map_is_in_fov(fov_map, x, y)
                if visible:
                    blt.bkcolor(blt.color_from_name("orange"))
                    game_map.tiles[x][y].explored = True
                    blt.put(x, y, ' ')
                elif game_map.tiles[x][y].explored:
                    blt.bkcolor(blt.color_from_name("dark orange"))
                    blt.put(x, y, ' ')
        else:
            # Draw all tiles in the game map
            for y in range(game_map.height):
                for x in range(game_map.width):
                    wall: bool = game_map.tiles[x][y].block_sight

                    if wall:
                        blt.bkcolor(blt.color_from_name(colors.get("dark_wall")))
                        blt.put(x, y, ' ')
                    else:
                        blt.bkcolor(blt.color_from_name(colors.get("dark_ground")))
                        blt.put(x, y, ' ')

    entities_in_render_order = sorted(entities, key=lambda ent: ent.render_order.value)

    # Draw all entities in the list
    for entity in entities_in_render_order:
        draw_entity(entity, fov_map)

    # libtcod.console_print_ex(con, 1, screen_height - 2, libtcod.BKGND_NONE, libtcod.LEFT,
    # 'HP: {0:02}/{1:02}'.format(player.fighter.hp, player.fighter.max_hp))
    # blt.color(blt.color_from_name("white"))
    # blt.bkcolor(blt.color_from_name("black"))
    # blt.print(x=1, y=screen_height - 2, s=f"HP: {player.fighter.hp:02}/{player.fighter.max_hp:02}")

    current_layer = 10
    render_bar(current_layer, 1, panel_y, bar_width, "HP", player.fighter.hp, player.fighter.max_hp, "light red", "darkest red")

    y = 2
    for message in message_log.messages:
        blt.color(blt.color_from_name(message.color))
        blt.puts(message_log.x, panel_y + y, message.text)
        y += 1

    blt.refresh()


def clear_all(entities: list):
    for entity in entities:
        clear_entity(entity)


def draw_entity(entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        blt.color(blt.color_from_name(entity.color))
        blt.bkcolor(blt.color_from_name("transparent"))
        blt.put_ext(entity.x, entity.y, 0, -2, entity.char, None)


def clear_entity(entity):
    # erase the character that represents this object
    blt.bkcolor(blt.color_from_name("transparent"))
    blt.put_ext(entity.x, entity.y, 0, 0, ' ', None)
