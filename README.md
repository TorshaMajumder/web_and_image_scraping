# Web and Image Scraping

***
This repository contains two parts: **Web Scraping** and **Image Scraping**.
***
#### Web Scraping:
For scraping static webpages, run the **static_webpage_scraping.ipynb** file.
**URL**: [Wikipedia Page](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file))
**Dependencies**: requests, pandas, bs4, lxml

For scraping interactive webpages, run the **interactive_webpage_scraping.ipynb** file.
**URL**: 
* [Webpage 1](https://mars.nasa.gov/news/)
* [Webpage 2](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
* [Webpage 3](http://space-facts.com/mars/)
* [Webpage 4](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

**Dependencies**: selenium, splinter, webdriver_manager, pandas, bs4
***
#### Image Scraping:
For scraping images, packages used: **BeautifulSoup** and **Scrapy**.
**URL** : [Website](https://rubikscode.net/blog/)
**Dependencies**: beautifulsoup4, scrapy, Pillow, shutil

For scraping images through  **BeautifulSoup** run the main.py file. 
The scraped images are stored under the folder **Image_Scraping -> images -> image_soup**

For scraping images through **Scrapy**:
* Inside the project folder, open **Terminal**.
* Type **scrapy startproject scrape_image** (this will create a folder **scrape_image**).
* Under the folder **scrape_image -> scrape_image -> spiders**, add **main_spider.py** file.
* Open **Terminal** change the directory to **scrape_image**.
* Type **scrapy crawl my_spider** (this will create a folder **image_scrapy -> full**, which will contain all the scraped images).









