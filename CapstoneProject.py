# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1veX7mHvvijxrh9h9tyrDbMZBqZnzQlT7

# **Capstone Project - DQLab Tetris 2**

# Sumber Data
Source Url: https://www.bps.go.id/indicator/28/1980/3/tingkat-penyelesaian-pendidikan-menurut-jenjang-pendidikan-dan-provinsi.html

Source Url: https://www.bps.go.id/indicator/28/1466/3/angka-melek-huruf-penduduk-umur-15-59-tahun-menurut-provinsi.html

Source Url: https://www.bps.go.id/indicator/19/1172/3/upah-rata---rata-per-jam-pekerja-menurut-provinsi.html

# Import Library
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

"""# Load Dataset

"""

data_upah = pd.read_excel('/content/sample_data/2015 -2021 Upah Rata - Rata Per Jam Pekerja Menurut Provinsi.xlsx')
data_melek_huruf = pd.read_excel('/content/sample_data/2015-2021 Angka Melek Huruf Penduduk Umur 15-59 Tahun Menurut Provinsi.xlsx')
data_tingkat_pendidikan = pd.read_excel('/content/sample_data/2015-2021 Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Provinsi.xlsx')

"""# Knowing Dataset Dimension"""

data_upah.shape

data_melek_huruf.shape

data_tingkat_pendidikan.shape

"""# Data Cleansing"""

#adding prefix
data_upah1 = data_upah.add_prefix('upah_')
data_upah2 = data_upah1.rename(columns={'upah_Provinsi':'Provinsi'})
data_upah2

data_melek_huruf1 = data_melek_huruf.add_prefix('melek_huruf_')
data_melek_huruf2 = data_melek_huruf1.rename(columns={'melek_huruf_Provinsi':'Provinsi'})
print(data_melek_huruf2)
kolom_melek_huruf = data_melek_huruf2.columns
print(kolom_melek_huruf)

join_data = pd.merge(
    data_upah2,
    data_melek_huruf2,
    on='Provinsi', 
    how='inner')
print(join_data)

Data = pd.merge(
    join_data,
    data_tingkat_pendidikan, 
    how='inner', 
    on='Provinsi')
print(Data)
Data

"""# Aggregating to find spesific key"""

Data1 = pd.DataFrame(Data['Provinsi'])
Data1

Data1['Rerata_Melek_Huruf(2015-2021)'] = Data[['melek_huruf_2015','melek_huruf_2016','melek_huruf_2017','melek_huruf_2018','melek_huruf_2019','melek_huruf_2020','melek_huruf_2021']].mean(axis=1)
Data1['Rerata_Tingkat_Pendidikan_SD(2015-2021)'] = Data[['SD_2015','SD_2016','SD_2017','SD_2018','SD_2019','SD_2020','SD_2021']].mean(axis=1)
Data1['Rerata_Tingkat_Pendidikan_SMP(2015-2021)'] = Data[['SMP_2015','SMP_2016','SMP_2017','SMP_2018','SMP_2019','SMP_2020','SMP_2021']].mean(axis=1)
Data1['Rerata_Tingkat_Pendidikan_SMA(2015-2021)'] = Data[['SMA_2015','SMA_2016','SMA_2017','SMA_2018','SMA_2019','SMA_2020','SMA_2021']].mean(axis=1)
Data1['Rerata_Upah(2015-2021)'] = Data[['upah_2015','upah_2016','upah_2017','upah_2018','upah_2019','upah_2020','upah_2021']].mean(axis=1)
Data1

"""# Filtering"""

Data1.describe()

Data1[Data1['Provinsi']=='INDONESIA']

pyplot.scatter(Data1['Rerata_Melek_Huruf(2015-2021)'], Data1['Rerata_Tingkat_Pendidikan_SD(2015-2021)'])
pyplot.scatter(Data1['Rerata_Melek_Huruf(2015-2021)'], Data1['Rerata_Tingkat_Pendidikan_SMP(2015-2021)'])
pyplot.scatter(Data1['Rerata_Melek_Huruf(2015-2021)'], Data1['Rerata_Tingkat_Pendidikan_SMA(2015-2021)'])

"""# Highlight yang berada jauh dari persebaran data
![image.png](data:image/png;base64,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)

maka dibuat batas, yaitu data yang dibawah rata-rata keseluruhan atau daerah yang bernilai minimum
"""

Data1['Rerata_Melek_Huruf(2015-2021)'].min()
Data_Provinsi = Data1[Data1['Rerata_Melek_Huruf(2015-2021)']==Data1['Rerata_Melek_Huruf(2015-2021)'].min()]
Data_Provinsi

"""apakah variabel melek huruf dan tingkat pendidikan mempengaruhi upah di Papua ? """

Data1[Data1['Provinsi'] == 'INDONESIA']

"""ternyata rata-rata upah di Papua diatas rata-rata total provinsi di seluruh Indonesia"""

DataUpah = Data1[Data1['Rerata_Upah(2015-2021)']>15302.285714].sort_values('Rerata_Upah(2015-2021)', ascending=False).head()
DataUpah