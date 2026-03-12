import matplotlib.pyplot as plt
import math

def simulate_steering(wheelbase, steer_angle_deg):
    # Setup simulation parameters
    speed = 5.0 # meters per second
    dt = 0.1    # time step (0.1 seconds)
    total_time = 10 # seconds
    
    # Initial position and orientation
    x, y, theta = 0, 0, 0
    path_x, path_y = [0], [0]
    
    # Convert steering angle to radians
    delta = math.radians(steer_angle_deg)
    
    # Run simulation loop
    for _ in range(int(total_time / dt)):
        # Bicycle Model Equations
        x += speed * math.cos(theta) * dt
        y += speed * math.sin(theta) * dt
        # The change in heading (theta) depends on speed and steering angle
        theta += (speed / wheelbase) * math.tan(delta) * dt
        
        path_x.append(x)
        path_y.append(y)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(path_x, path_y, label=f'Steer Angle: {steer_angle_deg}°')
    plt.title("Vehicle Trajectory - Kinematic Steering Model")
    plt.xlabel("X Position (meters)")
    plt.ylabel("Y Position (meters)")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    
    # Save the plot as an image
    plt.savefig("steering_trajectory.png")
    print("Simulation finished. Trajectory saved as steering_trajectory.png")

if __name__ == "__main__":
    # Simulate a car with 2.5m wheelbase at 15 degree steering
    simulate_steering(wheelbase=2.5, steer_angle_deg=15)
