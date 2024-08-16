class Functions():
    def linear(self, x_val, slope, intercept):
        return x_val * slope + intercept
    def quadratic(self, x_val, A_val, B_val, C_val):
        return x_val * x_val * A_val + x_val * B_val + C_val