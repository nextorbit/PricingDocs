import connexion
import six

from swagger_server import util


def addurl(productID, url):  # noqa: E501
    """Add a new URL to given product

    Adds your own URL or a competitor&#39;s URL to one of your products. # noqa: E501

    :param productID: Product id which you want to add a URL
    :type productID: int
    :param url: The URL which is to be added.
    :type url: str

    :rtype: None
    """
    return 'do some magic!'


def deleteurl(urlID):  # noqa: E501
    """Delete URL

    Deletes url with given id. # noqa: E501

    :param urlID: The unique ID of the URL whose information is to be deleted.
    :type urlID: int

    :rtype: None
    """
    return 'do some magic!'


def get_infourl(urlID):  # noqa: E501
    """Get URL info

    Returns URL info with given id. # noqa: E501

    :param urlID: The unique ID of the URL whose information is needed.
    :type urlID: int

    :rtype: None
    """
    return 'do some magic!'
