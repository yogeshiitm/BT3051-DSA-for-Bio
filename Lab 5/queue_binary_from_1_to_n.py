# https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

from queue import Queue #inbuilt
q = Queue()
q.enqueu("1")

s=q.deque() -->    q.enqueue(s+'0')   q.enqueue(s+'1')
1           -->         10   (2)          11   (3)
10          -->         100  (4)          101  (5)
11          -->         110  (6)          111  (7)
100         -->         1000 (8)          1001 (9)

