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
        self.content = getPageContent(bollywoodtaraneUrl)

    def scrapeLatestMovieNames(self):
        """
        function for getting the names of latest movie names
        :return:
        """
        soup = BeautifulSoup(self.content, 'html.parser')
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
        soup = BeautifulSoup(self.content, "lxml")

        lists = soup.findAll("ul", {"class" : "list-unstyled"})
        moviesNames = lists[0]

        self.logger.debug("==========================================================")
        self.logger.debug(" ||             Top latest movies:                     || ")
        self.logger.debug("==========================================================")

        self.logger.debug("     Sr No.                 Movie name                    ")

        # get all songs name list
        moviesNameList = moviesNames.find_all('li')
        for i, movieName in enumerate(moviesNameList):
            # remove extra space and text from the name
            movie_name = movieName.text.strip()
            self.logger.debug("      %d                     %s" % ((i+1), movie_name))

    def scrapeTopDownloadedSongsNames(self):
        """
        function for getting top latest downloaded songs names
        :param self:
        :return:
        """
        soup = BeautifulSoup(self.content, "lxml")
        lists = soup.findAll("ul", {"class": "list-unstyled"})
        songsName = lists[1]
        self.logger.debug("==========================================================")
        self.logger.debug(" ||             Top latest Downloaded songs names      || ")
        self.logger.debug("==========================================================")
        self.logger.debug("     Sr No.                 Song name                    ")

        # get all songs name list
        songsNameList = songsName.find_all('li')
        for i, songName in enumerate(songsNameList):
            # remove extra space and text from the name
            song_name = songName.text.replace('Latest', '').strip()
            self.logger.debug("      %d                     %s" % ((i+1), song_name))
