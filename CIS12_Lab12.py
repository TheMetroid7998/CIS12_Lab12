import math

class Sun:
    def __init__(self, name:str, mass:float, temp:float, radius:float, x_pos=0.0, y_pos=0.0):
        self.name = name
        self.mass = mass
        self.position = (x_pos, y_pos)
        self.radius = radius
        self.temperature = temp

    def __str__(self):
        pass

    def get_position(self, position):
        return self.position

    def get_mass(self, mass):
        return self.mass


class Planet:
    def __init__(self, name:str, mass:float, distance:float, x_pos:float, x_vel:float, y_vel:float, color:str, y_pos:float=0.0):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.position = (x_pos, y_pos)
        self.velocity = (x_vel, y_vel)

    def __str__(self):
        pass


    def get_position(self, x_pos, y_pos):
        return self.position

    def set_position(self, x_pos, y_pos, new_position):
        pass

    def get_velocity(self, velocity):
        return self.velocity

    def set_velocity(self, velocity, new_position):
        pass

class SolarSystem:
    def __init__(self, sun, planets:list, gravity:float):
        self.sun = Sun
        self.planets = []
        self.gravity = gravity

    def add_sun(self, sun:Sun):
        pass
        return self.sun

    def add_planet(self, new_planet:Planet):


        return self.planets.append(planet)

    def show_planets(self):
        pass

    def move_planets(self):
        dt = .001  # Constant time interval for each solar system iteration.

        for planet in self.planets:
            # Move the distance covered in the interval dt
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            # After the move we need to calculate the new distance from the sun using the distance formula.
            dist_x = self.sun.get_position()[0] - planet.get_x_pos()
            dist_y = self.sun.get_position()[1] - planet.get_y_pos()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            # Let's calculate our new acceleration so we can set our new velocity
            acc_x = U.G * self.sun.get_mass() * dist_x / new_distance ** 3
            acc_y = U.G * self.sun.get_mass() * dist_y / new_distance ** 3

            # Now let's calculate the new x and y velocities and update them for the planet
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)

class Simulation:
    def __init__(self, solar_system:SolarSystem, sun:Sun, planets:list):
        self.system_solar = solar_system
        self.sun = sun
        self.planets = []

    def run(self):
        for _ in self.num.periods:





if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, color="green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, .1, 62, 10.0, 125.0, color="red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()