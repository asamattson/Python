print("-=-=-=-=-=-=-=-=-=-=Imperial to Metric Converter-=-=-=-=-=-=-=-=-=-=")
print("Putting in non-numerical values will result in a program crash.")
# Inches to Centimeters converter
inches = input("How many inches would you like to convert to centimeters? ")
inches = int(inches)
cm = (inches * 2.54)
print(cm)

# Pounds to Kilograms converter
pounds = input("How many pounds would you like to convert to kilograms? ")
pounds = int(pounds)
kg = (pounds / 2.2)
print(kg)

# Miles to Kilometers
miles = input("How many miles would you like to convert to kilometers?")
miles = int(miles)
kilo = (miles * 1.609)
print(kilo)

# Yards to meters
yards = input("How many yards would you like to convert to meters")
yards = int(yards)
meters = (yards / 1.094)
print(meters)