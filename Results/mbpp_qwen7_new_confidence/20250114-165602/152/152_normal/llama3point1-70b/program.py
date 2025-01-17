def max_aggregate(tuples):
    aggregate_dict = {}
    for name, score in tuples:
        if name in aggregate_dict:
            aggregate_dict[name] += score
        else:
            aggregate_dict[name] = score
    max_name = max(aggregate_dict, key=aggregate_dict.get)
    return (max_name, aggregate_dict[max_name])
