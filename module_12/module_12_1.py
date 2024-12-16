import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        brian = Runner("Brian Daniel Pintado Álvarez")
        for _ in range(10):
            brian.walk()
        self.assertEqual(brian.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        bolt = Runner("Usain St. Leo Bolt")
        for _ in range(10):
            bolt.run()
        self.assertEqual(bolt.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        brian = Runner("Brian Daniel Pintado Álvarez")
        bolt = Runner("Usain St. Leo Bolt")
        for _ in range(10):
            brian.walk()
            bolt.run()
        self.assertNotEqual(brian.distance, bolt.distance)


if __name__ == "__main__":
    unittest.main()
