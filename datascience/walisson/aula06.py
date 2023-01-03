import pandas as pd

import numpy as np

steps=pd.Series(data=[4216,3867,7934,4180,5344],index=["seg","ter","qua","qui","sex"])

print(steps.values)
print(steps.index)
print(steps.mean())
