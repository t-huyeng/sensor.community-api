# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.sensorcommunity.api.v1_api import V1Api
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.sensorcommunity.api.v1_api import V1Api
from deutschland.sensorcommunity.api.v2_api import V2Api
