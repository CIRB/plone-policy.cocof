from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyCocof(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.cocof
        xmlconfig.file('configure.zcml',
                       policy.cocof,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.cocof:default')

POLICY_COCOF_FIXTURE = PolicyCocof()
POLICY_COCOF_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_COCOF_FIXTURE, ),
                       name="PolicyCocof:Integration")