import argparse
import csv

import matplotlib.pyplot as plt
import numpy as np

desc = "Plot the TCP sequence numbers over time"
epilog = "Author: Nadir Fejzic <nadirfejzo@gmail.com>"


def save_plot(out_file: str, csv_file: str):
    timestamps = []
    sequence_numbers = []

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            timestamps.append(float(row[0]))
            sequence_numbers.append(int(row[1]))

    elapsed_time = [(timestamp - timestamps[0]) for timestamp in timestamps]

    _, ax = plt.subplots(figsize=(12, 5))

    ax.scatter(elapsed_time, sequence_numbers, marker=".", s=0.5)
    ax.set_xlabel("Elapsed Time (seconds)")
    ax.set_ylabel("TCP Sequence Number")
    ax.set_title("TCP Sequence Numbers over Time")

    plt.xticks(np.arange(min(elapsed_time), max(elapsed_time), 0.2))
    plt.savefig(out_file, dpi=200)


def parse_args():
    parser = argparse.ArgumentParser(prog="uqi_p", description=desc, epilog=epilog)
    parser.add_argument("iteration", help="iteration of the experiment")
    parser.add_argument("csv_file", help="iteration of the experiment")

    args, _ = parser.parse_known_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    iteration = args.iteration
    csv_file = args.csv_file
    filename = f"tcp_time_seq_{iteration}.png"
    save_plot(filename, csv_file)
