import pandas as pd
import json as js
import plotly.graph_objs as go

# Get the data from the CSV file
#df = pd.read_csv('owid-covid-data.csv')
def cleandata(dataset, keepcolumns):
    df = pd.read_csv(dataset)
    df = df[keepcolumns]
    #df['date'] = df['date'].astype('datetime64[ns]').dt.date
    non_countries = ['World', 'Europe', 'North America', 'South America', 'Asia', 'European Union', 'Africa']
    df = df[~df['location'].isin(non_countries)]
    return df

def date_list():
    covid_df = cleandata('data/owid-covid-data.csv', ['location', 'date'])
    covid_dates = covid_df.date.unique().tolist()
    return covid_dates

def graph1(date):
    covid_df = cleandata('data/owid-covid-data.csv',['location', 'date', 'total_cases'])
    covid_df = covid_df[covid_df.date == date]
    covid_df.sort_values('total_cases', ascending=False, inplace=True)
    covid_df = covid_df.nlargest(20,'total_cases')
    covid_df = covid_df.to_json(orient='records')
    #json_df = js.loads(covid_df)
    return covid_df

def graph2(date):
    covid_df = cleandata('data/owid-covid-data.csv',['location', 'date', 'new_cases'])
    covid_df = covid_df[covid_df.date == date]
    covid_df.sort_values('new_cases', ascending=False, inplace=True)
    covid_df = covid_df.nlargest(20,'new_cases')
    covid_df = covid_df.to_json(orient='records')
    #json_df = js.loads(covid_df)
    return covid_df

def graph3(date):
    covid_df = cleandata('data/owid-covid-data.csv',['location', 'date','total_deaths'])
    covid_df = covid_df[covid_df.date == date]
    covid_df.sort_values('total_deaths', ascending=False, inplace=True)
    covid_df = covid_df.nlargest(20,'total_deaths')
    covid_df = covid_df.to_json(orient='records')
    #json_df = js.loads(covid_df)
    return covid_df

def graph4(date):
    covid_df = cleandata('data/owid-covid-data.csv',['location', 'date', 'new_deaths'])
    covid_df = covid_df[covid_df.date == date]
    covid_df.sort_values('new_deaths', ascending=False, inplace=True)
    covid_df = covid_df.nlargest(20,'new_deaths')
    covid_df = covid_df.to_json(orient='records')
    #json_df = js.loads(covid_df)
    return covid_df