'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    return '<span style="font-weight:normal; font-family:\'Oswald\';">%{properties.NOM}</span>' +\
              '<extra></extra>'


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    return '<span style="font-weight:normal; font-family:\'Oswald\';">' + name + '</span>' +\
              '<extra></extra>'