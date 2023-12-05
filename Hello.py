import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Prediction of Body Fat",
    page_icon="👋",
)

# 加载模型和Scaler
male_model = joblib.load('male_model.pkl')
female_model = joblib.load('female_model.pkl')
male_scaler = joblib.load('male_scaler.pkl')
female_scaler = joblib.load('female_scaler.pkl')

# 创建Streamlit应用
st.title('Body Fat Prediction Application')
# 添加用户输入组件
st.divider()

col1, col2, col3, col4 = st.columns([1.1,1,1,1],gap="medium")

def calc():
    # 构建输入数据
    input_data = pd.DataFrame({
        'Age': [age],
        'Weight': [weight],
        'Height': [height],
        'Neck': [neck],
        'Chest': [chest],
        'Waist': [waist],
        'Hip': [hip],
        'Thigh': [thigh],
        'Knee': [knee],
        'Ankle': [ankle],
        'Biceps': [biceps],
        'Forearm': [forearm],
        'Wrist': [wrist],
    })
    model = male_model
    scaler = male_scaler
    if gender == 'Female':
        model = female_model
        scaler = female_scaler

    # 使用Scaler进行缩放
    input_data_scaled = scaler.transform(input_data)

    # 使用模型进行预测
    prediction = model.predict(input_data_scaled)
    st.divider()
    # 显示预测结果
    st.metric(label="body fat percentage", value=f"{prediction[0]:.2f}%")

with col1:
    gender = st.radio('Gender', ['Male', 'Female'],horizontal=True)
    age = st.number_input('Age', min_value=0, max_value=99, value=25)
    st.divider()
    weight = st.slider('Weight', min_value=40, max_value=200, value=70, help="Unit: kg")
    height = st.slider('Height', min_value=140, max_value=220, value=170, help="Unit: cm")
with col2:
    neck = st.slider('Neck', min_value=20, max_value=40, value=30, help="Unit: cm")
    chest = st.slider('Chest', min_value=70, max_value=150, value=90, help="Unit: cm")
    waist = st.slider('Waist', min_value=50, max_value=120, value=80, help="Unit: cm")
    hip = st.slider('Hips', min_value=70, max_value=150, value=90, help="Unit: cm")
    thigh = st.slider('Thigh', min_value=40, max_value=90, value=50, help="Unit: cm")
with col3:
    knee = st.slider('Knee', min_value=30, max_value=60, value=40, help="Unit: cm")
    ankle = st.slider('Ankle', min_value=20, max_value=40, value=25, help="Unit: cm")
    biceps = st.slider('Biceps', min_value=20, max_value=45, value=30, help="Unit: cm")
    forearm = st.slider('Forearm', min_value=20, max_value=40, value=30, help="Unit: cm")
    wrist = st.slider('Wrist', min_value=10, max_value=25, value=15, help="Unit: cm")
with col4:
    # 进行预测
    if st.button('Calculate',type="primary",use_container_width=True):
        calc()

