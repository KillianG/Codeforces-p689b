def distance(start, arrival):
    return abs(start - arrival)

def mike_shortcut(nb_intersec, shortcuts):
    for i in range(1, nb_intersec+1):
        nrj = 0
        s = 1
        while s != i :
            nrj+=1
            if distance(s, i) > distance(shortcuts[s-1], i):
                s = shortcuts[s]
                continue
            if (s > i):
              s -= 1
            else:
              s += 1
        print(nrj, end=' ')
    print()


if __name__ == '__main__':
    nb_intersec = int(input())
    shortcuts = [int(item) for item in input().split(' ')]
    mike_shortcut(nb_intersec, shortcuts)