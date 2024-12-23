import unittest
import module_12_1_edit
import module_12_2_edit

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_edit.TournamentTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1_edit.RunnerTest))

testing = unittest.TextTestRunner(verbosity=2)
testing.run(runST)
