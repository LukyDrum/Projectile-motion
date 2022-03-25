from tkinter import Tk, Label, Button
from calculations import Projectile
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backend_bases import MouseButton

# Hide toolbar
matplotlib.rcParams["toolbar"] = "None"


class Pop_up:
    """
    Creates a pop up window using Tkinter.
    It lets user save graphs.
    """
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Save plot")

        self.text = Label(master, text="Save plot")
        self.text.pack()

        self.butt1 = Button(master, text="Save plot: Trajectory", command=lambda: self._save_subplot(1))
        self.butt1.pack()
        self.butt2 = Button(master, text="Save plot: Velocity", command=lambda: self._save_subplot(2))
        self.butt2.pack()
    
    def _save_subplot(self, subplot):
        """
        Save graph.
        Argument must be either 1 or 2:
            1 for first graph
            2 for second graph
        """
        if subplot == 1:
            extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig("ax1.png", bbox_inches = extent.expanded(1.2, 1.3))
        elif subplot == 2:
            extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig("ax2.png", bbox_inches = extent.expanded(1.2, 1.3))
        else:
            print("Error - cannot save graph\nArgument needs to be 1 or 2")


def right_click(event):
    """
    Right click action.
    Opens a pop up window by right clicking in Matplotlib window.
    """
    if event.button is MouseButton.RIGHT:
        pop = Pop_up(Tk())
        pop.master.mainloop()


def setup_plots(ball: Projectile):
    """
    Sets up and plots the graphs.
    It is called on star of the window and then everytime a sliders value is changed.
        => Updates the plot
    """
    ax1.set_title("Trajectory")
    ax1.set(xlabel="x [m]", ylabel="y [m]")
    ax2.set_title("Velocity")
    ax2.set(xlabel="time [s]", ylabel="velocity [m/s]")

    # Trajectory
    # Without air
    ax1.plot([x[0] for x in ball.trajectory_no_air.coordinates], [x[1] for x in ball.trajectory_no_air.coordinates], label="No air")
    # With air
    ax1.plot([x[0] for x in ball.trajectory_with_air.coordinates], [x[1] for x in ball.trajectory_with_air.coordinates], label="With air")

    # Velocity
    # Without air
    ax2.plot([x[0] for x in ball.trajectory_no_air.velocities], [x[1] for x in ball.trajectory_no_air.velocities], label="No air")
    # With air
    ax2.plot([x[0] for x in ball.trajectory_with_air.velocities], [x[1] for x in ball.trajectory_with_air.velocities], label="With air")

    # Show legend for both graphs
    ax1.legend()
    ax2.legend()


# Default values - mass and radius are those of a baseball
default_values = {
    "velocity" : 34,
    "angle" : 45,
    "mass" : 0.145,
    "radius" : 0.0375
}

# Instance of Projectile with default values => baseball
ball = Projectile(
    default_values["velocity"], default_values["angle"],
    default_values["mass"], default_values["radius"]
    )

# Create Figure and plots
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Projectile motion")

setup_plots(ball)

ax1.set_aspect("auto")
plt.connect("button_press_event", right_click)

# Called everytime a value of slider is changed
def update_plot(val):
    ax1.clear()
    ax2.clear()
    # New projectile with updated values
    ball = Projectile(slider_velocity.val, slider_angle.val, slider_mass.val, slider_radius.val)
    
    setup_plots(ball)

    plt.draw()

# Setup sliders
plt.subplots_adjust(bottom=0.5)
ax_slider_velocity = plt.axes([0.1, 0.35, 0.8, 0.05])
ax_slider_angle = plt.axes([0.1, 0.25, 0.8, 0.05])
ax_slider_mass = plt.axes([0.1, 0.15, 0.8, 0.05])
ax_slider_radius = plt.axes([0.1, 0.05, 0.8, 0.05])

# Slider for velocity, angle, mass and radius
# Function that updates the plots is called each time a slider is moved
slider_velocity = Slider(ax_slider_velocity, "Initial\nvelocity\n[m/s]", valmin=15, valmax=70, valinit= default_values["velocity"], valstep=0.1)
slider_velocity.on_changed(update_plot)
slider_angle = Slider(ax_slider_angle, "Angle\n[°]", valmin=1, valmax=89, valinit= default_values["angle"], valstep=0.1)
slider_angle.on_changed(update_plot)
slider_mass = Slider(ax_slider_mass, "Mass\n[kg]", valmin=0.01, valmax=2, valinit= default_values["mass"], valstep=0.01)
slider_mass.on_changed(update_plot)
slider_radius = Slider(ax_slider_radius, "Radius\n[m]", valmin=0.01, valmax=1, valinit= default_values["radius"], valstep=0.01)
slider_radius.on_changed(update_plot)

# Maximize window on start
plt.get_current_fig_manager().window.showMaximized()
# Set window title
plt.get_current_fig_manager().window.setWindowTitle("Projectile motion")

plt.show()