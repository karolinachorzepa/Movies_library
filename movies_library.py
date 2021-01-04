class Library():
    def __init__(self,title,release,genre,watched):
        self.title=title
        self.release=release
        self.genre=genre
        self.watched = watched
    def __str__(self):
        return f"{self.title} was relased in {self.watched}"
    def play(self):
        return self.watched + 1
movie1=Library("Monthy Python", 1982, "comedy",998)
movie2=Library("Titanic", 1999, "thiller",129)
movie3=Library("Park", 2001, "horror",4521)
movie4=Library("Parasite", 2018, "thiller",3699)
print(movie2)
class Series():
    def __init__(self, title, release, genre, episode, season, watched):
        self.title=title
        self.release=release
        self.genre=genre
        self.episode=episode
        self.season=season
        self.watched = watched
    def __str__(self):
        return f"{self.title} {self.episode}{self.season}"
Se1 = Series("Dark",2017,"comedy","E01","S02",2789)
Se2 = Series("Adnie",2013,"comedy","E01","S02",111)
Se3 = Series("Friends",1995,"comedy","E04","S01",27569)

library=[
    ("Movie 1"),("Monthy Python"), ("release",1982), ("genre","comedy"),("watched",998),
    ("Movie 2"),("Titanic"), ("release",1999), ("genre","romantic thiller"),("watched",239),
    ("Movie 3"),("Park Southern"), ("release",2014), ("thiller"),("watched",34),
    ("Movie 4"),("Forrest Gump"), ("release",1994), ("comedy"),("watched",2978),
    ("Serial 1"),("Dark"), ("release",2017), ("comedy"),("watched",998),("episode","E01"),("season","S02"),("watched",2789),
    ("Serial 2"),("Friends"), ("release",1998), ("comedy"),("watched",998),("episode","E01"),("season","S02"),("watched",234),
    ("Serial 3"),("Anie"), ("release",2017), ("comedy"),("watched",789),("episode","E02"),("season","S04"),("watched",564),
    ("Serial 4"),("Queen"), ("release",2015), ("comedy"),("watched",12345),("episode","E01"),("season","S07"),("watched",349077),
]


print(type(library))
print(movie3.play())
print(movie3)
print(Se1)
