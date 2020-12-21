from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

class Scrape_BeautifulSoup():

    def download_image(self, image):
        response = requests.get(image[0], stream = True)
        #
        # remove white spaces & special characters from the image name
        #
        real_name = ''.join(e for e in image[1] if e.isalnum())
        #
        # store the images under images -> image_soup folder
        #
        file = open(".//images//image_soup//{}.jpg".format(real_name), 'wb')
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response


    def scrape(self, url):
        response = requests.get(url)
        #
        # create a BeautifulSoup object for the response object
        #
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify())
        #
        # image files are located inside <a> tag with class = "entry-featured-image-url"
        #
        image = soup.find_all("a", class_='entry-featured-image-url')
        #print(image, len(image), sep='\n')
        #
        # list to store the image information
        #
        image_info = []
        for i in image:
            image_tag = i.findChildren("img")
            image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))
        #print(image_info)

        for i in range(len(image_info)):
            self.download_image((image_info[i]))








