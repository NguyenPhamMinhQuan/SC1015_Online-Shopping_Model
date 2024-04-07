import pygame
import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = height
        self.width = width
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None

        # setting the initial line
        initial_blocks = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # Example pattern, customize as needed
            # Add more patterns as needed
        ]

        # Fill the field with empty cells
        self.field = [[0] * width for _ in range(height)]

        # Insert the initial configuration of blocks at the bottom of the field
        for row_index, row in enumerate(initial_blocks):
            self.field[height - len(initial_blocks) + row_index] = row

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

   def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                # Shift all rows above the cleared row downwards
                for i1 in range(i, 0, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
        self.figure = None


    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = 1
        self.break_lines()
        self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

    def evaluate_placement(self, col, rotation, row):
        # Simulate placing two consecutive blocks and evaluate the resulting grid state
        grid_state = [row[:] for row in self.field]
        
        # Apply the first block to the grid state
        new_grid_state = self.apply_block_to_grid(grid_state, col, rotation)

        # Calculate the score based on the resulting grid state
        score = self.calculate_score(new_grid_state)

        return score

    def apply_block_to_grid(self, grid_state, col, rotation):
        # Apply the first block to the grid state
        new_grid_state = [row[:] for row in grid_state]
        block_image = self.figure.image()
        for i in range(4):
            for j in range(4):
                if i * 4 + j in block_image:
                    if self.figure.y + i >= self.height or col + j >= self.width:
                        # Block placement is out of bounds, skip it
                        continue
                    new_grid_state[self.figure.y + i][col + j] = 1  # Mark the cell as occupied by the block
        return new_grid_state

    def calculate_score(self, grid_state):
        # Calculate the score based on the resulting grid state
        # For simplicity, let's count the number of filled cells in the bottom row
        bottom_row = grid_state[-1]
        score = sum(bottom_row)
        return score


# Initialize the game engine
pygame.init()

# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
