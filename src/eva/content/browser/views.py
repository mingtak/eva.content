# -*- coding: utf-8 -*-
from eva.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from DateTime import DateTime

import random
import logging


logger = logging.getLogger("EVA EVENT")


class Sign(BrowserView):
    """ Sign """

    template = ViewPageTemplateFile("template/sign.pt")

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request

#        import pdb; pdb.set_trace()
        if not bool(request.form.has_key('name') and request.form.has_key('tel') and request.form.has_key('email') and request.form.has_key('where')):
            return self.template()

        name = request.form.get('name')
        tel = request.form.get('tel')
        email = request.form.get('email')
        where = request.form.get('where')

        if not bool( name and tel and email and where ):
            return 1 # 缺資料
        else:
            return 'true' # 成功


class CoverView(BrowserView):
    """ Cover View """

    template = ViewPageTemplateFile("template/cover_view.pt")

    def getRandomStr(self):
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 6))


    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request
        return self.template()
