from math import log10, sqrt
import cv2
import numpy as np


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    print("MSE ", mse)
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def main():
    original = cv2.imread("images/out1.png")
    compressed = cv2.imread("images/in1.png", 1)
    value = PSNR(original, compressed)
    print(f"1st PSNR value is {value} dB")
    original = cv2.imread("images/in2.png")
    compressed = cv2.imread("images/out2.png", 1)
    value = PSNR(original, compressed)
    print(f"2nd PSNR value is {value} dB")
    original = cv2.imread("images/in3.png")
    compressed = cv2.imread("images/out3.png", 1)
    value = PSNR(original, compressed)
    print(f"3rd PSNR value is {value} dB")
    original = cv2.imread("images/in4.png")
    compressed = cv2.imread("images/out4.png", 1)
    value = PSNR(original, compressed)
    print(f"4th PSNR value is {value} dB")
    original = cv2.imread("images/in5.png")
    compressed = cv2.imread("images/out5.png", 1)
    value = PSNR(original, compressed)
    print(f"5th PSNR value is {value} dB")

if __name__ == "__main__":
    main()