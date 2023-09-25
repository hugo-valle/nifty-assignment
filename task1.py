"""
Calculate your water bill based on usage
"""
# Global variables
COST_PER_GALLON = 0.08  # after BASED_GALLONS


def main():
    """My main function driver
    """
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    gallons_usage = int(input('How many gallons you used this month? '))
    
    final_charge = (gallons_usage * COST_PER_GALLON)
    print(f'You used {gallons_usage} gallons, your bill is ${final_charge}')
    

if __name__ == '__main__':
    main()