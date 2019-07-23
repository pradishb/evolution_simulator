from framework.framework import (Framework, Keys, main)
from Box2D import (b2EdgeShape, b2FixtureDef, b2PolygonShape, b2_dynamicBody,
                   b2_kinematicBody, b2_staticBody)


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

        # # The platform
        # float dx = x1 - x0; //delta x
        # float dy = y1 - y0; //delta y
        # float linelength = sqrtf(dx * dx + dy * dy)
        # dx /= linelength
        # dy /= linelength
        # //Ok, (dx, dy) is now a unit vector pointing in the direction of the line
        # //A perpendicular vector is given by (-dy, dx)
        # const float thickness = 5; //Some number
        # const float px = 0.5 * thickness * (-dy) #perpendicular vector with lenght thickness * 0.5
        # const float py = 0.5 * thickness * dx
        # glBegin(GL_QUADS)
        # glVertex2f(x0 + px, y0 + py)
        # glVertex2f(x1 + px, y1 + py)
        # glVertex2f(x1 - px, y1 - py)
        # glVertex2f(x0 - px, y0 - py)
        # glEnd()


        fixture_1 = b2FixtureDef(
            shape=b2PolygonShape(vertices=[(5, 5), (10, 10), (1, 10)]),
            density=2,
            friction=0.6,
        )

        fixture_2 = b2FixtureDef(
            shape=b2PolygonShape(vertices=[(10,10), (15, 5), (15,0)]),
            density=2,
            friction=0.6,
        )

        body_a = self.world.CreateDynamicBody(
            # shapes=b2EdgeShape(vertices=[(-50, 0), (50, 0)]),
            # position=(0, 5),
            fixtures=fixture_1,
        )

        body_b = self.world.CreateDynamicBody(
            fixtures=fixture_2,
            # shapes=b2EdgeShape(vertices=[(10, 10), (15, 5)]),
            # position=(4, 5),
        )

        self.world.CreateRevoluteJoint(
            bodyA=body_a,
            bodyB=body_b,
            anchor=(10, 10)
        )


if __name__ == "__main__":
    main(BodyTypes)
