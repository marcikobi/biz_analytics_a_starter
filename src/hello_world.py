print('hello_world')
#%%
print(5+5)



multiplier = 4
result = multiplier * -3
print(result)#%%

recent_years = [2020, 2021, 2022]
print(recent_years[0])

for year in recent_years:
    print(year)

for number in range(10):
    print(number)

#%%
years = [2010,2020]
emissions_per_year = [10.3, 7.7]

slope = (emissions_per_year[1]-emissions_per_year[0]) / (years[1]-years[0])
intercept = emissions_per_year[0] - (slope * years[0])

def model(desired_year):
    model_result = slope * desired_year + intercept
    return model_result

emissions_in_2022 = model(2022)
print(emissions_in_2022)
#%%

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

from scipy.stats import linregress

regression_result = linregress(x=years, y=emissions_per_year)

scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept
scipy_pvalue = regression_result.pvalue

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

emissions_in_2022_scipy = scipy_model(2022)
print(emissions_in_2022_scipy)




model_results = []
scipy_model_results = []
for year in years:
    model_result = model(year)
    scipy_model_result =scipy_model(year)

    model_results.append(model_result)
    scipy_model_results.append(scipy_model_result)

print(emissions_per_year)
print(model_result)
print(scipy_model_results)

#%%

#%%

#%%