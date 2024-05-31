import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
###  This is a sub sub header
This is text
""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 5)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")

import datetime

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('The date is:', d)

import datetime

t = st.time_input('Set an alarm for', datetime.time(8, 45))

st.write('The time is', t)


st.write(f"{d} {t}")

# x and y given as array_like objects
import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

st.plotly_chart(fig)