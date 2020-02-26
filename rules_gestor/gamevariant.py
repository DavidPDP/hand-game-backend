# This Python script represents the valid instances of the game 
# variants (through the singleton pattern). For this first sprint 
# they're created statically, but the code allows the extension to 
# make them lazy objects with expiration time for variants that aren't by default.
from .dtos import OutputGameMultimediaDTO
from .repository import get_game_variant_rules, get_game_variant_multimedia
import asyncio

class GameVariant:
    """
    Author: johan.ballesteros@outlook.com
    Represents a game variant (business object) that allows 
    to global manage rules and resources when a match instance is created.
    """
    def __init__(self,mode):
        self.mode = mode
        self.multimedia = get_game_variant_multimedia(mode)
        self.rules = get_game_variant_rules(mode)

    def mode(self):
        return self.mode

    def multimedia(self):
        return self.multimedia

    def check_winner(self,player1_move: str,player2_move: str) -> str:
        """
        Verifies who has the winning movement, according to 
        the rules of the game variant.
        """
        winner = ''
        move_tuple = '%s-%s' % (player1_move,player2_move)
        
        if move_tuple in self.rules:
            winner = 'Player 1'
        else:
            winner = 'Player 2'
            
        return winner

# init default games variant
games_variant = {}
games_variant['Easy'] = GameVariant(mode='Easy')
games_variant['Normal'] = GameVariant(mode='Normal')
games_variant['Hard'] = GameVariant(mode='Hard')

def get_game_variant(mode: str) -> GameVariant:
    return games_variant[mode]

def get_game_multimedia(mode: str) -> OutputGameMultimediaDTO:
    return games_variant[mode].multimedia
