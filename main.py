def celsius_to_fahrenheit(celsius):
    if celsius < float(-273.15):
        return "That temperature you entered doesn't make sense!"
    else:
        fahrenheit = (celsius * (9 / 5)) + 32
        files = open("numbers.txt", 'a+')
        files.write(str(fahrenheit) + "\n")
        files.close()
        return fahrenheit


temperatures = [10, -20, -298, 100]

for temp in temperatures:
    (celsius_to_fahrenheit(temp));
