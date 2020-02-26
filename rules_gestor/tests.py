# You can't hide a bad architecture with a great interface - Bob Martin
# The importance of TDD methodology as a pillar for development:
# https://www.youtube.com/watch?v=KtHQGs3zFAM
from django.test import TestCase
from .gamevariant import GameVariant

class RulesGestorExceptions(Enum):
    invalid_move = 'This move does not exist in this game variant'

class RulesGestorTestCase(TestCase):
    """
    Author: johan.ballesteros@outlook.com
    nb: normal behavior
    eb: exception behavior
    """
    def setUp(self):
        easy_game = GameVariant(mode='Easy')
        normal_game = GameVariant(mode='Normal')
        hard_game = GameVariant(mode='Hard')

        moves_tuples_nb = [
            ['Rock','Paper','Player1'],
            ['Scissors','Rock','Player2']            
        ]
        moves_tuples_eb = [
            ['this move does not exist','this move does not exist','None']
        ]

    def test_check_winner_nb(self):
        for move_tuple in self.moves_tuples_nb:
            winner = self.easy_game.test_check_winner(
                player1_move=move_tuple[0],player2_move=move_tuple[1]
            )
            self.assertEqual(winner,move_tuple[2])
    
    def test_check_winner_eb(self):
        for move_tuple in self.moves_tuples_eb:
            with self.assertRaises(Exception) as exception:
                self.easy_game.test_check_winner(
                   player1_move=move_tuple[0],player2_move=move_tuple[1] 
                )
            self.assertEqual(exception.exception.message,RulesGestorExceptions.invalid_move.value)

