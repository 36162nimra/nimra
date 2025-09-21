import pandas as pd
import numpy as np

def test_function():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [np.nan, 2, 3, 4],
        'C': [1, np.nan, np.nan, 4]
    })

    # Fill NaN values with the mean of each column
    df_filled = df.fillna(df.mean())

    # Check if there are any NaN values left
    assert df_filled.isnull().sum().sum() == 0, "There are still NaN values in the DataFrame"

    print("jhebfjs")
    print(df_filled)

