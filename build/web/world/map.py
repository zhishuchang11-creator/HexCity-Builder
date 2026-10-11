from world.tile import Tile

class HexMap:
    def __init__(self):
        self.tiles = []
        self.add_tile(0, 0, "grass")

    def add_tile(self, q, r, tile_type):
        if self.get_tile(q, r) is None:
            self.tiles.append(Tile(q, r, tile_type))

    def get_tile(self, q, r):
        for tile in self.tiles:
            if tile.q == q and tile.r == r:
                return tile
        return None

    def is_adjacent_to_existing(self, q, r):
        neighbours = [
            (q + 1, r),
            (q - 1, r),
            (q, r + 1),
            (q, r - 1),
            (q + 1, r - 1),
            (q - 1, r + 1)
        ]
        return any(self.get_tile(nq, nr) for nq, nr in neighbours)
    