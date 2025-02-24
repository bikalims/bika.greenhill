# -*- coding: utf-8 -*-

import transaction

from bika.lims import api
from bika.greenhill.config import PRODUCT_NAME
from bika.greenhill.config import logger

from senaite.core.catalog import SAMPLE_CATALOG
from senaite.core.catalog import SETUP_CATALOG
from senaite.core.upgrade import upgradestep
from senaite.core.upgrade.utils import UpgradeUtils
from senaite.core.upgrade.utils import uncatalog_brain

version = "1.0.1"


@upgradestep(PRODUCT_NAME, version)
def upgrade(tool):
    portal = tool.aq_inner.aq_parent
    ut = UpgradeUtils(portal)
    ver_from = ut.getInstalledVersion(PRODUCT_NAME)

    if ut.isOlderVersion(PRODUCT_NAME, version):
        logger.info("Skipping upgrade of {0}: {1} > {2}".format(
            PRODUCT_NAME, ver_from, version))
        return True

    logger.info("Upgrading {0}: {1} -> {2}".format(PRODUCT_NAME, ver_from, version))

    # -------- ADD YOUR STUFF BELOW --------

    logger.info("{0} upgraded to version {1}".format(PRODUCT_NAME, version))
    return True


def replace_swab_sample_type(tool):
    """Convert raw ReportOption for new RenderInReport boolean field
    """
    logger.info("Setting Sample Type on Samples...")
    query = {
        "portal_type": "AnalysisRequest",
    }
    brains = api.search(query, SAMPLE_CATALOG)
    total = len(brains)

    query = {
        "portal_type": "SampleType",
        "title": "Swab",
    }
    sample_type_brains = api.search(query, SETUP_CATALOG)
    if len(sample_type_brains) == 1:
        sample_type = sample_type_brains[0].getObject()
    else:
        logger.info("Sample Type NOT FOUND exiting...")
        return

    for num, brain in enumerate(brains):
        if num and num % 100 == 0:
            logger.info("Processed objects: {}/{}".format(num, total))

        if num and num % 1000 == 0:
            # reduce memory size of the transaction
            transaction.savepoint()

        try:
            obj = api.get_object(brain)
        except AttributeError:
            obj = None

        if not obj:
            uncatalog_brain(brain)
            continue

        if obj.getSampleTypeTitle() == "NewSwab":
            obj.setSampleType(sample_type)
        if obj.getSampleTypeTitle() == "Air Plate":
            obj.setSampleType(sample_type)

        # Flush the object from memory
        obj._p_deactivate()

    logger.info("Setting Sample Type on Samples [DONE]")
