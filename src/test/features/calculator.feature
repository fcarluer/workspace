Feature: test du calculateur.
I wish to demonstrate
How easy writing Acceptance Tests
In Python really is.
 
	Background:I am using the calculator
 
Scenario: Calculate 2 plus 2
    Given I have "2" and "2"
    When I Add them
    Then I should see "4"
		    
Scenario: Calculate 3 plus 3
    Given I have "3" and "3"
    When I Add them
    Then I should see "6"
		    
		    
		Scenario: Calculate 4 plus 3
		    Given I have "4" and "3"
		    When I Add them
		    Then I should see "7".
		    
		Scenario: Calculate 2 less 2
		    Given I have "2" and "2"
		    When I soustract them
		    Then I should see "0".
		    
		Scenario: Calculate 2 divided by 2
		    Given I have "2" and "2"
		    When I divide them
		    Then I should see "1".
		    
	  Scenario: Calculate 2 multiplied by 2
		    Given I have "2" and "2"
		    When I multiplied them
		    Then I should see "1".