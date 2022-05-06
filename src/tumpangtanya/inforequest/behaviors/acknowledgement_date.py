# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset, primary
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from tumpangtanya.inforequest import _


class IAcknowledgementDateMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IAcknowledgementDate(model.Schema):
    """ """

    directives.order_after(acknowledgement_date='IInforequestCost.submission_cost')
    acknowledgement_date = schema.Date(
        title=_(u"Date when request was acknowledged as received."),
        required=False,
    )

@implementer(IAcknowledgementDate)
@adapter(IAcknowledgementDateMarker)
class AcknowledgementDate(object):
    def __init__(self, context):
        self.context = context

    @property
    def acknowledgement_date(self):
        if safe_hasattr(self.context, "acknowledgement_date"):
            return self.context.acknowledgement_date
        return None

    @acknowledgement_date.setter
    def acknowledgement_date(self, value):
        self.context.acknowledgement_date = value
