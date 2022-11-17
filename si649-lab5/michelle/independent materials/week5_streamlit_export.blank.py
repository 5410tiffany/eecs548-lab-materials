# Your Name
# si649f20 altair transforms 2

# imports we will use
import altair as alt
import pandas as pd
import streamlit as st

#Title
st.title("Lab6 by <Your Name>")

#Import data
df1=pd.read_csv("https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df1.csv")
df2=pd.read_csv("https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df2_count.csv")
df3=pd.read_csv("https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df3.csv")
df4=pd.read_csv("https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df4.csv")

# change the 'datetime' column to be explicitly a datetime object
df2['datetime'] = pd.to_datetime(df2['datetime'])
df3['datetime'] = pd.to_datetime(df3['datetime'])
df4['datetime'] = pd.to_datetime(df4['datetime'])

#Sidebar


###### Making of all the charts


########Vis 1

##Interaction requirement 2, change opacity when hover over

##Interaction requirement 3 and 4, create brushing filter

##Static Component - Bars

##Static Component - Emojis

##Static Component - Text

##Put all together


########Vis 2

#Zooming and Panning

#vertical line

#interaction dots

#Static component line chart

#Put all together


########Vis3

#Altair version

#Streamlit widget version


########Vis4 BONUS OPTIONAL

#Altair version

#Streamlit widget version


##### Display graphs