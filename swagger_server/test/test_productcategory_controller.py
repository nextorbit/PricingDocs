# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPRODUCTCATEGORYController(BaseTestCase):
    """PRODUCTCATEGORYController integration test stubs"""

    def test_edit_category(self):
        """Test case for edit_category

        Change the name of a particular category
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '/product-category/edit/category/id',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_category(self):
        """Test case for get_category

        Get a specific category on the platform
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '/product-category/get/category/id',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getall_category(self):
        """Test case for getall_category

        List all categories in the store
        """
        query_string = [('startfrom', 56)]
        response = self.client.open(
            '/product-category/startFrom',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
