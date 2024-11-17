from socket import *

host = "localhost"

server = socket( AF_INET, SOCK_DGRAM )

for port in range(100):
    
    if server.connect_ex( (host, port)) == 0:
        print(f"{port} is open at {host}")
    else:
        print(f"{port} is closed at {host}")
        
"""

0 is open at localhost
1 is open at localhost
2 is open at localhost
3 is open at localhost
4 is open at localhost
5 is open at localhost
6 is open at localhost
7 is open at localhost
8 is open at localhost
9 is open at localhost
10 is open at localhost
11 is open at localhost
12 is open at localhost
13 is open at localhost
14 is open at localhost
15 is open at localhost
16 is open at localhost
17 is open at localhost
18 is open at localhost
19 is open at localhost
20 is open at localhost
21 is open at localhost
22 is open at localhost
23 is open at localhost
24 is open at localhost
25 is open at localhost
26 is open at localhost
27 is open at localhost
28 is open at localhost
29 is open at localhost
30 is open at localhost
31 is open at localhost
32 is open at localhost
33 is open at localhost
34 is open at localhost
35 is open at localhost
36 is open at localhost
37 is open at localhost
38 is open at localhost
39 is open at localhost
40 is open at localhost
41 is open at localhost
42 is open at localhost
43 is open at localhost
44 is open at localhost
45 is open at localhost
46 is open at localhost
47 is open at localhost
48 is open at localhost
49 is open at localhost
50 is open at localhost
51 is open at localhost
52 is open at localhost
53 is open at localhost
54 is open at localhost
55 is open at localhost
56 is open at localhost
57 is open at localhost
58 is open at localhost
59 is open at localhost
60 is open at localhost
61 is open at localhost
62 is open at localhost
63 is open at localhost
64 is open at localhost
65 is open at localhost
66 is open at localhost
67 is open at localhost
68 is open at localhost
69 is open at localhost
70 is open at localhost
71 is open at localhost
72 is open at localhost
73 is open at localhost
74 is open at localhost
75 is open at localhost
76 is open at localhost
77 is open at localhost
78 is open at localhost
79 is open at localhost
80 is open at localhost
81 is open at localhost
82 is open at localhost
83 is open at localhost
84 is open at localhost
85 is open at localhost
86 is open at localhost
87 is open at localhost
88 is open at localhost
89 is open at localhost
90 is open at localhost
91 is open at localhost
92 is open at localhost
93 is open at localhost
94 is open at localhost
95 is open at localhost
96 is open at localhost
97 is open at localhost
98 is open at localhost
99 is open at localhost

"""