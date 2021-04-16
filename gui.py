import tkinter as tk

window = tk.Tk()
window.title("I23 Control")

# frames
sizes_frame = tk.Frame(master=window, borderwidth=1)
d2_sel_frame = tk.Frame(master=window, borderwidth=1)

# labels
x_y_size_label = tk.Label(master=sizes_frame, text="X Y Size")
d2_position_label = tk.Label(master=d2_sel_frame, text="D2 Position")
x_low_label = tk.Label(master=sizes_frame, text="X Low")
x_high_label = tk.Label(master=sizes_frame, text="X High")
x_point_label = tk.Label(master=sizes_frame, text="X Points")
y_low_label = tk.Label(master=sizes_frame, text="Y Low")
y_high_label = tk.Label(master=sizes_frame, text="Y High")
y_point_label = tk.Label(master=sizes_frame, text="Y Points")

# entrys
x_size_entry = tk.Entry(master=sizes_frame)
y_size_entry = tk.Entry(master=sizes_frame)
d2_position_entry = tk.Entry(master=d2_sel_frame)
x_low_entry = tk.Entry(master=sizes_frame)
x_high_entry = tk.Entry(master=sizes_frame)
x_point_entry = tk.Entry(master=sizes_frame)
y_low_entry = tk.Entry(master=sizes_frame)
y_high_entry = tk.Entry(master=sizes_frame)
y_point_entry = tk.Entry(master=sizes_frame)

values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}

v = tk.StringVar(d2_sel_frame, "1")

for (text, value) in values.items():
    tk.Radiobutton(master=d2_sel_frame, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue").pack(ipady = 5)


# positioning
x_y_size_label.grid(row=1, column=1)
x_size_entry.grid(row=1, column=2)
y_size_entry.grid(row=1, column=3)


sizes_frame.grid(row=1, column=1)
d2_sel_frame.grid(row=2, column=1)

window.mainloop()
