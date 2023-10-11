class player:

  def play(self):
    print("The player is playing cricket")


class Batsman(player):

  def play(self):
    print("The same bastman is batting")


class Bowler(player):

  def play(self):
    print("The boeler is bowling")


batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
