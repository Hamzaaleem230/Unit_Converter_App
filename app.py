import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight and Time Instantly")
st.write("Welcome! Select a category, enter the value, and select the unit you want to convert to.")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])


def convert_units(category, unit, value):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60

    return 0

if category == "Length":
    unit = st.selectbox("📏 Select a unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select a unit", ["Hours to Minutes", "Minutes to Hours", "Minutes to Seconds", "Seconds to Minutes"])

value = st.number_input("Enter the value")

if st.button("Convert"):
    result = convert_units(category, unit, value)
    st.success(f"The converted value is: {result}")