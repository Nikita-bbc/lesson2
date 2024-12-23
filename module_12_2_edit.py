import unittest
import runner_from_github


class TournamentTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.name_1 = runner_from_github.Runner('Усэйн', 10)
        self.name_2 = runner_from_github.Runner('Андрей', 9)
        self.name_3 = runner_from_github.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key, ':', value)  # не знаю как сделать по-другому

    """def tearDown(self):
        print(self.all_results)"""  # этот метод, как по мне, более подходящий

    def test_first_run(self):
        runners = runner_from_github.Tournament(90, self.name_1, self.name_3)
        results = runners.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[2], 'Ник')

    def test_second_run(self):
        runners = runner_from_github.Tournament(90, self.name_2, self.name_3)
        results = runners.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[2], 'Ник')

    def test_third_run(self):
        runners = runner_from_github.Tournament(90, self.name_1, self.name_2, self.name_3)
        results = runners.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[3], 'Ник')


if __name__ == '__main__':
    unittest.main()
