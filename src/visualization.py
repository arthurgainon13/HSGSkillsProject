
import matplotlib.pyplot as plt

def plot_results(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Portfolio Value'], label='Portfolio Value')
    plt.legend()
    plt.show()
