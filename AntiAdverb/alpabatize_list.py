from list import alist

'''
Quick and dirty tool to alphabetize the manual alist and ensure uniqueness.
NOTE: Code won't work if list.py is open.
'''


def main():
    new_list = set(alist)
    with open('list.py', 'wt') as file:
        file.write("alist = [\n")
        for line in sorted(new_list):
            file.write("    '{}',\n".format(line))
        file.write("    ]\n")
        print("Done")


if __name__ == '__main__':
    main()
