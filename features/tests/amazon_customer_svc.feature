# Created by epbca at 2/23/2023
Feature: Amazon Customer Service tests

  Scenario: Verify customer service UI Elements are present
    Given Open Amazon Customer Service page
    Then Verify that Welcome Banner is present
    Then Verify that 10 welcome quick links are present
    Then Verify that Search banner is present
    Then Verify that search text field is present
    Then Verify that All help topics banner is present
    Then Verify that 11 help quick links are present
