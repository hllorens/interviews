# x-y=k  or y=x-k
def find_all_pairs(arr,k):
  print(f'\ninput={arr},k={k}')
  store={}
  ret=[]
  # store key=element_value value=position of an element that would pair with it
  # e.g., 17 -> position 0 (which is 4)
  for xi in range(len(arr)):
    store[arr[xi]-k]=arr[xi]
  print(f'store={store}')
  # find pair
  for yi in range(len(arr)):
    if(arr[yi] in store):
      ret.append([store[arr[yi]],arr[yi]])
    else:
      print(str(yi)+': no pair for '+str(arr[yi]))
  return ret




# x + y = k or y= k - x
def find_a_pair(arr,k):
  store={}
  # store key=element_value value=position of an element that would pair with it
  # e.g., 17 -> position 0 (which is 4)
  for xi in range(len(arr)):
    store[k-arr[xi]]=xi
  print(store)
  # find pair
  for yi in range(len(arr)):
    if(arr[yi] in store and not arr[yi]==yi):
      return [store[arr[yi]],yi]
    else:
      print(str(yi)+': no pair for '+str(arr[yi]))
  return []


print(find_a_pair([4, 6, 10, 15, 16],21))
print(find_all_pairs([0, -1, -2, 2, 1],1))



