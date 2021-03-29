import numpy as np

def InputFile():
   f = open("MyTextIn.txt")
   lst = []
   for line in f:
       strs = line.split(' ')
       for s in strs:
           if s != ' ':
               lst = lst + [int(s)]
   n = int(lst[0])
   k = int(lst[1])
   array = np.zeros((n, k), dtype=int)
   t = 2
   for i in range(n):
       num = int(lst[t])
       t += 1
       for j in range(k):
           array[i][j] = lst[t]
           t += 1
   f.close()
   return n, k, array

def OutputFile(result, x, n):
   f = open("MyTextOut.txt", 'wt')
   x += 1
   s = str(x) + '\n'
   f.write(s)
   for i in range(1, n):
       s1 = str(result[i][0])
       s2 = str(result[i][1])
       f.write(s1 + ' ' + s2 + '\n')

def SortAndCountInver(A):
   n = len(A)
   if n == 1:
       return A, 0;
   else:
       L = A[:int(len(A) / 2)]
       R = A[int(len(A) / 2):]
       L, x = SortAndCountInver(L)
       R, y = SortAndCountInver(R)
       A, z = MergeAndCountSplitInv(A, L, R)
       return A, x + y + z

def MergeAndCountSplitInv(A, L, R):
   c = []
   i = 0
   j = 0
   z = 0
   while i < len(L) and j < len(R):
       if L[i] <= R[j]:
           c.append(L[i])
           i += 1
       else:
           c.append(R[j])
           j += 1
           z += (len(L) - i)
   c = c + L[i:]
   c = c + R[j:]
   return c, z;

def InSorter(array, x, n, k):
   for i in range(k):
       for j in range(k-i-1):
           if array[x][j] > array[x][j+1]:
               for t in range(n):
                   array[t][j], array[t][j+1] = array[t][j+1], array[t][j]
   return array

def OutSorter(result, n):
   for i in range(n):
       for j in range(n - i - 1):
           if result[j][1] > result[j + 1][1]:
               result[j][1], result[j + 1][1] = result[j + 1][1], result[j][1]
               result[j][0], result[j + 1][0] = result[j + 1][0], result[j][0]
   return result

def Counter(array, x, n, k):
   array = InSorter(array, x, n, k)
   result = np.zeros((n, 2), dtype=int)
   t = 0
   for i in range(n):
       if i != x:
           t += 1
           result[t][0] = i+1
           mas = array[i]
           A, result[t][1] = SortAndCountInver(list(mas))
   result = OutSorter(result, n)
   OutputFile(result, x, n)

n, k, array = InputFile()
x = int(input("Choose the User to be compared:"))
x -= 1
Counter(array, x, n, k)

