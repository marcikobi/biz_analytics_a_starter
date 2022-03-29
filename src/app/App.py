import streamlit as st
st.title('Prediction of the average daily usage of digital media in the United States')

"Author: Grégoire Heidt (https://github.com/GregoireHeidt)"
#%%

from scipy.stats import linregress
st.subheader("Prediction")

years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
daily_usage = [2.7,2.9,3.2,3.7,4.4,4.9,5.1,5.4,5.7,6.0,6.3]

regression_result = linregress(years, daily_usage)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept


def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

if prediction_rounded > 24:
    prediction_rounded = 24
elif prediction_rounded < 0:
    prediction_rounded = 0
else:
    pass
"The predicted average daily usage of digital media in the United States for the chosen year:"

st.write(prediction_rounded)

"Hours per day"

st.subheader("About the model:")

"This model is a linear regression based on the years 2008 until 2018 "

#%%

#%%
