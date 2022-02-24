# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s tumpangtanya.inforequest -t test_info_request.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src tumpangtanya.inforequest.testing.TUMPANGTANYA_INFOREQUEST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/tumpangtanya/inforequest/tests/robot/test_info_request.robot
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

Scenario: As a site administrator I can add a info request
  Given a logged-in site administrator
    and an add info request form
   When I type 'My info request' into the title field
    and I submit the form
   Then a info request with the title 'My info request' has been created

Scenario: As a site administrator I can view a info request
  Given a logged-in site administrator
    and a info request 'My info request'
   When I go to the info request view
   Then I can see the info request title 'My info request'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add info request form
  Go To  ${PLONE_URL}/++add++info request

a info request 'My info request'
  Create content  type=info request  id=my-info_request  title=My info request

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the info request view
  Go To  ${PLONE_URL}/my-info_request
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a info request with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the info request title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
