import numpy as np
import pandas as pd

# index = pd.date_range("1/1/2000", periods=8)
# s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3))


print(df)

with open("pandas.csv","w") as f:
    f.write(df.to_csv())