# -*- coding: utf-8 -*-
import unittest

from plone.app.testing import TEST_USER_ID, setRoles
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

from tumpangtanya.inforequest.behaviors.submission_date import ISubmissionDateMarker
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class SubmissionDateIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_submission_date(self):
        behavior = getUtility(IBehavior, "tumpangtanya.inforequest.submission_date")
        self.assertEqual(
            behavior.marker,
            ISubmissionDateMarker,
        )
