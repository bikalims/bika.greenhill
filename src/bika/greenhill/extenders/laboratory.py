# -*- coding: utf-8 -*-

from Products.Archetypes.Widget import ImageWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from bika.greenhill import _
from bika.greenhill.extenders.fields import ExtImageField
from bika.greenhill.interfaces import IBikaGreenhillLayer
from bika.lims.interfaces import ILaboratory

sanas_accreditation_logo_field = ExtImageField(
    "SANASAccreditationBodyLogo",
    mode="rw",
    schemata="Accreditation",
    widget=ImageWidget(
        label=_(
            "label_laboratory_sanas_accreditation_body_logo_title",
            "SANAS Accreditation Logo",
        ),
        description=_(
            "description_laboratory_sanas_accreditation_body_logo_title",
            default="Please upload the logo you are authorised to use on your "
                    "website and results reports by your accreditation body. "
                    "Maximum size is 175 x 175 pixels."
        ),
    ),
)


@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class LaboratorySchemaExtender(object):
    adapts(ILaboratory)
    layer = IBikaGreenhillLayer

    fields = [
        sanas_accreditation_logo_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields
