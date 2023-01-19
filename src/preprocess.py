'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    
    # Calculate the total of occurences per act
    total_occ_per_act = my_df.groupby(['Act']).size()
    
    # Sum the lines per players
    my_df = my_df.groupby(['Act', 'Player']).size().reset_index(name='PlayerLine')
    
    # Calculate the player's line per act percentage
    my_df['PlayerPercent'] = my_df.apply(lambda x: (x['PlayerLine'] / total_occ_per_act[x['Act']]) * 100, axis=1)
    
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    
    # Find the top 5 players of each act
    top_players = my_df.groupby(['Act', ])["PlayerLine"].nlargest(5)
    
    # Create a mask for the players that are not in the top 5
    mask = ~my_df.index.isin(top_players.index.get_level_values(1))

    # For each act, rename players not in the top 5
    my_df.loc[mask, 'Player'] = 'Others'
    
    # Update count and percentage of plays
    my_df = my_df.groupby(['Act','Player'], as_index=False).agg({'PlayerLine': 'sum','PlayerPercent':'sum'})
    
    # Rename columns
    my_df = my_df.rename(columns={'PlayerLine':'LineCount','PlayerPercent':'PercentCount'})
    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''

    # Clean players name
    my_df['Player'] = my_df['Player'].str.title()
    
    return my_df
