# -*- coding: utf-8 -*-

from senaite.core.interfaces import IHideActionsMenu
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from zope import schema
from bika.greenhill.interfaces import IFacility


class IFacilitySchema(model.Schema):
    """A container for sample containers
    """

    title = schema.TextLine(
        title=u"Title",
        required=False,
    )

    number = schema.TextLine(
        title=u"Number",
        required=False,
    )

    description = schema.Text(
        title=u"Description",
        required=False,
    )


@implementer(IFacility, IFacilitySchema, IHideActionsMenu)
class Facility(Container):
    """A container for sample containers
    """
