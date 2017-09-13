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
class MinHeap(object):
	"""
	Implements the classic data structure min-heap.

	Provides functions for heapifying an unsorted list, heap-sorting the list,
	insert and delete (pop) from heap in O(lg n).
	"""
	def __init__(self, items):
		"""
		Create a new MinHeap instance using a list of unsorted items
		Time Complexity: O(n)
		"""
		self.heap = copy.deepcopy(items)				# Do not want to alter items
		self.min_heapify_list(self.heap)
		return

	def insert(self, elem):
		"""
		Insert element elem into the heap.
		Time Complexity: O(lg(n))
		"""
		self.heap.append(elem)
		heap_size = len(h) + 1
		self.percolate_up(heap_size-1)
		return

	def pop(self):
		"""
		Remove the smallest element, and return it as well
		Time Complexity: O(lg(n))
		"""
		temp = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap[-1] = temp
		popped_element = self.heap.pop()
		MinHeap.min_heapify(self.heap, 0, len(self.heap))
		return popped_element

	def delete_by_pos(self, pos):
		"""
		Delete the element at position pos and return the element.
		Time Complexity: O(lg(n))
		"""
		n = len(self.heap)
		parent_pos = int((pos-1)/2)
		deleted_element = self.heap[pos]
		self.heap[pos] = self.heap[n-1]
		self.heap.pop()
		if self.heap[pos] < self.heap[parent_pos]:
			self.percolate_up(pos)
		else:
			MinHeap.min_heapify(self.heap, pos, n-1)
		return deleted_element

	def percolate_up(self, pos):
		"""
		An element at position pos is not at its correct place, keep percolating it up 
		till it reaches a place congruous with the min-heap data structure.
		Time Complexity: O(lg(n))
		"""
		if pos > 0:
			parent_pos = int((pos-1)/2)
			if self.heap[parent_pos] > self.heap[pos]:
				temp = self.heap[parent_pos]
				self.heap[parent_pos] = self.heap[pos]
				self.heap[pos] = temp
				self.percolate_up(parent_pos)
		return

	def get_sorted_elements_descending(self):
		sorted_elements = copy.deepcopy(self.heap)
		for last_pos in range(len(self.heap)-1, 0, -1):
			temp = sorted_elements[0]
			sorted_elements[0] = sorted_elements[last_pos]
			sorted_elements[last_pos] = temp
			MinHeap.min_heapify(sorted_elements, 0, last_pos)
		return sorted_elements

	@staticmethod
	def min_heapify(l, current_pos, heap_length):
		"""
		Perform the well known heapify operation.
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
			MinHeap.min_heapify(l, min_pos, heap_length)
		return

	@staticmethod
	def min_heapify_list(l):
		"""
		Convert a list into a min-heap
		Time Complexity: O(n)
		"""
		n = len(l)
		for current_pos in range(int(floor(n/2)) - 1, -1, -1):
			MinHeap.min_heapify(l, current_pos, len(l))
		return

	@staticmethod
	def heap_sort(l, asc=True):
		"""
		Given a list l, sort it using the heap-sort method
		Time Complexity: O(nlg(n))
		Return: sorted list l
		"""
		# Don't want to sort the reference itself, so we rebind the reference to mimick pass by value on the object
		l = copy.deepcopy(l)
		n = len(l)
		MinHeap.min_heapify_list(l)
		for current_pos in range(n-1, 0, -1):
			temp = l[current_pos]
			l[current_pos] = l[0]
			l[0] = temp
			MinHeap.min_heapify(l, 0, current_pos)
		if asc:
			return l[::-1]
		else:
			return l

	@staticmethod
	def check_list_min_heap(l):
		"""
		Given list l, determine if it qualifies as a binary min-heap
		Return True/False
		Time Complexity: O(n)
		"""
		answer = True
		for current_pos in range(int(floor(len(l)/2))):
			left_child = l[2*current_pos + 1]
			right_child = l[2*current_pos + 2] if 2*current_pos + 2 < len(l) else None
			if l[current_pos] > left_child or (right_child is not None and l[current_pos] > right_child):
				answer = False
				break
		return answer


################################################

# Extension of https://stackoverflow.com/a/407922
class PriorityQueueSet(object):

    """
    Combined priority queue and set data structure.

    Acts like a priority queue, except that its items are guaranteed to be
    unique. Provides O(1) membership test, O(log N) insertion and O(log N)
    removal of the smallest item.

    Important: the items of this data structure must be both comparable and
    hashable (i.e. must implement __cmp__ and __hash__). This is true of
    Python's built-in objects, but you should implement those methods if you
    want to use the data structure for custom objects.
    """

    def __init__(self, items=None):
        """
        Create a new PriorityQueueSet.

        Arguments:
            items (list): An initial item list - it can be unsorted and
                non-unique. The data structure will be created in O(N).
        """
        self.set =  set(items) if items is not None else set()
        self.heap = list(self.set)
        min_heapify_list(self.heap)
        return

    def has_item(self, item):
        """Check if ``item`` exists in the queue."""
        return item in self.set

    def pop_smallest(self):
        """Remove and return the smallest item from the queue."""
        smallest = heapq.heappop(self.heap)
        del self.set[smallest]
        return smallest

    def add(self, item):
        """Add ``item`` to the queue if doesn't already exist."""
        if item not in self.set:
            self.set[item] = True
            heapq.heappush(self.heap, item)



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


def max_heapify_list(l):
	"""
	Convert a list into a max-heap
	Time Complexity: O(n)
	"""
	n = len(l)
	for current_pos in range(int(floor(n/2)) - 1, -1, -1):
		max_heapify(l, current_pos, len(l))
	return


def heap_sort_ascending(l):
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
	MinHeap.min_heapify_list(l)
	for i in range(0, k):
		last_idx = n-i-1
		temp = l[0]
		l[0] = l[last_idx]
		l[last_idx] = temp
		MinHeap.min_heapify(l, 0, n-i-1)
	return l[n-k]


def main():
	l1 = [90, 15, 10, 7, 12, 2, 7, 3]
	l2 = [90, 15, 10, 7, 12, 2, 17]
	l3 = [-2, -1]
	
	print(check_list_max_heap(l1))
	print(check_list_max_heap(l2))
	print(check_list_max_heap(l3))

	print(heap_sort_ascending(l1))
	print(heap_sort_ascending(l2))
	print(heap_sort_ascending(l3))

	print(find_kth_smallest_element(l1, 3))

	#########################################

	h1 = MinHeap(l1)
	print(MinHeap.check_list_min_heap(h1.heap))
	print(MinHeap.heap_sort(l1))
	print(h1.pop())
	print(h1.delete_by_pos(2))
	print(MinHeap.check_list_min_heap(h1.heap))
	print(h1.get_sorted_elements_descending())


if __name__ == "__main__":
	main()