from rendering.Renderer import Renderer
from simulation.Simulation import Simulation


def main():
    width = 50
    height = 50

    sim = Simulation(width, height)
    renderer = Renderer()

    steps = []

    while not sim.is_finished():
        steps.append(sim.simulate_step())

    renderer.render_grid_simulation(steps)


if __name__ == "__main__":
    main()
