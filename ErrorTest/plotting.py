import numpy as np
import parser as p
import matplotlib.pyplot as plt


def plot(data):
    variance = np.var(data)
    standard = np.std(data)
    plt.plot(difference, label='Differences')
    plt.title(f'Variance:{variance}')
    plt.text(2, -5, 'This is the bottom', ha='center')
    plt.show()
    return


def main(filename='test_outputTesting.txt'):
    print(filename)
    data = p.get_output_values(filename)
    print(f'data:{data}')
    for set in data:
        plot(set)
    return


if __name__ == "__main__":
    main()
