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
        imgUrlsDivs = soup.findAll("div", {"class": "col-md-2"})
        captionDivs = soup.findAll("div", {"class": "caption"})

        if captionDivs and imgUrlsDivs:
            for (imgUrlDiv, captionDiv) in zip(imgUrlsDivs, captionDivs):

                self.logger.debug("---------------------------------------")
                src = imgUrlDiv.find('img')['src']
                capDivs = captionDiv.findAll('div')
                movieName = capDivs[0].string
                rDate = capDivs[1].string
                self.logger.debug("Movie Name :=%s" % movieName)
                self.logger.debug("Releasing Date := %s   " % rDate)
                self.logger.debug("MoviePosterUrl: %s" % src)

