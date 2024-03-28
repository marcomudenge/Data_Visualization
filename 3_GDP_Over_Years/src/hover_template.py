'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''

    hov = '<span style="font-weight:bold;">Country : </span>'+\
          '<span style="font-weight:normal;">%{id}</span>'   +\
          '<span style="font-weight:bold;"><br>Population : </span>'+\
          '<span style="font-weight:normal;">%{marker.size}</span>'   +\
          '<span style="font-weight:bold;"><br>GDP : </span>'+\
          '<span style="font-weight:normal;">%{x} $ (USD)</span>'+\
          '<span style="font-weight:bold;"><br>CO2 emissions : </span>'+\
          '<span style="font-weight:normal;">%{y} metric tonnes</span>'+\
              '<extra></extra>'
    
    return hov
