import pandas as pd
import pytest
# from helper import get_counts_by_gender
import os

from src.helper import get_counts_by_gender

# Add the src directory to the sys.path to ensure modules can be found
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_get_counts_by_gender():
    # Create a sample DataFrame
    data = {
        "Sex": ["male", "female", "male", "female", "male", "female", "male"]
    }
    df = pd.DataFrame(data)

    # Expected output
    expected_output = {"male": 4, "female": 3}

    # Run the function
    result = get_counts_by_gender(df)

    # Assert the result
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
