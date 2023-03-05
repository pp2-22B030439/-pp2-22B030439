from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
a = input()
b = input()
print("Square root of " + str(a) + " after " + str(b) + " miliseconds is " + str(delay(lambda x: math.sqrt(x), int(b), int(a))))