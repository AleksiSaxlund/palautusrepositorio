*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  m  matti123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  MATT1asd  matti123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  matti  matt1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattiaaaaaa
    Output Should Contain  Password must contain atleast one number

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command