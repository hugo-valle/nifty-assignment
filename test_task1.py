"""Test code for task1.py
"""
import pytest
from task1 import simple_water_bill, COST_PER_GALLON


# Test cases for simple_water_bill()
# Use pytest.mark.parametrize decorator to pass multiple test cases
# https://docs.pytest.org/en/stable/parametrize.html
# first element in the tuple is the input, second element is the expected output
@pytest.mark.parametrize("gallons_usage, expected_output", [
    (100, "You used 100 gallons, your bill is $8.0\n"),
    (200, "You used 200 gallons, your bill is $16.0\n"),
    (2500, "You used 2500 gallons, your bill is $200.0\n"),
    (3214, "You used 3214 gallons, your bill is $257.12\n"),
])


def test_simple_water_bill(monkeypatch, capsys, gallons_usage, expected_output):
    # Simulate user input using monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: str(gallons_usage))

    # Call the function and capture its output
    simple_water_bill()
    captured = capsys.readouterr()

    # Check if the output matches the expected output
    assert captured.out == expected_output

# You can add more test cases as needed
