# Created by epbca at 2/14/2023
Feature: Amazon search test


  Scenario: Logged out user sees Sign In when clicking on Returns and Orders.
    Given Open Amazon page
    When Click on Returns and Orders
    Then Verify that Sign in page opened
