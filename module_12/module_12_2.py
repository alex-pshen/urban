from runner_and_tournament import *
import unittest


class TournamentTest(unittest.TestCase):

    __DEFAULT_DISTANCE = 90

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = []
        return super().setUpClass()

    def setUp(self) -> None:
        self.bolt = Runner("Usain St. Leo Bolt", 10)
        self.andrew = Runner("Андрей Епишин", 9)
        self.nick = Runner("Nick", 3)
        return super().setUp()

    @classmethod
    def tearDownClass(cls) -> None:
        print()
        for item in cls.all_results:
            print(item)
        return super().tearDownClass()

    def run_tournament(self, *participants, outsider=None, leader=None):
        tournament = Tournament(self.__DEFAULT_DISTANCE, *participants)
        results = tournament.start()

        if outsider:
            self.assertEqual(results[len(participants)], outsider)

        if leader:
            self.assertEqual(results[1], leader)

        # Convert runner objects to names
        for key in results:
            results[key] = str(results[key])
        self.all_results.append(results)

    def test_challenge_1(self):
        self.run_tournament(self.bolt, self.nick, outsider=self.nick)

    def test_challenge_2(self):
        self.run_tournament(self.andrew, self.nick, outsider=self.nick)

    def test_challenge_3(self):
        self.run_tournament(self.bolt, self.andrew, self.nick, outsider=self.nick)

    # Тест на ошибку, когда менее быстрый бегун может оказаться первым
    def test_challenge_4(self):
        self.run_tournament(self.andrew, self.bolt, self.nick, leader=self.bolt)


if __name__ == "__main__":
    unittest.main()
