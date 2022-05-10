# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
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

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(IGovernmentAgencyInfoRequest)
@adapter(IGovernmentAgencyInfoRequestMarker)
class GovernmentAgencyInfoRequest(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
