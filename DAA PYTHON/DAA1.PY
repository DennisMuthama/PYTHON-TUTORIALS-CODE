import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))  # Determine the number of steps
    x_inc = dx / steps  # Increment in x per step
    y_inc = dy / steps  # Increment in y per step
    
    x, y = x1, y1
    points = []
    
    for _ in range(steps + 1):  # Generate points
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    
    return points

# Example: Line from (2, 3) to (10, 8)
line_points = dda(2, 3, 10, 8)

# Plot the line
x_coords, y_coords = zip(*line_points)
plt.plot(x_coords, y_coords, marker='o', label="Original Line")
plt.title("DDA Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()