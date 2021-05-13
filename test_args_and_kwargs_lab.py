"""

Unit tests to test the return_color() function for the various type of arguments.

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

from args_and_kwargs_lab import return_colors
from args_and_kwargs_lab import improved_return

# Part 1 below ---------------------------------------------------------------------------------------------

def test_positional_arguments():
    expected = 'red', 'orange', 'yellow', 'green'
    assert return_colors('red', 'orange', 'yellow', 'green') == expected


def test_keyword_arguments():
    expected = 'white', 'black', 'gray', 'silver'
    kwargs = {'fore_color': 'white', 'back_color': 'black', 'link_color': 'gray', 'visited_color': 'silver'}
    assert return_colors(**kwargs) == expected


def test_combination_arguments():
    expected = 'purple', 'blue', 'red', 'chartreuse'
    assert return_colors('purple', link_color='red', back_color='blue') == expected


def test_tuple_dict_arguments():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    expected = 'red', 'blue', 'chartreuse','chartreuse'
    assert return_colors(*regular, **links) == expected

# Part 2 for generic parameters below ---------------------------------------------------------------------

def test_improved_positional_arguments():
    expected = 'red', 'orange', 'yellow', 'green'
    assert improved_return('red', 'orange', 'yellow', 'green') == expected


def test_improved_keyword_arguments():
    expected = 'white', 'black', 'gray', 'silver'
    kwargs = {'fore_color': 'white', 'back_color': 'black', 'link_color': 'gray', 'visited_color': 'silver'}
    assert improved_return(**kwargs) == expected


def test_improved_combination_arguments():
    expected = 'purple', 'blue', 'red', 'chartreuse'
    assert improved_return('purple', link_color='red', back_color='blue') == expected

def test_improved_tuple_dict_arguments():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    expected = 'red', 'blue', 'chartreuse','chartreuse'
    assert improved_return(*regular, **links) == expected