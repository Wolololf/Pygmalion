import random

from pathfinding.a_star import pathfinder, grid_neighbours


class Simulation:

    def __init__(self, width, height):
        self.simulationFrame = 0

        self.width = width
        self.height = height

        finder = pathfinder(neighbours=grid_neighbours(width, height))
        self.start = (random.randint(0, width), random.randint(0, height))
        self.end = (random.randint(0, width), random.randint(0, height))

        self.current_position = self.start
        self.travelled_path = [self.current_position]

        self.simulation_step_count, self.path = finder(self.start, self.end)

    def get_simulation_step_count(self):
        return self.simulationFrame

    def simulate_step(self):
        self.current_position = self.path[self.simulationFrame]
        self.travelled_path.append(self.current_position)
        self.simulationFrame += 1

        return [[self.determine_tile_state((x, y)) for x in range(self.width)] for y in range(self.height)]

    def determine_tile_state(self, pos):
        if pos == self.current_position:
            return 3
        elif pos == self.start:
            return 1
        elif pos == self.end:
            return 2
        elif pos in self.travelled_path:
            return 4

        return 0

    def is_finished(self):
        return self.simulationFrame > self.simulation_step_count
