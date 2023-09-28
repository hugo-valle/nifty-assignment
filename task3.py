"""
Calculate your water bill based on tier pricing
"""


def tier_water_bill():
    """My main function driver
    """
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    gallons_usage = int(input('How many gallons you used this month? '))
    
    charge_tier1 = charge_tier2 = charge_tier3 = 0.00
    gallons_tier1 = gallons_tier2 = gallons_tier3 = 0
    # Basic, minimum charge
    if gallons_usage <= 2000:
        charge_tier1 = 30.00
        gallons_tier1 = gallons_usage
    else:
        # Tier 2: 2001 - 5000 gallons
        # Gallons in this range are charged at $0.08 per gallon
        if gallons_usage > 2000 and gallons_usage <= 5000:
            # Tier 1: 2000 gallons
            charge_tier1 = 30.00
            gallons_tier1 = 2000
            # Tier 2: 2001 - 5000 gallons
            gallons_tier2 = gallons_usage - gallons_tier1
            charge_tier2 = gallons_tier2 * 0.08
        # Tier 3: more than 5000 gallons
        # Gallons in this range are charged at $0.20 per gallon
        else:
            # Tier 1: 2000 gallons
            charge_tier1 = 30.00
            gallons_tier1 = 2000
            # Tier 2: 2001 - 5000 gallons
            gallons_tier2 = 3000
            charge_tier2 = gallons_tier2 * 0.08
            # Tier 3: more than 5000 gallons 
            gallons_tier3 = gallons_usage - (gallons_tier1 + gallons_tier2)
            charge_tier3 = gallons_tier3 * 0.20

    final_charge = charge_tier1 + charge_tier2 + charge_tier3
    print(f'You used {gallons_usage} gallons, your bill is ${final_charge:.2f}')
    print(f'Tier1 (0-2000): {gallons_tier1} gallons,  ${charge_tier1:.2f}')
    print(f'Tier2 (2001-5000): {gallons_tier2} gallons,  ${charge_tier2:.2f}')
    print(f'Tier3 (more than 5000): {gallons_tier3} gallons,  ${charge_tier3:.2f}')


if __name__ == '__main__':
    tier_water_bill()
