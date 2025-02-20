import csv
import requests
from bs4 import BeautifulSoup
import re


def store_articles(row_articles, file_name):
    """
    Appends scraped articles to a CSV file.
    
    Parameters:
    row_articles (list): List of article data rows.
    file_name (str): Name of the output CSV file.
    """
    
    with open(f"{file_name}.csv", mode='a', encoding='utf-8', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerows(row_articles)


def scrape_articles(link):
    """
    Scrapes an article from the given link.
    
    Parameters:
    link (str): URL of the article to scrape.
    
    Returns:
    list: A list containing the title, subtitle, content, and categories of the article,
          or "error" if scraping fails.
    """

    req = requests.get(link)
    soup = BeautifulSoup(req.text, "html.parser")
    
    try:

        categories = [category.text for category in soup.find('div', {'class': 'topics'}).find_all('a')]
        categories = " ".join(categories)

        title = soup.find('header', {'class': 'article-header'}).find('h1').text.strip()
        subtitle = soup.find('p', {'class': 'article__subhead'}).text.strip()

        content = [p.text for p in soup.find('div', {'class': "wysiwyg wysiwyg--all-content"}).find_all('p')]
        content = re.sub("\t", ' ', ' '.join(content))
        
    except:

        return "error"
    
    return [title, subtitle, content, categories]
