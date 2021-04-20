

class Search:

    def linear_search(self, target, arr):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
            
        return -1

    # print(linearSearch(23, [4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1]))

    def binary_search(self, arr, target):
        lower = 0
        upper = len(arr)

        # print("LOWER:" + str(lower))
        # print("UPPER:" + str(upper))

        while lower <= upper:
            mid = int((lower + upper) / 2)
            # print("MID:" + str(mid))
            if arr[mid] == target:
                return mid        
            elif arr[mid] < target: # Search right sub-list.
                lower = mid + 1
                # print("Upper" + str(upper))
            else: # Search left sub-list.
                upper = mid - 1
                # print("Lower:" + str(lower))
        
        return -1

    def binary_search_rec(self, arr, target):
        mid = len(arr) // 2
        print("MID: " + str(mid))
        print(arr)
        print("LENGTH: " + str(len(arr)))
        if len(arr) == 0:
            return -1
        elif arr[mid] == target:
            print("TARGET")
            return 0
        elif target < arr[mid]:
            print("LEFT")
            print(arr[:mid])
            return self.binary_search_rec(arr[:mid], target)
        else:
            print("RIGHT")
            print(arr[mid:])
            return self.binary_search_rec(arr[mid + 1:], target)

    # sorted = sorting.insersionSort([4, 6, 3, 6, 8, 23, 6, 2344, 743, 23, 1])
    # print(binarySearch(sorted, 743))
