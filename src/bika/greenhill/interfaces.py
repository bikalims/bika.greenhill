# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from bika.lims.interfaces import IBikaLIMS
from senaite.impress.interfaces import ILayer as ISenaiteIMPRESS
from senaite.lims.interfaces import ISenaiteLIMS


class IBikaGreenhillLayer(IBikaLIMS, ISenaiteLIMS, ISenaiteIMPRESS):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IBikaGreenhillBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBikaGreenhill(Interface):
    """Marker interface for bika greenhill
    """


class IFacilities(Interface):
    """Marker interface for Facilities
    """


class IFacility(Interface):
    """Marker interface for Facility
    """
