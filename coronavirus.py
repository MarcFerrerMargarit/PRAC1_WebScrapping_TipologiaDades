import requests
from bs4 import BeautifulSoup, re
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

current_region = ""
regions = []
countries = []
sum_cases = []
sum_deaths = []
confirmed_cases_14_days = []

for item in soup.select('table tr'):
    try:
        region = item.select('td')[0].get_text()
        if(region != "Total"):
            if region.strip():
                current_region = region
            regions.append(current_region)
            country = item.select('td')[1].get_text()
            countries.append(country)
            confirmed = item.select('td')[2].get_text()
            sum_cases.append(confirmed)
            deaths = item.select('td')[3].get_text()
            sum_deaths.append(deaths)
            cases_14_days= item.select('td')[4].get_text()
            confirmed_cases_14_days.append(cases_14_days)
    except Exception as e:
        # raise e
        print('')
df = pd.DataFrame(data = regions, columns=["Region"])
df["Country"] = countries
df["Sum of Cases"] = sum_cases
df["Sum of Deaths"] = sum_deaths
df["Confirmed cases during 14-days period"] = confirmed_cases_14_days
