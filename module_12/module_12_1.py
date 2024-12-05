from HumanMoveTest.runner import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        brian = Runner("Brian Daniel Pintado Álvarez")
        for _ in range(10):
            brian.walk()
        self.assertEqual(brian.distance, 50)

    def test_run(self):
        bolt = Runner("Usain St. Leo Bolt")
        for _ in range(10):
            bolt.run()
        self.assertEqual(bolt.distance, 100)

    def test_challenge(self):
        brian = Runner("Brian Daniel Pintado Álvarez")
        bolt = Runner("Usain St. Leo Bolt")
        for _ in range(10):
            brian.walk()
            bolt.run()
        self.assertNotEqual(brian.distance, bolt.distance)


if __name__ == "__main__":
    unittest.main()
