def GetByTitle(type, title):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type': type,
        'search': title,
        'page': 1,
        'perPage': 10
    }
    return variables
