#################################################################
#                                                               #
#       utils file for handling bollywood tarane utils funs     #
#                                                               #
#################################################################

from requests import request
import logging

APP_NAME = 'BollywoodTaraneScraper'
bollywoodtaraneUrl = "http://www.bollywoodtarane.com/"


# function for getting logger
def getLogger():
    logging.basicConfig(format='[%(name)s][%(levelname)s] %(message)s', level=logging.DEBUG)
    return logging.getLogger(APP_NAME)


# function for getting page contents from the url
def getPageContent(url):
    content = None
    try:
        # make request to the bollywood tarane url
        response = request('GET', url=bollywoodtaraneUrl)
        content = response.content
        return content
    except Exception as e:
        print("Got exception while getting the content of the page:  %s" % bollywoodtaraneUrl)
        print("Exception: %s" % e)
    return content