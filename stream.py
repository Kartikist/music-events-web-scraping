import streamlit as st
import plotly.express as px
import temp as t

st.title("Temperature graph")


date, temp = t.send()

figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temp (C)"} )
st.plotly_chart(figure)
            


