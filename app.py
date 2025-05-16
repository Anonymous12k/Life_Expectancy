import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("life_expectancy_lr_model.pkl")

st.title("🌍 Life Expectancy Predictor")

with st.form("predict_form"):
    st.subheader("Enter Your Data")

    country = st.text_input("Country (Name)")
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2015, step=1)

    status = st.selectbox("Development Status", ["Developing", "Developed"])

    adult_mortality = st.number_input("Adult Mortality", min_value=0, step=1)
    infant_deaths = st.number_input("Infant Deaths", min_value=0, step=1)

    alcohol = st.number_input("Alcohol Consumption (liters per capita)", min_value=0.0, format="%.2f")
    percentage_expenditure = st.number_input("Percentage Expenditure on Health", min_value=0.0, format="%.2f")

    hepatitis_b = st.number_input("Hepatitis B Immunization (%)", min_value=0, max_value=100, step=1)
    measles = st.number_input("Measles Cases", min_value=0, step=1)

    bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
    under_five_deaths = st.number_input("Under-Five Deaths", min_value=0, step=1)
    polio = st.number_input("Polio Immunization (%)", min_value=0, max_value=100, step=1)
    total_expenditure = st.number_input("Total Health Expenditure (%)", min_value=0.0, format="%.2f")
    diphtheria = st.number_input("Diphtheria Immunization (%)", min_value=0, max_value=100, step=1)

    hiv = st.number_input("HIV/AIDS Rate", min_value=0.0, format="%.4f")
    gdp = st.number_input("GDP", min_value=0.0, format="%.2f")
    population = st.number_input("Population", min_value=0, step=1)

    thinness_1_19 = st.number_input("Thinness 1-19 Years (%)", min_value=0.0, format="%.2f")
    thinness_5_9 = st.number_input("Thinness 5-9 Years (%)", min_value=0.0, format="%.2f")

    income_comp = st.number_input("Income Composition of Resources", min_value=0.0, max_value=1.0, format="%.3f")
    schooling = st.number_input("Schooling (years)", min_value=0.0, max_value=20.0, format="%.1f")

    submitted = st.form_submit_button("Predict")

if submitted:
    # Encode inputs
    status_encoded = 0 if status == "Developing" else 1
    country_encoded = 0  # Placeholder, replace with your actual encoding logic

    # Model input dataframe
    input_df = pd.DataFrame([[country_encoded, year, status_encoded, adult_mortality, infant_deaths, alcohol,
                              percentage_expenditure, hepatitis_b, measles, bmi, under_five_deaths, polio,
                              total_expenditure, diphtheria, hiv, gdp, population, thinness_1_19,
                              thinness_5_9, income_comp, schooling]],
                            columns=['Country', 'Year', 'Status', 'Adult Mortality', 'infant deaths', 'Alcohol',
                                     'percentage expenditure', 'Hepatitis B', 'Measles ', ' BMI ',
                                     'under-five deaths ', 'Polio', 'Total expenditure', 'Diphtheria ', ' HIV/AIDS',
                                     'GDP', 'Population', ' thinness  1-19 years', ' thinness 5-9 years',
                                     'Income composition of resources', 'Schooling'])

    # Create a display version with readable values
    display_df = input_df.copy()
    display_df.at[0, 'Country'] = country     # Show country as string
    display_df.at[0, 'Status'] = status       # Show status as original label

    # Display input summary
    st.subheader("📝 Input Summary")
    st.table(display_df.T.rename(columns={0: "Value"}))

    # Predict and display result
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Life Expectancy: **{prediction:.2f} years**")
