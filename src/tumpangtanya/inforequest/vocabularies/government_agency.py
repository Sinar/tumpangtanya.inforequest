# -*- coding: utf-8 -*-

# from plone import api
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from tumpangtanya.inforequest import _


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class GovernmentAgency(object):
    """ """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u"ptg-sg", _(u"Pejabat Tanah dan Galian, Selangor")),
            VocabItem(u"ptg-pg", _(u"Pejabat Tanah dan Galian, Penang")),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


GovernmentAgencyFactory = GovernmentAgency()