
############################################################
##          Main file for running the                     ##
##          BollywoodTaraneScraper                        ##
############################################################

from bollywoodtarane import BollywoodTarane
from utils import getLogger

logger = getLogger()

class Main():
    """
    Main class for running the all methods
    of the bollywoodtarane scraper
    """
    def __init__(self):
        """
        Init function for main class
        """
        self.logger = logger
        self.logger.debug("Setting up main...")
        self.bollywood = BollywoodTarane()

    def run(self):
        self.logger.debug("Main running.....")

        # scrape latest movies names for this month
        self.logger.debug("Scrapping latest movies names for this month..")
        self.bollywood.scrapeLatestMovieNames()

        # scrape top latest movies names
        self.logger.debug("Scrapping top latest movies names")
        self.bollywood.scrapeTopLatestMoviesNames()

        # scrape top latest downloaded songs names
        self.logger.debug("Scrapping top latest downloaded songs names")
        self.bollywood.scrapeTopDownloadedSongsNames()

if __name__ == "__main__":
    main = Main()
    main.run()
