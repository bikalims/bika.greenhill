# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import StringWidget
from Products.CMFCore.permissions import View
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from bika.lims.permissions import FieldEditEnvironmentalConditions
from .fields import ExtStringField
from bika.lims.interfaces import IAnalysisRequest
from bika.greenhill import _
from bika.greenhill.interfaces import IBikaGreenhillLayer


environmental_condition_field = ExtStringField(
    'EnvironmentalConditions',
    mode="rw",
    read_permission=View,
    write_permission=FieldEditEnvironmentalConditions,
    widget=StringWidget(
        label=_("Environmental conditions"),
        description=_("The environmental condition during sampling"),
        visible={
            'add': 'edit',
            'header_table': 'prominent',
        },
        render_own_label=True,
        size=20,
    ),
)

@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    layer = IBikaGreenhillLayer

    fields = [
        environmental_condition_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields