from typing import Dict, List
from bs4 import BeautifulSoup



from Scrapers.brand_scraper import brand_retrieval
from Scrapers.price_scraper import price_retrieval, price_error_handling
from Scrapers.depre_scraper import depreciation_value_per_year_retrieval, depreciation_value_per_year_error_handler
from Scrapers.roadtax_scraper import road_tax_retrieval, road_tax_error_handler
from Scrapers.regdate_scraper import registered_date_retrieval
from Scrapers.coeLeft_scraper import days_of_coe_retrieval
from Scrapers.mileage_scraper import mileage_retrieval, mileage_error_handler
from Scrapers.manuyear_scraper import manufactured_year_retrieval
from Scrapers.transmission_scraper import transmission_retrieval
from Scrapers.dereg_scraper import dereg_value_retrieval, dereg_value_error_handler
from Scrapers.omv_scraper import omv_retrieval, omv_error_handler
from Scrapers.arf_scraper import arf_retrieval
from Scrapers.coeprice_scraper import coe_retrieval, coe_error_handler
from Scrapers.engcap_scraper import engine_capacity_retrieval, engine_capacity_error_handler
from Scrapers.power_scraper import power_retrieval
from Scrapers.curbweight_scraper import curb_weight_retrieval, curb_weight_error_handler
from Scrapers.numberOwners_scraper import number_of_owners_retrieval
from Scrapers.vehicleType_scraper import type_of_vehicle_retrieval


def extract_details(html: str) -> Dict[str, List]:
    soup = BeautifulSoup(html, 'lxml')

    data = {
        'brand': brand_retrieval(soup),
        'price': price_retrieval(soup),
        'depre': depreciation_value_per_year_retrieval(soup),
        'roadtax': road_tax_retrieval(soup),
        'reg_date': registered_date_retrieval(soup),
        'coeLeft': days_of_coe_retrieval(soup),
        'mile': mileage_retrieval(soup),
        'manuyear': manufactured_year_retrieval(soup),
        'transmission': transmission_retrieval(soup),
        'dereg': dereg_value_retrieval(soup),
        'omv': omv_retrieval(soup),
        'arf': arf_retrieval(soup),
        'coeprice': coe_retrieval(soup),
        'eng_cap': engine_capacity_retrieval(soup),
        'power': power_retrieval(soup),
        'curb_weight': curb_weight_retrieval(soup),
        'no_of_owners': number_of_owners_retrieval(soup),
        'veh_type': type_of_vehicle_retrieval(soup)
    }

    return data






