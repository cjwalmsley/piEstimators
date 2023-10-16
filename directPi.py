import random

class piEstimator:
    import random

    def __init__(self, numberOfRuns):
        self.numberOfRuns = numberOfRuns
        self.numberOfHits = 0
        self.x = 0
        self.y = 0

    def computeEstimate(self):
        for each in range(self.numberOfRuns):
            self.computeRunResult()
        return self.numberOfHits

    def computeRunResult(self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1, 1)
        if self.x**2 + self.y**2 < 1:
            self.numberOfHits = self.numberOfHits +1


if __name__ == '__main__':
    estimator = piEstimator(400000)
    print(estimator.computeEstimate())
