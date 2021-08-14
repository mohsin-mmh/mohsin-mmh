import pandas as pd
import json as js
import plotly.graph_objs as go
import plotly.express as px


def cleandata(dataset, keepcolumns = ['Country Name', '1990', '2015'], value_variables = ['1990', '2015']):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """    
    df = pd.read_csv(dataset, skiprows=4)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    top10country = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
    df = df[df['Country Name'].isin(top10country)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = value_variables)
    df_melt.columns = ['country','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt


def return_table():
      df = cleandata('data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2.csv')
      df.columns = ['country','year','hectaresarablelandperperson']
      df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
      countrylist = df.country.unique().tolist()
      records = df.to_records(index=False)
      result = list(records)
      return result


def return_graph1():

    """Creates four high chart visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    #First chart plots ararble land for 2015 as a bar chart
    df = cleandata('data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2.csv')
    df.columns = ['country','year','hectaresarablelandperperson']
    df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
    df = df[df['year'] == 2015]
    x = df.country.tolist()
    y = df.hectaresarablelandperperson.tolist()
    merged_list = [(x[i], y[i]) for i in range(0, len(x))]
    return merged_list

def fig2():
    df = pd.read_csv('data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2.csv', skiprows=4)

    # Filter for 1990 and 2015, top 10 economies
    df = df[['Country Name','1990', '2015']]
    countrylist = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada', 'Pakistan']
    df = df[df['Country Name'].isin(countrylist)]
    
    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = ['1990', '2015'])
    df_melt.columns = ['country','year', 'hectaresarablelandperperson']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year    
    df_melt.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)

    # prepare data into x, y lists for plotting
    fig = px.scatter(df_melt, x="year", y="hectaresarablelandperperson", color="country", size="hectaresarablelandperperson", hover_data=['country'])
    
    return fig