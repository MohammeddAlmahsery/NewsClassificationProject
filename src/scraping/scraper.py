import requests
from bs4 import BeautifulSoup
from utils import store_articles, scrape_articles  # Importing utility functions

# Fetch the yearly archive XML sitemap from https://aljazeera.com/robots.txt
req = requests.get("https://www.aljazeera.com/sitemaps/article-archive.xml")
yearly_archive_xml = BeautifulSoup(req.text, "lxml-xml")

# Extract all yearly archive links from the sitemap
yearly_archive_links = [link.text for link in yearly_archive_xml.find_all('loc')]

monthly_archive_xml = []

# Fetch and parse monthly archive XML for each year
for year in yearly_archive_links:
    
    req = requests.get(year)
    monthly_archive_xml.append(BeautifulSoup(req.text, "lxml-xml"))

monthly_archive_links = []

# Extract all monthly archive links from the parsed XML
for month in monthly_archive_xml:
    
    links = [link.text for link in month.find_all('loc')]
    monthly_archive_links.extend(links)

articles_links = [] 

# Extract article links from each monthly archive page
for month in monthly_archive_links:
    
    req = requests.get(month)
    month_soup = BeautifulSoup(req.text, "lxml-xml")
    
    links = [link.text for link in month_soup.find_all('loc')]
    articles_links.extend(links)

data = []

# Loop through all article links and scrape content
for i, link in enumerate(articles_links, 1):
    
    data.append(scrape_articles(link))

    # Store data every 1000 articles
    if i % 1000 == 0:
        store_articles(data, "../../data/raw")  
        data = []  
