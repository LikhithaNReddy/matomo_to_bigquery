import json
from piwikapi.analytics import PiwikAnalytics
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from google.oauth2 import service_account

# load variables into environment
load_dotenv()
token = os.getenv("TOKEN")

    # Build url string
base_url = 'https://matomo.more-fire.com/index.php?module=API'
site_num = '&idSite=1'
return_format = '&format=json'
period = '&period=day'
date_range = '&date=last30'
method = '&method=VisitsSummary.get'
token_string = "&token_auth=" + token

my_url = base_url + site_num + return_format + period + date_range + method + token_string


            # send request for report
r = requests.get(my_url)
data = pd.DataFrame((r.json()),index=[0]).T
data = data.reset_index()
data

print(data.head(10))