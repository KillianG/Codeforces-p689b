if __name__ == '__main__':
    nb_intersec = int(input())
    shortcuts = [int(item) for item in input().split(' ')]
    for i in range(nb_intersec+1):
        nrj = 0
        for s in range(len(shortcuts)):
            if s == i:
                print(nrj, end=' ')
                break
            elif shortcuts[s] <= i:
                s = shortcuts[s]
            nrj += 1
    print()