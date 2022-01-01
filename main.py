import os


def main():
    one = os.environ.get("ONE")
    two = os.environ.get("SECOND")
    print("Show message on the stdout")
    print(one, two)

    
if __name__ == "__main__":
    main()
   
