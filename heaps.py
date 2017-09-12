"""
This module deals with many aspects of the heap data structure.
Author: Avikalp Srivastava
"""

from __future__ import print_function
from __future__ import division

import numpy as np

from math import floor
import copy


################################################
def max_heapify(l, current_pos, heap_length):
	"""
	Perform the well known heapify operation and return the list/heap
	Time Complexity: O(lg(n)), where n is heap_length
	"""
	max_pos = current_pos
	left_child_pos = (current_pos << 1) + 1
	right_child_pos = left_child_pos + 1
	if left_child_pos < heap_length and l[left_child_pos] > l[max_pos]:
		max_pos = left_child_pos
	if right_child_pos < heap_length and l[right_child_pos] > l[max_pos]:
		max_pos = right_child_pos
	if max_pos != current_pos:
		temp = l[current_pos]
		l[current_pos] = l[max_pos]
		l[max_pos] = temp
		max_heapify(l, max_pos, heap_length)
	return


def min_heapify(l, current_pos, heap_length):
	"""
	Perform the well known heapify operation and return the list/heap
	Time Complexity: O(lg(n)), where n is heap_length
	"""
	min_pos = current_pos
	left_child_pos = (current_pos << 1) + 1
	right_child_pos = left_child_pos + 1
	if left_child_pos < heap_length and l[left_child_pos] < l[min_pos]:
		min_pos = left_child_pos
	if right_child_pos < heap_length and l[right_child_pos] < l[min_pos]:
		min_pos = right_child_pos
	if min_pos != current_pos:
		temp = l[current_pos]
		l[current_pos] = l[min_pos]
		l[min_pos] = temp
		min_heapify(l, min_pos, heap_length)
	return


def max_heapify_list(l):
	"""
	Convert a list into a max-heap
	Time Complexity: O(n)
	"""
	n = len(l)
	for current_pos in range(int(floor(n/2)) - 1, -1, -1):
		max_heapify(l, current_pos, len(l))
	return


def min_heapify_list(l):
	"""
	Convert a list into a min-heap
	Time Complexity: O(n)
	"""
	n = len(l)
	for current_pos in range(int(floor(n/2)) - 1, -1, -1):
		min_heapify(l, current_pos, len(l))
	return


def heap_sort(l):
	"""
	Given a list l, sort it using the heap-sort method
	Time Complexity: O(nlg(n))
	Return: sorted list l
	"""
	# Don't want to sort the reference itself, so we rebind the reference to mimick pass by value on the object
	l = copy.deepcopy(l)
	n = len(l)
	max_heapify_list(l)
	for current_pos in range(n-1, 0, -1):
		temp = l[current_pos]
		l[current_pos] = l[0]
		l[0] = temp
		max_heapify(l, 0, current_pos)
	return l


################################################
# 1. Check if given list is a binary max-heap

def check_list_max_heap(l):
	"""
	Given list l, determine if it qualifies as a binary max-heap
	Return True/False
	Time Complexity: O(n)
	"""
	answer = True
	for current_pos in range(int(floor(len(l)/2))):
		left_child = l[2*current_pos + 1]
		right_child = l[2*current_pos + 2] if 2*current_pos + 2 < len(l) else None
		if l[current_pos] < left_child or (right_child is not None and l[current_pos] < right_child):
			answer = False
			break
	return answer


# 2. Find the kth smallest element of an unsorted list l
# P.S.: There exist methods with expected and worst-case linear time as well for this.

def find_kth_smallest_element(l, k):
	"""
	Return the kth smallest element of the list l. Here k is 1-indexed.
	Time Complexity: O(n + klg(n))
	"""
	l = copy.deepcopy(l)
	n = len(l)
	min_heapify_list(l)
	for i in range(0, k):
		last_idx = n-i-1
		temp = l[0]
		l[0] = l[last_idx]
		l[last_idx] = temp
		min_heapify(l, 0, n-i-1)
	return l[n-k]


def main():
	l1 = [90, 15, 10, 7, 12, 2, 7, 3]
	l2 = [90, 15, 10, 7, 12, 2, 17]
	l3 = [-2, -1]
	
	print(check_list_max_heap(l1))
	print(check_list_max_heap(l2))
	print(check_list_max_heap(l3))

	print(heap_sort(l1))
	print(heap_sort(l2))
	print(heap_sort(l3))

	print(find_kth_smallest_element(l1, 3))


if __name__ == "__main__":
	main()