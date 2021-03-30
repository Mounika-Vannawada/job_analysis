import pandas as pd

import csv

URL=['monster.csv','dice.csv']

col=["job_title","date_added","job_type","job_description","location","page_url","salary","sector"]

df1 = pd.concat([ pd.read_csv(f,sep=',', usecols=col, encoding='latin-1')  for f in URL])

df1.head()

df1.to_csv( "combined.csv", quotechar='"', quoting=csv.QUOTE_ALL, index=False, encoding='latin-1')