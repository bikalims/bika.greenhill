# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

from bika.greenhill.interfaces import IBikaGreenhillLayer
from bika.lims.api import get_request


_ = MessageFactory('bika.greenhill')


def is_installed():
    """Returns whether the product is installed or not"""
    request = get_request()
    return IBikaGreenhillLayer.providedBy(request)
