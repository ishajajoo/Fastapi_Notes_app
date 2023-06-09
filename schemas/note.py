def noteEntity(item):
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc" : item["desc"],
        "important" : item["important"]
    }

def notesEntity(items):
    return [noteEntity(item) for item in items]