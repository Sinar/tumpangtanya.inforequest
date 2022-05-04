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


class IInforequestCostMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IInforequestCost(model.Schema):
    """ """

    directives.order_after(submission_cost="ISubmissionDate.submission_date")
    submission_cost = schema.Decimal(
        title=_(u"Submission Cost"),
        description=_(u'''Cost for submitting or filing an information
            request.'''),
        required=False,
    )

    directives.order_after(response_cost="IResponseDate.response_date")
    response_cost = schema.Decimal(
        title=_(u"Response Cost"),
        description=_(u'''Cost for getting response for information request such as
        printing, CD or other related costs.'''),
        required=False,
    )


@implementer(IInforequestCost)
@adapter(IInforequestCostMarker)
class InforequestCost(object):
    def __init__(self, context):
        self.context = context

    @property
    def submission_cost(self):
        if safe_hasattr(self.context, "submission_cost"):
            return self.context.submission_cost
        return None

    @submission_cost.setter
    def submission_cost(self, value):
        self.context.submission_cost = value

    @property
    def response_cost(self):
        if safe_hasattr(self.context, "response_cost"):
            return self.context.response_cost
        return None

    @response_cost.setter
    def response_cost(self, value):
        self.context.response_cost = value
