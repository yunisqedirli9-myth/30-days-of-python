class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
        self.n = len(data)

    def count(self):
        return self.n

    def sum(self):
        return sum(self.data)

    def min(self):
        return self.data[0]

    def max(self):
        return self.data[-1]

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.n)

    def median(self):
        mid = self.n // 2
        if self.n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        counts = {x: self.data.count(x) for x in set(self.data)}
        max_val = max(counts, key=counts.get)
        return (max_val, counts[max_val])

    def var(self):
        mu = self.mean()
        return round(sum((x - mu) ** 2 for x in self.data) / self.n, 1)

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        freq = {x: self.data.count(x) for x in set(self.data)}
        dist = [(round((c / self.n) * 100, 1), x) for x, c in freq.items()]
        return sorted(dist, reverse=True)

    def describe(self):
        lines = [
            f"Count: {self.count()}",
            f"Sum: {self.sum()}",
            f"Min: {self.min()}",
            f"Max: {self.max()}",
            f"Range: {self.range()}",
            f"Mean: {self.mean()}",
            f"Median: {self.median()}",
            f"Mode: {self.mode()}",
            f"Variance: {self.var()}",
            f"Standard Deviation: {self.std()}",
            f"Frequency Distribution: {self.freq_dist()}"
        ]
        return "\n".join(lines)

# Data və Çap
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())
