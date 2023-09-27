"""
Calculate your water bill based on tier pricing
"""


def tier_water_bill():
    """My main function driver
    """
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    gallons_usage = int(input('How many gallons you used this month? '))

    # Basic, minimum charge
    if gallons_usage <= 2000:
        final_charge = 30.00
    else:
        # Tier 2: 2001 - 5000 gallons
        # Gallons in this range are charged at $0.08 per gallon
        if gallons_usage > 2000 and gallons_usage <= 5000:
            gallons_tier2 = gallons_usage - 2000
            final_charge = (gallons_tier2 * 0.08) + 30.00
        # Tier 3: more than 5000 gallons
        # Gallons in this range are charged at $0.20 per gallon
        else:
            gallons_tier2 = gallons_usage - 2000
            gallons_tier3 = gallons_tier2 - 3000
            final_charge = (gallons_tier2 * 0.08) + (gallons_tier3 * 0.20) + 30.00

    print(f'You used {gallons_usage} gallons, your bill is ${final_charge:.2f}')


if __name__ == '__main__':
    tier_water_bill()
