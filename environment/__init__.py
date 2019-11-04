"Environment Module"
from Box2D import b2EdgeShape, b2FixtureDef, b2PolygonShape

from settings import STEP_LIMIT, MOTOR_SPEED, MAX_MOTOR_TORQUE, DENSITY, FRICTION
from creature import Creature, find_adjacent_edges
from framework.framework import Framework
from maths.maths import line_to_rectangle
from maths.maths import get_position_of_creature
THICKNESS = 0.5


class Environment(Framework):
    "Environment class"
    speed = 1000  # platform speed
    env = None

    def __init__(self, name, creatures):
        Environment.name = name
        self.env = super(Environment, self).__init__()
        self.settings.drawJoints = False
        Environment.step_limit = STEP_LIMIT

        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-1000, -1), (1000, -1)])
        )
        Environment.description = []
        Environment.creature_bodies = {}
        for creature in creatures:
            body = {}

            for edge in creature.edges:
                vertex = creature.vertices[edge[0]], creature.vertices[edge[1]]
                point = line_to_rectangle(*vertex, THICKNESS)

                fixture = b2FixtureDef(
                    shape=b2PolygonShape(vertices=point),
                    density=DENSITY,
                    friction=FRICTION,
                )
                fixture.filter.groupIndex = -1
                body[tuple(edge)] = self.world.CreateDynamicBody(
                    fixtures=fixture,
                )

            for edge in creature.edges:
                adjacent = find_adjacent_edges(edge, creature.edges)
                for a_edge in adjacent:
                    anchor = int(creature.vertices[edge[0]][0]), int(creature.vertices[edge[0]][1])
                    self.world.CreateRevoluteJoint(
                        bodyA=body[tuple(edge)],
                        bodyB=body[tuple(a_edge)],
                        anchor=anchor,
                        collideConnected=True,
                        motorSpeed=MOTOR_SPEED,
                        maxMotorTorque=MAX_MOTOR_TORQUE,
                        enableMotor=True,
                    )
            Environment.creature_bodies[creature.identity] = body
            Environment.starting_position[creature.identity] = get_position_of_creature(
                body.values())
        if len(creatures) == 1:
            Environment.description.append(f"Creature #{creatures[0].identity}")
