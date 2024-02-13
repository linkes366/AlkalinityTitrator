import numpy as np
import parser as p
import matplotlib.pyplot as plt


def pdf(x, points):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (points - mean)**2 / (2 * std**2))
    return y_out


def plot(data):
    variance = np.var(data)
    standard = np.std(data)
    mean = np.mean(data)
    points = np.arange(np.min(data), np.max(data), standard/2)  # ok with /2 as long as enough data points, otherwise /4
    y = pdf(data, np.array(points))
    plt.figure(figsize=(6, 6))
    plt.plot(np.array(points), y, color='blue',
             linestyle='dashed')

    plt.scatter(points, y, marker='o', s=25, color='green', label='STD Curve with STD/2')

    g = pdf(data, data)
    plt.plot(data, g, color='black',
             linestyle='solid')

    plt.scatter(data, g, marker='o', s=25, color='red', label='Data Points STD')
    plt.xlabel('Voltage')
    plt.ylabel('Probability')
    var = "{:.2f}".format(variance)
    std = "{:.2f}".format(standard)
    men = "{:.2f}".format(mean)
    plt.title(f'Variance: {var}mV   STD: {std}mV   Mean: {men}mV')
    plt.legend()
    plt.grid(True)
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
