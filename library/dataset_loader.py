import pandas as pd
import marimo as mo

Data = pd.DataFrame(
    {
        'x':[1,2,3,4],
        'y':[10,11,20,22]
    }
   )

Data = mo.ui.experimental_data_editor(Data)
def dataset():
    return Data
   