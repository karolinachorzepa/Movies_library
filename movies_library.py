from random import randint

class Movies():
    def __init__(self,title,release,genre,watched):
        self.title=title
        self.release=release
        self.genre=genre
        self.watched = watched
    def __str__(self):
        return f"{self.title} was relased in {self.release}"
    def play(self, step=1):
        self.watched += step
    def current_views(self):
        return self.watched
    
class Series(Movies):
  def __init__(self,title,release,genre,episode,season,watched):
    super(self.__class__,self).__init__(title,release,genre,watched)
    self.episode=episode
    self.season=season
    def __str__(self):
        return f"{self.title}\n {self.episode}\n{self.season}\n"


library=[
    Movies(title="Monthy Python", release = 1982, genre="comedy", watched=998),
    Movies(title="Titanic", release=1999, genre="thiller",watched=129),
    Series(title="Dark",release=2017,genre="comedy",episode="E01",season="S02",watched=2789),
    Series(title="Friends",release=1995,genre="comedy",episode="E04",season="S01",watched=27569)
    ]

def top_titles():
    for a,b in enumerate(library):
        if b.watched > 130:
            print(f"{b} with {b.watched} views")
top_titles()
#def generate_views(times=10):
    #generate_views()
def search(library, title):
    for picture in library:
        if picture.title == title:
            return picture

def get_movies():
    for row in library:
        if isinstance (row,Movies):
            print(f"{row.title}")
get_movies()

def get_series():
    for row in library:
        if isinstance (row,Series):
            print(f"{row.title}")
get_series()




print(search(library,"Titanic"))
