import streamlit as st
import csv
import pandas


st.set_page_config(layout='wide')

col1,col2 = st.columns(2)

with col1:
    st.image("images\photo.jpeg",width=500)

with col2:
    st.title("  ninud")
    st.info('they call me cool (i am delusional).')

info = '''apps i did not make:'''
st.title(info)

# with open('data.csv','r') as file:
#     data = csv.reader(file, delimiter=';')
#     for row in data:
#         st.write(row)

col3, chumma_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    df = pandas.read_csv('data.csv', sep=';')
    for index, row in df[::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.write(f"[github repo]({row['url']})")
with col4:
    df = pandas.read_csv('data.csv', sep=';')
    for index, row in df[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.write(f"[github repo]({row['url']})")



