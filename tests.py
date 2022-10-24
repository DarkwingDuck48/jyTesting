from unittest import TestCase, main
from main import simple_func

class SimpeTest(TestCase):
    
    def test_simple_func(self):
        name = "Max"
        age = 30
        test_str = simple_func(name, age)
        self.assertEqual(test_str, "My name is %s. Age is %s" % (name, age))
        
    def test_error(self):
        self.assertTrue(False)
        
if __name__ == "__main__":
    main()