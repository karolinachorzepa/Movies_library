class Library():
    def __init__(self,title,release,genre,watched):
        self.title=title
        self.release=release
        self.genre=genre
        self.watched = watched
    def __str__(self):
        return f"{self.title} was relased in {self.watched}"
movie1=Library("Monthy Python", 1982, "comedy",998)
movie2=Library("Titanic", 1999, "thiller",129)
movie3=Library("Park", 2001, "horror",4521)
movie4=Library("Parasite", 2018, "thiller",3699)
print(movie2)
