# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s tumpangtanya.inforequest -t test_foi_request.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src tumpangtanya.inforequest.testing.TUMPANGTANYA_INFOREQUEST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/tumpangtanya/inforequest/tests/robot/test_foi_request.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a foi request
  Given a logged-in site administrator
    and an add foi request form
   When I type 'My foi request' into the title field
    and I submit the form
   Then a foi request with the title 'My foi request' has been created

Scenario: As a site administrator I can view a foi request
  Given a logged-in site administrator
    and a foi request 'My foi request'
   When I go to the foi request view
   Then I can see the foi request title 'My foi request'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add foi request form
  Go To  ${PLONE_URL}/++add++foi request

a foi request 'My foi request'
  Create content  type=foi request  id=my-foi_request  title=My foi request

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the foi request view
  Go To  ${PLONE_URL}/my-foi_request
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a foi request with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the foi request title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
