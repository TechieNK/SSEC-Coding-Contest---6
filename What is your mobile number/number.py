a = []
for i in range(int(input())):
  a.append(input())
for i in a:
  if len(i)!=10 or i[0]=='0' or i<'1000000000':
    print("NO")
  else:
    print("YES")
