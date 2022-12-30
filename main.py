if __name__ == '__main__':
    nb_intersec = int(input())
    shortcuts = [int(item) for item in input().split(' ')]
    for i in range(nb_intersec+1):
        for s in range(len(shortcuts)):
            if s == i:
                print(s, end=' ')
                break
    print()