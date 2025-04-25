import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid conversion"


def main():
    st.title("Unit Converter")

    st.header("Temperature Converter")
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"Result: {result} {to_unit}")


if __name__ == "__main__":
    main()
