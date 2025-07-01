
# Ask the user to input the temperature in Celsius
temperature = float(input("Enter the current temperature in Celsius: "))

# Check the temperature range and print the appropriate message
if temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:  # temperature < 10
    print("It's a cold day. Stay warm!")