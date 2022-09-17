import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.set_page_config(page_title = 'GROUND ELEVATION VISUALIZER', layout='wide')
st.write('By Maaz Jamshaid')
st.title('UAV SMALL SCALE RAW DATA GROUND ELEVATION ANALYZER')


test = st.button('Use Sample File ')
own_file = st.button('Upload Your Own File')
if test:
    st.subheader('DEFAULT COLORMAP: VIRIDIS ')
    st.subheader('CHOOSE COLORMAP:')
    mode1 = st.button('JET')
    mode2 = st.button('SEISMIC')
    mode3 = st.button('PuOr')

    cmap = None
    if mode1:
        cmap = 'jet'
    elif mode2:
        cmap = 'seismic'
    elif mode3:
        cmap = 'PuOr'

    st.markdown('---')
    excel_data_df = pd.read_excel('flight_data.xlsx')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.write(excel_data_df)

    X = excel_data_df['x'].tolist()
    Y = excel_data_df['y'].tolist()
    Z = excel_data_df['z'].tolist()

    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    # Flatten trial data to meet your requirement:
    x = X.ravel()
    y = Y.ravel()
    z = Z.ravel()

    # Resampling on as square grid with given resolution:
    resolution = 8
    xlin = np.linspace(min(x), max(x), resolution)
    ylin = np.linspace(min(y), max(y), resolution)
    Xlin, Ylin = np.meshgrid(xlin, ylin)

    # Linear multi-dimensional interpolation:
    interpolant = interpolate.NearestNDInterpolator([r for r in zip(x, y)], z)
    Zhat = interpolant(Xlin.ravel(), Ylin.ravel()).reshape(Xlin.shape)
    # Render and interpolate again if necessary:
    fig, axe = plt.subplots()
    axe.imshow(Zhat, origin="lower", cmap=cmap, interpolation='bicubic', extent=[min(x), max(x), min(y), max(y)])

    # plt.xlabel('X Values', fontsize = 15)
    # plt.ylabel('Y Values', fontsize = 15)

    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.yticks(np.arange(min(y), max(y) + 1, 1.0))

    axe.set_xticklabels([])
    axe.set_yticklabels([])

    axe.grid(True, linewidth=0.3, color='w')
    norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=False)

    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm))
    st.title('ANALYZER')
    st.write(fig, figsize=(2, 2))

else:
    st.subheader('Choose an EXCEL file')
    upload = st.file_uploader('EXCEL FILE: Use x,y,z for Latitude, Longitude, Altitude', type='xlsx')

    if upload:
        st.subheader('DEFAULT COLORMAP: VIRIDIS ')
        st.subheader('CHOOSE COLORMAP:')
        mode1 = st.button('JET')
        mode2 = st.button('SEISMIC')
        mode3 = st.button('PuOr')

        cmap = None
        if mode1:
            cmap = 'jet'
        elif mode2:
            cmap = 'seismic'
        elif mode3:
            cmap = 'PuOr'

        st.markdown('---')
        excel_data_df = pd.read_excel(upload, engine='openpyxl')
        col1, col2, col3 = st.columns(3)
        with col2:
            st.write(excel_data_df)

        X = excel_data_df['x'].tolist()
        Y = excel_data_df['y'].tolist()
        Z = excel_data_df['z'].tolist()

        X = np.array(X)
        Y = np.array(Y)
        Z = np.array(Z)
        # Flatten trial data to meet your requirement:
        x = X.ravel()
        y = Y.ravel()
        z = Z.ravel()

        # Resampling on as square grid with given resolution:
        resolution = 8
        xlin = np.linspace(min(x), max(x), resolution)
        ylin = np.linspace(min(y), max(y), resolution)
        Xlin, Ylin = np.meshgrid(xlin, ylin)

        # Linear multi-dimensional interpolation:
        interpolant = interpolate.NearestNDInterpolator([r for r in zip(x, y)], z)
        Zhat = interpolant(Xlin.ravel(), Ylin.ravel()).reshape(Xlin.shape)
        # Render and interpolate again if necessary:
        fig, axe = plt.subplots()
        axe.imshow(Zhat, origin="lower", cmap=cmap, interpolation='bicubic', extent=[min(x), max(x), min(y), max(y)])

        # plt.xlabel('X Values', fontsize = 15)
        # plt.ylabel('Y Values', fontsize = 15)

        plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
        plt.yticks(np.arange(min(y), max(y) + 1, 1.0))

        axe.set_xticklabels([])
        axe.set_yticklabels([])

        axe.grid(True, linewidth=0.3, color='w')
        norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=False)

        plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm))
        st.title('ANALYZER')
        st.write(fig, figsize=(2, 2))








