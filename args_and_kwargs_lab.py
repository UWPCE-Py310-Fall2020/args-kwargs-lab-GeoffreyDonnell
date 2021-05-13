"""
Write a function that has four optional parameters (with defaults):
(1)fore_color
(2)back_color
(3)link_color
(4)visited_color
Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)

Call it with a couple different parameters set. That is, write tests that verify that all of the following
work as advertised:

(1) Positional arguments:
return_color('red', 'blue', 'yellow', 'chartreuse')

(2) Using just keyword arguments:
return_color(link_color='red', back_color='blue')

(3) Using a combination of positional and keyword arguments:
return_color('purple', link_color='red', back_color='blue')

(4) Using *some_tuple and/or **some_dict
    (4a) regular = ('red', 'blue')
    (4b) links = {'link_color': 'chartreuse'}
    (4c) return_color(*regular, **links)

"""