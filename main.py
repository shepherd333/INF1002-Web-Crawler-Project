from WebScraping import extract_listingid, generate_individual_urls
from WebScraping import get_html, get_html_with_retry
from DataExtractor import extract_details
from DataProcessing import process_data, remove_na_rows, save_data_to_csv


def main():
    base_url = "https://www.sgcarmart.com/used_cars/listing.php?BRSR={}&RPG=100&AVL=2&VEH=0"
    base_individual_url = "https://www.sgcarmart.com/used_cars/info.php?ID="
    num_pages = 50  # Set the number of pages you want to scrape

    # Step 1: Call the extract_listingid function to get the list of listing IDs
    listingid_array = extract_listingid(base_url, num_pages)

    print(len(listingid_array))

    # Step2: Call the generate_individual_urls function to create individual listing URLs
    individual_urls = generate_individual_urls(base_individual_url, listingid_array)

    print(len(individual_urls))

    # Step 3: Extract details for each individual URL
    data = []
    for idx, url in enumerate(individual_urls, start=1):
        print(f"Processing Item {idx}/{len(individual_urls)} - URL: {url}")  # Add this line for debugging
        individual_html = get_html_with_retry(url)  # You need to define the get_html function
        individual_data = extract_details(individual_html)
        data.append(individual_data)
        print(f"Processed Item {idx}/{len(individual_urls)} - URL: {url}")  # Add this line for debugging

    # Step 4: Process and save the data
    print("Before process_data: ", data)
    processed_data = process_data(data)
    print("After process_data: ", processed_data)
    processed_data = remove_na_rows(processed_data)
    print("After remove_na_rows: ", processed_data)
    save_data_to_csv(processed_data, 'ProcessedData.csv')


if __name__ == "__main__":
    main()

