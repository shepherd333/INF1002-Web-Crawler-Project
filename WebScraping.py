from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from random import randint
from DataExtractor import extract_details



class CustomException(Exception):
    pass


def get_html(url, timeout=10):

    # Create a session instance
    session = requests.Session()

    # Define user-agent headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = session.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Check if the response content is not empty
        if response.text.strip():
            return response.text
        else:
            raise CustomException(f"Empty response received from {url}")
    except requests.exceptions.RequestException as e:
        raise CustomException(f"Error making the request: {e}")
    except requests.exceptions.Timeout as e:
        raise CustomException(f"Timeout error: {e}")
    finally:
        session.close()


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def extract_listingid(baseurl, num_pages):
    listingid_array = []

    for page_number in range(1, num_pages + 1):
        try:
            # Calculate the appropriate page number based on the iteration
            page_start = (page_number - 1) * 100 + 100  # Start with BRSR=100 for the second page onwards
            url = baseurl.format(page_start)
            html = get_html(url)

            # Parse the HTML into a BeautifulSoup object
            soup = BeautifulSoup(html, 'html.parser')

            table = soup.select_one('table[style="margin-top:1px;"]')
            if table:
                links = table.find_all('a', href=re.compile(r'info.php\?ID=\d+'))

                for link in links:
                    href = link.get("href")
                    if href:
                        match = re.search(r'ID=(\d+)', href)
                        if match:
                            listing_id = match.group(1)
                            if listing_id not in listingid_array:
                                listingid_array.append(listing_id)
        except Exception as e:
            print(f"Error processing page {page_number}: {e}")


    return listingid_array


def generate_individual_urls(base_individual_url, listingid_array):
    individual_urls = []
    for listing_id in listingid_array:
        individual_url = f"{base_individual_url}{listing_id}"
        individual_urls.append(individual_url)
    return individual_urls


import time


def get_html_with_retry(url, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 503:
                print(f"Service Unavailable, retrying in a moment... (Retry {retries + 1}/{max_retries})")
                time.sleep(5)  # Wait for 5 seconds before retrying
                retries += 1
            else:
                raise  # Re-raise other HTTP errors
    raise CustomException("Max retries exceeded.")


