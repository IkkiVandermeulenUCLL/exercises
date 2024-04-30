def directors(movies):
    return {movie.director for movie in movies}

def common_elemnts(xs, ys):
    return {n for n in xs if n in ys}