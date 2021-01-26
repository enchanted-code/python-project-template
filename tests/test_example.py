from python_project import core

class Test_Add_Inputs:
    """
    tests for the core.add_inputs function
    """
    def test_standard(self):
        """
        test 2 inputs without using the *args of add_inputs
        """
        assert core.add_inputs(1, 4) == 5

    def test_multiple(self):
        """
        test 4 inputs using the *args of add_inputs
        """
        assert core.add_inputs(2, 4, 6, 2) == 14
