def find_object_by_id(id, object_list):
    return next((obj for obj in object_list if obj["id"] == id), None)