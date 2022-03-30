# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model

# from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from tumpangtanya.inforequest import _


class IFoiRequest(model.Schema):
    """Marker interface and Dexterity Python Schema for FoiRequest"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('foi_request.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    details = RichText(
        title=_(u"Details"),
        description=_(
            u"""
         Additional details about this FOI request"""
        ),
        required=False,
    )

    responses = RichText(
        title=_(u"Reponse Details"),
        description=_(
            u"""
         Additional follow up information related to this request"""
        ),
        default=_(
            u"""
         <h3>Timeline</h3>
         <ul>
             <li>Date <date> ... </li> 
        </ul>
         """
        ),
        required=False,
    )

    # Submission Documents
    directives.order_after(submission_documents="ISubmissionDate.submission_date")
    directives.widget(
        "submission_documents",
        RelatedItemsFieldWidget,
        pattern_options={
            "mode": "auto",
            "favourites": [],
        },
    )

    submission_documents = RelationList(
        title=u"Submission Documents",
        description=_(
            u"""
            Documents for submisssion such as forms, letters or
            receipts.
            """
        ),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type="File"),
        ),
        required=False,
    )

    # Requested Documents
    directives.order_after(requested_documents="IResponseDate.response_date")
    directives.widget(
        "requested_documents",
        RelatedItemsFieldWidget,
        pattern_options={
            "mode": "auto",
            "favourites": [],
        },
    )

    requested_documents = RelationList(
        title=u"Requested Documents",
        description=_(
            u"""
            Documents from successful request
            """
        ),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type="File"),
        ),
        required=False,
    )


@implementer(IFoiRequest)
class FoiRequest(Container):
    """Content-type class for IFoiRequest"""
