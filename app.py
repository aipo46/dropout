import numpy as np
import pandas as pd
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import time

encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()

    # Perform transformations
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.fit_transform(data["Tuition_fees_up_to_date"])
    df["Scholarship_holder"] = encoder_Scholarship_holder.fit_transform(data["Scholarship_holder"])
    df["Debtor"] = encoder_Debtor.fit_transform(data["Debtor"])
    df["Displaced"] = encoder_Displaced.fit_transform(data["Displaced"])
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.fit_transform(data["Daytime_evening_attendance"])
    df["Gender"] = encoder_Gender.fit_transform(data["Gender"])
    df["Admission_grade"] = scaler_Admission_grade.fit_transform(np.asarray(data["Admission_grade"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.fit_transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.fit_transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.fit_transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.fit_transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.fit_transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.fit_transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.fit_transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.fit_transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1, 1))
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.fit_transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1, 1))
    
    return df

model = joblib.load("logistic_regression_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
   
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)
    return final_result



#Setting page
st.set_page_config(page_title="🎓 Students Performance", 
                   layout="wide")

col1, col2 = st.columns([4, 10])

with col2:
    st.header('JAYA JAYA INSTITUT')
    #st.subheader("Prediction of Student's Academic Performance")

st.sidebar.write("""Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus..
""")

add_selectitem = st.sidebar.selectbox("Pilihan Menu", ("Student's Academic Performance",))

st.sidebar.write(
    "Dataset bisa di download di : [Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)"
    )

# Initialize an empty dictionary to store user input
data = {}

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

col1, col2, col3, col4 = st.columns(4)
with col1:
    encoder_Tuition_fees_up_to_date = LabelEncoder()
    encoder_Tuition_fees_up_to_date.fit(['Not Update', 'Update'])
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees', options=['Not Update', 'Update'], index=0)
    data['Tuition_fees_up_to_date'] = [encoder_Tuition_fees_up_to_date.transform([Tuition_fees_up_to_date])[0]]
with col2:
    encoder_Scholarship_holder = LabelEncoder()
    encoder_Scholarship_holder.fit(['Non Scholarship', 'Scholarship'])
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=['Non Scholarship', 'Scholarship'], index=0)
    data['Scholarship_holder'] = [encoder_Scholarship_holder.transform([Scholarship_holder])[0]]
with col3:
    encoder_Debtor = LabelEncoder()
    encoder_Debtor.fit(['Non Debtor', 'Debtor'])
    Debtor = st.selectbox(label='Debtor', options=['Non Debtor', 'Debtor'], index=0)
    data['Debtor'] = [encoder_Debtor.transform([Debtor])[0]]
with col4:
    encoder_Displaced = LabelEncoder()
    encoder_Displaced.fit(['Non Displaced', 'Displaced'])
    Displaced = st.selectbox(label='Displaced', options=['Non Displaced', 'Displaced'], index=0)
    data['Displaced'] = [encoder_Displaced.transform([Displaced])[0]]
    
col5, col6, col7, col8 = st.columns(4)
with col5:
    encoder_Daytime_evening_attendance = LabelEncoder()
    encoder_Daytime_evening_attendance.fit(['Daytime', 'Evening'])
    Daytime_evening_attendance = st.selectbox(label='Attendance', options=['Daytime', 'Evening'], index=0)
    data['Daytime_evening_attendance'] = [encoder_Daytime_evening_attendance.transform([Daytime_evening_attendance])[0]]
with col6:
    encoder_Gender = LabelEncoder()
    encoder_Gender.fit(['Female', 'Male'])
    Gender = st.selectbox(label='Gender', options=['Female', 'Male'], index=0)
    data['Gender'] = [encoder_Gender.transform([Gender])[0]]
with col7:
    Admission_grade = st.number_input(label='Admission Grade', value=100)
    data['Admission_grade'] = [Admission_grade]
with col8:
    Previous_qualification_grade = st.number_input(label='Previous Qualification Grade', value=100)
    data['Previous_qualification_grade'] = [Previous_qualification_grade]

col9, col10, col11, col12 = st.columns(4)
with col9:
    Curricular_units_1st_sem_approved = st.number_input(label='Curricular Units 1st Semester Approved', value=5)
    data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
with col10:
    Curricular_units_1st_sem_grade = st.number_input(label='Curricular Units 1st Semester Grade', value=12)
    data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]
with col11:
    Curricular_units_1st_sem_enrolled = st.number_input(label='Curricular Units 1st Semester Enrolled', value=6)
    data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
with col12:
    Curricular_units_1st_sem_credited = st.number_input(label='Curricular Units 1st Semester Credited', value=0)
    data['Curricular_units_1st_sem_credited'] = [Curricular_units_1st_sem_credited]
    
col13, col14, col15, col16 = st.columns(4)
with col13:
    Curricular_units_2nd_sem_approved = st.number_input(label='Curricular Units 2nd Semester Approved', value=5)
    data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
with col14:
    Curricular_units_2nd_sem_grade = st.number_input(label='Curricular Units 2nd Semester Grade', value=12)
    data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]
with col15:
    Curricular_units_2nd_sem_enrolled = st.number_input(label='Curricular Units 2nd Semester Enrolled', value=6)
    data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
with col16:
    Curricular_units_2nd_sem_credited = st.number_input(label='Curricular Units 2nd Semester Credited', value=0)
    data['Curricular_units_2nd_sem_credited'] = [Curricular_units_2nd_sem_credited]

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

# Display user input
with st.expander("Inputan Dataset"):
        st.dataframe(data=user_input_df, width=1200, height=20)
# Preprocess data and make prediction on button click
if st.button('Click Here to Predict'):
    new_data = data_preprocessing(data=data)
    with st.spinner('Memprediksi...'):
        time.sleep(2)  # Simulating prediction process
        output = prediction(new_data)
        st.success(f"Hasil Prediksi: {output}")

#st.snow()