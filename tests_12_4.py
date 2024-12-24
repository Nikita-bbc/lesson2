import logging
import unittest
import new_runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='a', encoding='utf-8',
                            format="%(asctime)s / %(levelname)s / %(message)s")
    def test_walk(self):
        try:
            runner = new_runner.Runner('Egor', -5)
            logging.info("test_walk выполнен успешно")
            runner.walk()
            '''self.assertEqual(runner.distance, 50)'''
        except ValueError as vl:
            logging.warning(f"Неверная скорость для Runner, {vl}", exc_info=True)

    def test_run(self):
        try:
            runner = new_runner.Runner(52)
            runner.run()
            logging.info('test_run выполнено успешно')
            '''self.assertEqual(runner.distance, 100)'''
        except TypeError as tp:
            logging.warning(f'Имя некорректно, {tp}', exc_info=True)

    def test_challenge(self):
        runner_1 = new_runner.Runner('Igor')
        runner_2 = new_runner.Runner('Kirill')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()

