*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pelle
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  The username is too short

Register With Valid Username And Too Short Password
    Set Username  pelle
    Set Password  ka
    Set Confirmation  ka
    Submit Credentials
    Register Should Fail With Message   The password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  The password and confirmation do not match

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Text  password_confirmation  ${confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}