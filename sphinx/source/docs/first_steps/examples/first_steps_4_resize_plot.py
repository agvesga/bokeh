from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with a specific size
p = figure(
    title="Plot resizing example",
    plot_width=350,
    plot_height=250,
    x_axis_label="x",
    y_axis_label="y",
)

# chage plot size
p.plot_width = 450
p.plot_height = 150

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# show the results
show(p)
