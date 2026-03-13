content = open('/dev/stdin').read()
open('/home/ubuntu/kol-academic/index.html', 'w').write(content)
print("Done:", len(content), "chars")
