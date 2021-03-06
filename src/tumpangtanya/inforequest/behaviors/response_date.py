# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from tumpangtanya.inforequest import _


class IResponseDateMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IResponseDate(model.Schema):
    """ """

    # response date
    directives.order_after(response_date="IInforequestCost.submission_cost")
    response_date = schema.Date(
        title=_(u"Date when requests responded to by government agency"),
        required=False,
    )


@implementer(IResponseDate)
@adapter(IResponseDateMarker)
class ResponseDate(object):
    def __init__(self, context):
        self.context = context

    @property
    def response_date(self):
        if safe_hasattr(self.context, "response_date"):
            return self.context.response_date
        return None

    @response_date.setter
    def response_date(self, value):
        self.context.response_date = value
