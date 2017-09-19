#

# This Kata is straightforward. Implement a binary search routine
# (using the specification below) in the language and technique of
# your choice. Tomorrow, implement it again, using a totally different
# technique. Do the same the next day, until you have five totally
# unique implementations of a binary chop. (For example, one solution
# might be the traditional iterative approach, one might be recursive,
# one might use a functional style passing array slices around, and so
# on).


# def test_chop
#   assert_equal(-1, chop(3, []))
#   assert_equal(-1, chop(3, [1]))
#   assert_equal(0,  chop(1, [1]))
#   #
#   assert_equal(0,  chop(1, [1, 3, 5]))
#   assert_equal(1,  chop(3, [1, 3, 5]))
#   assert_equal(2,  chop(5, [1, 3, 5]))
#   assert_equal(-1, chop(0, [1, 3, 5]))
#   assert_equal(-1, chop(2, [1, 3, 5]))
#   assert_equal(-1, chop(4, [1, 3, 5]))
#   assert_equal(-1, chop(6, [1, 3, 5]))
#   #
#   assert_equal(0,  chop(1, [1, 3, 5, 7]))
#   assert_equal(1,  chop(3, [1, 3, 5, 7]))
#   assert_equal(2,  chop(5, [1, 3, 5, 7]))
#   assert_equal(3,  chop(7, [1, 3, 5, 7]))
#   assert_equal(-1, chop(0, [1, 3, 5, 7]))
#   assert_equal(-1, chop(2, [1, 3, 5, 7]))
#   assert_equal(-1, chop(4, [1, 3, 5, 7]))
#   assert_equal(-1, chop(6, [1, 3, 5, 7]))
#   assert_equal(-1, chop(8, [1, 3, 5, 7]))
# end

# find value in a sorted array of a.

import pytest

def chop(value, a):
    length = len(a)

    if a == None or length == 0:
         return -1

    if length == 1:
        if a[0] == value:
            return 0
        else:
            return -1

    mid = len(a)//2

    if value == a[mid]:
        return mid
    elif value > a[mid]:
        i = chop(value, a[mid:length])
        if i == -1: return i
        return i + mid
    else:
        return chop(value, a[0:mid])

    return -1

if __name__ == '__main__':
  assert -1 == chop(3, [])
  assert -1 == chop(3, [1])
  assert 0 == chop(1, [1])
  #
  assert 0 == chop(1, [1, 3, 5])
  assert 1 == chop(3, [1, 3, 5])
  assert 2 == chop(5, [1, 3, 5])
  assert -1 == chop(0, [1, 3, 5])
  assert -1 == chop(2, [1, 3, 5])
  assert -1 == chop(4, [1, 3, 5])
  assert -1 == chop(6, [1, 3, 5])
  #
  assert 0 == chop(1, [1, 3, 5, 7])
  assert 1 == chop(3, [1, 3, 5, 7])
  assert 2 == chop(5, [1, 3, 5, 7])
  assert 3 == chop(7, [1, 3, 5, 7])
  assert -1 == chop(0, [1, 3, 5, 7])
  assert -1 == chop(2, [1, 3, 5, 7])
  assert -1 == chop(4, [1, 3, 5, 7])
  assert -1 == chop(6, [1, 3, 5, 7])
  assert -1 == chop(8, [1, 3, 5, 7])
