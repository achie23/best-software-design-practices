from utils import list_functions as ls
from utils import hash_functions as hash
from utils.list_functions import get_max

ht = {"h1":1, "kay":6}
print(hash.max_value(ht))

values = [1,2,3,4,5,6,7,8,9]
print(ls.get_average(values))

print(get_max(values))
