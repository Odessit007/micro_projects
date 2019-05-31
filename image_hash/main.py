import argparse
import numpy as np
import os
from PIL import Image

M = 2 ** 64


def _diff_hash(img, size, direction):
    """
    Computes dHash for given image
    :param img: Pillow image object
    :param size: resulting hash will have size*size bits
    :return: (size*size)-bit unsigned integer

        Detailed algorithm steps for columns comparison (row comparison is done almost the same way):
    1. Convert to grayscale:
        img0 = img.convert('L')
    2. Resize to (size+1 x size):
        img1 = img0.resize((size+1, size))
    3. Key step
        img3 = img1[:, 1:] > img1[:, :size]
    4. Compute the hash
        Iterate through the rows of img3 and treat each value (0 or 1) as bit value of hash.
    """
    img = img.convert('L')
    if direction == 0:
        img = img.resize((size + 1, size))
        img = np.array(img)
        img_binary = img[:, 1:] > img[:, :size]
        return sum([1 << i for (i, val) in enumerate(np.nditer(img_binary)) if val])
    elif direction == 1:
        img = img.resize((size, size + 1))
        img = np.array(img)
        img_binary = img[1:, :] > img[:size, :]
        return sum([1 << i for (i, val) in enumerate(np.nditer(img_binary)) if val])


def diff_hash(img, size=8):
    h0 = _diff_hash(img, size, 0)
    h1 = _diff_hash(img, size, 1)
    return h0 + M*h1


def hamming_distance(x, y):
    xor = x ^ y
    ans = 0
    while xor:
        xor = xor & (xor - 1)
        ans += 1
    return ans


if __name__ == '__main__':
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description='First test task on images similarity.')
    parser.add_argument('--path', required=True, help='folder with images')
    args = parser.parse_args()

    # Computing d-hash for each image in the given directory
    size = 8
    hashes = []
    img_names = []
    for img_name in os.listdir(args.path):
        img_full_path = os.path.join(args.path, img_name)
        with Image.open(img_full_path) as img:
            h = diff_hash(img, size)
            hashes.append(h)
            img_names.append(img_name)

    # Finding and printing all duplicate pairs
    n = len(hashes)
    sq_size = size * size
    for i in range(n):
        for j in range(i + 1, n):
            h1 = hashes[i]
            h2 = hashes[j]
            d = hamming_distance(h1, h2) / sq_size
            if d <= 0.3:
                print(img_names[i], img_names[j])
