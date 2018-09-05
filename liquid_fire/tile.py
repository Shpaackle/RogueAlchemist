from .point import Point


class Tile:
    def __init__(self, pos: Point, tile):
        self.pos = pos
        self.tile = tile

    def __eq__(self, other):
        return self.pos == other.pos and self.tile == other.tile
