"Environment Module"
from settings import RENDER

from glob import glob
from random import randint

import numpy as np

from Box2D import b2EdgeShape, b2FixtureDef, b2PolygonShape
from creature import (create_edges, create_vertices,
                               find_adjacent_edges)
from framework.framework import Framework
from maths.maths import line_to_rectangle
from maths.maths import get_position_of_creature
THICKNESS = 0.5

class Environment(Framework):
    "Environment class"
    name = "Evolution Simulator"

    speed = 1000  # platform speed

    def __init__(self):
        super(Environment, self).__init__()
        self.settings.drawJoints = False
        self.settings.render = RENDER
        edges = None
        vertices = None

        if self.settings.creatureId == -1:
            self.settings.creatureId = len(glob("data/vertices/*.npy"))
            n = 3
            vertices = create_vertices(n, 10)
            edges = create_edges(n)
            np.save("data/vertices/%d" % self.settings.creatureId, vertices)
            np.save("data/edges/%d" % self.settings.creatureId, edges)
        else:
            vertices = np.load(
                "data/vertices/%d.npy" % self.settings.creatureId)
            edges = np.load("data/edges/%d.npy" % self.settings.creatureId)

        Environment.description = "Creature #%d" % self.settings.creatureId

        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-500, 0), (500, 0)])
        )

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
            body[tuple(edge)] = self.world.CreateDynamicBody(
                fixtures=fixture,
            )
        print(len(body))

        for edge in edges:
            adjacent = find_adjacent_edges(edge, edges)
            for a_edge in adjacent:
                anchor = int(vertices[edge[0]][0]), int(vertices[edge[0]][1])
                print("connectiong", edge, a_edge, "at", anchor)
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
    