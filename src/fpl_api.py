import requests
import pandas as pd

fpl = 'https://fantasy.premierleague.com/api/bootstrap-static/'


df = requests.get(fpl).json()
print(df.keys())