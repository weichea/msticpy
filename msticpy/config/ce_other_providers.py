# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Other Providers Component Edit."""
from .._version import VERSION
from .ce_provider_base import CEProviders

__version__ = VERSION
__author__ = "Ian Hellen"


# pylint: disable=too-many-ancestors, duplicate-code
class CEOtherProviders(CEProviders):
    """Other (GeoIP) providers edit component."""

    _DESCRIPTION = "Settings for Other (GeoIP) Providers"
    _COMP_PATH = "OtherProviders"
    # _HELP_TEXT inherited from base
    _HELP_URI = {
        "GeoIP Providers": (
            "https://msticpy.readthedocs.io/en/latest/"
            + "data_acquisition/GeoIPLookups.html"
        ),
        "Key Vault Configuration": (
            "https://msticpy.readthedocs.io/en/latest/getting_started/"
            + "msticpyconfig.html#specifying-secrets-as-key-vault-secrets"
        ),
        "MSTICPy Configuration": (
            "https://msticpy.readthedocs.io/en/latest/"
            + "getting_started/msticpyconfig.html"
        ),
        "Help on this tab": (
            "https://msticpy.readthedocs.io/en/latest/getting_started/"
            + "SettingsEditor.html#adding-geoip-providers"
        ),
    }
