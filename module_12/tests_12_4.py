import logging
import unittest
from rt_with_exceptions import Runner

FORMAT = "%(asctime)s %(levelname)s %(funcName)s : %(message)s"

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="UTF-8",
    format=FORMAT,
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            brian = Runner(name="Brian Daniel Pintado Álvarez", speed=-1)
            for _ in range(10):
                brian.walk()
            self.assertEqual(brian.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(err)
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            bolt = Runner(name=None)
            for _ in range(10):
                bolt.run()
            self.assertEqual(bolt.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(err)
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        brian = Runner("Brian Daniel Pintado Álvarez")
        bolt = Runner("Usain St. Leo Bolt")
        for _ in range(10):
            brian.walk()
            bolt.run()
        self.assertNotEqual(brian.distance, bolt.distance)


if __name__ == "__main__":
    unittest.main()
