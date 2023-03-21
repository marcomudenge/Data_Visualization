'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


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
    # Cleaner way to do this?
    # Possible to use variables instead of 0,1,2 for customdata?
    
    new_title = html.Div(children=figure['data'][curve]['customdata'][point][0],
                         style={'color': figure['data'][curve]['marker']['color']})
    
    new_mode = figure['data'][curve]['customdata'][point][1]
    
    new_theme = figure['data'][curve]['customdata'][point][2]
    if new_theme != None:
        new_theme = html.Div(['Thématique:',
                            html.Ul([html.Li(x) for x in new_theme.split()])])
    
    style.update({'visibility': 'visible'})
    
    return new_title, new_mode, new_theme, style
