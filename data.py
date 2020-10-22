class FrequencyData:
    def __init__(self, value: list, freq: list):
        assert len(value) == len(freq), "Dimensions are not the same"
        self.data = self._set_data(value, freq)
        self.m = sum(freq)

    def _set_data(self, value, freq):
        data = []
        for i in range(0, len(value)):
            data.append({'value': value[i], 'freq': freq[i]})
        return data

    @property
    def mean(self):
        total = sum([d['value'] * d['freq'] for d in self.data])
        return total / self.m

    @property
    def variance(self):
        mean = self.mean 
        gp_diff = 0  # to shore the sum of sq difference

        for d in self.data:
            sq_diff = (d['value'] - mean) ** 2
            gp_diff += d['freq'] * sq_diff

        variance = (gp_diff / (self.m - 1)) ** (1 / 2)
        return variance