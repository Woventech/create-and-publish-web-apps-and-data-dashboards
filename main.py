import streamlit as st
import pandas as pd

data = {
  'series_1' : [1, 2, 3, 5, 7],
  'series_2': [10, 20, 35, 58, 100]
}
df = pd.DataFrame(data)

st.title('Our first streamlit app ')
st.subheader('introducing streamlit in automate everything')
st.write('''this is our first web app. Enjoy it!''')
st.write(df)
st.line_chart(df)
st.area_chart(df)


myslider= st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)
