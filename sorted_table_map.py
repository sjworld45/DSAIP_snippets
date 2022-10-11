from map_base import MapBase 

class SortedTableMap(MapBase):

	def _find_index(self, k, low, high):
		if high < low :
			return high + 1 

		else: 
			mid = (low + high) // 2
			if k == self._table[mid]._key:
				return mid 

			elif k < self._table[mid]._key:
				return self._find_index(k, low, mid-1)

			else:
				return self._find_index(k, mid+1, high)


	def __init__(self):
		self._table = []

	def __len__(self):
		return len(self._table)

	def __getitem__(self, k):
		j = self._find_index(k, 0, len(self._table)-1)
		if j == len(self._table) or self._table[j]._key ! = k:
			raise KeyError('Key Error: '+ repr(k))
		return self._table[j]._value
