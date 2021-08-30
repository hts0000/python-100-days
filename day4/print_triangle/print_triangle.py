"""
*
**
***
****
*****
"""
for i in range(6):
    for _ in range(i):
        print("*", end="")
    print()

"""
    *
   **
  ***
 ****
*****
"""
for i in range(6):
    for _ in range(5 - i):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print()

"""
    *
   ***
  *****
 *******
*********
"""
for i in range(6):
    for _ in range(5 - i):
        print(" ", end="")
    for _ in range(i * 2 - 1):
        print("*", end="")
    print()
