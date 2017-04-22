###########################################################
##                                                       ##
##  Scraper for scraping latest movie names from the web ##
##  http://www.bollywoodtarane.com/                      ##
##                                                       ##
###########################################################

from utils import *
from bs4 import BeautifulSoup


class BollywoodTarane:
    """
    class for scrapping the latest movie name from
    the http://www.bollywoodtarane.com/
    """
    def __init__(self):
        """
        initialize various variables for
        the bollywood scraper
        """
        self.logger = getLogger()
        self.hostUrl = bollywoodtaraneUrl
        self.logger.debug("Scraper started.....")

    def scrapeLatestMovieNames(self):
        """
        function for getting the names of latest movie names
        :return:
        """
        #get content of the page from the site
        content = getPageContent(bollywoodtaraneUrl)
        soup = BeautifulSoup(content, 'html.parser')

        divs = soup.find_all(name='div', attrs={'class': 'panel panel-default'})

        for div in divs:
            print("Got div...")


if __name__ == "__main__":
    bollywood = BollywoodTarane()
    bollywood.scrapeLatestMovieNames()