# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from tumpangtanya.inforequest import _


class IInfoRequest(model.Schema):
    """Marker interface and Dexterity Python Schema for InfoRequest"""

    # request method

    # submission date
    submission_date = schema.Date(
        title=_(u"Date when request submitted"),
        required=False,
    )

    # government agency

    directives.widget(interest_type=SelectFieldWidget)
    interest_type = schema.Choice(
        title=_(u"Government Agency"),
        description=_(
            u"""
        Government Agency this request was made to
        """
        ),
        required=False,
        vocabulary="tumpangtanya.inforequest.GovernmentAgency",
    )

    details = RichText(
        title=_(u"Details"),
        description=_(
            u"""Additional details about this information
         request"""
        ),
        required=False,
    )

    supporting_document = namedfile.NamedFile(
        title=_(u"Supporting Document"),
        description=_(
            u"""Supporting document related to this request.
         """
        ),
        required=False,
    )


@implementer(IInfoRequest)
class InfoRequest(Container):
    """Content-type class for IInfoRequest"""
