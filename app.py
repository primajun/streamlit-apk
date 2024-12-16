import pickle 
import streamlit as st
import base64

model = pickle.load(open('model.sav', 'rb'))

#judul web
st.title ('Estimasi Harga Mobil Bekas')

Car_Name = st.text_input ('Nama Mobil')

Year = st.number_input('tahun mobil', min_value=0) 
Pprice = st.number_input('harga Mobil Terbaru', min_value=0)
present_price = Pprice/18652353

Kms_Driven = st.number_input('Kilometer Mobil', min_value=0)

Fuel_Type = st.radio('Bahan Bakar', {0, 1, 2})
Seller_Type = st.radio('Jenis Penjual', [0, 1])
Transmission = st.radio('Transmisi Mobil', [0, 1])
Owner = st.number_input('Jumlah Kepemilihan Mobil Sebelumnya', min_value=0, max_value=10)

predict = ''

if st.button('Estmiasi Harga'):

    if Year < 0 or present_price < 0 or Kms_Driven < 0 or Owner < 0:
        st.error('input Tidak Boleh Negatif!')
    else:
        
        predict = predict(
            [[Year, present_price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]]
        )
        toRupiah = Pprice *  18652353
        st.writer('Estimasi Harga Dalam Rupiah :')
        st.success(f'Rp. {toRupiah[0]:,.0f}')