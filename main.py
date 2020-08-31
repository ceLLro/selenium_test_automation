import unittest
import TestCases

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
