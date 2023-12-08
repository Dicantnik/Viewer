import random
import string

def generate_random_code():
    
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(6)))

    return result_str