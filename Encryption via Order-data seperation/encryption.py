def fun(a,b,c):
  for i in range(len(a)):
    if a[i]==b and c == 0:
      return i+1
    if a[i]==b and c != 0:
      c-=1
for i in range(int(input())):
  qst=input()
  string = qst.split()
  sorted_string=[]
  for i in range(len(string)):
    sorted_string.append(str(''.join(sorted(string[i]))))
  st = ""
  for i in sorted_string:
    st+=i+" "
  st.strip()
  print(st)
  count=0
  k=0
  for i in range(len(st)):
    if st[i]!=" ":
      if i!=0 and st[i]==st[i-1]:
        count+=1
      else:
        count=0
      print(fun(string[k],st[i],count), end="")
    else:
      print(" ",end="")
      k+=1
