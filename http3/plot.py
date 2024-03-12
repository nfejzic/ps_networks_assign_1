import argparse
import csv

import matplotlib.pyplot as plt
import numpy as np

desc = "Plot the UDP packet numbers over time"
epilog = "Author: Nadir Fejzic <nadirfejzo@gmail.com>"


def save_plot(out_file: str, timestamps_file: str):
    timestamps = []
    packet_numbers = []

    with open(timestamps_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            packet_numbers.append(int(row[0]))
            timestamps.append(float(row[1]))

    elapsed_time = [(timestamp - timestamps[0]) for timestamp in timestamps]

    _, ax = plt.subplots(figsize=(12, 5))

    ax.scatter(elapsed_time, packet_numbers, marker=".", s=0.5)
    ax.set_xlabel("Elapsed Time (seconds)")
    ax.set_ylabel("Packet Number")
    ax.set_title("UDP Time Sequence Plot")

    plt.xticks(np.arange(min(elapsed_time), max(elapsed_time), 0.2))
    plt.savefig(out_file, dpi=200)


def parse_args():
    parser = argparse.ArgumentParser(prog="uqi_p", description=desc, epilog=epilog)
    parser.add_argument("iteration", help="iteration of the experiment")
    parser.add_argument("in_file", help="iteration of the experiment")

    args, _ = parser.parse_known_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    iteration = args.iteration
    in_file = args.in_file
    filename = f"udp_time_seq_{iteration}.png"
    save_plot(filename, in_file)
