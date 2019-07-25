from framework.framework import (Framework, main)
from Box2D import (b2EdgeShape, b2FixtureDef, b2PolygonShape)
from maths.maths import line_to_rectangle
from creature.creature import create_edges, create_vertices, find_adjacent_edges


THICKNESS = 0.5


class BodyTypes(Framework):
    name = "Environment"
    description = "Sample"
    speed = 100  # platform speed

    def __init__(self):
        super(BodyTypes, self).__init__()

        # The ground
        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-500, 0), (500, 0)])
        )

        vertices = create_vertices(3, 10)
        edges = create_edges(3)
        body = {}

        for edge in edges:
            vertex = vertices[edge[0]], vertices[edge[1]]
            point = line_to_rectangle(*vertex, THICKNESS)

            fixture = b2FixtureDef(
                shape=b2PolygonShape(vertices=point),
                density=2,
                friction=0.6,
            )

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
                    maxMotorTorque=1000,
                    enableMotor=True,
                )


if __name__ == "__main__":
    main(BodyTypes)
