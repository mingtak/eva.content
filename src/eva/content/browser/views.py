# -*- coding: utf-8 -*-
from eva.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from DateTime import DateTime

import json
import random
import logging


logger = logging.getLogger("EVA EVENT")


class Again(BrowserView):
    """ Again """

    template = ViewPageTemplateFile("template/again.pt")

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request

        if 'eva-macau.playgroup.com.tw' not in request.get('HTTP_REFERER'):
            request.response.redirect(portal.absolute_url())
            return

        return self.template()


class Sign(BrowserView):
    """ Sign """

    template = ViewPageTemplateFile("template/sign.pt")

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request

        if 'eva-macau.playgroup.com.tw' not in request.get('HTTP_REFERER'):
            request.response.redirect(portal.absolute_url())
            return

        if not bool(request.form.has_key('name') and request.form.has_key('tel') and request.form.has_key('email') and request.form.has_key('where')):
            return self.template()

        name = request.form.get('name')
        tel = request.form.get('tel')
        email = request.form.get('email')
        where = request.form.get('where')

        if not bool( name and tel and email and where ):
            return 1 # 缺資料

        result = json.loads(portal['result'].description)
        email = email.lower()
        if result.has_key(email):
            return 2 # 已登錄過

        result[email] = [name, tel, where, DateTime().strftime('%Y/%m/%d %H:%M')]
        portal['result'].description = json.dumps(result)
        return 'true' # 成功


class CoverView(BrowserView):
    """ Cover View """

    award_template = ViewPageTemplateFile("template/award_list.pt")

    template = ViewPageTemplateFile("template/cover_view.pt")
    #line_template = ViewPageTemplateFile("template/line.pt")

    def getRandomStr(self):
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 6))


    def __call__(self):
        return self.award_template()

        portal = api.portal.get()
        context = self.context
        request = self.request

        self.isLine = False
        if 'line' in request.get('HTTP_X_REQUESTED_WITH', '').lower():
            self.isLine = True

        if 'line' in request.get('HTTP_USER_AGENT', '').lower():
            self.isLine = True

        return self.template()


class UserList(BrowserView):
    """ User List """

    template = ViewPageTemplateFile("template/user_list.pt")


    def award(self):
        context = self.context
        result = json.loads(context.description)
        award1 = random.choice(result.keys())
        award2 = random.choice(result.keys())
        return [award1, award2]

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request
        return self.template()
