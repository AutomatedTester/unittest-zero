# Overview #

This is a little project to wrap native asserts in Python into a basic DSL so 
that you don't need to rely on unittest or any other testing framework. This 
built to be used with py.test. Documentation can be found [here](http://automatedtester.github.com/unittest-zero/).

## Example ##

    from unittestzero import Assert


    class TestSomethingCool:

        def test_equals(self):
            Assert.equal(1, 1)

## How to run the tests against this frame work ##

Update your PYTHONPATH to the directory and then its a simple 
    py.test . 
in the the tests folder
