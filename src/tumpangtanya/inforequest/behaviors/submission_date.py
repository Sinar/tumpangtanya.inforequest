# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from tumpangtanya.inforequest import _


class ISubmissionDateMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ISubmissionDate(model.Schema):
    """ """

    # submission date
    submission_date = schema.Date(
        title=_(u"Date when request submitted"),
        required=False,
    )


@implementer(ISubmissionDate)
@adapter(ISubmissionDateMarker)
class SubmissionDate(object):
    def __init__(self, context):
        self.context = context

    @property
    def submission_date(self):
        if safe_hasattr(self.context, "submission_date"):
            return self.context.submission_date
        return None

    @submission_date.setter
    def submission_date(self, value):
        self.context.submission_date = value
