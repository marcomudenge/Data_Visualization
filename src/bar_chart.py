'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    fig.update_layout(
        template=pio.templates['INF8808_TP2'], #TODO : ask if we really had to create a theme or just update simple_white
        dragmode=False,
        barmode='relative',
        title='Lines per act' #TODO : ask if title needs to be aligned to the left (fig 2 and 3)
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    fig.data = [] #reset figure before updating
    
    for char in sorted(set(data['Player'])): #sorted to have the blocks in the same order as in Fig2 and 3
        fig.add_trace(go.Bar(
                x = ["Act "+ str(i) for i in data[data["Player"] == char]["Act"]],
                y = data.loc[data['Player'] == char][MODE_TO_COLUMN[mode]],  
                name = char,
                hovertemplate = get_hover_template(char, mode)
                #not accurate : Romeo doesn't speak in act IV and his data for Act V are shifted
                #TODO : fix this
            )
        )
    
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    new_fig = go.Figure(fig)
    
    if mode == "Percent":
        new_fig.update_yaxes(title='Lines (%)')
    else:
        new_fig.update_yaxes(title= 'Lines (Count)')
        
    return new_fig
