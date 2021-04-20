class Sort:
    def selectionSort(self, arr):
        length = len(arr)
        
        for i in range(length):
            indexSmallest = i # Index of the start of the unsorted part of the array.
            for j in range(i + 1, length):
                if arr[j] < arr[indexSmallest]:
                    indexSmallest = j
            
            if indexSmallest != i:
                arr = self.swap(indexSmallest, i, arr)

        return arr
                


    def swap(self, index1, index2, arr):
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp
        return arr


    # print(selectionSort([4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1]))

    def bubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr = self.swap(j, j + 1, arr)

        return arr

    # print(bubbleSort([4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1]))

    def bubbleSortImproved(self, arr):
        flag = False
        length = len(arr)
        while not flag:
            flag = True
            for j in range(length - 1):
                if arr[j] > arr[j + 1]:
                    flag = False
                    arr = self.swap(j, j + 1, arr)

            length = length - 1

        return arr

    # print(bubbleSortImproved([4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1]))

    def insersionSort(self, arr):
        for i in range(len(arr)):
            itemToInsert = arr[i] # Copy of next item to be inserted.
            indexHole = i # Index of hole where item to be inserted was.

            # Locate where to insert the item within the sorted part of the list.
            while indexHole > 0 and arr[indexHole - 1] > itemToInsert:
                arr[indexHole] = arr[indexHole - 1]
                indexHole = indexHole - 1

            arr[indexHole] = itemToInsert

        return arr

    # print(insersionSort([4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1]))


    def merge_sort(self, arr):

        if len(arr) <= 1:
            return arr

        l_arr = arr[:len(arr) // 2]
        r_arr = arr[len(arr) // 2:]
        print("LEFT: " + str(l_arr))
        print("RIGHT: " + str(r_arr))
            
        left = self.merge_sort(l_arr)
        right = self.merge_sort(r_arr)
        return self.merge(left, right)

    def merge(self, arr_a, arr_b):
        results = []
        index_a = 0
        index_b = 0
        # Loop through each element and compare and append to results 
        # accordingly.
        while index_a < len(arr_a) and index_b < len(arr_b):
            if arr_a[index_a] < arr_b[index_b]:
                results.append(arr_a[index_a])
                index_a += 1
            else:
                results.append(arr_b[index_b])
                index_b += 1
        
        # If all elements in one list has been added into resutls 
        # then just add rest of other array to end.
        if index_a == len(arr_a):
            results.extend(arr_b[index_b:])
        else:
            results.extend(arr_a[index_a:])
        
        print("SORTED_SUB: " + str(results))
        return results


    # print("SORTED: " + str(merge_sort([44, 67, 12, 19, 34, 27, 87, 12])))
    # print(merge([44, 67], [12, 19]))

    def quick_sort(self, arr):
        length = len(arr)
        if length <= 1:
            return arr
        else:
            pivot = arr.pop()
        
        items_greater = []
        items_lower = []

        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)