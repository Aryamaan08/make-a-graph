from matplotlib import pyplot as plt

if __name__ == '__main__':
    graph_choice = input('Enter choice:\n Bar graph or Line graph? ')
    if graph_choice == 'Bar graph':
        color = input('Enter color choice (word or hex value): ')
        print('Enter x values: ', end='')
        x = [n for n in input().split(', ')]
        print('Enter respective data: ', end='')
        data = [int(n) for n in input().split(', ')]
        xlab = input('Label for x values: ')
        ylab = input('Label for data (y values): ')
        title = input('Enter title: ')
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
        plt.bar(x, data, color=color)
        plt.show()
    elif graph_choice == 'Line graph':
        color = input('Enter color choice (word or hex value): ')
        print('Enter x values: ', end='')
        x = [n for n in input().split(', ')]
        print('Enter respective data: ', end='')
        data = [int(n) for n in input().split(', ')]
        xlab = input('Label for x values: ')
        ylab = input('Label for data (y values): ')
        title = input('Enter title: ')
        additional = input('Marker (*- star, o- circle, s- square): ')
        plt.plot(x, data, color=color, marker=additional)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
        plt.show()
    else:
        print('Invalid type')
