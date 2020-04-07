import pytest
from  calculator.funCalculator import   Calculator

"""
# import the package
import antigravity

# import the antigravity module
from antigravity import antigravity

# or an object inside the antigravity module
from antigravity.antigravity import my_object

"""

"""
Run test  :  >pytest -v -s
"""

@pytest.fixture()
def setup():
    #how-to-share-global-variables-between-tests
    # These variables are controlled via pytest hooks.
    pytest.calculator = Calculator()
    pytest.x=5
    pytest.y=6
    print('\nresources_a() "setup"')
    print("Test parameters , x =", pytest.x, "and  y=",pytest.y)
    
    def teardown():
        print('\nresources_a_teardown()')
        
        
        

def test_calculator_addition(setup):
        resultat = pytest.calculator.addition(pytest.x,pytest.y)
        print("Test addition")
        assert resultat  == 11,"test failed"
 
def test_calculator_subtraction(setup):
        resultat = pytest.calculator.subtraction(pytest.x,pytest.y)
        print("Test subtraction")
        assert resultat == -1,"test failed"