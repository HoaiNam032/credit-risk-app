# 💳 Credit Risk Analysis & Prediction

## 📝 Giới thiệu
Dự án này được thực hiện trong môn học **Phân tích dữ liệu** với mục tiêu:
- Phân tích các yếu tố ảnh hưởng đến **rủi ro tín dụng**.  
- Xác định các đặc điểm quan trọng liên quan đến khả năng vỡ nợ.  
- Ứng dụng các mô hình **Machine Learning** để dự đoán người vay có khả năng vỡ nợ.  
- So sánh, đánh giá và lựa chọn mô hình tối ưu.  

---

 **Xem bản rút gọn nội dung & slide thuyết trình (Canva)**:  
(https://www.canva.com/design/DAGaSLrmj7g/08tlG_nK8LW4u2qz2MsagA/edit)


---

## 📂 Dữ liệu
- Dataset: **Credit Risk Dataset** (Kaggle)  
- Số lượng bản ghi: **32,582**  
- Số biến đặc trưng: **12**  
- Biến mục tiêu: **loan_status** (0 = không vỡ nợ, 1 = vỡ nợ)  

### Một số biến quan trọng:
- `person_age`: Tuổi của người vay  
- `person_income`: Thu nhập hàng năm  
- `loan_amnt`: Số tiền vay  
- `loan_int_rate`: Lãi suất  
- `person_home_ownership`: Tình trạng sở hữu nhà (RENT, OWN, MORTGAGE)  
- `loan_grade`: Điểm tín dụng (A → G)  
- `loan_percent_income`: Tỷ lệ tiền vay so với thu nhập  
- `cb_person_default_on_file`: Lịch sử nợ xấu  

---

## 📊 Các bước thực hiện
1. **Khám phá & thống kê mô tả dữ liệu**  
   - Sử dụng **Python (pandas, numpy)** để đọc/ghi dữ liệu, kiểm tra kích thước tập dữ liệu, phân bố nhãn, mô tả thống kê cơ bản (mean, median, std).  

2. **Tiền xử lý dữ liệu**  
   - Loại bỏ giá trị rỗng & trùng lặp bằng **pandas** (`dropna`, `drop_duplicates`).  
   - Xử lý outlier bằng các hàm thống kê của **numpy/pandas**.  
   - Mã hóa biến phân loại bằng **One-Hot Encoding** hoặc **LabelEncoder** trong scikit-learn.  
   - Xử lý dữ liệu mất cân bằng bằng **SMOTE** từ thư viện `imblearn`.  

3. **Trực quan hóa dữ liệu**  
   - Vẽ biểu đồ phân tích biến mục tiêu, phân phối biến định lượng & định tính bằng **matplotlib, seaborn**.  
   - Phân tích mối quan hệ giữa các biến và rủi ro vỡ nợ thông qua biểu đồ hộp, histogram và countplot.  

4. **Phân tích tương quan (Correlation Matrix)**  
   - Tính toán hệ số tương quan bằng **pandas.corr()**.  
   - Vẽ heatmap bằng **seaborn** để xác định mối liên hệ giữa các biến độc lập và biến mục tiêu.  

5. **Xây dựng mô hình Machine Learning**  
   - Triển khai nhiều mô hình bằng **scikit-learn** và **CatBoost/XGBoost**:  
     - CatBoostClassifier  
     - DecisionTreeClassifier  
     - XGBClassifier  
     - RandomForestClassifier  
   - Viết script Python để chia tập dữ liệu train/test và huấn luyện mô hình.  

6. **Đánh giá mô hình**  
   - Đánh giá bằng các chỉ số **Accuracy, Precision, Recall, F1 Score** với `sklearn.metrics`.  
   - Vẽ **AUC - ROC Curve** bằng matplotlib để phân tích khả năng phân tách lớp.  
   - Phân tích **Feature Importance** từ CatBoost, XGBoost và Random Forest để rút ra insight.  

---

## 🚀 Kết quả
- **CatBoost** đạt hiệu suất tốt nhất:  
  - Accuracy: **93.87%**  
  - F1 Score: **83.64%**  
  - AUC: **0.95**  
- **XGBoost** cũng cho kết quả tương đối cao (Accuracy: **93.82%**)  
- Các mô hình **Decision Tree** và **Random Forest** có hiện tượng **overfitting**.  

👉 **CatBoost** được lựa chọn là mô hình tối ưu trong bài toán dự đoán rủi ro tín dụng.  

---


