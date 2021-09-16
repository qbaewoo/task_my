def swap(m,i,j):
  temp=m[i]
  m[i]=m[j]
  m[j]=temp

def perm(ch, crt_ind=0):
  if crt_ind == len(ch)-1:
    print(''.join(ch))
  for i in range(crt_ind, len(ch)):
    swap(ch, crt_ind, i)
    perm(ch, crt_ind+ 1)
    swap(ch, crt_ind, i)
 
 
if __name__== '__main__':
  a = ['a','b','c']
  ret=perm(a)