#!/usr/bin/env python
# coding: utf-8

import altair as alt
import streamlit as st
import pandas as pd
datasetURL = "https://raw.githubusercontent.com/eytanadar/si649public/master/lab5/assets/hw/movie_after_1990.csv"
movies_test = pd.read_csv(datasetURL, encoding="latin-1")


# TODO: Replicate visualization 1


base = alt.Chart(movies_test).transform_joinaggregate(
    groupby=['year'],
    averageBudget='average(budget)',
    MaxBudget='max(budget)'
).transform_filter(
    (alt.datum.budget > (2 * alt.datum.averageBudget)
     ) & (alt.datum.year >= 1990) & (alt.datum.year <= 1997)
)

dot_chart = base.mark_circle().encode(
    alt.X('year:O'),
    alt.Y('budget:Q')
)

line_chart = base.mark_line().encode(
    alt.X('year:O'),
    alt.Y('averageBudget:Q')
)

text = dot_chart.transform_filter(
    alt.datum.budget == alt.datum.MaxBudget
).mark_text(
    align='center',
    dy=-15  # delta x = 7 pixel aside
).encode(alt.Text('title:N'))


viz1 = (dot_chart + line_chart + text).properties(width=600, height=300)


base = alt.Chart(movies_test).transform_bin(
    'binned_rating', 'rating'
).transform_aggregate(
    groupby=['binned_rating', 'test_result'],
    count='count()'
).transform_filter(
    (alt.datum.test_result != 'dubious') & (alt.datum.binned_rating >= 2)
)

heatmap = base.mark_rect().encode(
    y='test_result:N',
    x='binned_rating:O',
    color='count:Q'
)

text = base.mark_text().encode(
    alt.X('binned_rating:O'),
    alt.Y('test_result:N'),
    alt.Text('count:Q'))

text_white = base.transform_filter(
    alt.datum.count >= 265
).mark_text(color='white').encode(
    alt.X('binned_rating:O'),
    alt.Y('test_result:N'),
    text='count:Q')

highlight = base.transform_joinaggregate(
    groupby=['test_result'],
    max_rating='max(binned_rating)'
).transform_filter(
    alt.datum.max_rating >= 9
).mark_rect(filled=False, color='red').encode(
    y='test_result:N',
    x='binned_rating:O',
)


viz2 = (heatmap + text + text_white +
        highlight).properties(width=500, height=100)


base_dom = alt.Chart(movies_test).transform_filter(
    alt.datum.country_binary == 'U.S. and Canada'
).transform_window(
    groupby=['test_result'],
    sort=[alt.SortField('dom_gross', order='ascending')],
    gross_rank='rank(*)'
)

bar_dom = base_dom.mark_bar().encode(
    alt.X('average(dom_gross):Q', title='Average of dom_gross'),
    alt.Y('test_result:N'),
    alt.Color('average(dom_gross):Q')
)

text_dom = base_dom.transform_filter(
    alt.datum.gross_rank == 10
).mark_text(
    align='left',
    dx=7,
    color='black'
).encode(
    alt.X('gross_rank:Q', title='Average of dom_gross'),
    alt.Y('test_result:N'),
    alt.Text('title:N')
)


base_int = alt.Chart(movies_test).transform_filter(
    alt.datum.country_binary != 'U.S. and Canada'
).transform_window(
    groupby=['test_result'],
    sort=[alt.SortField('int_gross', order='ascending')],
    gross_rank='rank(*)'
)


bar_int = base_int.mark_bar().encode(
    alt.X('average(int_gross):Q',  title='Average of int_gross'),
    alt.Y('test_result:N'),
    alt.Color('average(int_gross):Q', scale=alt.Scale(
        domain=[103263397, 192241463], scheme="reds"))
)

text_int = base_int.transform_filter(
    alt.datum.gross_rank == 10
).mark_text(
    align='left',
    dx=7,
    color='white'
).encode(
    alt.X('gross_rank:Q',  title='Average of int_gross'),
    alt.Y('test_result:N'),
    alt.Text('title:N')
)


viz3 = ((bar_dom + text_dom) & (bar_int + text_int)).resolve_scale(
    color='independent',
    x='shared'
)


base = alt.Chart(movies_test).transform_fold(
    ["budget", "int_gross"],
    as_=["Finance", "dollars"]
)
viz4 = base.mark_bar().encode(
    alt.Y('Finance:N'),
    alt.X('average(dollars):Q'),
    alt.Color('Finance:N')
)


# Title
st.title("Lab5 by Yi-Ting Hsiao")

# create a list of options
options = ["Viz1", "Viz2", "Viz3", "Viz4"]
# create a select box
selectbox = st.sidebar.selectbox(
    label="Select a vizualization to display",
    options=options
)

chart = None
# create a chart that uses the select box
if selectbox == "Viz1":
    viz1
elif selectbox == "Viz2":
    viz2
elif selectbox == "Viz3":
    viz3
elif selectbox == "Viz4":
    viz4
# render the chart
