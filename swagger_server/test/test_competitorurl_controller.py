# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCOMPETITORURLController(BaseTestCase):
    """COMPETITORURLController integration test stubs"""

    def test_addurl(self):
        """Test case for addurl

        Add a new URL to given product
        """
        query_string = [('productID', 56),
                        ('url', 'url_example')]
        response = self.client.open(
            '/url-api/add/url',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteurl(self):
        """Test case for deleteurl

        Delete URL
        """
        query_string = [('urlID', 56)]
        response = self.client.open(
            '/url-api/delete/url/id',
            method='GET',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_infourl(self):
        """Test case for get_infourl

        Get URL info
        """
        query_string = [('urlID', 56)]
        response = self.client.open(
            '/url-api/get/url/id',
            method='GET',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
