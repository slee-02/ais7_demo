import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide"
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown(" 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text("Loading data...")
mpg = load_data(url)
data_load_state.text("Done! (using st.cache)")

st.sidebar.header("User Input Features")
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('Origin', sorted_unique_origin, sorted_unique_origin)
selected_year = st.sidebar.selectbox("Year", list(mpg.model_year.unique()))

if selected_year > 0 :
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots(fig_size=(10, 3))
sns.countplot(data=mpg, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

pxh = px.histogram(mpg, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

