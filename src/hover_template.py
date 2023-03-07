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
    # TODO : Remaining : Add correct values (replace xy,x,z) - MM 2023/03/07

    hov = '<span style="font-weight:bold; color:black;">'+ "Country : "+'</span>'+\
          '<span style="font-weight:normal; color:black;">'+ '%{y}' +'</span>'   +\
          '<span style="font-weight:bold; color:black;">'+ "<br>Population : "+'</span>'+\
          '<span style="font-weight:normal; color:black;">'+ '%{x}' +'</span>'   +\
          '<span style="font-weight:bold; color:black;">'+ "<br>GDP : "+'</span>'+\
          '<span style="font-weight:normal; color:black;">'+ '%{z}' +'</span>'+\
          '<span style="font-weight:bold; color:black;">'+ "<br>CO2 emissions : "+'</span>'+\
          '<span style="font-weight:normal; color:black;">'+ '%{z}' +'</span>'+\
              '<extra></extra>'
    
    return hov
