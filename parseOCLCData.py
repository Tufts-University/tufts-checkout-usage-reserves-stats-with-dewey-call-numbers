import pandas as pd
import numpy as np
from tkinter import filedialog
from tkinter import Tk      




Tk().withdraw()  # Hide the root window

file = filedialog.askopenfilename()


df = pd.read_csv(file)

print(df.head())

year_columns = [
    'Course Fiscal Year',
    'Loan Fiscal Year',
    'Usage Date Fiscal Year',
]

df[year_columns] = df[year_columns].replace(
    r'(?i)^\s*(?:nan|none|null|nat|<na>)?\s*$',
    pd.NA,
    regex=True,
)
selected_df = df[
    (
        (df['Course Fiscal Year'] == df['Loan Fiscal Year'])
        | df['Course Fiscal Year'].isna()
        | df['Loan Fiscal Year'].isna()
    )
    & (
        (df['Course Fiscal Year'] == df['Usage Date Fiscal Year'])
        | df['Course Fiscal Year'].isna()
        | df['Usage Date Fiscal Year'].isna()
    )
    & (
        (df['Loan Fiscal Year'] == df['Usage Date Fiscal Year'])
        | df['Loan Fiscal Year'].isna()
        | df['Usage Date Fiscal Year'].isna()
    )
].copy()
selected_df.to_csv('selected_data.csv', index=False)

  # Replace 'column_name' and 'value' with your criteria  