# coding: utf-8

"""
    Sensor Community API

    This is the API for the Sensor Community. There are two domains where the same data is served.  https://api.luftdaten.info - This is optimized for receiving data. DON'T use this to request data.  https://data.sensor.community - This is faster and more reliable for serving data, so should be used for reporting cases. Where it is not supported for a certain endpoint, the previous domain must be used.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import test
from test.model.result import Result
from test import configuration


class TestResult(unittest.TestCase):
    """Result unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
