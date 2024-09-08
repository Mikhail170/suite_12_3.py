import unittest
import tests_12_1
import tests_12_3

testsSuite = unittest.TestSuite()
testsSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
testsSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testsSuite)
