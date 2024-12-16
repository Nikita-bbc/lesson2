import unittest
import runner_from_github


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = runner_from_github.Runner('Egor')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = runner_from_github.Runner('Artem')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = runner_from_github.Runner('Igor')
        runner_2 = runner_from_github.Runner('Kirill')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
