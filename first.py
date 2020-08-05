def repeating(arr,n):
    arr1=[]
    for i in range(0,n):
        arr[arr[i]%n]=arr[arr[i]%n]+n
    for i in range(0,n):
        x=arr[i]//n
        arr1.append(x)
    for i in range(0,n):
        arr[i]=arr[i]%n
    for i in range(0,n):
        if arr1[arr[i]]==1:
            print("First non-repeating element is  ",arr[i])
            break
arr=[3,5,3,4,3,5,6]
n=len(arr)
repeating(arr,n)