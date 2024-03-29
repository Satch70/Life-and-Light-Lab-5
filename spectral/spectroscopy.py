import matplotlib.pyplot as plt
import numpy as np
import os

def load_spectral_data(filepath):
    """
    Load and parse spectral data from a given file.
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
        data_start_index = lines.index(">>>>>Begin Spectral Data<<<<<\n") + 1
        data_lines = lines[data_start_index:]
        data = [list(map(float, line.split('\t'))) for line in data_lines]
    return np.array(data)

def filter_range(data, min_wavelength=480, max_wavelength=800):
    """
    Filter data for the specified wavelength range.
    """
    return data[(data[:, 0] >= min_wavelength) & (data[:, 0] <= max_wavelength)]

def plot_spectra(filenames, folder='data', save_path=None):
    """
    Plot the reflectance spectra for given filenames within a folder.
    Optionally save the plot to the specified path.
    """
    plt.figure(figsize=(10, 6))

    for filename in filenames:
        filepath = os.path.join(folder, filename)
        data = load_spectral_data(filepath)
        filtered_data = filter_range(data)
        plt.plot(filtered_data[:, 0], filtered_data[:, 1], label=filename.split('.')[0])

    plt.title('Reflectance Spectrum')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance (%)')
    plt.legend()
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)  # Save the figure to the specified path
    plt.show()  # Display the figure

if __name__ == "__main__":
    filenames = ['healthy.txt', 'sad1.txt']
    save_path = 'data/spectral_plot.png'  # Example path and filename where to save the plot
    plot_spectra(filenames, save_path=save_path)
