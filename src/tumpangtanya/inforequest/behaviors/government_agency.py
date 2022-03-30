# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from tumpangtanya.inforequest import _


class IGovernmentAgencyMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IGovernmentAgency(model.Schema):
    """ """

    directives.widget(government_agency=SelectFieldWidget)
    directives.order_after(government_agency='IFoiRequest.detail')
    directives.order_after(government_agency='IInfoRequest.detail')
    government_agency = schema.Choice(
        title=_(u"Government Agency"),
        description=_(
            u"""
        Government Agency this request was made to
        """
        ),
        required=False,
        vocabulary="tumpangtanya.inforequest.GovernmentAgency",
    )


@implementer(IGovernmentAgency)
@adapter(IGovernmentAgencyMarker)
class GovernmentAgency(object):
    def __init__(self, context):
        self.context = context

    @property
    def government_agency(self):
        if safe_hasattr(self.context, "government_agency"):
            return self.context.government_agency
        return None

    @government_agency.setter
    def government_agency(self, value):
        self.context.government_agency = value
