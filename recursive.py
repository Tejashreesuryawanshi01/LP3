step_count=0
def recursive (n):
    global step_count
    step_count +=1
    if n<=1:
        return n
    return recursive(n-1)+recursive(n-2)
n=int(input("enter fibonacci "))
result=recursive(n)
print(f"recursive number:{result}")
print(f"Stepcount number:{step_count}")