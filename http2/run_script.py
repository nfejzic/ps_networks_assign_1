import getpass
import signal
import subprocess
import time
from os import remove


def download_image_generate_run(sudo_pw: str, img_url: str, iteration: int = 1):
    temp_file_name = "temp.pcap"
    temp_file = open(temp_file_name, "w")

    tcpdump = subprocess.Popen(
        [
            "sudo",
            "-S",
            "tcpdump",
            "host",
            "drive.usercontent.google.com",
        ],
        stdout=temp_file,
        stdin=subprocess.PIPE,
        universal_newlines=True,
    )

    # tcpdump.communicate(sudo_pw + "\n")

    # call curl to download the image
    curl_call = subprocess.Popen(
        [
            "/opt/homebrew/opt/curl/bin/curl",
            "--request",
            "GET",
            "--http2",
            img_url,
            "--output",
            "/dev/null",
        ]
    )

    curl_call.wait()

    # time.sleep(10)

    tcpdump.terminate()

    # call tshark to generate the csv file
    csv_file_name = f"output_{iteration}.csv"
    # csv_file = open(csv_file_name, "w")
    tshark_call = subprocess.Popen(
        [
            "tshark",
            "-r",
            temp_file_name,
            "-Y",
            '"tcp"',
            "-T",
            "fields",
            "-e",
            "frame.time_epoch",
            "-e",
            "tcp.seq",
        ],
        stdout=subprocess.PIPE,
    )

    tshark_call.wait()
    # remove(temp_file_name)


def exit_gracefully(signum, frame):
    print("Exiting exit_gracefully")


def main():
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)

    img_url = "https://drive.usercontent.google.com/download?id=1a962uMzTnizkw7NmA3okLps-ynT3q2Gw&export=download&authuser=0"
    # sudo_pw = getpass.getpass("Enter sudo password: ")
    download_image_generate_run("", img_url)


if __name__ == "__main__":
    main()
