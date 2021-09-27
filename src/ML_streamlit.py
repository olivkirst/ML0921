import pandas as pd
import streamlit as st
import csv
import seaborn as sns
import matplotlib.pyplot as plt


dfc_tt= pd.read_csv(r".\data\\processed\\Long_lat_pozos_train_test.csv", sep=",")
dfc_v= pd.read_csv(r".\data\\processed\\Long_lat_pozos_val.csv", sep=",")

st.set_page_config(layout="wide")

# returns ','
# Sidebar config
add_file = st.sidebar.file_uploader('Otros datos oara cargar si necesario', type = 'csv')
if add_file is not None: #
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(add_file)
    separator = dialect.delimiter
    df = pd.read_csv(add_file, sep = separator)
page = st.sidebar.selectbox(
    'Menu',
    ('home', 'datos', 'filtrado')
)

# Main page
def main_page():
    st.title('ANALISIS DE DATOS DE POZOS DE OIL & GAS')
    st.markdown('<h2>Mapa', unsafe_allow_html = True)
    with st.beta_expander('Origen de los datos'):
        st.write('The well log data used in this repo is licensed as Norwegian License for Open Government Data (NLOD) 2.0. '
                 '“Lithofacies data was provided by the FORCE Machine Learning competition with well logs and seismic 2020”. ')
# st.balloons()
    with st.echo():
        st.write("Esta forma tienen nuestros datos")
        st.dataframe(dfc_tt)

def datos():

    st.title('Localizacíon de los pozos')
    st.markdown('## Mapa con los pozos de entrenamiento y testeo (98)')
    st.map(data =dfc_tt)
    st.markdown('## Mapa con  los pozos  de validación (10) ')
    st.map(data = dfc_v)


if page == 'home':
    main_page()
elif page == 'datos':
    datos()