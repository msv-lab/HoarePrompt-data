def max_aggregate(scores):
    aggregate_scores = {}
    
    for name, score in scores:
        if name in aggregate_scores:
            aggregate_scores[name] += score
        else:
            aggregate_scores[name] = score
            
    max_name = max(aggregate_scores, key=aggregate_scores.get)
    return (max_name, aggregate_scores[max_name])

# Tests
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)]) == ('Juan Whelan', 72)
assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)]) == ('Sabah Colley', 70)
