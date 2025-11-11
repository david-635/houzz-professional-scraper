thonimport json
import requests
from extractors.houzz_parser import parse_houzz_page
from outputs.exporters import export_to_json
from config.settings import CONFIG

def run_scraper():
    search_url = CONFIG['search_url']
    response = requests.get(search_url)
    if response.status_code == 200:
        data = parse_houzz_page(response.text)
        export_to_json(data, CONFIG['output_file'])
    else:
        print(f"Failed to retrieve data from {search_url}, status code: {response.status_code}")

if __name__ == "__main__":
    run_scraper()