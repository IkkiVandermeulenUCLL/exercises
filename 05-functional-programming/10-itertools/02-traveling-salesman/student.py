from itertools import permutations,pairwise

def find_shortest_path(distance, city_count):
    def total_distance(path):
        return sum(distance(a,b) for a,b in pairwise(path))
    
    paths = ([0, *comb, 0] for comb in permutations(range(1,city_count)))
    return min(paths, key=total_distance)
