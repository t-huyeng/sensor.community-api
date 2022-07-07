"""
    Sensor Community API

    This is the API for the Sensor Community. There are two domains where the same data is served.  https://api.luftdaten.info - This is optimized for receiving data. DON'T use this to request data.  https://data.sensor.community - This is faster and more reliable for serving data, so should be used for reporting cases. Where it is not supported for a certain endpoint, the previous domain must be used.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import test
from test.api.v1_api import V1Api  # noqa: E501


class TestV1Api(unittest.TestCase):
    """V1Api unit test stubs"""

    def setUp(self):
        self.api = V1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_data_by_api_id(self):
        """Test case for get_data_by_api_id

        All measurements of the last 5 minutes for one sensor  # noqa: E501
        """
        pass

    def test_get_data_last5_minutes(self):
        """Test case for get_data_last5_minutes

        Average of all measurements per sensor of the last 5 minutes for all.  # noqa: E501
        """
        pass

    def test_get_sensor_values_with_filter(self):
        """Test case for get_sensor_values_with_filter

        All measurements of the last 5 minutes filtered by query.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
