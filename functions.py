# Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    if celsius < float(-273.15):
        return "That temperature you entered doesn't make sense!"
    else:
        fahrenheit = (celsius * (9 / 5)) + 32
        return fahrenheit


temperatures = [10, -20, -298, 100]

for temp in temperatures:
    print(celsius_to_fahrenheit(temp));


# Length of the String

def lengthOfString(myString):
    if type(myString) == int:
        return "Sorry integers don't have length."

    elif type(myString) == float:
        return "Sorry floats don't have length."

    else:
        return len(myString)


text = input("Enter a string: ")
print(lengthOfString(str(text)))

# Converting AUD into Nepali Rupees

def currency_converter(rate, aud):
    nepali = aud * rate
    return nepali


rate = input("Enter rate: ")
aud = input("Enter Australian Dollar: ")
print("The AUD", float(aud), "into Nepali Rs. is", currency_converter(float(rate), float(aud)))

# File Read

file = open("example.txt", 'r')
content = file.readlines()
file.close()
for i in content:
    print(len(i.strip()))
