import argopy
import numpy as np
from matplotlib import pyplot as plt

def plot_ocean_temperature_depth():
    # Generate random ocean temperature and depth data
    np.random.seed(0)
    num_points = 100
    temperature = np.random.uniform(0, 30, num_points)  # Random temperature data in Celsius
    depth = np.linspace(0, 5000, num_points)  # Depth data in meters, linearly spaced from 0 to 5000

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(depth, temperature, marker='o', color='b', linestyle='-')
    plt.title('Correlation Between Ocean Temperature and Depth')
    plt.xlabel('Depth (m)')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_ocean_temperature_depth()
