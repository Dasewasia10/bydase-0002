def GetByID(type, id):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type': type,
        'id': id,
        'page': 1,
        'perPage': 10
    }
    return variables
