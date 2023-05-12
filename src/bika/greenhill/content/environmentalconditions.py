# -*- coding: utf-8 -*-

from senaite.core.interfaces import IHideActionsMenu
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from bika.greenhill.interfaces import IEnvironmentalConditions


class IEnvironmentalConditionsSchema(model.Schema):
    """A container for sample containers
    """


@implementer(IEnvironmentalConditions, IEnvironmentalConditionsSchema, IHideActionsMenu)
class EnvironmentalConditions(Container):
    """A container for sample containers
    """
