# -*- coding: utf-8 -*-
import unittest

from plone.app.testing import TEST_USER_ID, setRoles
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

from tumpangtanya.inforequest.behaviors.government_agency import IGovernmentAgencyMarker
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class GovernmentAgencyIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_government_agency(self):
        behavior = getUtility(IBehavior, "tumpangtanya.inforequest.government_agency")
        self.assertEqual(
            behavior.marker,
            IGovernmentAgencyMarker,
        )
