import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("emp.pkl", "rb"))

# App title
st.title("Employee Performance Rating Predictor")

st.markdown("Enter the employee details below:")

# Get user input
age = st.number_input("Age", min_value=18, max_value=60, value=30)
gender = st.selectbox("Gender", ("Male", "Female"))
education_background = st.selectbox("Education Background", ("Life Sciences", "Other", "Medical", "Marketing", "Technical Degree", "Human Resources"))
marital_status = st.selectbox("Marital Status", ("Single", "Married", "Divorced"))
emp_department = st.selectbox("Department", ("Sales", "Development", "Research & Development", "Human Resources", "Finance", "Marketing"))
emp_job_role = st.selectbox("Job Role", ("Manager", "Sales Executive", "Research Scientist", "Developer", "Human Resources", "Finance Executive"))
business_travel = st.selectbox("Business Travel Frequency", ("Travel_Rarely", "Travel_Frequently", "Non-Travel"))
distance_from_home = st.slider("Distance From Home", 0, 50, 10)
emp_education_level = st.selectbox("Education Level (1=Low, 5=High)", range(1, 6))
emp_environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
emp_hourly_rate = st.slider("Hourly Rate", 20, 150, 60)
emp_job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 3)
emp_job_level = st.slider("Job Level (1-5)", 1, 5, 2)
emp_job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
num_companies_worked = st.slider("Number of Companies Worked", 0, 10, 2)
overtime = st.selectbox("OverTime", ("Yes", "No"))
last_salary_hike = st.slider("Last Salary Hike (%)", 0, 50, 15)
relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", 1, 4, 3)
total_experience = st.slider("Total Work Experience (Years)", 0, 40, 10)
training_times = st.slider("Training Times Last Year", 0, 10, 3)
work_life_balance = st.slider("Work Life Balance (1-4)", 1, 4, 3)
experience_in_company = st.slider("Years at Current Company", 0, 30, 5)
experience_in_role = st.slider("Years in Current Role", 0, 20, 5)
years_since_promotion = st.slider("Years Since Last Promotion", 0, 15, 2)
years_with_manager = st.slider("Years With Current Manager", 0, 20, 4)
attrition = st.selectbox("Attrition", ("Yes", "No"))

# Convert categorical values to numeric (based on your mapping)
gender = 1 if gender == "Male" else 0
marital_status_map = {"Single": 0, "Married": 1, "Divorced": 2}
marital_status = marital_status_map[marital_status]

business_travel_map = {"Travel_Rarely": 0, "Travel_Frequently": 1, "Non-Travel": 2}
business_travel = business_travel_map[business_travel]

overtime = 1 if overtime == "Yes" else 0
attrition = 1 if attrition == "Yes" else 0

# Dummy encodings — replace with actual LabelEncoder mappings if needed
education_background = 0
emp_department = 0
emp_job_role = 0

# Prepare feature array (make sure you have all 26 features here, excluding PerformanceRating)
features = np.array([[age, gender, education_background, marital_status, emp_department,
                      emp_job_role, business_travel, distance_from_home, emp_education_level,
                      emp_environment_satisfaction, emp_hourly_rate, emp_job_involvement,
                      emp_job_level, emp_job_satisfaction, num_companies_worked, overtime,
                      last_salary_hike, relationship_satisfaction, total_experience,
                      training_times, work_life_balance, experience_in_company,
                      experience_in_role, years_since_promotion, years_with_manager, attrition]])

# Prediction
if st.button("Predict Performance Rating"):
    prediction = model.predict(features)
    st.success(f"Predicted Performance Rating: {int(prediction[0])}")
