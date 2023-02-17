# Created by epbca at 2/14/2023
Feature: Amazon cart tests


  Scenario: User clicks on cart icon and verify that Amazon Cart is empty.
    Given Open Amazon page
    When Click on cart icon
    Then Verify that Amazon cart is empty


 Scenario: User adds product to cart and verify that item is it cart.
   Given Open Amazon page
   When Input Tablets into search field
   When Clicks on search icon
   When Click on Amazon Fire HD 10 inch tablet
   When Click on Add to Cart
   When Click on Go to Cart
   Then Verify that Amazon Cart contains selected item


