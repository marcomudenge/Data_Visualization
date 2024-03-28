'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''

    if mode == 'Percent':
        hov = '<span style="font-size:24px; color:black; font-family:\'Grenze Gotisch\';">'+name+'</span>'+\
              '<br><br>%{y:.2f}% of lines'+\
              '<extra></extra>'
    else:
        hov = '<span style="font-size:24px; color:black; font-family:\'Grenze Gotisch\';">'+name+'</span>'+\
              '<br><br>%{y} lines'+\
              '<extra></extra>'
    
    return hov
