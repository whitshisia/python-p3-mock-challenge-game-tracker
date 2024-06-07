class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if len(title) == 0:
            raise ValueError("Title must be longer than 0 characters")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result")
        self._results.append(result)

    def results(self):
        return self._results

    def players(self):
        players = {result.player for result in self._results}
        return list(players)
    
    def average_score(self, player):
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player")
        scores = [result.score for result in self._results if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return 0.0
class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be of type str")
        if not (2 <= len(username) <= 16):
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be of type str")
        if not (2 <= len(new_username) <= 16):
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self._username = new_username

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result")
        self._results.append(result)

    def results(self):
        return self._results

    def games_played(self):
        games = {result.game for result in self._results}
        return list(games)
    def has_played(self, game):
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")
        return any(result.game == game for result in self._results)

    def times_played(self, game):
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")
        return sum(1 for result in self._results if result.game == game)

    def average_score(self, game):
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")
        scores = [result.score for result in self._results if result.game == game]
        if scores:
            return sum(scores) / len(scores)
        return 0.0
class Result:
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("Player must be an instance of Player")
        if not isinstance(game, Game):
            raise TypeError("Game must be an instance of Game")
        if not isinstance(score, int):
            raise TypeError("Score must be of type int")
        if not (1 <= score <= 5000):
            raise ValueError("Score must be between 1 and 5000, inclusive")
        self._player = player
        self._game = game
        self._score = score
        player.add_result(self)  
        game.add_result(self)    

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game
