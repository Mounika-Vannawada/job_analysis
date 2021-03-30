from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
This method is used to extract all data items from
the XML file
Arguments:
    url -> Url for the job site
    query -> Search key
    items -> Attributes to fetch
"""
def extract_xml_data(url, query, items):
    final_url = create_url(url, query)
    url_xml = urlopen(final_url)
    xml = url_xml.read()
    url_xml.close()
    data  = []

    soup_page = BeautifulSoup(xml,features="lxml")
    for job_listing in soup_page.findAll("item"):
        attrs = {}
        for item in items:
            if item == "link":
                attrs[item] = job_listing.find('link').next_sibling
            else:
                attrs[item] = "" if not job_listing.find(item) else job_listing.find(item).text
        data.append(attrs)

    return data

def create_url(url, query):
    query = query.replace(" ", "%20%")
    return url + query

"""
if __name__ == "__main__":
    # Testing the xml parser
    url= "http://rss.jobsearch.monster.com/rssquery.ashx?q=" # monster
    query= "engineer"
    item = ["title", "description", "link", "guid", "pubdate"]
    print(extract_xml_data(url, query, item))
    
    url = "https://rss.indeed.com/rss?q=" # indeed
    query = "engineer"
    item = ["title", "link", "source", "guid", "pubdate", "description", "georss"]
    print(extract_xml_data(url, query, item))
"""