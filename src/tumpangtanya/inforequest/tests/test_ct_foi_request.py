# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import TEST_USER_ID, setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

from tumpangtanya.inforequest.content.foi_request import IFoiRequest  # NOQA E501
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class FoiRequestIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_foi_request_schema(self):
        fti = queryUtility(IDexterityFTI, name="foi request")
        schema = fti.lookupSchema()
        self.assertEqual(IFoiRequest, schema)

    def test_ct_foi_request_fti(self):
        fti = queryUtility(IDexterityFTI, name="foi request")
        self.assertTrue(fti)

    def test_ct_foi_request_factory(self):
        fti = queryUtility(IDexterityFTI, name="foi request")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFoiRequest.providedBy(obj),
            u"IFoiRequest not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_foi_request_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="foi request",
            id="foi_request",
        )

        self.assertTrue(
            IFoiRequest.providedBy(obj),
            u"IFoiRequest not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("foi_request", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("foi_request", parent.objectIds())

    def test_ct_foi_request_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="foi request")
        self.assertTrue(
            fti.global_allow, u"{0} is not globally addable!".format(fti.id)
        )

    def test_ct_foi_request_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="foi request")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "foi_request_id",
            title="foi request container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )
