class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scores = {}
        self.scores[player1_name] = 0
        self.scores[player2_name] = 0
        self.players = [player1_name, player2_name]
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        self.scores[player_name] += 1
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def _even_scores(self):
        return self.scores[self.players[0]] == self.scores[self.players[1]]

    def _find_name_for_even(self):
        return ""
        
    def get_score(self):
        if self._even_scores():
            return self._find_name_for_even()
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All"
            elif self.m_score1 == 1:
                score = "Fifteen-All"
            elif self.m_score1 == 2:
                score = "Thirty-All"
            elif self.m_score1 == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
