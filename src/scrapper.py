import requests
from bs4 import BeautifulSoup, re
import pandas as pd
import os


class WebScrapper:

    def __init__(self):
        self.data = pd.DataFrame(
            columns=["Region", "Country", "Sum of Cases", "Sum of Deaths",
                     "Confirmed cases during 14-days period"])
        self.collect_data()

    def collect_data(self):
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
                if (region != "Total"):
                    if region.strip():
                        current_region = region
                    regions.append(current_region)
                    country = item.select('td')[1].get_text()
                    countries.append(country)
                    confirmed = item.select('td')[2].get_text()
                    sum_cases.append(confirmed)
                    deaths = item.select('td')[3].get_text()
                    sum_deaths.append(deaths)
                    cases_14_days = item.select('td')[4].get_text()
                    confirmed_cases_14_days.append(cases_14_days)
            except Exception as e:
                # raise e
                print('')
        self.data["Region"] = regions
        self.data["Country"] = countries
        self.data["Sum of Cases"] = sum_cases
        self.data["Sum of Deaths"] = sum_deaths
        self.data["Confirmed cases during 14-days period"] = confirmed_cases_14_days
    def print_data(self):
        print(self.data)

    def get_data(self):
        return self.data

    def export_to_csv(self):
        self.data.to_csv('csv/covid_notification_world_cases_dataset.csv', index=False)

# def main():
#     webScrapper = WebScrapper()
#     webScrapper.export_to_csv()

# if __name__ == "__main__":
#     main()
