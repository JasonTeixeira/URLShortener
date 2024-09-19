import random
import string

def generate_random_url():
    # Define possible domain and path characters
    letters = string.ascii_lowercase
    domains = ['.com', '.net', '.org', '.io', '.gov']
    
    # Generate a random domain name (e.g., www.something.com)
    domain_length = random.randint(20, 25)
    domain_name = ''.join(random.choice(letters) for _ in range(domain_length))
    
    # Randomly choose a top-level domain
    domain_extension = random.choice(domains)
    
    # Generate a random path (e.g., /path/to/resource)
    path_length = random.randint(20, 25)
    path = ''.join(random.choice(letters) for _ in range(path_length))
    
    # Construct the full URL
    random_url = f'https://www.{domain_name}{domain_extension}/{path}'
    
    return random_url

# Test the random URL generator
if __name__ == '__main__':
    for i in range(5):  # Generate 5 random URLs
        print(generate_random_url())
