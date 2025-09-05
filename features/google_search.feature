Feature: Google Search with date filters
  As a user of Google
  I want to search for "semrush ai"
  So that I can see results filtered by date

  Scenario: Search for "prowly ai" filtered by Past 24 Hours
    Given I am on google.com
    When I search for "prowly ai"
    And I apply the "Past 24 hours" date filter
    Then I should see results published within the last 24 hours related to "prowly ai"

  Scenario: Search for "prowly ai" when no results match the selected date
    Given I am on google.com
    When I search for "prowly ai"
    And I apply the "Past hour" date filter
    And no results are available in that time range
    Then I should see a message indicating "No results found"
    And I should be provided with suggestions to broaden the date filter

  Scenario: Search for "prowly ai" with an invalid date filter
    Given I am on google.com
    When I search for "prowly ai"
    And I apply an invalid time range from 1/1/9999 to 1/1/9999 date filter
    And no results are available in that time range
    Then I should see a message indicating "No results found"
    And I should be provided with suggestions to broaden the date filter