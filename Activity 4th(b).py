# binary search
myList = [1,2,3,4,5,6]
start = 0
end = len(myList)-1
x = int(input("Enter the value : "))

while start <= end:

        mid = start + (end - start)//2

        if myList[mid] == x:
            print("Element found at index :",mid)
            break

        elif myList[mid] < x:
            start = mid + 1

        else:
            end = mid - 1

if myList[mid] != x:
    print("Element not found in the list")