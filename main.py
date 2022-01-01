import os
import requests


def main():
    id = os.environ.get("ID", 1)
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    print(response)

    
if __name__ == "__main__":
    main()
   
