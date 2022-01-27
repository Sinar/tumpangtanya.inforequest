# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s tumpangtanya.inforequest -t test_successful_info_request.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src tumpangtanya.inforequest.testing.TUMPANGTANYA_INFOREQUEST_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/tumpangtanya/inforequest/tests/robot/test_successful_info_request.robot
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

Scenario: As a site administrator I can add a Successful Info Request
  Given a logged-in site administrator
    and an add Info Request form
   When I type 'My Successful Info Request' into the title field
    and I submit the form
   Then a Successful Info Request with the title 'My Successful Info Request' has been created

Scenario: As a site administrator I can view a Successful Info Request
  Given a logged-in site administrator
    and a Successful Info Request 'My Successful Info Request'
   When I go to the Successful Info Request view
   Then I can see the Successful Info Request title 'My Successful Info Request'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Info Request form
  Go To  ${PLONE_URL}/++add++Info Request

a Successful Info Request 'My Successful Info Request'
  Create content  type=Info Request  id=my-successful_info_request  title=My Successful Info Request

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Successful Info Request view
  Go To  ${PLONE_URL}/my-successful_info_request
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Successful Info Request with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Successful Info Request title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}