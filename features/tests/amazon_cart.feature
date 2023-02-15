# Created by epbca at 2/14/2023
Feature: Amazon cart tests


  Scenario: User clicks on cart icon and verify that Amazon Cart is empty.
    Given Open Amazon page
    When Click on cart icon
    Then Verify that Amazon cart is empty