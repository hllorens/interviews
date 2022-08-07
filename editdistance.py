'''
Edit distance between 2 rand strings
a=[h,e,c,t,o,r]
b=[m,o,n]
result=-h + m la o coincide bla bla
'''

def editDistance(a,b):
  #print('call with a='+a+' b='+b)
  edits=0
  result=""
  if(len(a)==0):
    #print('basecase a')
    result=b
    edits=len(b)
  elif(len(b)==0):
    #print('basecase b')
    result=a
    edits=len(a)
  else:
    if(a[0]==b[0]):
      (edits,result)=editDistance(a[1:],b[1:])
      result=a[0]+result
    else:
      #complex recursion: see if it is better to add or to remove
      (edits_remove,result_remove)=editDistance(a[1:],b)
      (edits_add,result_add)=editDistance(a,b[1:])
      if(edits_remove<=edits_add):
        result="-"+a[0]+result_remove
        edits=edits_remove+1
      else:
        result="+"+b[0]+result_add
        edits=edits_add+1

  return (edits,result)

a='ab'
b='acc'
print('a='+a+' b='+b+' res='+str(editDistance(a,b)))
print()
a='ab'
b='acb'
print('a='+a+' b='+b+' res='+str(editDistance(a,b)))
print()
a='abab'
b='acacb'
print('a='+a+' b='+b+' res='+str(editDistance(a,b)))
print()









