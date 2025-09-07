Feature: Bing Search with category filters
  As a user of Bing
  I want to search for "semrush ai"
  So that I can see relevant results filtered by category

  Scenario: Search for "semrush ai" filtered by category Videos
    Given I am on "bing.com"
    When I search for "semrush ai"
    And I select the "Videos" category filter
    Then I should see only video results related to "semrush ai"

  Scenario: Search for "semrush ai" filtered by category Images
    Given I am on "bing.com"
    When I search for "semrush ai"
    And I select the "Images" category filter
    Then I should see only image results related to "semrush ai"

  Scenario: Search for "semrush ai" filtered by category Maps
    Given I am on "bing.com"
    When I search for "semrush ai"
    And I select the "Maps" category filter
    Then I should see only map results related to "semrush ai"