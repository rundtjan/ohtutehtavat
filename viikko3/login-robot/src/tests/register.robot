*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pelle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  The username is too short

Register With Valid Username And Too Short Password
    Input Credentials  pelle  kalle12
    Output Should Contain  The password is too short

Register With Invalid Username And Valid Password
    Input Credentials  pelle22  kalle123
    Output Should Contain  The username should contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pelle  kalleyykaakoo
    Output Should Contain  The password should contain both letters and numbers

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
