def draw_point(x, y):
    print x
    print y

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)
