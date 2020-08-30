from urllib.request import urlretrieve
from humanize import naturalsize as ns
import sys


prompt = "\t»»\t"

def handel_progress(block_num, block_size, total_size):
    wanted_data = block_num * block_size

    if total_size > 0:
        down_percent = wanted_data * 100 / total_size
        in_norsize = ns(down_percent)
        out_norsize = ns(total_size)
        sys.stdout.write(f"\rWe're in: {in_norsize}, and out {out_norsize}")
        sys.stdout.flush()

def main(): 
    url = input("[+] Please enter your url. \n" + prompt)
    file_name = input("[+] Name your file!\n" + prompt)
    location = "/home/coderisho/Desktop"
    location += file_name
    urlretrieve(url, location, handel_progress)


if __name__ == "__main__":
    main()
