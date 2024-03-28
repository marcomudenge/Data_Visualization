'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
from dash import html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    name, mode, new_theme, _ = figure['data'][curve]['customdata'][point]
    
    title = html.Div(children=name,
                         style={'color': figure['data'][curve]['marker']['color']})
    
    if new_theme:
        theme = html.Div(['Thématique :',
                            html.Ul([html.Li(x) for x in new_theme.split()])])
    else:
        theme = html.Div()
    
    style.update({'visibility': 'visible'})
    
    return title, mode, theme, style
