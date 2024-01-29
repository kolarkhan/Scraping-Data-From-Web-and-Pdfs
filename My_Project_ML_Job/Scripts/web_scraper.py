import requests
from bs4 import BeautifulSoup


def scrape_names_and_meanings(url):
    all_names = []
    all_meanings = []

    for url in url:
        names = []
        meanings = []

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table containing names and meanings
            table = soup.find('table')

            # Check if the table is found
            if table:
                # Iterate through rows in the table
                for row in table.find_all('tr'):
                    # Extract columns (cells) from each row
                    columns = row.find_all(['th', 'td'])

                    # Ensure there are at least two columns
                    if len(columns) >= 2:
                        name = columns[0].get_text(strip=True)
                        meaning = columns[1].get_text(strip=True)

                        # Append names and meanings to their respective lists
                        names.append(name)
                        meanings.append(meaning)

        # Ensure that the lengths of Names and Mean are the same
        min_length = min(len(names), len(meanings))
        names = names[:min_length]
        meanings = meanings[:min_length]

        # Append names and meanings from the current page to the overall lists
        all_names.extend(names)
        all_meanings.extend(meanings)

    return all_names, all_meanings


if __name__ == "__main__":
    urls = [
        r'https://hamariweb.com/names/muslim/boy/',
        r'https://hamariweb.com/names/muslim/boy/page-2'
    ]
    Names, Mean = scrape_names_and_meanings(urls)
    print(len(Names), len(Mean))
