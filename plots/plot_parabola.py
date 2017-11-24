import numpy
import matplotlib
import matplotlib.pyplot as plot
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str)
    parser.add_argument("--save", type=str, default=None)
    args = parser.parse_args()

    data = numpy.load(args.data)

    plot.figure()
    plot.plot(data["x_data"], data["y_data"])
    plot.xlabel("This is $x$")
    plot.ylabel("This is $y$")

    plot.tight_layout()

    if args.save is None:
        plot.show()
    else:
        plot.savefig(args.save)
