# Created by epbca at 2/14/2023
Feature: Amazon search test


  Scenario: Logged out user sees Sign In when clicking on Returns and Orders.
    Given Open Amazon page
    When Click on Returns and Orders
    Then Verify that Sign in page opened

    Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Input Tablets into search field
    When Clicks on search icon
    Then Verify that every product has a name and image
