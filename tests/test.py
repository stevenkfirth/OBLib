# -*- coding: utf-8 -*-

from OBLib import DeterministicModel
import pandas as pd

m=DeterministicModel(all_days=[5,21,21,5])
#m.inputs.all_days=[1]
output=m.run(start=pd.Timestamp(2021,1,1,0,0),
             freq="H",
             periods=8760)

print(m)
print(output.df)

output.df[:48].plot()



