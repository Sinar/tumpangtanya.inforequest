# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import TEST_USER_ID, setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

from tumpangtanya.inforequest.content.failed_info_request import (
    IFailedInfoRequest,  # NOQA E501
)
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class FailedInfoRequestIntegrationTest(unittest.TestCase):

    layer = TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Info Request",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_failed_info_request_schema(self):
        fti = queryUtility(IDexterityFTI, name="Failed Info Request")
        schema = fti.lookupSchema()
        self.assertEqual(IFailedInfoRequest, schema)

    def test_ct_failed_info_request_fti(self):
        fti = queryUtility(IDexterityFTI, name="Failed Info Request")
        self.assertTrue(fti)

    def test_ct_failed_info_request_factory(self):
        fti = queryUtility(IDexterityFTI, name="Failed Info Request")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFailedInfoRequest.providedBy(obj),
            u"IFailedInfoRequest not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_failed_info_request_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Failed Info Request",
            id="failed_info_request",
        )

        self.assertTrue(
            IFailedInfoRequest.providedBy(obj),
            u"IFailedInfoRequest not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("failed_info_request", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("failed_info_request", parent.objectIds())

    def test_ct_failed_info_request_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Failed Info Request")
        self.assertFalse(fti.global_allow, u"{0} is globally addable!".format(fti.id))

    def test_ct_failed_info_request_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Failed Info Request")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "failed_info_request_id",
            title="Failed Info Request container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )
