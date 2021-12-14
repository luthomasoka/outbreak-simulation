from outbreak import multiple_infections
import pytest
import turtle

# Defining towo objects for testing
obj_a = turtle.Turtle()
obj_b = turtle.Turtle()

def test_outbreak():

    # Tests the color change of object when collision occurs
    assert multiple_infections(obj_a, obj_b) == obj_b.color("cyan") or obj_b.color("cyan")

pytest.main(["-v", "--tb=line", "-rN", __file__])
