import numpy as np
import matplotlib.pyplot as plt

def position(t, x0, v0, a):
    return x0 + v0 * t + 0.5 * a * t**2

def velocity(t, v0, a):
    return v0 + a * t

def main():
    # Consider a projectile launched at a speed of 50 m/s and an angle of 45 degrees.
    #
    # Goal: create plots of x vs. t, y vs. t, v_x vs. t, and v_y vs. t
    #       for 0 < t < 10 seconds
    #
    #

    speed = 50.0
    theta = np.radians(45)
    g = 9.81

    vx0 = speed * np.cos(theta)
    vy0 = speed * np.sin(theta)

    # TODO: create time array using np.linspace
    t = np.linspace(0, 10, 1000)

    # TODO: compute position and velocity arrays
    x = position(t, 0, vx0, 0)
    y = position(t, 0, vy0, -g)

    vx = velocity(t, vx0, 0)
    vy = velocity(t, vy0, -g)

    # TODO: make and save plots

    plt.figure()
    plt.plot(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("x position (m)")
    plt.title("x vs. t")
    plt.grid(True)
    plt.savefig("x_vs_t.png")

    plt.figure()
    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("y position (m)")
    plt.title("y vs. t")
    plt.grid(True)
    plt.savefig("y_vs_t.png")

    plt.figure()
    plt.plot(t, vx)
    plt.xlabel("Time (s)")
    plt.ylabel("v_x (m/s)")
    plt.title("v_x vs. t")
    plt.grid(True)
    plt.savefig("vx_vs_t.png")

    plt.figure()
    plt.plot(t, vy)
    plt.xlabel("Time (s)")
    plt.ylabel("v_y (m/s)")
    plt.title("v_y vs. t")
    plt.grid(True)
    plt.savefig("vy_vs_t.png")

    plt.show()

main()
