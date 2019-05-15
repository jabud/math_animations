
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Plot example 1 on a hyperbolic surface.
x = np.arange(-2, 2, 0.05)
y = np.arange(-2, 2, 0.05)
x, y = np.meshgrid(x, y)

# Plot other surfaces that can be used for transformations.

# A quadratic surface.
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')

quadratic = x**2 * y**2
ax.plot_surface(
    x, y, quadratic,
    cmap=cm.summer,
    alpha=.3,
    linewidth=0,
    antialiased=False,
)
ax.contour(x, y, quadratic, cmap=cm.summer)
ax.set_zticklabels([])
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.axis([-2., 2., -2., 2.])
ax.set_zlim([0, 4.])

fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')

# A rippled surface.
ripple = np.cos((x**2 + y**2)**.5)**2
ax.plot_surface(
    x, y, ripple,
    cmap=cm.summer,
    alpha=.3,
    linewidth=0,
    antialiased=False,
)
ax.contour(x, y, ripple, cmap=cm.summer)
ax.set_zticklabels([])
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.axis([-2., 2., -2., 2.])
ax.set_zlim([0., 1.])

# A peaked surface.
fig = plt.figure(6)
ax = fig.add_subplot(111, projection='3d')
peaked = np.cos(2 * x) * np.sin(3 * y)
ax.plot_surface(
    x, y, peaked,
    cmap=cm.summer,
    alpha=.3,
    linewidth=0,
    antialiased=False,
)
ax.contour(x, y, peaked, cmap=cm.summer)
ax.set_zticklabels([])
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.axis([-2., 2., -2., 2.])
ax.set_zlim([-1., 1.])

# Example 2.
# Illustrate higher dimensional transformations.
# Generate the data. 
n_points = 5
scale = .1
# x_green = np.random.normal(loc=-2., scale=scale, size=n_points) 
# y_green = np.zeros(n_points)
# z_green = np.zeros(n_points)
# x_yellow = np.random.normal(loc=-1.4, scale=scale, size=n_points) 
# y_yellow = np.zeros(n_points)
# z_yellow = np.zeros(n_points)
# x_orange = np.random.normal(loc=0., scale=scale, size=n_points) 
# y_orange = np.zeros(n_points)
# z_orange = np.zeros(n_points)
# x_purple = np.random.normal(loc=1.4, scale=scale, size=n_points) 
# y_purple = np.zeros(n_points)
# z_purple = np.zeros(n_points)
# x_black = np.random.normal(loc=2., scale=scale, size=n_points) 
# y_black = np.zeros(n_points)
# z_black = np.zeros(n_points)

# Show five types of fruit on a line,
# based on whether or not it is good to eat.
fig = plt.figure(7)
ax = fig.add_subplot(111, projection='3d')
# x_line = np.arange(-2.1, 2.1, .01)
# y_line = np.zeros(x_line.size)
# z_line = np.zeros(x_line.size)
# ax.plot(x_line, y_line, zs=z_line, color='black')
# markersize = 40.
# ax.scatter(
#     x_green, y_green, zs=z_green,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_yellow, y_yellow, zs=z_yellow,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_orange, y_orange, zs=z_orange,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_purple, y_purple, zs=z_purple,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_black, y_black, zs=z_black,
#     c='black',
#     marker='x',
#     s=markersize,
# )

# ax.set_xlabel('<-- green, yellow, orange, purple, black -->')
# ax.set_zticklabels([])
# ax.set_yticklabels([])
# ax.set_xticklabels([])
# ax.axis([-3., 3., -3., 3.])
# ax.set_zlim([-3., 3.])

# Transform the data to two dimensions.
shift = 2.2
# y_green = x_green**2  - shift
# y_yellow = x_yellow**2 - shift
# y_orange = x_orange**2 - shift
# y_purple = x_purple**2 - shift
# y_black = x_black**2 - shift
# fig = plt.figure(8)
# ax = fig.add_subplot(111, projection='3d')
# y_line = x_line**2 - shift
# ax.plot(x_line, y_line, zs=z_line, color='black')
# ax.scatter(
#     x_green, y_green, zs=z_green,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_yellow, y_yellow, zs=z_yellow,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_orange, y_orange, zs=z_orange,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_purple, y_purple, zs=z_purple,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_black, y_black, zs=z_black,
#     c='black',
#     marker='x',
#     s=markersize,
# )

# ax.set_xlabel('<-- green, yellow, orange, purple, black -->')
# ax.set_zticklabels([])
# ax.set_yticklabels([])
# ax.set_xticklabels([])
# ax.axis([-3., 3., -3., 3.])
# ax.set_zlim([-3., 3.])

# # Transform the data to three dimensions.
# z_green = y_green**2  - shift
# z_yellow = y_yellow**2 - shift
# z_orange = y_orange**2 - shift
# z_purple = y_purple**2 - shift
# z_black = y_black**2 - shift
# fig = plt.figure(9)
# ax = fig.add_subplot(111, projection='3d')
# z_line = y_line**2 - shift
# ax.plot(x_line, y_line, zs=z_line, color='black')
# ax.scatter(
#     x_green, y_green, zs=z_green,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_yellow, y_yellow, zs=z_yellow,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_orange, y_orange, zs=z_orange,
#     c='black',
#     marker='x',
#     s=markersize,
# )
# ax.scatter(
#     x_purple, y_purple, zs=z_purple,
#     c='green',
#     marker='o',
#     s=markersize,
# )
# ax.scatter(
#     x_black, y_black, zs=z_black,
#     c='black',
#     marker='x',
#     s=markersize,
# )

# Optionally, show the resulting quadratic surface.
show_surface = True
if show_surface:
    x = np.arange(-2.5, 2.5, 0.05)
    y = np.arange(-2.5, 2.5, 0.05)
    x, y = np.meshgrid(x, y)
    dual_quad = y**2 - shift
    ax.plot_surface(
        x, y, dual_quad,
        cmap=cm.summer,
        alpha=.3,
        linewidth=0,
        antialiased=False,
    )

# Optionally, show a good planar discriminator.
show_discriminator = False
if show_discriminator:
    plane = 0. * x
    ax.plot_surface(
        x, y, plane,
        alpha=.3,
        linewidth=0,
        antialiased=False,
    )

ax.set_xlabel('<-- green, yellow, orange, purple, black -->')
ax.set_zticklabels([])
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.axis([-3., 3., -3., 3.])
ax.set_zlim([-4., 4.])

plt.show()