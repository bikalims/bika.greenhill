# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import View
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from .fields import ExtUIDReferenceField
from bika.lims.interfaces import IAnalysisRequest
from bika.lims.browser.widgets import ReferenceWidget
from bika.greenhill import _
from bika.greenhill.interfaces import IBikaGreenhillLayer

environmental_condition_field = ExtUIDReferenceField(
    'EnvironmentalCondition',
    allowed_types=('EnvironmentalCondition',),
    mode="rw",
    read_permission=View,
    widget=ReferenceWidget(
        label=_("Environmental conditions"),
        description=_("The environmental condition during sampling"),
        size=20,
        render_own_label=True,
        visible={
            'add': 'edit',
            'secondary': 'disabled',
        },
        catalog_name='portal_catalog',
        base_query={"is_active": True,
                    "sort_on": "sortable_title",
                    "sort_order": "ascending"},
        showOn=True,
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