import pandas as pd
import requests
from bs4 import BeautifulSoup


class WebScrapper:

    # Init function
    def __init__(self):
        #Create dataframe for the dataset
        self.data = pd.DataFrame(
            columns=["Region", "Country", "Sum of Cases", "Sum of Deaths",
                     "Confirmed cases during 14-days period"]
        )
        self.url = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
        }
        self.collect_data()

    # Function to get the data by scrapping
    def collect_data(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'lxml')
        current_region = ""
        regions = []
        countries = []
        sum_cases = []
        sum_deaths = []
        confirmed_cases_14_days = []
        # Check the table to get the data
        for item in soup.select("table tr"):
            try:
                region = item.select("td")[0].get_text()
                if region != "Total":
                    if region.strip():
                        current_region = region
                    regions.append(current_region)
                    country = item.select("td")[1].get_text()
                    countries.append(country)
                    confirmed = item.select("td")[2].get_text()
                    sum_cases.append(confirmed)
                    deaths = item.select("td")[3].get_text()
                    sum_deaths.append(deaths)
                    cases_14_days = item.select("td")[4].get_text()
                    confirmed_cases_14_days.append(cases_14_days)
            except Exception as e:
                # raise e
                print('')
        # Set up the dataframe with data
        self.data["Region"] = regions
        self.data["Country"] = countries
        self.data["Sum of Cases"] = sum_cases
        self.data["Sum of Deaths"] = sum_deaths
        self.data[
            "Confirmed cases during 14-days period"] = confirmed_cases_14_days

    # Function for printing dataset
    def print_data(self):
        print(self.data)

    # Return dataframe containing the dataset
    def get_data(self):
        self.data = pd.read_csv("csv/covid_notification_world_cases_dataset.csv")
        return self.data

    # Export the dataframe to csv
    def export_to_csv(self):
        self.data.to_csv(
            "csv/covid_notification_world_cases_dataset.csv",
            index=False
        )


# Main function
def main():
    webScrapper = WebScrapper()
    webScrapper.export_to_csv()


if __name__ == "__main__":
    main()
