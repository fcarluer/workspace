from lettuce import world
from lettuce import step
from lettuce import before
from lettuce import after
from nose.tools import *
from app.calculator import Calculator
    
@before.all
def say_hello():
    print "Hello there!"
    print "Lettuce will start to run tests right now..." 
 
@step('I am using the calculator')
def select_calc(step):
    print ('Attempting to use calculator...')
    world.calc = Calculator()
    print ('calculator connected...')
    
    
@step('I have "([^"]*)" and "([^"]*)"')
def given_i_have_group1_and_group1(step, x, y):
    world.x = x
    world.y = y

@step('I add them')
def given_i_input_group1_add_group1(step):
    world.result = world.calc.add(int(world.x), int(world.y))

@step('I soustract them')
def given_i_input_group1_less_group1(step):
    world.result = world.calc.soustract(int(world.x), int(world.y))

@step('I divide them')
def given_i_input_group1_divided_by_group1(step):
    world.result = world.calc.divide(int(world.x), int(world.y)) 

@step('I multiplied them')
def given_i_input_group1_multiplied_by_group1(step):
    world.result = world.calc.multiply(int(world.x), int(world.y)) 

@step(u'I should see "([^"]+)"')
def result(step, expected_result):
    actual_result = world.result
    assert_equals(int(expected_result), actual_result)
    
@after.all
def say_goodbye(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
    print "Goodbye!"
    
@before.each_feature
def setup_some_feature(feature):
    print "Running the feature %r, at file %s" % (
        feature.name,
        feature.described_at.file
    )