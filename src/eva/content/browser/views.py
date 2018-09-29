# -*- coding: utf-8 -*-
from eva.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from DateTime import DateTime

import logging


logger = logging.getLogger("EVA EVENT")
class CoverView(BrowserView):
    """ Cover View """

    template = ViewPageTemplateFile("template/cover_view.pt")

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request
        return self.template()
