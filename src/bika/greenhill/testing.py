# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import bika.greenhill


class BikaGreenhillLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bika.greenhill)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bika.greenhill:default')


BIKA_GREENHILL_FIXTURE = BikaGreenhillLayer()


BIKA_GREENHILL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BIKA_GREENHILL_FIXTURE,),
    name='BikaGreenhillLayer:IntegrationTesting',
)


BIKA_GREENHILL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BIKA_GREENHILL_FIXTURE,),
    name='BikaGreenhillLayer:FunctionalTesting',
)


BIKA_GREENHILL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BIKA_GREENHILL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BikaGreenhillLayer:AcceptanceTesting',
)
