import math

class SteeringModel:
    def __init__(self, wheelbase):
        self.L = wheelbase  # Length between front and rear axles (meters)
        self.max_steer = math.radians(35) # Max steering angle 35 degrees

    def calculate_turning_radius(self, steer_angle_deg):
        """Calculates the turning radius (R) in meters."""
        delta = math.radians(steer_angle_deg)
        delta = max(min(delta, self.max_steer), -self.max_steer)

        if delta == 0:
            return float('inf') 
        
        radius = self.L / math.tan(delta)
        return radius

if __name__ == "__main__":
    car = SteeringModel(wheelbase=2.5)
    test_angle = 20
    r = car.calculate_turning_radius(test_angle)
    print(f"Turning Radius: {round(r, 2)}m")
