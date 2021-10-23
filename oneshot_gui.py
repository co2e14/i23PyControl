import tkinter as tk
from tkinter import ttk
import oneshot
import sys
import time
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("I23 Oneshot")


def get_input():
    d2_gui_val = float(v.get())
    print("d2:", str(d2_gui_val))
    x_size_gui_val = float(x_size_entry.get())
    print("x size:", str(x_size_gui_val))
    y_size_gui_val = float(y_size_entry.get())
    print("y size:", str(y_size_gui_val))
    x_low_gui_val = float(x_low_entry.get())
    print("x low:", str(x_low_gui_val))
    x_high_gui_val = float(x_high_entry.get())
    print("x high:", str(x_high_gui_val))
    x_point_gui_val = float(x_point_entry.get())
    print("x point:", str(x_point_gui_val))
    y_low_gui_val = float(y_low_entry.get())
    print("y low:", str(y_low_gui_val))
    y_high_gui_val = float(y_high_entry.get())
    print("y high:", str(y_high_gui_val))
    y_point_gui_val = float(y_point_entry.get())
    print("y point:", str(y_point_gui_val))
    print("There will be", str(int(x_point_gui_val) * int(y_point_gui_val)), "points")

    plot = s3_d2_scan.runscan(
        d2_gui_val,
        x_size_gui_val,
        y_size_gui_val,
        x_low_gui_val,
        x_high_gui_val,
        x_point_gui_val,
        y_low_gui_val,
        y_high_gui_val,
        y_point_gui_val,
    )
    canvas = FigureCanvasTkAgg(plot, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# frames
sizes_frame = tk.LabelFrame(master=window, text="X Y Size", borderwidth=5)
d2_sel_frame = tk.LabelFrame(master=window, text="D2 Diode Select", borderwidth=5)
x_y_step_frame = tk.LabelFrame(
    master=window, text="X Y limits and steps", borderwidth=5
)
plot_frame = tk.LabelFrame(master=window, text="Plot", borderwidth=5)

# labels
x_size_label = tk.Label(master=sizes_frame, text="X Size").grid(row=1, column=1)
y_size_label = tk.Label(master=sizes_frame, text="Y Size").grid(row=1, column=3)
d2_position_label = tk.Label(master=d2_sel_frame, text="D2 Position")
x_low_label = tk.Label(master=x_y_step_frame, text="X Low").grid(row=1, column=1)
x_high_label = tk.Label(master=x_y_step_frame, text="X High").grid(row=2, column=1)
x_point_label = tk.Label(master=x_y_step_frame, text="X Points").grid(row=3, column=1)
y_low_label = tk.Label(master=x_y_step_frame, text="Y Low").grid(row=1, column=3)
y_high_label = tk.Label(master=x_y_step_frame, text="Y High").grid(row=2, column=3)
y_point_label = tk.Label(master=x_y_step_frame, text="Y Points").grid(row=3, column=3)

# entrys
x_size_entry = tk.Entry(master=sizes_frame)
x_size_entry.grid(row=1, column=2)
y_size_entry = tk.Entry(master=sizes_frame)
y_size_entry.grid(row=1, column=4)
d2_position_entry = tk.Entry(master=d2_sel_frame)
x_low_entry = tk.Entry(master=x_y_step_frame)
x_low_entry.grid(row=1, column=2)
x_high_entry = tk.Entry(master=x_y_step_frame)
x_high_entry.grid(row=2, column=2)
x_point_entry = tk.Entry(master=x_y_step_frame)
x_point_entry.grid(row=3, column=2)
y_low_entry = tk.Entry(master=x_y_step_frame)
y_low_entry.grid(row=1, column=4)
y_high_entry = tk.Entry(master=x_y_step_frame)
y_high_entry.grid(row=2, column=4)
y_point_entry = tk.Entry(master=x_y_step_frame)
y_point_entry.grid(row=3, column=4)

v = tk.StringVar(d2_sel_frame, "-145.00")


for (text, value) in d2_position.items():
    tk.Radiobutton(
        master=d2_sel_frame,
        text=text,
        variable=v,
        value=value,
        indicator=0,
        background="light blue",
    ).pack(ipady=5, fill="both")

# frame positions
sizes_frame.grid(row=1, column=1)
ttk.Separator(master=window).grid(row=2, column=1, pady=10, sticky="ew")
d2_sel_frame.grid(row=3, column=1)
ttk.Separator(master=window).grid(row=4, column=1, pady=10, sticky="ew")
x_y_step_frame.grid(row=5, column=1)
ttk.Separator(master=window).grid(row=6, column=1, pady=10, sticky="ew")
plot_frame.grid(row=7, column=1)
ttk.Separator(master=window).grid(row=8, column=1, pady=10, sticky="ew")
tk.Button(master=window, text="Run", command=get_input).grid(row=9, column=1)


window.mainloop()
