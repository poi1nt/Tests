def get_unique_id():
    ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}
    unique_id = set()
    for key in ids:
        unique_id.update(set(ids[key]))
    return list(unique_id)
