'''
#1
import matplotlib.pyplot as plt
import numpy as np

def plot_function(alpha, beta):
    x = np.linspace(-10, 10, 100)
    y = (x**beta + alpha**beta) / (x**beta)

    plt.plot(x, y, label=f"a={alpha}, b={beta}")
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plot_{alpha}_{beta}.svg")
    plt.show()

plot_function(1, 1)
plot_function(2, 1)
plot_function(1, 2)
'''
#2
import matplotlib.pyplot as plt
import numpy as np

def plot_function(alpha, beta):
    x1 = np.linspace(0.01, 1, 100)
    y1 = (x1**beta + alpha**beta) / (x1**beta)

    x2 = np.linspace(1, 10, 100)
    y2 = (x2**beta + alpha**beta) / (x2**beta)

    plt.plot(x1, y1, label=f"a={alpha}, b={beta}")
    plt.plot(x2, y2, linestyle="--", color="blue")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plot_{alpha}_{beta}.svg")
    plt.show()

plot_function(1, 1)
plot_function(2, 1)
plot_function(1, 2)

#3
import matplotlib.pyplot as plt
import numpy as np

def plot_function(alpha, beta):
    x1 = np.linspace(-10, 0, 100)
    y1 = (x1**beta + alpha**beta) / (x1**beta)

    x2 = np.linspace(0, 10, 100)
    y2 = (x2**beta + alpha**beta) / (x2**beta)

    plt.plot(x1, y1, label=f"a={alpha}, b={beta}")
    plt.plot(x2, y2, label=f"a={alpha}, b={beta}")
    plt.axhline(y=0, color='black', linestyle='--')

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plot_{alpha}_{beta}.svg")
    plt.show()

plot_function(1, 1)
plot_function(2, 1)
plot_function(1, 2)




































