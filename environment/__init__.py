"Environment Module"
from Box2D import b2EdgeShape, b2FixtureDef, b2PolygonShape


from settings import RENDER
from creature import Creature, find_adjacent_edges
from framework.framework import Framework
from maths.maths import line_to_rectangle
from maths.maths import get_position_of_creature
THICKNESS = 0.5


class Environment(Framework):
    "Environment class"
    name = "Evolution Simulator"

    speed = 1000  # platform speed

    def __init__(self, creature: Creature):
        super(Environment, self).__init__()
        self.settings.drawJoints = False
        self.settings.render = RENDER

        Environment.description = f"Creature #{creature.identity}"

        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-500, 0), (500, 0)])
        )

        body = {}

        for edge in creature.edges:
            vertex = creature.vertices[edge[0]], creature.vertices[edge[1]]
            point = line_to_rectangle(*vertex, THICKNESS)

            fixture = b2FixtureDef(
                shape=b2PolygonShape(vertices=point),
                density=2,
                friction=0.6,
            )
            fixture.filter.groupIndex = -1
            body[tuple(edge)] = self.world.CreateDynamicBody(
                fixtures=fixture,
            )
        print(len(body))

        for edge in creature.edges:
            adjacent = find_adjacent_edges(edge, creature.edges)
            for a_edge in adjacent:
                anchor = int(creature.vertices[edge[0]][0]), int(creature.vertices[edge[0]][1])
                self.world.CreateRevoluteJoint(
                    bodyA=body[tuple(edge)],
                    bodyB=body[tuple(a_edge)],
                    anchor=anchor,
                    collideConnected=True,
                    motorSpeed=100,
                    maxMotorTorque=250,
                    enableMotor=True,
                )

        Environment.starting_position = get_position_of_creature(body.values())
