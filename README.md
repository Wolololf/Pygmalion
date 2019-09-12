# Pygmalion
Hopefully, this will become a basic simulation of medieval infantry combat driven by an AI.

# Game plan
## Visualisation
1. Figure out how to draw a grid and fill grid spaces with different colours.
2. Figure out how to animate a grid over time.

## Entities

All entities need position information. Some may later also get rotation information (if it becomes relevant for the simulation and/or visualisation).
Entity config data should be stored in JSON files, loaded in and assigned to instances of units.

### Grid tile
#### Data
1. Type
2. Traversal cost

### Unit
#### Data
1. Type
2. Movement speed
3. Hitpoints
4. Damage
5. Range

#### Actions
1. Move
2. Attack

### Target

## Behaviour priorities
1. Reach goal
2. Stay alive
3. Kill enemies

The priorities should pick the highest one based on a simple set of rules, e.g. "Stay alive" becomes more important the lower the health is, and "reach goal" becomes more important the further the goal is.
The factor for how quickly each goal increases should later be defined by the AI but for now I'll pick some values.

## Simulation scenario progression
Scenario data should be stored in JSON files and include information such as terrain size and tile distribution as well as unit and goal placements.
Scenarios may also contain victory conditions such as reaching an area, surviving some amount of ticks or killing certain amounts or types of enemies.

1. Unarmed unit walking towards a target on equal-cost terrain.
2. Armed unit walking towards and attacking an unarmed opponent.
3. Armed unit attacking armed opponent.
4. Two armed units attacking opponent in sequence (ideally, one should run away first).
5. Ranged unit
...?

### Pathfinding
Basic A*

### Machine learning
The AI will be trained on a set of training scenarios that are run repeatedly before it is then evaluated against an unknown test scenario.

For now, each unit is its own AI (the AI will be trained per unit type?) and is aware of the whole grid for now, but might later be limited to data in sight.
#### Input data
1. Health
2. Current position
3. Path to target
4. Positions and health of enemies and allies

#### Output data
1. Priorities
2. Intermediate target
3. Actions
