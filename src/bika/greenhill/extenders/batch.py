# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import StringWidget, SelectionWidget
from Products.Archetypes.Widget import BooleanWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from senaite.core.api import geo
from .fields import ExtBooleanField, ExtStringField
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

country_of_origin_field = ExtStringField(
    'CountryOfOrigin',
    vocabulary=map(
        lambda country: (country.alpha_2, country.name), geo.get_countries()),
    default='',
    widget=SelectionWidget(
        label=_("Country of origin"),
        description=_("The country where the samples come from"),
        format='select',
    )
)

removal_permit_number_field = ExtStringField(
    'RemovalPermit',
    required=0,
    widget=StringWidget(
        label=_("Removal permit number"),
        description=_('Permit to release container consignment'),
    )
)

facility_number_field = ExtStringField(
    'Facility',
    widget=StringWidget(
        label=_("Facility number"),
        description=_("Identification number for exporting facility"),
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
        label=_("Seal number"),
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
        country_of_origin_field,
        removal_permit_number_field,
        facility_number_field,
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
