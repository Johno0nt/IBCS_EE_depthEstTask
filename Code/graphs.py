import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np


# def concentric():
#     # Set the radii for each of the six circles
#     r0 = 0.05 # Inner circle radius
#     r1 = 3.0
#     d = 0.8 # Common difference for arithmetic sequence of radii
#     radii = np.array([r0, r1, r1+d, r1+2*d, r1+3*d, r1+4*d])

#     # Create a figure and axis object
#     fig, ax = plt.subplots(figsize=(5,5))

#     # Plot each of the circles
#     for i, r in enumerate(radii):
#         if i == 0:
#             # Add an ellipsis at the fifth circle
#             circle = plt.Circle((0,0), r, color='black', fill=True)
#             ax.add_artist(circle)
#         if i == 4:
#             # Add an ellipsis at the fifth circle
#             circle = plt.Circle((0,0), r, fill=False, linestyle='--', linewidth=1)
#             ax.add_artist(circle)
#         else:
#             # Plot the other circles normally
#             circle = plt.Circle((0,0), r, fill=False, linewidth=2)
#             ax.add_artist(circle)

#     # Set axis limits and remove ticks
#     ax.set_xlim(-7,7)
#     ax.set_ylim(-7,7)
#     ax.set_xticks([])
#     ax.set_yticks([])

#     # Add a title and show the plot
#     plt.show()

# Define the function for an Archimedean spiral
def archimedean_spiral(t, a):
    r = a * t
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

def spiralModel():
    # Set the parameters for the spiral and inner circle
    a = 0.1 # Spacing between the arms of the spiral
    r1 = 0.05
    r0 = 2.0 # Radius of the inner circle

    # Create an array of values for t from 0 to 10pi
    t = np.linspace(0, 10*np.pi, 1000)

    # Compute the x and y coordinates for the spiral
    x, y = archimedean_spiral(t, a)

    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(5,5))

    # Plot the spiral starting at the edge of the inner circle
    ax.plot(r0 * np.cos(t), r0 * np.sin(t), color='k', linewidth=2)
    ax.plot(x + r0 * np.cos(t), y + r0 * np.sin(t), color='k', linewidth=2)

    # Set axis limits and remove ticks
    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a title and show the plot
    plt.title("Roll of Tape Spiral Starting from Inner Circle")
    plt.show()

def segmentedSpiral():
    a = 0.1 # Spacing between the arms of the spiral
    r0 = 1.0 # Radius of the inner circle

    # Create an array of values for t from 0 to 20pi
    t = np.linspace(0, 20*np.pi, 10000)

    # Compute the x and y coordinates for the spiral
    x, y = archimedean_spiral(t, a)

    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(5,5))

    # Set the number of segments
    num_segments = 20

    # Plot the spiral segments
    for i in range(num_segments):
        start = int(i * len(t) / num_segments)
        end = int((i + 1) * len(t) / num_segments)
        label = f"$S_{{{i+1}}}^{{\\circ}}$"
        color = plt.cm.hsv(i/num_segments)
        ax.plot(x[start:end] + r0 * np.cos(t[start:end]), y[start:end] + r0 * np.sin(t[start:end]), linewidth=2, label=label)
    
    # Set axis limits and remove ticks
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a legend and title
    ax.legend()
    plt.title("Toilet Paper Spiral Starting on Inner Circle")
    plt.show()


segmentedSpiral()
spiralModel()