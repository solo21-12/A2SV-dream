for _ in range(int(input())):
    duration, max_quests = map(int, input().split())
    skiing = list(map(int, input().split()))
    movie = list(map(int, input().split()))
    
    total_exp = 0
    max_exp = 0
    max_movie_friends = 0
    
    for day in range(duration):
        if max_quests == day:
            break
        
        total_exp += skiing[day]
        max_movie_friends = max(max_movie_friends, movie[day])
        max_exp = max(max_exp, total_exp + (max_quests - day - 1) * max_movie_friends)
    
    print(max_exp)
