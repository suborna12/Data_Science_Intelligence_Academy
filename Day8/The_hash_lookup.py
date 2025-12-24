class HashSet:
    def __init__(self, total_buckets=10):
        self.total_buckets = total_buckets
        self.buckets = [None] * total_buckets

    def add(self, value):
        index = calculate_hash(value) % self.total_buckets
        self.buckets[index] = value


# Hash function
def calculate_hash(value):
    return hash(value)

def set_contains(set, target):
    hash_value = calculate_hash(target)
    bucket_index = hash_value % set.total_buckets
    memory_slot = set.buckets[bucket_index]
    if memory_slot == target:
        return True
    else:
        return False

list_n = list(range(-1000, 1000))
set_n = set(list_n)
print(set_contains(set, -5))

    