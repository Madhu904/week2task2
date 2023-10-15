def length_converter(value, from_unit, to_unit):
    if from_unit == "m" and to_unit == "ft":
        return value * 3.28084
    elif from_unit == "ft" and to_unit == "m":
        return value / 3.28084
   
def get_user_input():
    while True:
        try:
            value = float(input("Enter the length value you wish to convert: "))
            from_unit = input("Enter the source unit (meters - 'm' or feet - 'ft'): ")
            to_unit = input("Enter the target unit (meters - 'm' or feet - 'ft'): ")

            if from_unit in ("m", "ft") and to_unit in ("m", "ft"):
                return value, from_unit, to_unit
            else:
                print("Unsupported units. Please enter 'm' for meters or 'ft' for feet.")

        except ValueError:
            print("OOPS!!Invalid input. Please enter a valid number for the value.")
        except KeyboardInterrupt:
            print("Length conversion canceled.")
            exit()

# Main program
def main():
    print("Hey there!!! Welcome to the Length Converter!")
    value, from_unit, to_unit = get_user_input()
    result = length_converter(value, from_unit, to_unit)

    if result is not None:
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        print("Error occurred. Please check your input and re-enter.")

if __name__ == "__main__":
    main()


