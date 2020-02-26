# This Python script represents decoupling between the persistence layer 
# and the business layer, through the repository pattern. Do not try to do 
# everything in a single database call, follow the single responsibility principle. 
# Feel free to make as many calls as you need (no matter if repeated), 
# but as long as cohesion increases.
from .dtos import OutputGameMultimediaDTO
from .models import Rules, Modes

def get_game_variant_multimedia(mode: str) -> OutputGameMultimediaDTO:
    """
    Author: johan.ballesteros@outlook.com
    Creates a DTO that allows to encapsulate multimedia resources 
    that the user needs to interact with the game variant.
    """
    moves_query = Rules.objects.filter(mode__name=mode).distinct('winner__name')
    moves_urls = moves_query.values('winner__name','winner__image_url')

    game_query = Modes.objects.filter(name=mode)
    game_url = game_query.values('image_url')[0]['image_url']

    # Create DTO object (business object)
    game_dto = OutputGameMultimediaDTO().dump(dict(url=game_url,moves=moves_urls))
    
    return game_dto

def get_game_variant_rules(mode: str) -> dict:
    """
    Author: johan.ballesteros@outlook.com
    Creates a dictionary that maps the rules of the game variant 
    as follows: move1-move2 -> True. This allows to consult the tuple 
    of players movements. In case the tuple exists, who made the move1 won. 
    Otherwise, if the tuple don't found who made the move1 lost. 
    This is possible because the dictionary stores winning movements tuples.
    """
    moves_query = Rules.objects.filter(mode__name=mode).distinct('winner__name')
    moves_urls = moves_query.values('winner__name','loser__name')

    # Create Dict object (business object)
    rules_dict = {'%s-%s' %(rule['winner__name'],rule['loser__name']):True for rule in moves_urls}
    return rules_dict
    