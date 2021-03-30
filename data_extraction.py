from json_parser import parser
from xml_parser import extract_xml_data
from bs4 import BeautifulSoup
import xmltodict
job_sites_filename = "./job_sites.json"
roles_filename = './roles.json'


"""
 This method extracts data from all the sites
 Arguments: none
"""
def data_extract():
    final_data = []
    roles = parser(roles_filename)
    sites = parser(job_sites_filename) 
    for site in sites.keys():
        url = sites[site]["url"]
        item = sites[site]["item"]
        for role in roles:
            items = extract_xml_data(url, role, item)
            final_data.append(items)
    
    return final_data    


if __name__ == "__main__":
    data = data_extract()
    print(data) # check final data
