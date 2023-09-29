"""
Calculate your water bill based on tier pricing
"""

GALLONS_TIER1 = 2000  # gallons in tier 1
GALLONS_TIER2 = 5000  # gallons in tier 2

PRICE_TIER1 = 30.00     # price per gallon in tier 1
PRICE_TIER2 = 0.08      # price per gallon in tier 2
PRICE_TIER3 = 0.20      # price per gallon in tier 3 
    
charges = {'tier1': 0.0, 'tier2': 0.0, 'tier3': 0.0}
gallons = {'tier1': 0, 'tier2': 0, 'tier3': 0}


def _water_bill_tier1(gallons, charges, gallons_usage):
    """Calculate the water bill for tier 1

    Args:
        gallons (dict): water usage in gallons per tier
        charges (dict): water charges per tier
        gallons_usage (int): water usage in gallons
    """
    # Tier 1: Basic, minimum charge
    if gallons_usage <= GALLONS_TIER1:
        gallons['tier1'] += gallons_usage
        charges['tier1'] += PRICE_TIER1


def _water_bill_tier2(gallons, charges, gallons_usage):
    """Calculate the water bill for tier 2

    Args:
        gallons (dict): water usage in gallons per tier
        charges (dict): water charges per tier
        gallons_usage (int): water usage in gallons
    """
    # Tier 2: GALLONS_TIER1 + 1 to GALLONS_TIER2 gallons
    # Gallons in this range are charged at $PRICE_TIER2 per gallon
    if gallons_usage > GALLONS_TIER1 and gallons_usage <= GALLONS_TIER2:
        gallons['tier1'] += GALLONS_TIER1
        charges['tier1'] += PRICE_TIER1
        gallons['tier2'] += gallons_usage - GALLONS_TIER1
        charges['tier2'] += gallons['tier2'] * PRICE_TIER2


def _water_bill_tier3(gallons, charges, gallons_usage):
    """Calculate the water bill for tier 3

    Args:
        gallons (dict): water usage in gallons per tier
        charges (dict): water charges per tier
        gallons_usage (int): water usage in gallons
    """
    # Tier 3: more than GALLONS_TIER2 gallons
    # Gallons in this range are charged at $PRICE_TIER3 per gallon
    if gallons_usage > GALLONS_TIER2:
        gallons['tier1'] += GALLONS_TIER1
        charges['tier1'] += PRICE_TIER1
        gallons['tier2'] += GALLONS_TIER2 - GALLONS_TIER1
        charges['tier2'] += gallons['tier2'] * PRICE_TIER2
        gallons['tier3'] += gallons_usage - GALLONS_TIER2
        charges['tier3'] += gallons['tier3'] * PRICE_TIER3


def calculate_final_water_bill(gallons, charges):
    """Calculate the final water bill

    Args:
        gallons (dict): water usage in gallons per tier
        charges (dict): water charges per tier
    """
    charges['final'] = charges['tier1'] + charges['tier2'] + charges['tier3']
    gallons['final'] = gallons['tier1'] + gallons['tier2'] + gallons['tier3']


def print_water_bill(gallons, charges):
    """Print the water bill

    Args:
        gallons (dict): water usage in gallons per tier
        charges (dict): water charges per tier
    """
    print(f"You used {gallons['final']} gallons, your bill is ${charges['final']:.2f}")
    print(f"Tier1 (0-{GALLONS_TIER1}): {gallons['tier1']} gallons,  ${charges['tier1']:.2f}")
    print(f"Tier2 ({GALLONS_TIER1 + 1}-{GALLONS_TIER2}): {gallons['tier2']} gallons,  ${charges['tier2']:.2f}")
    print(f"Tier3 (more than {GALLONS_TIER2 +1}): {gallons['tier3']} gallons,  ${charges['tier3']:.2f}")
    
    
def tier_water_bill(year_usage):
    """Calculate the year's water bill based on tier pricing

    Args:
        year_usage (list): monthly water usage in gallons
    """
    
    for gallons_usage in year_usage:

        _water_bill_tier1(gallons, charges, gallons_usage)
        
        _water_bill_tier2(gallons, charges, gallons_usage)
        
        _water_bill_tier3(gallons, charges, gallons_usage)
        
    calculate_final_water_bill(gallons, charges)
    print_water_bill(gallons, charges)


if __name__ == '__main__':
    # Test case 1: 29370 gallons
    year_usage = [800, 900, 1500, 2000, 2050, 3000, 
                  3500, 4000, 4500, 5020, 1500, 600]
    tier_water_bill(year_usage)
