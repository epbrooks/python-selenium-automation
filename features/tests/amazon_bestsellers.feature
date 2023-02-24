# Created by epbca at 2/22/2023
Feature: Amazon Bestsellers tests

  Scenario: Verify header links
    Given Open Amazon Bestsellers Page
    Then Verify Header links are present
    Then Verify that header has 5 links