def movie_count(movies, director):
    return sum([movie for movie in movies if director == movie.director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if movie.actor == actor])

def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)

def is_prime(n):
    return not any(i for i in range(0,n) if n%i==0)

def is_increasing(ns):
    return not any(x>y for x,y in zip(ns, ns[1:]))

def count_matching(xs,ys):
    return sum(1 for x,y in zip(xs,ys) if x==y)

def weigted_sum(ns, weight):
    return sum(x*y for x,y in zip(weight))

def alternating_caps(string):
    chars = [value.upper() if index%2==0 else value.lower() for index, value in enumerate(string) ]
    return "".join(chars)

def find_repeated_words(string):
    return {y.replace(".", "").lower() for x,y in zip(string.split(), string.split()[1:]) if x.replace(".","").lower()==y.replace(".","").lower()}

print(find_repeated_words("this sentence has has repeated words. Words."))
print(alternating_caps("abcabc"))

