s = "My Name Is Zhang "
length = len(s)
flat = 1
i = 0
s1 = ""
while flat:
        if s[i].isupper():
            s1 = s1 + s[i].lower()
        else:
            s1 = s1 + s[i].upper()
        i = i + 1
        if i == length:
            flat = 0
print(s1)
s2 = s1.split(' ')
s3 = s2[::-1]
print(' '.join(s3))
