# Simple unique ID generator
_id = 1
def generate_id():
    global _id
    current_id = _id
    _id += 1
    return current_id
