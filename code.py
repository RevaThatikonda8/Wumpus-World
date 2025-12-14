import random

GRID_SIZE = 4

# Symbols
EMPTY = "."
PIT = "P"
WUMPUS = "W"
GOLD = "G"
AGENT = "A"

class WumpusWorld:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.agent_pos = (0, 0)
        self.place_objects()
        self.grid[0][0] = AGENT
        self.game_over = False

    def place_objects(self):
        # Place Wumpus
        self.place_random(WUMPUS)
        # Place Gold
        self.place_random(GOLD)
        # Place Pits
        for _ in range(3):
            self.place_random(PIT)

    def place_random(self, obj):
        while True:
            x, y = random.randint(0, 3), random.randint(0, 3)
            if self.grid[x][y] == EMPTY and (x, y) != (0, 0):
                self.grid[x][y] = obj
                break

    def display(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def get_percepts(self, x, y):
        percepts = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if self.grid[nx][ny] == PIT:
                    percepts.append("Breeze")
                if self.grid[nx][ny] == WUMPUS:
                    percepts.append("Stench")
        if self.grid[x][y] == GOLD:
            percepts.append("Glitter")
        return percepts

    def move_agent(self, move):
        x, y = self.agent_pos
        self.grid[x][y] = EMPTY

        if move == "up" and x > 0:
            x -= 1
        elif move == "down" and x < 3:
            x += 1
        elif move == "left" and y > 0:
            y -= 1
        elif move == "right" and y < 3:
            y += 1

        self.agent_pos = (x, y)
        self.check_status()
        self.grid[x][y] = AGENT

    def check_status(self):
        x, y = self.agent_pos
        cell = self.grid[x][y]

        if cell == PIT:
            print("💀 Fell into a pit! Game Over.")
            self.game_over = True
        elif cell == WUMPUS:
            print("👹 Eaten by the Wumpus! Game Over.")
            self.game_over = True
        elif cell == GOLD:
            print("✨ You found the Gold! You Win!")
            self.game_over = True

def main():
    world = WumpusWorld()

    while not world.game_over:
        world.display()
        x, y = world.agent_pos
        percepts = world.get_percepts(x, y)
        print("Percepts:", percepts)

        move = input("Move (up/down/left/right): ").lower()
        world.move_agent(move)

if __name__ == "__main__":
    main()

