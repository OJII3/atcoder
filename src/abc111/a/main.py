import sys

n = sys.stdin.readline().rstrip()

print(n.replace("9", "8").replace("1", "9").replace("8", "1"))
