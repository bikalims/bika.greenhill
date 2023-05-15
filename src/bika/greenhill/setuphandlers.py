# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from senaite.core.setuphandlers import add_dexterity_items
from bika.lims import api
from bika.greenhill.config import logger, PRODUCT_NAME, PROFILE_ID

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'bika.greenhill:uninstall',
        ]


def post_install(portal_setup):
    """Post install script"""
    profile_id = PROFILE_ID
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()
    add_senaite_setup_items(portal)
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.

def add_senaite_setup_items(portal):
    """Adds setup items to the new SENAITE setup
    """
    items = [
        ("facilites",  # ID
         "Facilities",  # Title
         "Facilities"),  # FTI
    ]
    setup = api.get_setup()

    add_dexterity_items(setup, items)

def setup_handler(context):
    """Generic setup handler"""
    if context.readDataFile("{}.txt".format(PRODUCT_NAME)) is None:
        return

    logger.info("{} setup handler [BEGIN]".format(PRODUCT_NAME.upper()))
    # portal = context.getSite()

    logger.info("{} setup handler [DONE]".format(PRODUCT_NAME.upper()))
