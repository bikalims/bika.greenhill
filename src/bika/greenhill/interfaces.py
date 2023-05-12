# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBikaGreenhillLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IBikaGreenhill(Interface):
    """Marker interface for bika greenhill
    """

class IEnvironmentalConditions(Interface):
    """Marker interface for Environmental Conditions
    """

class IEnvironmentalCondition(Interface):
    """Marker interface for Environmental Condition
    """

class IFacilities(Interface):
    """Marker interface for Facilities
    """

class IFacility(Interface):
    """Marker interface for Facility
    """