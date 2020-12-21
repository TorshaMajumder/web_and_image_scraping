# Inside the 'Main' File
# Import the class 'Scrape_BeautifulSoup' from the 'scrape_image_soup.py' file
from scrape_image_soup import Scrape_BeautifulSoup
#
# Main method
#
if __name__ == '__main__':
    url = "https://rubikscode.net/blog/"    # URL used for scraping
    obj = Scrape_BeautifulSoup()            # created an object for the class 'Scrape_BeautifulSoup()'
    obj.scrape(url)                         # passed the URL to the scrape() method inside the class

