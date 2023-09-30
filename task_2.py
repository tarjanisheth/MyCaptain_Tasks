fn=[0,1]
n=int(input("Enter the length of list needed:"))
for i in range(n-2):
          fn.append(fn[i]+fn[i+1])
          print(fn)