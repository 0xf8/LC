import pandas as pd
import numpy as np
import os

pd.set_option("display.max_rows", 20)
pd.set_option("display.max_columns", 60)
pd.set_option("display.max_colwidth", 20)
pd.set_option('display.width', 260)
pd.set_option('display.multi_sparse', True)
pd.options.display.float_format = '{:20,.2f}'.format

#import data
x1 = pd.read_csv('./LoanStats3a_securev1.csv', header=1, skipfooter=2)
x2 = pd.read_csv('./LoanStats3b_securev1.csv', header=1, skipfooter=2)
x3 = pd.read_csv('./LoanStats3c_securev1.csv', header=1, skipfooter=2)
x4 = pd.read_csv('./LoanStats3d_securev1.csv', header=1, skipfooter=2)

df = pd.concat([x2,x2,x3,x4], axis=0)
l = list(df.columns)
d = df.dtypes.to_dict()

df.drop(['desc', 'url', 'title', 'zip_code', 'emp_title'], axis=1, inplace=True)
df.reset_index(inplace=True, drop=True)
df['term'] = df.term.str[:3].str.strip().astype(np.int64)
df['int_rate'] = df.int_rate.str[:-1].astype(np.float64)/100
df['revol_util'] = df.revol_util.str[:-1].astype(np.float64)/100

df[df.loan_status == 'Fully Paid']


#fix dates munging
dates = ['issue_d', 'earliest_cr_line', 'last_pymnt_d', 'next_pymnt_d', 'last_credit_pull_d']
df.ix[:,dates] = df.ix[:,dates].convert_objects(convert_dates=True)

#something to map numer of outstanding loans
#regex match for empployment length
