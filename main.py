from calculations import Projectile
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def setup_plots(ball: Projectile):
    ax1.set_title("Trajectory")
    ax1.set(xlabel="x [m]", ylabel="y [m]")
    ax2.set_title("Velocity")
    ax2.set(xlabel="time [s]", ylabel="velocity [m/s]")

    # Trajectory
    # Without air
    ax1.plot([x[0] for x in ball.trajectory_no_air.coordinates], [x[1] for x in ball.trajectory_no_air.coordinates])
    # With air
    ax1.plot([x[0] for x in ball.trajectory_with_air.coordinates], [x[1] for x in ball.trajectory_with_air.coordinates])

    # Velocity
    # Without air
    ax2.plot([x[0] for x in ball.trajectory_no_air.velocities], [x[1] for x in ball.trajectory_no_air.velocities])
    # With air
    ax2.plot([x[0] for x in ball.trajectory_with_air.velocities], [x[1] for x in ball.trajectory_with_air.velocities])

# Default values - mass and radius are those of a baseball
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

# Create Figure and plots
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Projectile motion")

setup_plots(ball)

# Add sliders
plt.subplots_adjust(bottom=0.5)
ax_slider_velocity = plt.axes([0.1, 0.35, 0.8, 0.05])
ax_slider_angle = plt.axes([0.1, 0.25, 0.8, 0.05])
ax_slider_mass = plt.axes([0.1, 0.15, 0.8, 0.05])
ax_slider_radius = plt.axes([0.1, 0.05, 0.8, 0.05])

ax1.set_aspect("equal")

# Called everytime a value of slider is changed
def update_plot(val):
    ax1.clear()
    ax2.clear()
    # New projectile with updated values
    ball = Projectile(slider_velocity.val, slider_angle.val, slider_mass.val, slider_radius.val)
    
    setup_plots(ball)

    plt.draw()

# Setup sliders
slider_velocity = Slider(ax_slider_velocity, "Initial\nvelocity\n[m/s]", valmin=15, valmax=70, valinit= default_values["velocity"], valstep=0.1)
slider_velocity.on_changed(update_plot)
slider_angle = Slider(ax_slider_angle, "Angle\n[°]", valmin=1, valmax=90, valinit= default_values["angle"], valstep=0.1)
slider_angle.on_changed(update_plot)
slider_mass = Slider(ax_slider_mass, "Mass\n[kg]", valmin=0.01, valmax=2, valinit= default_values["mass"], valstep=0.01)
slider_mass.on_changed(update_plot)
slider_radius = Slider(ax_slider_radius, "Radius\n[m]", valmin=0.01, valmax=1, valinit= default_values["radius"], valstep=0.01)
slider_radius.on_changed(update_plot)

# Maximize window on start and add window title
plt.get_current_fig_manager().window.showMaximized()
plt.get_current_fig_manager().window.setWindowTitle("Projectile motion")

plt.show()