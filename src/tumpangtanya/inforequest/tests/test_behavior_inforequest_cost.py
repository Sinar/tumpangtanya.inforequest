# -*- coding: utf-8 -*-
import unittest

from plone.app.testing import TEST_USER_ID, setRoles
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

from tumpangtanya.inforequest.behaviors.inforequest_cost import IInforequestCostMarker
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class InforequestCostIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_inforequest_cost(self):
        behavior = getUtility(IBehavior, "tumpangtanya.inforequest.inforequest_cost")
        self.assertEqual(
            behavior.marker,
            IInforequestCostMarker,
        )
