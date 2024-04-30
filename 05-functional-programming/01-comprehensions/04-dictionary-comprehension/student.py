def title_to_director(movies):
    return {movie.title : movie.director for movie in movies}

def director_to_titles(movies):
    return {
        director : [movie.title for movie in movies]
        for director in {movie.director for movie in movies}
    }