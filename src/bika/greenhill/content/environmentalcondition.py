# -*- coding: utf-8 -*-

from senaite.core.interfaces import IHideActionsMenu
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from bika.greenhill.interfaces import IEnvironmentalCondition


class IEnvironmentalConditionSchema(model.Schema):
    """A container for sample containers
    """


@implementer(IEnvironmentalCondition, IEnvironmentalConditionSchema, IHideActionsMenu)
class EnvironmentalCondition(Container):
    """A container for sample containers
    """
