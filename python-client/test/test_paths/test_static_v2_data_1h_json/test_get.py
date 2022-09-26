# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import test
from test.paths.static_v2_data_1h_json import get  # noqa: E501
from test import configuration, schemas, api_client

from .. import ApiTestMixin


class TestStaticV2Data1hJson(ApiTestMixin, unittest.TestCase):
    """
    StaticV2Data1hJson unit test stubs
        Average of all measurements per sensor of the last hour.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
