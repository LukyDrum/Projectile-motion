from math import cos, pi, sin, radians, sqrt
from vectors import Vector
from copy import deepcopy

# Constants
G = 9.81 # m/s
AIR_DENISTY = 1.225 # kg/m^3
DRAG_COEF = 0.5 # Drag coeficient for (not smooth) ball


class Trajectory:
    def __init__(self, coordinates, velocities) -> None:
        self.coordinates = coordinates
        self.velocities = velocities
        self.max_distance = self.coordinates[-1][0]

        self.max_height = 0
        for coor in self.coordinates:
            if coor[1] > self.max_height:
                self.max_height = coor[1]


class Projectile:
    def __init__(
        self, v_init: float|int, alpha: float|int, 
        mass: float|int, radius: float|int, y_init: float|int=0
        ) -> None:
        self.alpha = radians(alpha)
        self.init_velocity = Vector(v_init * cos(self.alpha), v_init * sin(self.alpha))
        self.mass = mass
        self.radius = radius
        self.y_init = y_init
        self.cross_area = pi * radius**2

        self.delta_time = 0.01 # seconds

        self.trajectory_no_air = self._no_air_trajectory()
        self.trajectory_with_air = self._with_air_trajectory()


    def _no_air_trajectory(self) -> Trajectory:
        velocity: Vector = deepcopy(self.init_velocity)
        delta_time = self.delta_time

        # Default at time 0
        coors = [[0, 0]]
        velocities = [[0, velocity.magnitude()]]

        time = 0 # seconds
        # While y-coordinate is above 0 => above ground
        while coors[-1][1] >= 0:
            time += delta_time

            x = velocity.x * time
            
            velocity.y = velocity.y - G * delta_time
            y = coors[-1][1] + velocity.y * delta_time

            # Add new set of coordinates to the list
            coors.append([x, y])
            # Add new set of time and current velocity to the list
            velocities.append([time, velocity.magnitude()])
        
        return Trajectory(coors, velocities)

    def _with_air_trajectory(self) -> Trajectory:
        velocity: Vector = deepcopy(self.init_velocity)
        mass = self.mass
        cross_area = self.cross_area
        delta_time = self.delta_time

        # Default at time 0
        coors = [[0, 0]]
        velocities = [[0, velocity.magnitude()]]

        time = 0 # seconds
        # While y-coordinate is above 0 => above ground
        while coors[-1][1] >= 0:
            time += delta_time

            # Air drag in x-direction
            drag_x = -0.5 * AIR_DENISTY * velocity.x**2 * DRAG_COEF * cross_area
            a_x = drag_x / mass
            velocity.x = velocity.x + (a_x * delta_time)
            x = coors[-1][0] + velocity.x * delta_time

            # Air drag in y-direction
            drag_y = -0.5 * AIR_DENISTY * velocity.y**2 * DRAG_COEF * cross_area
            a_y = drag_y / mass - G
            velocity.y = velocity.y + (a_y * delta_time)
            y = coors[-1][1] + velocity.y * delta_time

            # Add new set of coordinates to the list
            coors.append([x, y])
            # Add new set of time and current velocity to the list
            velocities.append([time, velocity.magnitude()])
        
        return Trajectory(coors, velocities)