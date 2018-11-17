# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPRODUCTMASTERController(BaseTestCase):
    """PRODUCTMASTERController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add a new product
        """
        query_string = [('name', 'name_example'),
                        ('brand', 'brand_example'),
                        ('category', 'category_example'),
                        ('product_code', 'product_code_example'),
                        ('cost', 'cost_example')]
        response = self.client.open(
            '/product-master/add/id',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_productbatch(self):
        """Test case for add_productbatch

        Adding products to the platform in bulk.
        """
        data = dict(name='name_example',
                    brand='brand_example',
                    category='category_example',
                    product_code='product_code_example',
                    cost='cost_example')
        response = self.client.open(
            '/product-master/add/batch',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Delete given product and all of attached URLs
        """
        query_string = [('productID', 56)]
        response = self.client.open(
            '/product-master/delete/product/id',
            method='GET',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_product(self):
        """Test case for edit_product

        Edit Product Information
        """
        query_string = [('productID', 56)]
        response = self.client.open(
            '/product-master/edit/id',
            method='POST',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list(self):
        """Test case for get_list

        List of products in the user account
        """
        query_string = [('startfrom', 56)]
        response = self.client.open(
            '/product-master/start-from',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_info(self):
        """Test case for get_product_info

        Product information
        """
        query_string = [('productID', 56)]
        response = self.client.open(
            '/product-master/productid',
            method='GET',
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status_product(self):
        """Test case for status_product

        Get status of a batch import
        """
        response = self.client.open(
            '/product-master/progress/batchImport',
            method='GET',
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_summary(self):
        """Test case for summary

        List of products along with their pricing infromation in the user account
        """
        query_string = [('summary', 'summary_example'),
                        ('startfrom', 56)]
        response = self.client.open(
            '/product-master/summary/startfrom',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
