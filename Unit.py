# Unit Converter CLI Application
# File: unit_converter.py

def convert_temperature(value, from_unit, to_unit):
    # Celsius, Fahrenheit, Kelvin
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    if from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    if from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    if from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    if from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    if from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    raise ValueError('Unsupported conversion')

def unit_converter():
    print("--- Unit Converter ---")
    print("1: Temperature (C, F, K)")
    choice = input("Select conversion type: ")
    if choice == '1':
        val = float(input("Enter value: "))
        frm = input("From unit (C/F/K): ").upper()
        to = input("To unit (C/F/K): ").upper()
        try:
            res = convert_temperature(val, frm, to)
            print(f"{val}{frm} = {res:.2f}{to}")
        except ValueError as e:
            print(e)
    else:
        print("Option not implemented yet.")

if __name__ == '__main__':
    unit_converter()