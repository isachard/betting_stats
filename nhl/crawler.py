import requests
from bs4 import BeautifulSoup

class Crawler(object):
    """
        A class to crawl links from vegasinsider.com website.
    """

    def __init__ (self):

        file = open("links.txt","r")
        file = file.readlines()
        file.close()

