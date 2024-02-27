n = int(input())
ans = [[0 for _ in range(n)] for __ in range(n)]

p = 1
k = 0
while p < n*n:
    k += 1
    for j in range(k-1, n-k+1):
        ans[k-1][j] = p
        p += 1
    for j in range(k, n-k+1):
        ans[j][n-k] = p
        p += 1
    for j in range(n-k-1, k-2, -1):
        ans[n-k][j] = p
        p += 1
    for j in range(n-k-1, k-1, -1):
        ans[j][k-1] = p
        p += 1
# mark = None
# mark1, mark2, mark3, mark4 = None,None,None,None
#
# while True:
#     for j in range(n):
#         if ans[i][j] == 0:
#             ans[i][j] = k
#             k += 1
#     j = n - l - 1
#     if k > n*n: break
#     for i in range(n):
#         if ans[i][j] == 0:
#             ans[i][j] = k
#             k += 1
#     i = n - l - 1
#     if k > n * n: break
#     for j in range(n-l - 1, -1, -1):
#         if ans[i][j] == 0:
#             ans[i][j] = k
#             k += 1
#     j = 0 + l
#     if k > n * n: break
#     for i in range(n - l - 1, -1, -1):
#         if ans[i][j] == 0:
#             ans[i][j] = k
#             k += 1
#     if k > n * n: break
#     l += 1
#     i = 0 + l








if n == 1: print(1)
else:
    for wal in ans:
        print(*wal)

# for k in range(1, n**n + 1):
#     ans[i][j] = k
#     if not mark:
#         if j != n - 1 - l:
#             j += 1
#         else:
#             if i != n - 1 - l:
#                 i += 1
#             else:
#                 j -= 1
#                 mark = True
#     else:
#         if j !=  + l:
#             j -= 1
#             if j == 0 + l:
#                 l += 1
#         else:
#             if i != 0 + l:
#                 i -= 1
#             else:
#                 mark = False











    
