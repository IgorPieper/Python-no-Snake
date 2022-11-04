def partition(tablica, p, r):
    pivot = tablica[r]
    smaller = p
    for j in range(p, r):
        if tablica[j] <= pivot:
            tablica[smaller], tablica[j] = tablica[j], tablica[smaller]
            smaller = smaller + 1
    tablica[smaller], tablica[r] = tablica[r], tablica[smaller]
    return smaller


def quicksort(tablica, p, r):
    if p < r:
        q = partition(tablica, p, r)
        quicksort(tablica, p, q-1)
        quicksort(tablica, q + 1, r)


tablica = [2, 8, 6, -7, 2, 14, 17, 5]
quicksort(tablica, 0, len(tablica)-1)
print(tablica)
