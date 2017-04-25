##########################################################
##                                                      ##
##  Test cases for the bollywoodtarane                  ##
##                                                      ##
##########################################################

import unittest
from utils import getLogger
from bollywoodtarane import BollywoodTarane


class BollywoodTaraneTest(unittest.TestCase):

    def setUp(self):
        self.logger = getLogger()
        self.bWT = BollywoodTarane()
        self.logger.debug("Setting up bollywoodtestcases....")

    def testLatestMovieNames(self):
        """
        Test case for scrapping latest movie names
        from bollywood tarane
        """
        self.bWT.scrapeLatestMovieNames()

    def testLastTopMoviesNames(self):
        """
        Test case for getting the top last movies names
        """
        pass

    def testTopLatestDownloads(self):
        """
        Test for getting the top latest downloads
        """
        pass


    def tearDown(self):
        self.logger.debug("Tearing down bolloywood tarane test case......")

