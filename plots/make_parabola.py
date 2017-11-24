import numpy
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", type=str, required=True)
    args = parser.parse_args()

    # Prepare the data for the plot
    x_data = numpy.linspace(-1, 1, 100)
    y_data = x_data**2

    # Save the data
    numpy.savez(args.save, x_data=x_data, y_data=y_data)
