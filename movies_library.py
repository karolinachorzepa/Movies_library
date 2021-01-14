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


def search(library, title):
    for picture in library:
        if picture.title == title:
            return picture
print(search(library,"Titanic"))

def get_movies():
    for row in library:
        if type(row) == Movies:
            print(f"{row.title}")
get_movies()
#type to jest konkretna klasa 
def get_series():
    for row in library:
        if type(row) == Series:
            print(f"{row.title}")
get_series()


def top_titles():
    for v in library:
        if v.watched > 0:
            print(f"{v} with {v.watched} views")
            
top=sorted(library, key = lambda x: x.watched)[::3]

def generate_views(times = 10):
    for i in range(times):
        index = random_element()
        add_views(index)
        current_views = library[index].current_views
        title = library[index].title
        print(f"View generated for {title} ({current_views})")

def random_element():
    elements =len(library) 
    return randint(0, elements-1)

def add_views(index):
    views = randint(1,100)
    return library[index].play(views)

generate_views()
