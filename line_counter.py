import sys

def count_lines(filenames):
  count = 0
  for filename in filenames:
    with open(filename) as f:
      for line in f:
        count += 1
  return count

filenames = sys.argv[1:]
print(count_lines(filenames))
