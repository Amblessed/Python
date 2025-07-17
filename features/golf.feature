Feature: Golf feature


    Scenario: Search for Golf by name
        Given I start the browser
        When I go to "https://admlucid.com/Golf"
        And I type "Tiger Golf" in the search box
        Then I should see golf course "Tiger Golf"
    
    Scenario: Search for Golf country in country
        Given I start the browser
        When I go to "https://admlucid.com/Golf"
        And I select "Canada" in the dropdown list
        Then I should see golf course in the country "Canada"