import numpy as np
import matplotlib.pyplot as plt


def plot_index_profile(x, y, n_profile):
    plt.figure()
    plt.imshow(
        n_profile,
        extent=[x.min(), x.max(), y.min(), y.max()],
        origin="lower",
        aspect="equal",
    )
    plt.colorbar(label="Refractive index")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Index profile")
    plt.show()


def plot_mode_amplitude(x, y, mode):
    plt.figure()
    plt.imshow(
        mode,
        extent=[x.min(), x.max(), y.min(), y.max()],
        origin="lower",
        aspect="equal",
        cmap="RdBu_r",
    )
    plt.colorbar(label="Field amplitude")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Mode amplitude")
    plt.show()


def plot_mode_intensity(x, y, mode):
    intensity = np.abs(mode) ** 2

    plt.figure()
    plt.imshow(
        intensity,
        extent=[x.min(), x.max(), y.min(), y.max()],
        origin="lower",
        aspect="equal",
    )
    plt.colorbar(label="Intensity")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Mode intensity")
    plt.show()


def main():
    # Example usage of the plotting functions
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)

    # Create a sample index profile (e.g., a simple waveguide)
    n_profile = np.where((np.abs(X) < 0.5) & (np.abs(Y) < 0.5), 3.48, 1.44)

    # Create a sample mode (e.g., a Gaussian mode)
    mode = np.exp(-((X ** 2 + Y ** 2) / (0.1 ** 2)))

    plot_index_profile(x, y, n_profile)
    plot_mode_amplitude(x, y, mode)
    plot_mode_intensity(x, y, mode)

if __name__ == "__main__":
    main()