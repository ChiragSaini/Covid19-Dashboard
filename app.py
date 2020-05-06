import covid
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# common variables
GITHUB_REFERENCE = "<h5><a href='https://github.com/ChiragSaini/' target='_blank'>Github</a></h5>"
LINKED_IN_REFERENCE = "<h5><a href='https://www.linkedin.com/in/chiragsaini97/' target='_blank'>LinkedIn</a></h5>"
TWITTER_REFERENCE = "<h5><a href='https://twitter.com/ChiragSaini97' target='_blank'>Twitter</a></h5>"
SUBHEAD_TITLE = "Covid19 Dashboard"
SUBHEAD_CREDITS = "Made by Chirag Saini"
c = covid.Covid()


# converts DataFrame to presentable card view in rows
def get_ui_for_data(data_input):
    column_properties = "margin:3%; float:right; width:15%; text-align: right"
    base_card_styling = "margin:1%; padding:1%; " \
                        "text-align:center;" \
                        "width:16%; " \
                        "box-shadow:0 4px 8px 0 rgba(0,0,0,0.2);"
    return f"<div class='row'>" \
           f"<h5 style='color:black; {column_properties}'>{data_input[0]}</h5>" \
           f"<h5 style='color:blue; {base_card_styling}'><h6>Total</h6>{data_input[1]}</h5> " \
           f"<h5 style='color:red; {base_card_styling}'><h6>Deaths</h6>{data_input[2]}</h5> " \
           f"<h5 style='color:green; {base_card_styling}'><h6>Saved</h6>{data_input[3]}</h5> " \
           f"<h5 style='color:orange; {base_card_styling}'><h6>Active</h6>{data_input[4]}</h5> " \
           f"</div>"


@st.cache
def load_data_and_return_dataframe():
    all_cases = c.get_data()
    return pd.DataFrame({
        'Country': [i['country'] for i in all_cases],
        'Confirmed': [i['confirmed'] for i in all_cases],
        'Deaths': [i['deaths'] for i in all_cases],
        'Recovered': [i['recovered'] for i in all_cases],
        'Active': [i['active'] for i in all_cases]
        # 'latitude': [i['attributes']['Lat'] for i in all_cases],
        # 'longitude': [i['attributes']['Long_'] for i in all_cases]
    })


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
        data[1] = str(round(data[1] / 1000, 1)) + " K"
        data[2] = str(round(data[2] / 1000, 1)) + " K"
        data[3] = str(round(data[3] / 1000, 1)) + " K"
        data[4] = str(round(data[4] / 1000, 1)) + " K"
        # data[2] = str(data[2] / 1000) + " K"
        # data[3] = str(data[3] / 1000) + " K"
        # data[4] = str(data[4] / 1000) + " K"
        st.markdown(get_ui_for_data(data), unsafe_allow_html=True)

st.markdown("<h2>Top 10 Countries affected</h2>", unsafe_allow_html=True)
ax = df[:10].plot(kind='bar', legend=True, fontsize=8)
plt.ticklabel_format(axis="y", style="plain", scilimits=None)
ax.set_xticklabels(df[:10]["Country"])
st.pyplot()
for data in df[:10].values:
    data[1] = str(round(data[1] / 1000, 1)) + " K"
    data[2] = str(round(data[2] / 1000, 1)) + " K"
    data[3] = str(round(data[3] / 1000, 1)) + " K"
    data[4] = str(round(data[4] / 1000, 1)) + " K" 
    st.markdown(get_ui_for_data(data), unsafe_allow_html=True)

st.markdown("<h3> All Countries Data</h3>", unsafe_allow_html=True)
st.dataframe(df)

# navigation (sidebar) properties
st.sidebar.subheader(SUBHEAD_TITLE)
st.sidebar.subheader(SUBHEAD_CREDITS)
st.sidebar.markdown(GITHUB_REFERENCE, unsafe_allow_html=True)
st.sidebar.markdown(LINKED_IN_REFERENCE, unsafe_allow_html=True)
st.sidebar.markdown(TWITTER_REFERENCE, unsafe_allow_html=True)
