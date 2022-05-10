# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from tumpangtanya.inforequest import _


class IGovernmentAgencyInfoRequestMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IGovernmentAgencyInfoRequest(model.Schema):
    """
    """

    # Government Agency information reqeuest made to
    directives.widget(government_agency_info_request=SelectFieldWidget)
    government_agency_info_request = schema.Choice(
            title=u'Government Agency',
            description=u'Information requested from this agency',
            required=False,
            vocabulary='sinar.organization.Organizations',
    )

@implementer(IGovernmentAgencyInfoRequest)
@adapter(IGovernmentAgencyInfoRequestMarker)
class GovernmentAgencyInfoRequest(object):
    def __init__(self, context):
        self.context = context

    @property
    def government_agency_info_request(self):
        if safe_hasattr(self.context, 'government_agency_info_request'):
            return self.context.government_agency_info_request
        return None

    @government_agency_info_request.setter
    def government_agency_info_request(self, value):
        self.context.government_agency_info_request = value
