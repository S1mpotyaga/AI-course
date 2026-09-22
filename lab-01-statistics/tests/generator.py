import random

import numpy as np


class TestGenerator:
	"""Воспроизводимый генератор данных и эталонных ответов NumPy."""

	def __init__(self, seed=20260922):
		self.random = random.Random(seed)

	def values(self, minimum_length=1, maximum_length=20):
		length = self.random.randint(minimum_length, maximum_length)
		return [self.random.randint(-30, 30) for _ in range(length)]

	def cases(self, count=100):
		return [self.values() for _ in range(count)]

	def moment_order(self):
		return self.random.randint(1, 5)

	def interval(self, length):
		left = self.random.randint(1, length)
		right = self.random.randint(left, length)
		return left, right

	@staticmethod
	def array(values):
		return np.asarray(values, dtype=float)

	def mean(self, values):
		return float(np.mean(self.array(values)))

	def median(self, values):
		return float(np.median(self.array(values)))

	def variance(self, values):
		return float(np.var(self.array(values)))

	def std(self, values):
		return float(np.std(self.array(values)))

	def raw_moment(self, values, order):
		return float(np.mean(self.array(values) ** order))

	def central_moment(self, values, order):
		array = self.array(values)
		return float(np.mean((array - np.mean(array)) ** order))

	def skewness(self, values):
		variance = self.variance(values)
		if variance == 0:
			return None
		return self.central_moment(values, 3) / variance**1.5

	def prefixes(self, values):
		array = self.array(values)
		return (
			[0] + np.cumsum(array).tolist(),
			[0] + np.cumsum(array**2).tolist(),
			[0] + np.cumsum(array**3).tolist(),
		)

	def integer_values(self, minimum_length=1, maximum_length=20):
		length = self.random.randint(minimum_length, maximum_length)
		return [10**12 + self.random.randint(-30, 30) for _ in range(length)]
