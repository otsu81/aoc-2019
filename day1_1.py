import math

def required_fuel(mass):
    result = int(math.floor(mass/3) - 2)
    if result <= 0:
        return 0
    else:
        return result

def required_fuel_recursive(mass):
    result = int(math.floor(mass/3) - 2)
    if result <= 0:
        return 0
    else:
        return result + required_fuel_recursive(result)


def main():

    with open('day1_input.txt') as f:
        mylist = f.read().splitlines()

    total_fuel = 0
    for val in mylist:
        total_fuel += required_fuel(int(val))

    total_fuel_recursive = 0
    for val in mylist:
        total_fuel_recursive += required_fuel_recursive(int(val))

    print(f"Total fuel #1: {total_fuel}")
    print(f"Total fuel #2: {total_fuel_recursive}")

if __name__ == '__main__':
    main()