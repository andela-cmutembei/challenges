import sys

if __name__ == "__main__":
    input = sys.argv[1]
    with open(input) as problem:
        for index, line in enumerate(problem):
            if index:
                something = line.strip().split(' ')
                with open("output.txt", "a") as solution:
                    solution.write("Case #{0}: {1}\n".format(index, ' '.join(something[::-1])))
