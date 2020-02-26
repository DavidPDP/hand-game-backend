# This Python script represents the communication interface 
# of this subsystem with the entire environment, where the other 
# subsystems are located. Initially, this script uses the 
# facade pattern but if its complexity increases, this pattern 
# is preserved and the adapter patterns or others would possibly be added.
import asyncio
from .match import Match
from rules_gestor import gamevariant as rules_gestor_gamevariant


def get_game_multimedia_api(mode: str) -> rules_gestor_gamevariant.OutputGameMultimediaDTO:
    return rules_gestor_gamevariant.get_game_multimedia(mode=mode)

def get_match_winner_api(match: Match) -> str:
    gamevariant = rules_gestor_gamevariant.get_game_variant(mode=match.game_type)
    return gamevariant.check_winner(
        player1_move=match.player1_move,player2_move=match.player2_move
    )