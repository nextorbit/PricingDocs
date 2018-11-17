import connexion
import six

from swagger_server import util


def edit_category(ID):  # noqa: E501
    """Change the name of a particular category

    Edit and updates category name with given id. # noqa: E501

    :param ID: Unique ID of the category
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'


def get_category(ID):  # noqa: E501
    """Get a specific category on the platform

    Returns list of your categories. # noqa: E501

    :param ID: Unique ID of the category
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'


def getall_category(startfrom):  # noqa: E501
    """List all categories in the store

    Returns list of your categories. # noqa: E501

    :param startfrom: Offset for pagination.
    :type startfrom: int

    :rtype: None
    """
    return 'do some magic!'
