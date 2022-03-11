from calculations import Projectile
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


default_values = {
    "velocity" : 34,
    "angle" : 45,
    "mass" : 0.145,
    "radius" : 0.0375
}

ball = Projectile(
    default_values["velocity"], default_values["angle"],
    default_values["mass"], default_values["radius"]
    )

fig, ax = plt.subplots()
"""
ax.set_xlim(-2, 300)
ax.set_ylim(-2, 130)
"""
# Without air
ax.plot([x[0] for x in ball.trajectory_no_air.coordinates], [x[1] for x in ball.trajectory_no_air.coordinates])
# With air
ax.plot([x[0] for x in ball.trajectory_with_air.coordinates], [x[1] for x in ball.trajectory_with_air.coordinates])

plt.subplots_adjust(bottom=0.5)
ax_slider_velocity = plt.axes([0.1, 0.4, 0.8, 0.05])
ax_slider_angle = plt.axes([0.1, 0.3, 0.8, 0.05])
ax_slider_mass = plt.axes([0.1, 0.2, 0.8, 0.05])
ax_slider_radius = plt.axes([0.1, 0.1, 0.8, 0.05])

ax.set_aspect("equal")

def update_plot(val):
    ax.clear()
    """
    ax.set_xlim(-2, 300)
    ax.set_ylim(-2, 130)
    """
    # New projectile with updated values
    ball = Projectile(slider_velocity.val, slider_angle.val, slider_mass.val, slider_radius.val)
    # Withou air
    ax.plot([x[0] for x in ball.trajectory_no_air.coordinates], [x[1] for x in ball.trajectory_no_air.coordinates])
    # With air
    ax.plot([x[0] for x in ball.trajectory_with_air.coordinates], [x[1] for x in ball.trajectory_with_air.coordinates])
    plt.draw()

slider_velocity = Slider(ax_slider_velocity, "Initial\nvelocity\n[m/s]", valmin=15, valmax=70, valinit= default_values["velocity"], valstep=0.1)
slider_velocity.on_changed(update_plot)
slider_angle = Slider(ax_slider_angle, "Angle\n[°]", valmin=1, valmax=90, valinit= default_values["angle"], valstep=0.1)
slider_angle.on_changed(update_plot)
slider_mass = Slider(ax_slider_mass, "Mass\n[kg]", valmin=0.01, valmax=2, valinit= default_values["mass"], valstep=0.01)
slider_mass.on_changed(update_plot)
slider_radius = Slider(ax_slider_radius, "Radius\n[m]", valmin=0.01, valmax=1, valinit= default_values["radius"], valstep=0.01)
slider_radius.on_changed(update_plot)

plt.show()