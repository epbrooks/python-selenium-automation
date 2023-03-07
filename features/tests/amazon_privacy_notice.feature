# Created by epbca at 3/6/2023
Feature: Amazon Privacy Notice

Scenario: User can open and close Amazon Privacy Notice
  Given Open Amazon T&C page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  And User can switch back to original window