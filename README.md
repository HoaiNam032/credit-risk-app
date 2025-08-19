# 💳 Credit Risk Analysis & Prediction

## 📝 Giới thiệu
Dự án này được thực hiện trong môn học **Phân tích dữ liệu** với mục tiêu:
- Phân tích các yếu tố ảnh hưởng đến **rủi ro tín dụng**.  
- Xác định các đặc điểm quan trọng liên quan đến khả năng vỡ nợ.  
- Ứng dụng các mô hình **Machine Learning** để dự đoán người vay có khả năng vỡ nợ.  
- So sánh, đánh giá và lựa chọn mô hình tối ưu.  

Người thực hiện: **Trần Hoài Nam**  
GVHD: **ThS. Hồ Hướng Thiên**  
Lớp: **DH22CS02 – Đại học Mở TP.HCM**

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
2. **Tiền xử lý dữ liệu**  
   - Loại bỏ giá trị rỗng & trùng lặp  
   - Xử lý outlier  
   - Mã hóa biến phân loại  
   - Xử lý dữ liệu mất cân bằng (SMOTE Oversampling)  
3. **Trực quan hóa dữ liệu**  
   - Phân tích biến mục tiêu  
   - Phân phối biến định lượng & định tính  
   - Mối quan hệ giữa các biến & rủi ro vỡ nợ  
4. **Phân tích tương quan (Correlation Matrix)**  
5. **Xây dựng mô hình Machine Learning**  
   - CatBoost  
   - Decision Tree  
   - XGBoost  
   - Random Forest  
6. **Đánh giá mô hình**  
   - Accuracy, Precision, Recall, F1 Score  
   - AUC - ROC Curve  
   - Feature Importance  

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


