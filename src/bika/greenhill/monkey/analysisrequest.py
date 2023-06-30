# -*- coding: utf-8 -*-

from bika.greenhill.config import logger
from bika.lims.interfaces import IAddSampleFieldsFlush
from senaite import api
from zope.component import getAdapters


def get_client_info(self, obj):
    """Returns the client info of an object
    """
    info = self.get_base_info(obj)

    # Set the default contact, but only if empty. The Contact field is
    # flushed each time the Client changes, so we can assume that if there
    # is a selected contact, it belongs to current client already
    default_contact = self.get_default_contact(client=obj)
    if default_contact:
        contact_info = self.get_contact_info(default_contact)
        contact_info.update({"if_empty": True})
        info["field_values"].update({
            "Contact": contact_info
        })

    # Set default CC Email field
    info["field_values"].update({
        "CCEmails": {"value": obj.getCCEmails(), "if_empty": True}
    })

    # UID of the client
    uid = api.get_uid(obj)

    # catalog queries for UI field filtering
    filter_queries = {
        "Contact": {
            "getParentUID": [uid]
        },
        "CCContact": {
            "getParentUID": [uid]
        },
        "InvoiceContact": {
            "getParentUID": [uid]
        },
        "Template": {
            "getClientUID": [uid, ""],
        },
        "Profiles": {
            "getClientUID": [uid, ""],
        },
        "Specification": {
            "getClientUID": [uid, ""],
        },
        "Sample": {
            "getClientUID": [uid],
        },
        "Batch": {
            "getClientUID": [uid, ""],
        }
    }
    info["filter_queries"] = filter_queries
    return info


def get_sampletype_info(self, obj):
    """Returns the info for a Sample Type
    """
    info = self.get_base_info(obj)

    # client
    client = self.get_client()
    client_uid = client and api.get_uid(client) or ""

    info.update({
        "prefix": obj.getPrefix(),
        "minimum_volume": obj.getMinimumVolume(),
        "hazardous": obj.getHazardous(),
        "retention_period": obj.getRetentionPeriod(),
    })

    # catalog queries for UI field filtering
    sample_type_uid = api.get_uid(obj)
    filter_queries = {
        # Display Specifications that have this sample type assigned only
        "Specification": {
            "sampletype_uid": sample_type_uid,
            "getClientUID": [client_uid, ""],
        },
        # Display AR Templates that have this sample type assigned plus
        # those that do not have a sample type assigned
        "Template": {
            "sampletype_uid": [sample_type_uid, None],
            "getClientUID": [client_uid, ""],
        }
    }
    info["filter_queries"] = filter_queries

    return info


def sort_ordered_dict_by_list(adict, alist):
    for key in alist:
        move_to_end(adict, key)


def move_to_end(adict, key):
    current = ()
    other = []
    for k, v in adict.items():
        if k == key:
            current = [
                (k, v),
            ]
        else:
            other.append((k, v))
    if other:
        adict.clear()
        adict.update(other)
        adict.update(current)


def ajax_get_flush_settings(self):
    """Returns the settings for fields flush
    """
    flush_settings = {
        "Client": [
            "Contact",
            "CCContact",
            "InvoiceContact",
            "Template",
            "Profiles",
            "PrimaryAnalysisRequest",
            "Specification",
            "Batch"
        ],
        "Contact": [
            "CCContact"
        ],
        "SampleType": [
            "Specification",
            "Template",
        ],
        "PrimarySample": [
            "Batch"
            "Client",
            "Contact",
            "CCContact",
            "CCEmails",
            "ClientOrderNumber",
            "ClientReference",
            "ClientSampleID",
            "ContainerType",
            "DateSampled",
            "EnvironmentalConditions",
            "InvoiceContact",
            "Preservation",
            "Profiles",
            "SampleCondition",
            "SamplePoint",
            "SampleType",
            "SamplingDate",
            "SamplingDeviation",
            "StorageLocation",
            "Specification",
            "Template",
        ]
    }

    # Maybe other add-ons have additional fields that require flushing
    for name, ad in getAdapters((self.context,), IAddSampleFieldsFlush):
        logger.info("Additional flush settings from {}".format(name))
        additional_settings = ad.get_flush_settings()
        for key, values in additional_settings.items():
            new_values = flush_settings.get(key, []) + values
            flush_settings[key] = list(set(new_values))

    return flush_settings
