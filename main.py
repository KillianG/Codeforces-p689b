if __name__ == '__main__':
    nb_intersec = int(input())
    shortcuts = [int(item) for item in input().split(' ')]
    for i in range(1, nb_intersec+1):
        nrj = 0
        s = 1
        while s <= len(shortcuts):
            if s >= i:
                print(nrj, end=' ')
                break
            nrj+=1
            if shortcuts[s-1] <= i and shortcuts[s-1] > s:
                s = shortcuts[s]
                continue
            s+=1
    print()