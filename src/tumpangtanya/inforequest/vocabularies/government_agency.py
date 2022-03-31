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
            VocabItem(u"jabatan-hutan-selangor", _(u"Jabatan Hutan Negeri Selangor")),
            VocabItem(u"jais", _(u"Jabatan Agama Islam Selangor")),
            VocabItem(u"ptg-pg", _(u"Pejabat Tanah dan Galian, Penang")),
            VocabItem(u"mbpj", _(u"Majlis Bandaraya Petaling Jaya")),
            VocabItem(u"mbsj", _(u"Majlis Bandaraya Subang Jaya")),
            VocabItem(u"mbsp", _(u"Majlis Perbandaran Seberang Perai")),
            VocabItem(
                u"suk-selangor",
                _(
                    u"""Pejabat Setiausaha Kerajaan
                Negeri Selangor"""
                ),
            ),
            VocabItem(
                u"suk-penang",
                _(
                    u"""Pejabat Setiausaha Kerajaan
                Negeri Penang"""
                ),
            ),
            VocabItem(
                u"kewangan-sg",
                _(
                    u"""Jabatan Kewangan
                Negeri Selangor"""
                ),
            ),
            VocabItem(
                u"kewangan-pg",
                _(
                    u"""Jabatan Kewangan
                Negeri Penang"""
                ),
            ),
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
