'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME

#Note : the density of the x axis ticks does not match what is in the TP statement 
#(see Fig. 5 for Le Sud-Ouest in 2018, one tick per 2 weeks vs. 1 tick per month in our case)
#As there was no guideline for this in the statement, we did not set the density of ticks.

def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    fig = px.line()
    fig.update_layout(
        dragmode=False
    )
    fig.add_annotation(
        text="No data to display. Select a cell in the heatmap for more information.",
        showarrow=False,
        font=dict(size=10) #not sure if we had to fix it but it makes the page look closer to the TP guide
    )

    fig.update_yaxes(
        range=[0, 1],   # setting the range to have the percentages working for displaying the rectangle
        showgrid=False,         # hiding everything else
        showticklabels=False,
        zeroline=False
    )
    fig.update_xaxes(
        showgrid=False,
        showticklabels=False
    )

    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    fig.add_hrect(
        yref='paper',
        y0=0.25,
        y1=0.75,
        line_width=0,
        fillcolor=THEME['pale_color']
    )
    return None


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''

    if len(line_data) == 1:
        fig = px.scatter(line_data,
            x = 'Date_Plantation',
            y = 'Counts'
        )
    else:
        fig = px.line(line_data,
            x = 'Date_Plantation', 
            y = 'Counts'
        )
    
    fig.update_xaxes(
        tickformat = "%d %b" #zero-padded day + space + abbreviated month
    )
    fig.update_layout(
        title = "Trees planted in "+arrond+" in "+year,
        xaxis_title = "",
        yaxis_title = "Trees",
    )

    fig.update_traces(hovertemplate = hover_template.get_linechart_hover_template())
    
    return fig
