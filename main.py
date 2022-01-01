import os


def main():
	one = os.environ.get("INPUT_ONE")
	two = os.environ.get("INPUT_SECOND")
    print("Show message on the stdout")
    print(one, two)

    
if __name__ == "__main__":
    main()
   
