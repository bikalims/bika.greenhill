# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.QUEUE.
#
# SENAITE.QUEUE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2019-2021 by it's authors.
# Some rights reserved, see README and LICENSE.

import transaction
from Products.Archetypes.config import UID_CATALOG

from bika.lims import api
from bika.greenhill.config import PRODUCT_NAME
from bika.greenhill.config import logger

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


def convert_attachment_report_options(tool):
    """Convert raw ReportOption for new RenderInReport boolean field
    """
    logger.info("Convert attachment report options ...")
    query = {
        "portal_type": ["Attachment"],
    }
    brains = api.search(query, UID_CATALOG)
    total = len(brains)

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

        obj.setRenderInReport(False)

        # Flush the object from memory
        obj._p_deactivate()

    logger.info("Convert attachment report options [DONE]")
