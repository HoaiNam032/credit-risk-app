import streamlit as st
import pandas as pd
import pickle
from catboost import CatBoostClassifier

# Tải model đã lưu
@st.cache_resource
def load_model():
    with open('catboost_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.set_page_config(page_title="Dự Đoán Rủi Ro Tín Dụng", page_icon="🏦", layout="wide")
    
    st.sidebar.title("🏦 Ứng dụng dự đoán tín dụng")
    st.sidebar.markdown("Ứng dụng này giúp bạn **dự đoán khả năng vỡ nợ** của khách hàng dựa trên thông tin vay.")
    st.sidebar.info("📌 Lưu ý: Đây là công cụ hỗ trợ, không thay thế chuyên gia tài chính.")

    st.title("📊 Dự Đoán Rủi Ro Tín Dụng Khách Hàng")
    st.write("Vui lòng nhập đầy đủ thông tin để hệ thống phân tích và dự đoán khả năng vỡ nợ.")

    with st.expander("👤 Thông tin cá nhân khách hàng"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("🎂 Tuổi", 20, 80, 30)
            employment_years = st.number_input("💼 Số năm làm việc", 0, 50, 5)
            cred_hist_length = st.number_input("📈 Số năm lịch sử tín dụng", 0, 100, 10)
            home_ownership = st.selectbox("🏠 Sở hữu nhà", ["MORTGAGE", "OTHER", "OWN", "RENT"])
        with col2:
            income = st.number_input("💰 Thu nhập hàng năm ($)", 0, value=50000)
            default_on_file = st.selectbox("⚠️ Lịch sử vỡ nợ", ["N", "Y"])

    with st.expander("💳 Thông tin khoản vay"):
        col3, col4 = st.columns(2)
        with col3:
            loan_amount = st.number_input("💸 Số tiền vay ($)", 0, value=10000)
            loan_int_rate = st.number_input("📉 Lãi suất khoản vay (%)", 0.0, 100.0, 5.0)
        with col4:
            loan_intent = st.selectbox("🎯 Mục đích vay", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
            loan_grade = st.selectbox("🔠 Điểm tín dụng", ["A", "B", "C", "D", "E", "F", "G"])

    # Tính toán tỷ lệ thu nhập trên số tiền vay
    loan_percent_income = (loan_amount / income) * 100 if income > 0 else 0
    st.markdown(f"💡 **Tỷ lệ thu nhập trên số tiền vay:** `{loan_percent_income:.2f}%`")

    # Tạo DataFrame từ dữ liệu người dùng
    input_data = pd.DataFrame({
        'person_age': [age],
        'person_income': [income],
        'person_emp_length': [employment_years],
        'loan_amnt': [loan_amount],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_cred_hist_length': [cred_hist_length],
        'person_home_ownership': [home_ownership],
        'loan_intent': [loan_intent],
        'loan_grade': [loan_grade],
        'cb_person_default_on_file': [default_on_file]
    })

    # One-hot encoding các biến phân loại
    input_data_encoded = pd.get_dummies(input_data)

    # Load mô hình
    model = load_model()
    expected_features = model.feature_names_

    for feature in expected_features:
        if feature not in input_data_encoded.columns:
            input_data_encoded[feature] = 0
    input_data_encoded = input_data_encoded[expected_features]

    # Nút dự đoán
    if st.button("🚀 Dự đoán ngay"):
        prediction = model.predict(input_data_encoded)
        probability = model.predict_proba(input_data_encoded)[0]

        if prediction[0] == 1:
            st.error(f"❌ Rủi ro **CAO**: Khách hàng có khả năng vỡ nợ (Xác suất: {probability[1]:.2%})")
        else:
            st.success(f"✅ Rủi ro **THẤP**: Khách hàng ổn định tài chính (Xác suất: {probability[0]:.2%})")

if __name__ == '__main__':
    main()
