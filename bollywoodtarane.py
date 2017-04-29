###########################################################
##                                                       ##
##  Scraper for scraping latest movie names from the web ##
##  http://www.bollywoodtarane.com/                      ##
##                                                       ##
###########################################################

from lxml import html
from bs4 import BeautifulSoup
from utils import *


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
            self.logger.debug("==========================================================")
            self.logger.debug(" ||             Upcoming latest movies:                || ")
            self.logger.debug("==========================================================")
            for (imgUrlDiv, captionDiv) in zip(imgUrlsDivs, captionDivs):

                self.logger.debug("---------------------------------------")
                src = imgUrlDiv.find('img')['src']
                capDivs = captionDiv.findAll('div')
                movieName = capDivs[0].string
                rDate = capDivs[1].string
                self.logger.debug("Movie Name :=%s" % movieName)
                self.logger.debug("Releasing Date := %s   " % rDate)
                self.logger.debug("MoviePosterUrl: %s" % src)

    def scrapeTopLatestMoviesNames(self):
        """
        function for getting top latest movies names
        :param self:
        :return:
        """
        # get content of the page from the site
        content = getPageContent(bollywoodtaraneUrl)

        soup = BeautifulSoup(content, "lxml")

        lists = soup.findAll("ul", {"class" : "list-unstyled"})
        moviesNames = lists[0]

        self.logger.debug("==========================================================")
        self.logger.debug(" ||             Top latest movies:                     || ")
        self.logger.debug("==========================================================")

        self.logger.debug("     Sr No.                 Movie name                    ")
        srno = 1
        for movieName in moviesNames:
            if movieName.string.strip():
                self.logger.debug("      %d                     %s" % (srno, movieName.string.strip()))
                srno += 1
    