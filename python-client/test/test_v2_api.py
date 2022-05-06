"""
    Sensor Community API

    This is the API for the Sensor Community. There are two domains where the same data is served.  https://api.luftdaten.info - This is optimized for receiving data. DON'T use this to request data.  https://data.sensor.community - This is faster and more reliable for serving data, so should be used for reporting cases. Where it is not supported for a certain endpoint, the previous domain must be used.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland import sensorcommunity
from deutschland.sensorcommunity.api.v2_api import V2Api  # noqa: E501


class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self):
        self.api = V2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_data_last1_hour(self):
        """Test case for get_data_last1_hour

        average of all measurements per sensor of the last hour.  # noqa: E501
        """
        pass

    def test_get_data_last24_hour(self):
        """Test case for get_data_last24_hour

        average of all measurements per sensor of the 24 hours.  # noqa: E501
        """
        pass

    def test_get_data_last5_minutes_v2(self):
        """Test case for get_data_last5_minutes_v2

        average of all measurements per sensor of the last 5 minutes for all.  # noqa: E501
        """
        pass

    def test_get_dust_data_last5_minutes(self):
        """Test case for get_dust_data_last5_minutes

        average of all measurements per sensor of the last 5 minutes for all dust sensors only.  # noqa: E501
        """
        pass

    def test_get_temp_hum_air_data_last5_minutes(self):
        """Test case for get_temp_hum_air_data_last5_minutes

        average of all measurements per sensor of the last 5 minutes for all temp./humidity/air pressure sensors only.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
