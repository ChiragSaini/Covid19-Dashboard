import covid
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
c = covid.Covid()

@st.cache
def load_data_and_return_dataframe():
    all_cases = c.get_all_cases()
    df = pd.DataFrame({
    'Country': [i['attributes']['Country_Region'] for i in all_cases],
    'Confirmed': [i['attributes']['Confirmed'] for i in all_cases],
    'Deaths': [i['attributes']['Deaths'] for i in all_cases],
    'Recovered': [i['attributes']['Recovered'] for i in all_cases],
    'Active': [i['attributes']['Active'] for i in all_cases]
    # 'latitude': [i['attributes']['Lat'] for i in all_cases],
    # 'longitude': [i['attributes']['Long_'] for i in all_cases]
    })
    return df

df = load_data_and_return_dataframe()
st.title("COVID19 DashBoard")
st.header("COVID19 Dashboard made using Python and Streamlit")
st.subheader("Check any Country Status")
sel_country = st.multiselect(label="Select Country", options=df["Country"])
if sel_country:
    countries = []
    for c in sel_country:
        countries.append(df[df["Country"] == c].values)
    for arr in countries:
        data = arr[0]
        st.markdown(f"<div class='row ml-4'><h3>{data[0]}, </h3><h4>Confirmed:{data[1]}, </h4><h4 style='color:red'>Deaths:{data[2]}, </h4><h4 style='color:green'>Recovered:{data[3]},</h4><h4 style='color:orange'>Active:{data[4]},</h4></div>",unsafe_allow_html=True)

st.markdown("<h2>Top 10 Countries affected</h2>", unsafe_allow_html=True)
ax  =df[:10].plot(kind='bar', legend=True, fontsize=8)
ax.set_xticklabels(df[:10]["Country"])
st.pyplot()
for data in df[:10].values:
    st.markdown(f"<div class='row ml-4'><h3>{data[0]}, </h3><h4>Confirmed:{data[1]}, </h4><h4 style='color:red'>Deaths:{data[2]}, </h4><h4 style='color:green'>Recovered:{data[3]},</h4><h4 style='color:orange'>Active:{data[4]},</h4></div>",unsafe_allow_html=True)


st.markdown("<h3> All Countries Data</h3>", unsafe_allow_html=True)
st.dataframe(df)