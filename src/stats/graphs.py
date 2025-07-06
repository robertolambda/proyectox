import matplotlib.pyplot as plt

def plot(data, title="Data Plot", xlabel="X-axis", ylabel="Y-axis"):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()