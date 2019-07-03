def binarySearch(sorted_list, length, key):
    start = 0
    end = length-1
    while start<=end:
        mid= int((start+end)/2)
        if key==sorted_list[mid]:
            print("Item is at position",mid)
            break
        elif key<sorted_list[mid]:
            end= mid-1
        elif key>sorted_list[mid]:
            start=mid+1
    else:
        print("\n Element not found")
    return -1
list_to_search = []
n=int(input("Enter Size:"))
for i in  range(n):
    number= int(input("Enter Number:"))
    list_to_search.append(number)
list_to_search.sort()
print('\n\nThe list will be sorted, the sorted list is:', list_to_search)

key = int(input("\nEnter the number to search: "))

binarySearch(list_to_search,n,key)

