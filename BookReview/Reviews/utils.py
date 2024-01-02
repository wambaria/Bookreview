def average_rating(ratings_list):
    if not ratings_list:
        return 0
    return round(sum(ratings_list)/len(ratings_list))