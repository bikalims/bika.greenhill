# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import MultiSelectionWidget,TextAreaWidget,StringWidget,SelectionWidget
from Products.Archetypes.Widget import BooleanWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender, ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from bika.lims.browser.widgets import AddressWidget
from bika.lims.browser.fields import AddressField
from .fields import ExtBooleanField, ExtTextField, ExtStringField, ExtLinesField
from bika.lims.interfaces import IBatch
from bika.greenhill import _
from bika.greenhill.interfaces import IBikaGreenhillLayer


container_number_field = ExtStringField(
    'ContainerNumber',
    required=0,
    widget=StringWidget(
        label=_("Container number"),
        description=_('The container the sample batch arrived in'),
    )
)

# country_of_origin_field = AddressField(
#     "CountryOfOrigin",
#     widget=AddressWidget(
#         label=_("Country of Origin"),
#     ),
#     subfield_validators={
#         "country": "inline_field_validator",
#     },
# )

removal_permit_number_field = ExtStringField(
    'RemovalPermit',
    required=0,
    widget=StringWidget(
        label=_("Removal permit number"),
        description=_('Permit to release container consignment'),
    )
)

dalrrd_number_field = ExtStringField(
    'DALRRDNumber',
    required=0,
    widget=StringWidget(
        label=_("DALRRD number"),
        description=_('Number assigned to samples by DALRRD Inspector'),
    )
)

seal_number_field = ExtStringField(
    'SealNumber',
    required=0,
    widget=StringWidget(
        label=_("Seal number'"),
        description=_('Batch containers seal number'),
    )
)

seal_intact_field = ExtBooleanField(
    "SealIntact",
    mode="rw",
    widget=BooleanWidget(
        label=_(u"Seal intact"),
        description=_(u"Seal state on arrival"),
    ),
)

@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class BatchSchemaExtender(object):
    adapts(IBatch)
    layer = IBikaGreenhillLayer

    fields = [
        container_number_field,
        # country_of_origin_field,
        removal_permit_number_field,
        dalrrd_number_field,
        seal_number_field,
        seal_intact_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields