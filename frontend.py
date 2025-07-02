
import streamlit as st
import requests

st.title("🗽 US Visa Approval Prediction")

st.write("Fill in the details and click Predict:")

continent = st.text_input("Continent")
education_of_employee = st.text_input("Education of Employee")
has_job_experience = st.selectbox("Has Job Experience", ["Yes", "No"])
requires_job_training = st.selectbox("Requires Job Training", ["Yes", "No"])
no_of_employees = st.text_input("Number of Employees")
company_age = st.text_input("Company Age")
region_of_employment = st.text_input("Region of Employment")
prevailing_wage = st.text_input("Prevailing Wage")
unit_of_wage = st.selectbox("Unit of Wage", ["Year", "Month", "Week", "Hour"])
full_time_position = st.selectbox("Full Time Position", ["Yes", "No"])

if st.button("Predict Visa Status"):
    payload = {
        "continent": continent,
        "education_of_employee": education_of_employee,
        "has_job_experience": has_job_experience,
        "requires_job_training": requires_job_training,
        "no_of_employees": no_of_employees,
        "company_age": company_age,
        "region_of_employment": region_of_employment,
        "prevailing_wage": prevailing_wage,
        "unit_of_wage": unit_of_wage,
        "full_time_position": full_time_position,
    }

  
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(result.get("result", "No result"))
    else:
        st.error("Error: Could not get prediction.")
