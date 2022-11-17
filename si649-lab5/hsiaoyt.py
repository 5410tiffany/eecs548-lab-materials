# Your Name
# si649f20 altair transforms 2

# imports we will use
import altair as alt
import pandas as pd
import streamlit as st

# Title
st.title("Lab6 by Hsiao Yi-Ting")

# Import data
df1 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df1.csv")
df2 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df2_count.csv")
df3 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df3.csv")
df4 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df4.csv")

# change the 'datetime' column to be explicitly a datetime object
df2['datetime'] = pd.to_datetime(df2['datetime'])
df3['datetime'] = pd.to_datetime(df3['datetime'])
df4['datetime'] = pd.to_datetime(df4['datetime'])

# Sidebar


# Making of all the charts


# Vis 1

selection = alt.selection_single(on='mouseover', empty='none')
opacityCondition = alt.condition(selection, alt.value(1), alt.value(0.6))

brush = alt.selection_interval()
filterCondition = alt.condition(brush, alt.value(0.6), alt.value(0))


# Static Component - Bars
chart_bars = alt.Chart(df1).transform_window(
    sort=[alt.SortField('PERCENT', order='descending')],
    emoji_rank='rank(*)'
).transform_filter(
    alt.datum.emoji_rank <= 10
).mark_bar(height=15, color='orange', opacity=0.6
           ).encode(
    alt.X('PERCENT:Q', axis=None),
    alt.Y('EMOJI:N', axis=None, sort=alt.EncodingSortField(
        field='emoji_rank', order='ascending')),
    tooltip='EMOJI:N',
    opacity=opacityCondition
).add_selection(selection).transform_filter(
    brush
)

base = alt.Chart(df1).mark_bar().encode(
    alt.Y('EMOJI:N', axis=None, sort=alt.EncodingSortField(
        field='emoji_rank', order='ascending')
    ))


# Static Component - Emojis
emojis = base.mark_text(
    align='left',
    baseline='middle',
    dx=-10
).encode(
    text=alt.Text('EMOJI:N'),
    opacity=opacityCondition
).add_selection(selection).add_selection(brush)


# Static Component - Text
texts = base.mark_text(
    align='left',
    baseline='middle',
    dx=-10
).encode(
    text=alt.Text('PERCENT_TEXT:N'),
    opacity=opacityCondition
).add_selection(selection).add_selection(brush)


# Put all together
viz1 = (emojis | texts | chart_bars).configure_view(
    strokeWidth=0).configure_axis(domain=False)


# Vis 2
zoom_pan = alt.selection_interval(bind='scales', encodings=['x'])

# vertical line
hover = alt.selection_single(
    on='mouseover', empty='none', nearest=True, init={'datetime': '12:10'})
opacityCondition = alt.condition(hover, alt.value(1), alt.value(0))

# interaction dots
hover_intersection = alt.selection_single(on='mouseover', fields=['datetime:T'],
                                          empty='none')
opacityCondition_intersection = alt.condition(
    hover_intersection, alt.value(1), alt.value(0))

# Static component line chart
chart_line = alt.Chart(df2).mark_line().encode(
    alt.X('datetime:T'),
    alt.Y('tweet_count:Q'),
    alt.Color('team:N')
).add_selection(zoom_pan)

vline = alt.Chart(df2).mark_rule(size=4, color="lightgray").encode(
    alt.X('datetime:T'),
    opacity=opacityCondition
).add_selection(hover)

intersection_dots = alt.Chart(df2).mark_circle(size=70, color='black').encode(
    alt.X('datetime:T'),
    alt.Y('tweet_count:Q'),
    opacity=opacityCondition,
    tooltip=['tweet_count', 'datetime', 'team']
).add_selection(hover_intersection)

# Put all together
viz2 = vline + chart_line + intersection_dots


# Vis3
# altiar version
static = alt.Chart(df3).mark_line().encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average',
            axis=alt.Axis(tickCount=5)),
    color=alt.Color("emoji:N", legend=alt.Legend(title="Team")))

circle = alt.Chart(df3).mark_circle(size=30, color='black', opacity=0).encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average', axis=alt.Axis(tickCount=5)))


# radio button
emojis = list(df3['emoji'].unique())
radio = alt.binding_radio(options=emojis, name='Select Emoji: ')
selectionEmoji = alt.selection_single(
    fields=['emoji'], bind=radio, clear='click')

# circle interval
select_circle = alt.selection_interval(empty='none')
opacityCondition = alt.condition(select_circle, alt.value(1), alt.value(0))


# put all together
viz3 = static.add_selection(selectionEmoji).transform_filter(selectionEmoji) + circle.add_selection(
    select_circle).transform_filter(selectionEmoji).encode(opacity=opacityCondition)

# streamlit version
base0 = alt.Chart(df3).transform_filter(
    alt.datum.emoji == emojis[0]
)

base1 = alt.Chart(df3).transform_filter(
    alt.datum.emoji == emojis[1]
)

static0 = base0.mark_line().encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average',
            axis=alt.Axis(tickCount=5)),
    color=alt.Color("emoji:N", legend=alt.Legend(title="Team")))

static1 = base1.mark_line().encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average',
            axis=alt.Axis(tickCount=5)),
    color=alt.Color("emoji:N", legend=alt.Legend(title="Team")))

circle0 = base0.mark_circle(size=30, color='black', opacity=0).encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average', axis=alt.Axis(tickCount=5)))


circle1 = base1.mark_circle(size=30, color='black', opacity=0).encode(
    x=alt.X("datetime:T", title=None, axis=alt.Axis(tickCount=5)),
    y=alt.Y("tweet_count:Q", title='Four minte rolling average', axis=alt.Axis(tickCount=5)))

# put all together
viz3_streamlit_0 = static0 + circle0.add_selection(
    select_circle).encode(opacity=opacityCondition)

viz3_streamlit_1 = static1 + circle1.add_selection(
    select_circle).encode(opacity=opacityCondition)

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
    st.write('Altair version')
    viz3
    st.write('Streamlit version')
    genre = st.radio("Select Emoji: ", (emojis[0], emojis[1]))
    if genre == emojis[0]:
        viz3_streamlit_0
    else:
        viz3_streamlit_1

# elif selectbox == "Viz4":
#     viz4
# render the chart
