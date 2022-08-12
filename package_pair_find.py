# x-y=k  or y=x-k
def find_all_pairs(arr,k):
  return []
# x + y = k or y= k - x
def find_a_pair(arr,k):
  store={}
  # store
  for xi in range(len(arr)):
    #if(store
    store[k-arr[xi]]=xi
  for yi in range(len(arr)):
    if(arr[yi] in store and not arr[yi]==yi):
      return [store[arr[yi]],yi]
  return []


print(find_a_pair([4, 6, 10, 15, 16],21))

