def GetByStudio(studioName):
    variables = {
        'search': studioName,
        'page': 1,
        'perPage': 10
    }
    return variables
