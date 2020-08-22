pos = 0
def search(list, n):
  for i in range(len(list)-1):
    if list[i] == n:
      globals()['pos'] = i
      return True
        
  return False
  
list = [22,11,99,44,55,66,77,33,88]
n = 77
if search(list, n):
  print("Found at ",pos)
else:
  print("Not Found")
