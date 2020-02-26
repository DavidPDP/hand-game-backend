# You could think of a prototype pattern for matches objetcs, 
# but from the business concept each match is unique. 
# In case the users decide to rematch, system can reuse the same 
# current match object and clear the playing fields 
# (see the Match's rematch method).
import datetime
import uuid

class Player:
    """
    Author: johan.ballesteros@outlook.com
    Represents a player (business object) who is will to play.
    """
    def __init__(self,id: str):
        self.id = id
        self.score = 0
        self.active = True
    
    def win(self):
        self.score = self.score + 1
    
    def lose(self):
        self.score = self.score - 1
    
    def in_game(self):
        self.active = False
    
    def free(self):
        self.active = True

class Match:
    """
    Author: johan.ballesteros@outlook.com
    Represents a match (business object) which contains 
    the game logic and data.
    """
    def __init__(self,player1: Player, game_type: str):
        self.id = str(uuid.uuid4())
        self.game_type = game_type
        self.player1 = player1
        self.player2 = None
        self.player1_move = None
        self.player2_move = None
        self.winner = None
        self.start = datetime.datetime.now()
        self.end = None

    def register_player2(self, player2: Player):
        self.player2 = player2
    
    def register_player_move(self, player: Player, move: str):
        if self.player1 == player:
            self.player1_move = move
        else:
            self.player2_move = move

    def is_match_completed(self) -> bool:
        return True if (self.player1_move != None and self.player2_move != None) else False

    def finish(self, winner):
        self.end = datetime.datetime.now()
        self.winner = winner
    
    def rematch(self):
        self.player1_move = None
        self.player2_move = None
        self.winner = None
        self.start = datetime.datetime.now()
        self.end = None

class MatchFactory():
    """
    Author: johan.ballesteros@outlook.com
    Represents a factory of matches. The factory pattern applies correctly here, 
    this is because the matches are a critical business object of future analysis. 
    In the future, different types of match can be segregated, making this object 
    creation more complex. Thus, applying this pattern allows to comply with the 
    open-closed principle.
    """
    def create_match(self,player1: Player, game_type: str) -> Match:
        return Match(player1=player1,game_type=game_type)

# init players and matches in the system
matches = {}
players = {}

# init factory
macth_factory = MatchFactory()

def get_match(id: uuid) -> Match:
    try:
        return matches[id]
    except KeyError as exception:
        raise Exception('This match does not exist')

def create_match(player1: Player, game_type: str) -> str:
    new_match = macth_factory.create_match(player1=player1,game_type=game_type)
    matches[new_match.id] = new_match
    return str(new_match.id)

def join_match(player2: Player, match: Match):
    matches[match.id].register_player2(player2)

def get_player(id: str):
    try:
        return players[id]
    except KeyError as exception:
        raise Exception('This player does not exist')

def create_player(id: str):
    new_player = Player(id=id)
    players[new_player.id] = new_player
