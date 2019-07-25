from glob import glob

import numpy as np

from Box2D import b2EdgeShape, b2FixtureDef, b2PolygonShape
from creature.creature import (create_edges, create_vertices,
                               find_adjacent_edges)
from framework.framework import Framework
from maths.maths import line_to_rectangle

THICKNESS = 0.5


class Environment(Framework):
    name = "Evolution Simulator"
    description = "Evolution Simulator"
    speed = 1000  # platform speed

    def __init__(self):
        super(Environment, self).__init__()

        # The ground
        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-500, 0), (500, 0)])
        )

        vertices = create_vertices(10, 10)
        edges = create_edges(10)

        my_id = len(glob("data/vertices/*.npy"))
        np.save("data/vertices/%d" % my_id, vertices)
        np.save("data/edges/%d" % my_id, vertices)

        body = {}

        for edge in edges:
            vertex = vertices[edge[0]], vertices[edge[1]]
            point = line_to_rectangle(*vertex, THICKNESS)

            fixture = b2FixtureDef(
                shape=b2PolygonShape(vertices=point),
                density=2,
                friction=0.6,
            )
            fixture.filter.groupIndex = -1

            body[edge] = self.world.CreateDynamicBody(
                fixtures=fixture,
            )

        for edge in edges:
            adjacent = find_adjacent_edges(edge, edges)
            for a_edge in adjacent:
                anchor = vertices[edge[0]]
                print("connectiong", edge, a_edge, "at", anchor)
                self.world.CreateRevoluteJoint(
                    bodyA=body[edge],
                    bodyB=body[a_edge],
                    anchor=anchor,
                    collideConnected=True,
                    motorSpeed=100,
                    maxMotorTorque=250,
                    enableMotor=True,
                )
