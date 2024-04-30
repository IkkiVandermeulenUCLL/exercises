def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year==year]

def movies_with_actor(movies, actor):
    return [movies.title for movie in movies if actor in movie.actors]

def devisors(n):
    return [i for i in range(0,n) if n%i==0]