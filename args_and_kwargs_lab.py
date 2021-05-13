"""
PART ONE-------------------------------------------------------------------------------------------------

Write a function (return_colors)that has four optional parameters (with defaults):
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

PART TWO-------------------------------------------------------------------------------------------------

Write a new function (improved_return) with the parameters as:

*args and **kwargs

Have it return the colors (use strings for the colors again)

Call it with the same various combinations of arguments used above.

Also have it print args and kwargs directly, so you can be sure you understand what’s going on.

Note that in general, you can’t know what will get passed into **kwargs So maybe adapt your function to be able to do
something reasonable with any keywords.

"""


def return_colors(fore_color='red', back_color='blue', link_color='yellow', visited_color='gray'):
    print(f'The fore_color is {fore_color}.')
    print(f'The back_color is {back_color}.')
    print(f'The link_color is {link_color}.')
    print(f'The visited_color is {visited_color}.')
    return fore_color, back_color, link_color, visited_color



def improved_return(*args, **kwargs):
    print(f'The positional arguments are: {args}')
    print(f'The keyword arguments are: {kwargs}')

    # Default values if none are given
    fore_color = 'orange'
    back_color = 'green'
    link_color = 'purple'
    visited_color = 'pink'

    # Overrides the values from the positional arguments
    for index in range(0, len(args)):
        if index == 0:
            fore_color = args[0]
        if index == 1:
            back_color = args[1]
        if index == 2:
            link_color = args[2]
        if index == 3:
            visited_color = args[3]

    # Overrides the values from the keyword (dictionary) arguments
    if str(kwargs.get('fore_color')) != 'None':
        fore_color = kwargs.get('fore_color')

    if str(kwargs.get('back_color')) != 'None':
        back_color = kwargs.get('back_color')

    if str(kwargs.get('link_color')) != 'None':
        link_color = kwargs.get('link_color')

    if str(kwargs.get('visited_color')) != 'None':
        visited_color = kwargs.get('visited_color')

    return fore_color, back_color, link_color, visited_color


improved_return('purple', link_color='red', back_color='blue')
