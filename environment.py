from framework.framework import (Framework, main)
from Box2D import (b2EdgeShape, b2FixtureDef, b2PolygonShape)
from maths.maths import line_to_rectangle


THICKNESS = 0.5


class BodyTypes(Framework):
    name = "Environment"
    description = "Sample"
    speed = 100  # platform speed

    def __init__(self):
        super(BodyTypes, self).__init__()

        # The ground
        _ = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-50, 0), (50, 0)])
        )

        vertices = [
            [(5, 5), (10, 10)],
            [(10, 10), (15, 5)],
            [(10, 10), (5, 5)],
        ]

        body = []

        for vertex in vertices:
            point = line_to_rectangle(*vertex, THICKNESS)

            fixture = b2FixtureDef(
                shape=b2PolygonShape(vertices=point),
                density=2,
                friction=0.6,
            )

            body.append(
                self.world.CreateDynamicBody(
                    fixtures=fixture,
                )
            )

        # self.world.CreateRevoluteJoint(
        #     bodyA=body[0],
        #     bodyB=body[1],
        #     anchor=(10, 10),
        #     collideConnected=False,
        #     motorSpeed=300,
        #     maxMotorTorque=300,
        #     enableMotor=True,
        # )

        # self.world.CreateRevoluteJoint(
        #     bodyA=body[0],
        #     bodyB=body[2],
        #     anchor=(5, 5)
        # )


if __name__ == "__main__":
    main(BodyTypes)
