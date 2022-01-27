# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget

# from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from tumpangtanya.inforequest import _


class IFailedInfoRequest(model.Schema):
    """Marker interface and Dexterity Python Schema for FailedInfoRequest"""

    # request method
    directives.widget(request_failed_type=SelectFieldWidget)
    request_failed_type = schema.Choice(
        title=_(u"Reason for failure"),
        description=_(
            u"""
        Why did information request failed
        """
        ),
        required=False,
        vocabulary="tumpangtanya.inforequest.InfoRequestFailed",
    )

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('failed_info_request.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IFailedInfoRequest)
class FailedInfoRequest(Container):
    """Content-type class for IFailedInfoRequest"""
