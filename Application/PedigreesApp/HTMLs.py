def draw_rectangles(position_x, position_y, width, height, affected):
    rectangle_shape_1 = str('\t\t\t<rect x="') + str(position_x) + str('" y="') + str(position_y) + str('" ')
    rectangle_shape_2 = str('width="') + str(width) + str('" height="') + str(height) + str('" style="fill:')
    rectangle_shape_3 = None

    if affected == "1":
        rectangle_shape_3 = str('white;stroke-width:1;stroke:black"></rect>')
    elif affected == "2":
        rectangle_shape_3 = str('red;stroke-width:1;stroke:black"></rect>')
    else:
        rectangle_shape_3 = str('grey;stroke-width1;stroke:black"></rect>')

    return rectangle_shape_1 + rectangle_shape_2 + rectangle_shape_3


def draw_circles(center_position_x, center_position_y, radius, affected):
    circle_shape_1 = str('\t\t\t<circle cx="') + str(center_position_x) + str('" cy="') + str(center_position_y) + str('" ')
    circle_shape_2 = str('r="') + str(radius) + str('" stroke="black" stroke-width="1" fill="')

    if affected == "1":
        return circle_shape_1 + circle_shape_2 + str('white"></circle>')
    elif affected == "2":
        return circle_shape_1 + circle_shape_2 + str('red"></circle>')
    else:
        return circle_shape_1 + circle_shape_2 + str('grey"></circle>')

def draw_line(x1, y1, x2, y2):
    connection_1 = str('\t\t\t<line x1="') + str(x1) + str('" y1="') + str(y1)
    connection_2 = str('" x2="') + str(x2) + str('" y2="') + str(y2) + str('" style="stroke:rgb(0,0,0);stroke-width:1"></line>')
    return connection_1 + connection_2

def draw_children_shapes(family, start_x, start_y, end_x, end_y):
    html_code = str("")
    offset_pixels = None
    counter = start_x

    if len(family.children) > 0:
        offset_pixels = (end_x - start_x) / (len(family.children) - 1)


    for child in family.children:
        html_code += str("""\n""") + draw_line(counter, start_y, counter, start_y + 40)

        if child.sex == "1":
            html_code += str("""\n""") + draw_rectangles(counter - 20, start_y + 40, 40, 40, child.treat)
        elif child.sex == "2":
            html_code += str("""\n""") + draw_circles(counter, start_y + 63, 23, child.treat)

        counter = counter + offset_pixels

    return html_code

def draw_pedigree(family):
    pixels = (len(family.children) - 1) * 90

    html_code = str("""{% extends 'base.html' %}
{% block content %}
        <svg height="auto" width="auto">""") + str("""
""") + draw_rectangles(250, 100, 40, 40, family.father.treat) + str("""
""") + draw_circles(400, 120, 23, family.mother.treat) + str("""
""") + draw_line(290, 120, 377, 120) + str("""
""")
    
    if len(family.children) > 0:
        html_code += draw_line(333, 120, 333, 210) + str("""
""") + draw_line(333 - pixels/2, 210, 333 + pixels/2, 210) + str("""
""") + draw_children_shapes(family, 333 - pixels/2, 210, 333 + pixels/2, 210) + str("""\n\t\t</svg>
{% endblock content %}""")
    else:
        html_code += str("""\t\t</svg>
{% endblock content %}""")

    return html_code