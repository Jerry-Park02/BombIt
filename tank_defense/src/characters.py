import pymunk as pm
from pymunk import Vec2d


class Bird():
    def __init__(self, distance, angle, x, y, space):
        self.life = 20
        mass = 5
        radius = 6
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        angle = -angle
        body.apply_impulse_at_local_point(impulse.rotated(angle))
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.5
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def stop_if_slow(self, threshold=1.0):
        velocity = self.body.velocity
        speed = velocity.length
        # Stop vertically if y is close to 0
        if abs(self.body.position.y) < 1.0:
            self.body.velocity = Vec2d(0, 0)
            # 폭발할 예정입니다


class Army():
    def __init__(self, x, y, space):
        self.life = 20
        mass = 1
        width = 28
        height = 28
        inertia = pm.moment_for_box(mass,(width, height))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Poly.create_box(body, (width, height))
        shape.elasticity = 0.5
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape
