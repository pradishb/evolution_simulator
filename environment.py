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

        # The platform
        fixture = b2FixtureDef(
            shape=b2PolygonShape(box=(4, 0.5)),
            density=2,
            friction=0.6,
        )

        self.platform = self.world.CreateDynamicBody(
            position=(0, 5),
            fixtures=fixture,
        )


if __name__ == "__main__":
    main(BodyTypes)
