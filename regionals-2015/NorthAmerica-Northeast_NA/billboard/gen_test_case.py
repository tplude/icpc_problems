
import sys
import random
import time

def gen_new_testcase():
    random.seed(time.time())
    num_boards = random.randint(0,5000)
    print(num_boards)
    for b in range(num_boards):
        width = random.randint(0,30000)
        height = random.randint(0,30000)
        print("{} {}".format(width,height))

def main():
    number_tests = int(sys.argv[1])
    print(number_tests)
    for n in range(number_tests):
        gen_new_testcase()

if __name__ == '__main__':
    main()
