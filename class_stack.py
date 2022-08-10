class Stack:
  value=None
  pointer=None
  def __init__(self, v=None, p=None):
    self.value=v
    self.pointer=p

  def link(self,p):
    if isinstance(p,Stack):
      self.pointer=p
    else:
      print('Error linking')
  def hasPointer(self):
    if self.pointer is None:
      return 'False'
    return 'True'

  def __str__(self):
    return 'value='+str(self.value)+' pointer='+self.hasPointer()

  def pop(self):
    v=self.value
    if self.pointer is not None:
      self=self.p
    return v

s=Stack()
print(s)
s.value='2'
print(s)
sParent=Stack('1')
s.link(sParent)
print(s)
s.pop()
print(s)

