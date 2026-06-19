
import streamlit as st

st.set_page_config(page_title="Laptop Price Predictor")

st.title("💻 Laptop Price Predictor")
st.write("Summer Training Project")

company = st.selectbox(
    "Company",
    ['Apple','HP','Acer','Asus','Dell','Lenovo','Chuwi',
     'MSI','Microsoft','Toshiba','Huawei','Xiaomi',
     'Vero','Razer','Mediacom','Samsung','Google',
     'Fujitsu','LG']
)

cpu = st.selectbox(
    "CPU Brand",
    ['Intel Core i3',
     'Intel Core i5',
     'Intel Core i7',
     'AMD Processor',
     'Other Intel Processor']
)

ram = st.slider("RAM (GB)",2,64,8)

ssd = st.number_input("SSD Storage (GB)",0,2048,256)

hdd = st.number_input("HDD Storage (GB)",0,4096,0)

weight = st.number_input("Weight (kg)",0.5,5.0,1.5)

screen_size = st.number_input("Screen Size (Inches)",10.0,20.0,15.6)

touchscreen = st.selectbox("Touchscreen",[0,1])

ips = st.selectbox("IPS Display",[0,1])
import pickle
import pandas as pd

model = pickle.load(open('laptop_price_model.pkl','rb'))
columns = pickle.load(open('columns.pkl','rb'))

if st.button("Predict Price"):

    input_df = pd.DataFrame(0, index=[0], columns=columns)

    # Numerical features
    if 'Ram' in input_df.columns:
        input_df['Ram'] = ram

    if 'SSD' in input_df.columns:
        input_df['SSD'] = ssd

    if 'HDD' in input_df.columns:
        input_df['HDD'] = hdd

    if 'Weight' in input_df.columns:
        input_df['Weight'] = weight

    if 'Inches' in input_df.columns:
        input_df['Inches'] = screen_size

    if 'Touchscreen' in input_df.columns:
        input_df['Touchscreen'] = touchscreen

    if 'IPS' in input_df.columns:
        input_df['IPS'] = ips

    # Company
    company_col = f'Company_{company}'
    if company_col in input_df.columns:
        input_df[company_col] = 1

    # CPU Brand
    cpu_col = f'CPU_Brand_{cpu}'
    if cpu_col in input_df.columns:
        input_df[cpu_col] = 1

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Laptop Price: ₹{prediction:,.0f}")

