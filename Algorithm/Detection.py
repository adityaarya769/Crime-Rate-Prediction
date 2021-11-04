import pandas as pd
data = pd.read_csv("H:\Crime rate detection system1\website\indian_crime_list.csv")
data_years = data.drop(["Crime Head"], axis=1)
population = 1350000000
per_lakh = 100000

def crime(year):
    sum = data_years[year].sum()
    average = (sum/population)*per_lakh
    return average

print("2016: ", crime('2016'))
print("2017: ", crime('2017'))
print("2018: ", crime('2018'))