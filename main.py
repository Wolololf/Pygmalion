from rendering.render_loop import render_grid_simulation
from simulation.Simulation import Simulation


def main():
    width = 100
    height = 100

    sim = Simulation(width, height)

    steps = []

    while not sim.is_finished():
        steps.append(sim.simulate_step())

    render_grid_simulation(steps)


if __name__ == "__main__":
    main()
