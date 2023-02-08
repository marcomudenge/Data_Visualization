'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import numpy as np 


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''

    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'], format='%Y-%m-%d')
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    
    dataframe = dataframe[(dataframe['Date_Plantation'] > pd.to_datetime(str(start))) 
                & (dataframe['Date_Plantation'] < pd.to_datetime(str(end + 1)))]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # Sort values by area and date
    dataframe = dataframe.sort_values(by = ['Arrond_Nom', 'Date_Plantation'], ascending = [True, True])
    
    # Drop columns not needed for dataviz
    dataframe = dataframe.drop(['Arrond', 'Longitude', 'Latitude'], axis=1)
    dataframe['Date_Plantation'] = dataframe['Date_Plantation'].dt.strftime('%Y')
    dataframe = dataframe[['Arrond_Nom', 'Date_Plantation']].value_counts().reset_index(name='count')
    return dataframe


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # Get np arrays of unique areas and years. Used for index names and columns headers
    years = np.sort(yearly_df['Date_Plantation'].unique())
    areas = np.sort(yearly_df['Arrond_Nom'].unique())
    frame = pd.DataFrame(columns=years, index=areas)
    # Match all area/year in yearly_df to new frame
    for _, row in yearly_df.iterrows():
        frame.loc[[row['Arrond_Nom']],[row['Date_Plantation']]] = row['count']
    # Replace nan with zeros 
    frame = frame.fillna(0)
    return frame


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # Filter frame on arrond and year
    dataframe = dataframe[(dataframe['Arrond_Nom']==arrond) & (dataframe['Date_Plantation'].dt.year == year)]
    
    # Drop unnecessary columns
    dataframe = dataframe.drop(['Arrond', 'Longitude', 'Latitude'], axis=1)
    
    # Count number of trees for every date, sort by date
    dataframe = dataframe[['Date_Plantation']].value_counts().reset_index(name='Counts').sort_values('Date_Plantation')
    
    # Fill frame with zeros for dates that are not already present. 
    # (Source: https://skipperkongen.dk/2018/11/26/how-to-fill-missing-dates-in-pandas/)
    date_range = pd.date_range(start=dataframe.Date_Plantation.min(), end=dataframe.Date_Plantation.max())
    dataframe = dataframe.set_index('Date_Plantation').reindex(date_range).fillna(0).rename_axis('Date_Plantation').reset_index()
    return dataframe
