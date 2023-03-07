'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px

import hover_template


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The discrete color scale (sequence) to use is Set1 (see : https://plotly.com/python/discrete-color/)

        The markers' maximum size is 30 and their minimum
        size is 6.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Remaining : set the minimum mark size to 6 - MM 2023/03/07
    fig = px.scatter(my_df, x="GDP", y="CO2",
                     animation_frame="Year",
                     animation_group="Country Name",
                     size="Population", color="Continent",
                     color_discrete_sequence=px.colors.qualitative.Set1,
                     hover_name="Country Name", log_x=True, size_max=30,
                     range_x=[min(gdp_range),max(gdp_range)], 
                     range_y=[min(co2_range),max(co2_range)],
                     )

    return fig

def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''
    # TODO : Remaining : "as well as the hover template of each trace ..."
    
    fig.update_traces(hovertemplate=hover_template.get_bubble_hover_template())
    return fig


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year, and to remove
        the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns
            The updated figure
    '''
    # TODO : Update animation menu

    return fig


def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    
    fig.update_yaxes(title='CO2 emissions per capita (metric tonnes)')
    fig.update_xaxes(title='GDP per capita ($ USD)')
    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    
    fig.update_layout(template="simple_white")
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    
    fig.update_layout(legend_title="Legend")
    return fig
