# Your Name
# si649f20 Altair transforms 2

# imports we will use
import streamlit as st
import altair as alt
import pandas as pd

datasetURL = "https://raw.githubusercontent.com/eytanadar/si649public/master/lab5/assets/hw/movie_after_1990.csv"
movies_test = pd.read_csv(datasetURL, encoding="latin-1")

# Title
st.title("Lab5 by Yi-Ting Hsiao")
st.write("Hello World")

# Making of all charts
car_url = "https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/cars.json"
cars = pd.read_json(car_url)

hp_mpg = alt.Chart(cars).mark_circle(size=80, opacity=0.5).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color="Origin"
)

st.write(hp_mpg)


btn = st.button('Click me')
if btn:
    st.write(hp_mpg)
else:
    "click the button to see the viz"


# create a list of options
y_axis_options = ["Acceleration", "Miles_per_Gallon", "Displacement"]
# create a select box
y_axis_selectbox = st.sidevselectbox(
    label="Select the column to plot for the y-axis",
    options=y_axis_options
)
# create a chart that uses the select box
chart = alt.Chart(cars).mark_circle(size=80, opacity=0.5).encode(
    x='Horsepower:Q',
    y=y_axis_selectbox,
    color="Origin"
)
# render the chart
chart
