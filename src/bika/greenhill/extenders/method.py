# -*- coding: utf-8 -*-

from Products.Archetypes.Widget import BooleanWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from .fields import ExtBooleanField
from bika.lims.interfaces import IMethod
from bika.greenhill import _
from bika.greenhill.interfaces import IBikaGreenhillLayer


savc_registered_field = ExtBooleanField(
    "SAVCRegistered",
    mode="rw",
    widget=BooleanWidget(
        label=_(u"South African Veterinary Council registered"),
    ),
)

@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class MethodSchemaExtender(object):
    adapts(IMethod)
    layer = IBikaGreenhillLayer

    fields = [
        savc_registered_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields