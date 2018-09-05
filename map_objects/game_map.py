from random import randint
from typing import List

from components.ai import BasicMonster
from components.fighter import Fighter

from colors import Color
from entity import Entity
from map_objects.tile import Tile
from map_objects import dungeonGenerator
from render_functions import RenderOrder


class Room:
    def __init__(self, x: int, y: int, width: int, height: int, label: str=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if label is None:
            self.label = self.random_type()
        else:
            self.label = label

    def x2(self)->int:
        return self.x + self.width

    def y2(self)->int:
        return self.y + self.height

    def random_type(self)->str:
        # TODO: create method to choose random type
        return "untyped"


class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = []
        self.dungeon = dungeonGenerator.dungeonGenerator(width=width, height=height)

    def initialize_tiles(self):
        # creates a 2d array [self.width x self.height] of Tile objects set to not block
        # effectively setting the map to empty
        self.tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

    def place_entities(self, room, entities: List[Entity], max_monsters_per_room: int):
        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)

        for i in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(room.x + 1, room.x + room.width - 1)
            y = randint(room.y + 1, room.y + room.height - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y]):
                if randint(0, 100) < 80:
                    fighter_component = Fighter(hp=10, defense=0, power=3)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'o', Color.FOREST_GREEN, 'Orc', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                else:
                    fighter_component = Fighter(hp=16, defense=1, power=4)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'T', Color.DARK_GREEN, 'Troll', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)

                entities.append(monster)

    def is_blocked(self, x: int, y: int)->bool:
        if self.tiles[x][y].blocked:
            return True

        return False

    def generate_dungeon(self, player: Entity, entities: list, max_monsters_per_room: int, cave: bool=False):
        # used as placeholder to create dungeon from dungeonGenerator
        # TODO need to implement properly

        self.initialize_tiles()

        if cave:
            self.dungeon.generateCaves(p=40, smoothing=4)
            unconnected = self.dungeon.findUnconnectedAreas()
            for area in unconnected:
                if len(area) < 35:
                    for x, y in area:
                        self.dungeon.grid[x][y] = dungeonGenerator.EMPTY
        else:
            self.dungeon.placeRandomRooms(5, 11, 2, 4, 500)
            self.dungeon.generateCorridors()
            self.dungeon.connectAllRooms(30)
            self.dungeon.pruneDeadends(20)
            self.dungeon.placeWalls()

        for x, y, tile in self.dungeon:
            if tile == dungeonGenerator.WALL or tile == dungeonGenerator.EMPTY:
                self.tiles[x][y].blocked = True
                self.tiles[x][y].block_sight = True
            elif tile == dungeonGenerator.DOOR:
                self.tiles[x][y].block_sight = True

        start_room = self.dungeon.rooms[0]
        player.x = start_room.x + 1
        player.y = start_room.y + 1

        for room in self.dungeon.rooms:
            self.place_entities(room, entities, max_monsters_per_room)
