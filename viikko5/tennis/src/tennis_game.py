class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def equal_scores(self):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        
        return score
    
    def advantage_or_win(self):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        
        return score

    def score_end(self, score):
        temp_score = 0
        for player_turn in range(1, 3):
            if player_turn == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        
        return score

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.equal_scores()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.advantage_or_win()
        else:
            score = self.score_end(score)

        return score
