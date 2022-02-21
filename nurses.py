from cgi import test
from email.mime import base
from gettext import install
from turtle import color, title
import numpy as np
import pandas as pd
import streamlit as st
import plotly as plt
import chart_studio
import chart_studio.plotly as py
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import seaborn as sns
import altair as alt
import pydeck as pdk
from plotly.graph_objs import *
import streamlit_player
from streamlit_player import st_player



st.title("Health Facilities in Lebanon")


st_player("https://www.youtube.com/watch?v=KjGA3SG_qpY")


st.write("Lebanon hosts a wide range of both private and public health care. There is a high standard of medical and dental care, especially in Beirut and it's surrounding areas. Many, if not all, health professionals speak English and/or French in addition to Arabic.")

dataframe= pd.read_csv('health.csv')
health=pd.DataFrame(dataframe)




st.subheader('Raw data')  
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(health)


st.subheader('Number of Health Facilties per Governorate')

df=health[['Governorate','Name of Health Facility']]


df_new=df.groupby(['Governorate']).size().reset_index(name='Number of Health Faculties')
bars= alt.Chart(df_new, title="Number of Health Facilities per Governorate").mark_bar().encode(x=alt.X('Governorate', stack='zero'), y=alt.Y('Number of Health Faculties'), color=alt.Color('Governorate'))
st.altair_chart(bars, use_container_width=True)

governorate_option=health['Governorate'].unique().tolist()
governorate= st.selectbox('Select Governorate', governorate_option, 0)
health=health[health['Governorate']==governorate]

df=health[['Governorate','Name of Health Facility']]
df_new=df.groupby(['Governorate']).size().reset_index(name='Number of Health Faculties')
bars= alt.Chart(df_new, title="Number of Health Facilities per Governorate").mark_bar().encode(x=alt.X('Governorate', stack='zero'), y=alt.Y('Number of Health Faculties'), color=alt.Color('Governorate'))
st.altair_chart(bars, use_container_width=True)





st.text('We can conclude that Mount Lebanon has the highest number of health faculties and Bekaa has the lowest number')

import plotly as plt

df_new=health[['Longitud_E','Latitude_N','Village']]
mapbox_access_token = 'pk.eyJ1IjoiYW1pcmJhenppIiwiYSI6ImNremIydG9ocTBocmwyd3M2NWY4amR5N2MifQ._mUJN0M6kAAzEYhAuLAwmQ'
site_lat = df_new.Latitude_N
site_lon = df_new.Longitud_E
table = ff.create_table(df_new)
locations_name = df_new.Village
data = [
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    ),
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=8,color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        hoverinfo='none'
    )]

layout = go.Layout(
    title='Health faculties in Lebanon',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=33.8547,
            lon=-35.8623
        ),
        pitch=0,
        zoom=3,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
st.plotly_chart(fig)




data = pd.read_csv('pop.csv')
st.write(data)
import plotly.express as px


df6 = px.bar(data, x="Governorate", y="Population", color="Governorate",
animation_frame="Year", animation_group="Governorate", range_y=[0,9])
st.write(df6)

st.text("We notice that the South has the largest population although it does not have the highest number of health facilities")

st.subheader('Recommendation')  
if st.checkbox('show'):
    st.subheader('My recommendation')
    st.write("We recommend that more health facilities should be built in the South of Lebanon to support the large number of citizens")


