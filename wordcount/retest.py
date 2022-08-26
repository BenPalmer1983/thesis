import re








s = "this is \\begin{eq}a\end{eq} string"

s = re.sub('\begin{[^>]+}', '', s)
print(s)


