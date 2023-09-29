"""
Calculate your water bill based on tier pricing
"""


def tier_water_bill():
    """My main function driver
    """
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    year_usage = [800, 900, 1500, 2000, 2050, 3000, 
                  3500, 4000, 4500, 5020, 1500, 600]
    charges = {'tier1': 0.0, 'tier2': 0.0, 'tier3': 0.0}
    gallons = {'tier1': 0, 'tier2': 0, 'tier3': 0}
    for gallons_usage in year_usage:
        # Tier 1: Basic, minimum charge
        if gallons_usage <= 2000:
            gallons['tier1'] += gallons_usage
            charges['tier1'] += 30.00
        # Tier 2: 2001 - 5000 gallons
        # Gallons in this range are charged at $0.08 per gallon
        elif gallons_usage > 2000 and gallons_usage <= 5000:
            gallons['tier1'] += 2000
            charges['tier1'] += 30.00
            gallons['tier2'] += gallons_usage - 2000
            charges['tier2'] += gallons['tier2'] * 0.08
        # Tier 3: more than 5000 gallons
        # Gallons in this range are charged at $0.20 per gallon
        else:  # gallons_usage > 5000:
            gallons['tier1'] += 2000
            charges['tier1'] += 30.00
            gallons['tier2'] += 3000
            charges['tier2'] += gallons['tier2'] * 0.08
            gallons['tier3'] += gallons_usage - 5000
            charges['tier3'] += gallons['tier3'] * 0.20
        
    charges['final'] = charges['tier1'] + charges['tier2'] + charges['tier3']
    gallons['final'] = gallons['tier1'] + gallons['tier2'] + gallons['tier3']
    print(f"You used {gallons['final']} gallons, your bill is ${charges['final']:.2f}")
    print(f"Tier1 (0-2000): {gallons['tier1']} gallons,  ${charges['tier1']:.2f}")
    print(f"Tier2 (2001-5000): {gallons['tier2']} gallons,  ${charges['tier2']:.2f}")
    print(f"Tier3 (more than 5001): {gallons['tier3']} gallons,  ${charges['tier3']:.2f}")


if __name__ == '__main__':
    tier_water_bill()
