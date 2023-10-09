from WebScraping import extract_listingid, generate_individual_urls
from WebScraping import get_html
from DataExtractor import extract_details
from DataProcessing import process_data, save_data_to_csv


def main():
    base_url = "https://www.sgcarmart.com/used_cars/listing.php?BRSR={}&RPG=100&AVL=2&VEH=0"
    base_individual_url = "https://www.sgcarmart.com/used_cars/info.php?ID="
    num_pages = 5  # Set the number of pages you want to scrape

    # Call the extract_listingid function to get the list of listing IDs
    listingid_array = extract_listingid(base_url, num_pages)

    print(len(listingid_array))

    # Call the generate_individual_urls function to create individual listing URLs
    individual_urls = generate_individual_urls(base_individual_url, listingid_array)

    print(len(individual_urls))

    # Step 3: Extract details for each individual URL
    data = []
    for url in individual_urls:
        print(f"Processing URL: {url}")  # Add this line for debugging
        individual_html = get_html(url)  # You need to define the get_html function
        individual_data = extract_details(individual_html)
        data.append(individual_data)
        print(f"Processed URL: {url}")  # Add this line for debugging

    # Step 4: Process and save the data
    processed_data = process_data(data)
    save_data_to_csv(processed_data, 'ProcessedData.csv')


if __name__ == "__main__":
    main()

