class chair:
    def __init__(self, color, material, lags):
        self.color = color
        self.material = material
        self.lags = lags

    def sit(self):
        print("this chair", self.material, self.color, "color", self.lags, "legs")

    def __str__(self):
        return f"Стул(color = {self.color}, material = {self.material}, lags = {self.lags})"

    def __repr__(self):
        return f"Стул(color = {self.color}, material = {self.material}, lags = {self.lags})"

u = chair("blue", "wood", 4)
print([u])




