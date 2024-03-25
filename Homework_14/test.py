import re

my_string = "Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for delivery of goods: 31.12.2024"

if __name__ == '__main__':
    data = {
        'country': re.search(r', (\w+),', my_string).group(1),
        'region': re.search(r', (\w+ Region),', my_string).group(1),
        'city': re.search(r', ((?:\bS\w+|\b\w+str\b),)', my_string).group(1),
        'postal': re.search(r': (\d+),', my_string).group(1),
        'address': re.search(r', (.+), \d', my_string).group(1) + ', 1',
        'deadline': re.search(r': (\d{2}\.\d{2}\.\d{4})', my_string).group(1),
    }
    print(data)



