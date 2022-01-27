# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from tumpangtanya.inforequest.testing import (  # noqa: E501
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that tumpangtanya.inforequest is properly installed."""

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if tumpangtanya.inforequest is installed."""
        self.assertTrue(self.installer.is_product_installed("tumpangtanya.inforequest"))

    def test_browserlayer(self):
        """Test that ITumpangtanyaInforequestLayer is registered."""
        from plone.browserlayer import utils

        from tumpangtanya.inforequest.interfaces import ITumpangtanyaInforequestLayer

        self.assertIn(ITumpangtanyaInforequestLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("tumpangtanya.inforequest")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if tumpangtanya.inforequest is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("tumpangtanya.inforequest")
        )

    def test_browserlayer_removed(self):
        """Test that ITumpangtanyaInforequestLayer is removed."""
        from plone.browserlayer import utils

        from tumpangtanya.inforequest.interfaces import ITumpangtanyaInforequestLayer

        self.assertNotIn(ITumpangtanyaInforequestLayer, utils.registered_layers())
