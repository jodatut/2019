import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.ion()
# plt.plot([1.6, 2.7])

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

ts.plot()
