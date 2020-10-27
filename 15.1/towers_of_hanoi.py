class Peg:

    def __init__(self, number, pegs=None):
        self.number = number
        self.rings = pegs if pegs else list()

    def place_ring(self, ring):
        if self.rings and ring.size > self.rings[-1].size:
            raise Exception()
        
        self.rings.append(ring)
        return ring

    def remove_ring(self):
        ring = self.rings.pop()
        return ring

    def print_state(self):
        print(f"Peg {self.number} state {[r.size for r in self.rings]}")


class Ring:

    def __init__(self, size):
        self.size = size


def move_ring(from_peg, to_peg):
    to_peg.place_ring(from_peg.remove_ring())
    return (from_peg.number, to_peg.number)


def transfer_rings(n, p0, p1, p2):
    moves = list()

    if n == 1:
        moves.append(move_ring(p0, p1))
    else:
        moves += transfer_rings(n - 1, p0, p2, p1)
        moves.append(move_ring(p0, p1))
        moves += transfer_rings(n - 1, p2, p1, p0)

    return moves


n = 3
p0 = Peg(0, [Ring(i) for i in range(n, 0, -1)])
p1 = Peg(1)
p2 = Peg(2)

print(transfer_rings(n, p0, p1, p2))
