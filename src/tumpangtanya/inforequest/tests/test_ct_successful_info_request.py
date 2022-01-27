# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import TEST_USER_ID, setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

from tumpangtanya.inforequest.content.successful_info_request import (
    ISuccessfulInfoRequest,  # NOQA E501
)
from tumpangtanya.inforequest.testing import (  # noqa
    TUMPANGTANYA_INFOREQUEST_INTEGRATION_TESTING,
)


class SuccessfulInfoRequestIntegrationTest(unittest.TestCase):

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

    def test_ct_successful_info_request_schema(self):
        fti = queryUtility(IDexterityFTI, name="Successful Info Request")
        schema = fti.lookupSchema()
        self.assertEqual(ISuccessfulInfoRequest, schema)

    def test_ct_successful_info_request_fti(self):
        fti = queryUtility(IDexterityFTI, name="Successful Info Request")
        self.assertTrue(fti)

    def test_ct_successful_info_request_factory(self):
        fti = queryUtility(IDexterityFTI, name="Successful Info Request")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISuccessfulInfoRequest.providedBy(obj),
            u"ISuccessfulInfoRequest not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_successful_info_request_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Successful Info Request",
            id="successful_info_request",
        )

        self.assertTrue(
            ISuccessfulInfoRequest.providedBy(obj),
            u"ISuccessfulInfoRequest not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("successful_info_request", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("successful_info_request", parent.objectIds())

    def test_ct_successful_info_request_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Successful Info Request")
        self.assertFalse(fti.global_allow, u"{0} is globally addable!".format(fti.id))

    def test_ct_successful_info_request_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Successful Info Request")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "successful_info_request_id",
            title="Successful Info Request container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )