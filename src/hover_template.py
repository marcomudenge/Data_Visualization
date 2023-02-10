'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    hov = '<span style="font-weight:bold; color:black; font-family:\'Roboto Slab\';">'+ "Neighborhood : "+'</span>'+\
          '<span style="font-weight:normal; color:black; font:\'Roboto\';">'+ '%{y}' +'</span>'   +\
          '<span style="font-weight:bold; color:black; font:\'Roboto Slab\';">'+ "<br>Year : "+'</span>'+\
          '<span style="font-weight:normal; color:black; font:\'Roboto\';">'+ '%{x}' +'</span>'   +\
          '<span style="font-weight:bold; color:black; font:\'Roboto Slab\';">'+ "<br>Trees planted : "+'</span>'+\
          '<span style="font-weight:normal; color:black; font:\'Roboto\';">'+ '%{z}' +'</span>'+\
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
    hov = '<span style="font-weight:bold; color:black; font:\'Roboto Slab\';">'+ "Date : "+'</span>'+\
          '<span style="font-weight:normal; color:black; font:\'Roboto\';">'+ '%{x}' +'</span>'   +\
          '<span style="font-weight:bold; color:black; font:\'Roboto Slab\';">'+ "<br>Trees planted : "+'</span>'+\
          '<span style="font-weight:normal; color:black; font:\'Roboto\';">'+ '%{y}' +'</span>'+\
              '<extra></extra>'
    
    return hov

