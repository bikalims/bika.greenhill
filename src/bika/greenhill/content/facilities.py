# -*- coding: utf-8 -*-

from senaite.core.interfaces import IHideActionsMenu
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from bika.greenhill.interfaces import IFacilities


class IFacilitiesSchema(model.Schema):
    """A container for sample containers
    """


@implementer(IFacilities, IFacilitiesSchema, IHideActionsMenu)
class Facilities(Container):
    """A container for sample containers
    """
