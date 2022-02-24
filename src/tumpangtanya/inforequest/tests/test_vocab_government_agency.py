# -*- coding: utf-8 -*-
import unittest

from plone.app.testing import TEST_USER_ID, setRoles
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory, IVocabularyTokenized

from tumpangtanya.inforequest import _
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class GovernmentAgencyIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocab_government_agency(self):
        vocab_name = "tumpangtanya.inforequest.GovernmentAgency"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm("sony-a7r-iii").title,
            _(u"Sony Aplha 7R III"),
        )
