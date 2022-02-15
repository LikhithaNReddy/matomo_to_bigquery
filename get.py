from distutils import errors
from google.cloud import bigquery
import os
import logging 
import pandas as pd
credentials_path= '/Users/l.reddy/matomo_to_bigquery/matomo_to_bigquery/uselfortest.json'
os.environ['GOOGLE_APPLICATION_CREDENCIALS']=credentials_path

client=bigquery.Client()
table_id = 'morefire-developer-project.garden.test '



rows_to_insert=[
        {u"sensorName":'gar-001',u"temerature":"32",u"humidity":"32.8"},
        {u"sensorName":'gar-003',u"temerature":"34.7",u"humidity":"39.8"}
    ]


errors=client.insert_rows_json(table_id,rows_to_insert)
if errors==[]:
    print("new rows added")
else:
    print(f'encounters errors : {errors}')