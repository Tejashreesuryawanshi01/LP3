def fibonacci_iterative(n):
    step_count=0
    a,b=0,1
    for i in range(n):
         step_count +=1
         a,b=b,a+b
    return a, step_count
n=int(input("enter value of n:"))
result,step_count=fibonacci_iterative(n)

print(f"iterative number:{result}")
print(f"stepcount:{step_count}")

