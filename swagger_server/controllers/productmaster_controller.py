import connexion
import six

from swagger_server import util


def add_product(name, brand, category, product_code=None, cost=None):  # noqa: E501
    """Add a new product

    Adds a new product to the platform # noqa: E501

    :param name: Product name to be added
    :type name: str
    :param brand: Brand name of the specific product
    :type brand: str
    :param category: Group/Category of the product
    :type category: str
    :param product_code: Product Code assigned to the product
    :type product_code: str
    :param cost: Price of the product being added
    :type cost: str

    :rtype: None
    """
    return 'do some magic!'


def add_productbatch(name=None, brand=None, category=None, product_code=None, cost=None):  # noqa: E501
    """Adding products to the platform in bulk.

    Adds multiple products to the platform at one time # noqa: E501

    :param name: Product name to be added
    :type name: str
    :param brand: Brand name of the specific product
    :type brand: str
    :param category: Group/Category of the product
    :type category: str
    :param product_code: Product Code assigned to the product
    :type product_code: str
    :param cost: Price of the product being added
    :type cost: str

    :rtype: None
    """
    return 'do some magic!'


def delete_product(productID):  # noqa: E501
    """Delete given product and all of attached URLs

    Deletes a product with given id from the platform. # noqa: E501

    :param productID: The unique product ID whose information is to be deleted.
    :type productID: int

    :rtype: None
    """
    return 'do some magic!'


def edit_product(productID):  # noqa: E501
    """Edit Product Information

    Edits and Updates the information of the product present on the platform. # noqa: E501

    :param productID: The unique product ID whose information is to be edited.
    :type productID: int

    :rtype: None
    """
    return 'do some magic!'


def get_list(startfrom):  # noqa: E501
    """List of products in the user account

    Returns detailed information about the products added so far into the platform # noqa: E501

    :param startfrom: Offset for pagination. It can take 0 and exact multiples of 100 as a value.
    :type startfrom: int

    :rtype: None
    """
    return 'do some magic!'


def get_product_info(productID):  # noqa: E501
    """Product information

    Returns product info with the product id mentioned # noqa: E501

    :param productID: The unique product ID whose information is to be fetched.
    :type productID: int

    :rtype: None
    """
    return 'do some magic!'


def status_product():  # noqa: E501
    """Get status of a batch import

    Returns progress status of batch import product. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def summary(summary, startfrom):  # noqa: E501
    """List of products along with their pricing infromation in the user account

    Returns detailed information about the products and their respective prices added so far into the platform # noqa: E501

    :param summary: A keyword to obtain all price information related to the product.
    :type summary: str
    :param startfrom: Offset for pagination. It can take 0 and exact multiples of 100 as a value
    :type startfrom: int

    :rtype: None
    """
    return 'do some magic!'
