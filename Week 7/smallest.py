smallest = None
for num in [7,9,100,453,34,-1,-1000]:
    # "is" should only be used when comparing True, False, and None
    if smallest is None:
        smallest = num
    elif num < smallest: 
        smallest = num
    print(smallest, num)
print("The smallest is: ", smallest)