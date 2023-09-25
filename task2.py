"""
Calculate your water bill based on usage
"""


def simple_water_bill():
    """My main function driver
    """
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    gallons_usage = int(input('How many gallons you used this month? '))

    if gallons_usage <= 2000:
        final_charge = 30.00
    else:
        final_charge = (gallons_usage - 2000) * 0.08 + 30.00

    print(f'You used {gallons_usage} gallons, your bill is ${final_charge:.2f}')


if __name__ == '__main__':
    simple_water_bill()
