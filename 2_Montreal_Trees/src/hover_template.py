'''
    Provides the templates for the tooltips.
'''

#In the TP statement, there is a little blank space between the arrow and the text in hover templates (see fig. 7 and 8).
#As there was no guideline for this in the statement, we did not add this space in our template.

def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    hov = '<span style="font-weight:bold; font-family:\'Roboto Slab\';">Neighborhood : </span>'+\
          '<span style="font-weight:normal; font-family:\'Roboto\';">%{y}</span>'   +\
          '<span style="font-weight:bold; font-family:\'Roboto Slab\';"><br>Year : </span>'+\
          '<span style="font-weight:normal; font-family:\'Roboto\';">%{x}</span>'   +\
          '<span style="font-weight:bold; font-family:\'Roboto Slab\';"><br>Trees planted : </span>'+\
          '<span style="font-weight:normal; font-family:\'Roboto\';">%{z}</span>'+\
              '<extra></extra>'
    
    return hov

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    hov = '<span style="font-weight:bold; font-family:\'Roboto Slab\';">'+ "Date : "+'</span>'+\
          '<span style="font-weight:normal; font-family:\'Roboto\';">'+ '%{x}' +'</span>'   +\
          '<span style="font-weight:bold; font-family:\'Roboto Slab\';">'+ "<br>Trees : "+'</span>'+\
          '<span style="font-weight:normal; font-family:\'Roboto\';">'+ '%{y}' +'</span>'+\
              '<extra></extra>'
    
    return hov

