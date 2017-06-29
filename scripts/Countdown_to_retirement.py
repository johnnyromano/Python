print("When do you retire...")
year = int(input("What year were you born? "))
years = 2017 - year
days = years * 365

if days > 20000:
    print("Wow, you're old it's been {} days, that's {} years".format(days,years))
elif days > 10000:
    print("Lots of time left it's been {} days, that's {} years".format(days,years))
else:
    print("Time to get started it's only been {} days, that's {} years".format(days,years))
