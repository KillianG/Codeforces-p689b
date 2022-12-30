def distance(start, arrival):
    return abs(start - arrival)

def mike_shortcut(nb_intersec, shortcuts):
    for i in range(1, nb_intersec+1):
        nrj = 0
        s = 1
        while s != i :
            nrj+=1
            if distance(s, i) > distance(shortcuts[s-1], i):
                s = shortcuts[s-1]
                continue
            if (s > i):
              s -= 1
            else:
              s += 1
        print(nrj, end=' ')
    print()


if __name__ == '__main__':
    nb_intersec = 98 #int(input())
    shortcuts = [int(item) for item in "17 17 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 57 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 87 90 90 90 90 90 90 90 90 90 90 90 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 92 95 95 95 95 95 97 98 98".split(' ')] #[int(item) for item in input().split(' ')]
    mike_shortcut(nb_intersec, shortcuts)
    mike_shortcut(7, [4, 4, 4, 4, 7, 7, 7])