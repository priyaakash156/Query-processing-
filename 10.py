import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(0)  # for reproducibility
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Function to color negative numbers red and positive numbers black
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

# Apply the style
styled_df = df.style.applymap(color_negative_red)

# Display the styled DataFrame
styled_df
