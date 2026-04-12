from code_clemsou import insertion_sort, bubble_sort, selection_sort
import time
# Comparer les temps d'exécution des trois algorithmes de tri avec la fonction time.time() pour mesurer le temps avant et après l'exécution de chaque tri, puis afficher les résultats. ces algorithmes de tris.
for i in range(10):
    start = time.time()
    insertion_sort([5, 2, 8, 1, 9, 3, 7, 4, 6, 0, 12, 11, 10, 15, 14, 13, 20, 19, 18, 17, 16, 25, 24, 23, 22, 21, 30, 29, 28, 27, 26, 35, 34, 33, 32, 31, 40, 39, 38, 37, 36, 45, 44, 43, 42, 41, 50, 49, 48, 47, 46])
    end = time.time()
    print("Insertion Sort Time:", end - start)
    
    start = time.time()
    bubble_sort([5, 2, 8, 1, 9, 3, 7, 4, 6, 0])
    end = time.time()
    print("Bubble Sort Time:", end - start)
    
    start = time.time()
    selection_sort([5,2 ,8 ,1 ,9 ,3 ,7 ,4 ,6 ,0])
    end = time.time()
    print("Selection Sort Time:", end - start)



#start = time.time()
#bubble_sort  ([5, 2, 8, 1, 9, 3, 7, 4, 6, 0, 12, 11, 10, 15, 14, 13, 20, 19, 18, 17, 16, 25, 24, 23, 22, 21, 30, 29, 28, 27, 26, 35, 34, 33, 32, 31, 40, 39, 38, 37, 36, 45, 44, 43, 42, 41, 50, 49, 48, 47, 46])
#end = time.time()
#print(end - start)