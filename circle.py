import matplotlib.pyplot as plt

# Create a figure and an axis
fig, ax = plt.subplots()

# Draw a circle with radius 1 centered at (0, 0)
circle = plt.Circle((0, 0), radius=1, color='blue', fill=True)

# Add the circle to the plot
ax.add_patch(circle)

# Set equal scaling to ensure the circle isn't distorted
ax.set_aspect('equal', 'box')

# Set axis limits for better visualization
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Display the plot
plt.title('Circle using Matplotlib')
plt.show()



# # Set the limits and aspect of the plot
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_aspect('equal')

# # Display the plot
# plt.show()
