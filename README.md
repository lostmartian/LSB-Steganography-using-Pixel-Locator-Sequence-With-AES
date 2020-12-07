# Improved LSB Steganography 
> Improvised LSB Steganography technique using Pixel Locator Sequence with AES

This is the implementation of our research paper based on <b>LSB Steganography</b> submitted at [Second International Conference on Cyber Computing and Communications](https://www.nitj.ac.in/icsccc2021/) arxiv preprint : [2012.02494](https://arxiv.org/abs/2012.02494).

## Development Setup

The following modules must be installed before running this system:

```sh
pip3 install Pillow pyaes hashlib numpy Cryptodome pbkdf2 binascii
git clone https://github.com/lostmartian/Improved-LSB-Steganography.git
python3 main.py
```
## What is it all about ?

Image steganography is the art of hiding data into images. Secret data such as messages, audio, images can be hidden inside the cover image. This is mainly achieved by hiding the data into the LSB(Least Significant Bit) of the image pixels. To improve the security of steganography, we studied data encryption with AES(Advanced Encryption Standard) and LSB based data hiding technique with advanced user-defined encrypted data distribution in pixels other than the common linear computational method of storing data in a linear form. The pixel locater sequence will contain the location of the data(in form of pixel numbers) to be encrypted/decrypted which is further encrypted with AES thus providing double encryption for data and its location stored over pixels. Steganography has many applications such as medical, military, copyright information, etc.

<p align="center">
  <img width="250" height="300" src="images/sample_cmd/encryption.PNG">
  <br>
  Encrytion Procedure
</p>

<p align="center">
  <img width="250" height="300" src="images/sample_cmd/decryption.PNG">
  <br>
  Decryption Procedure
</p>

## Creators

<b>Sahil Gangurde</b> – [@lost_martian_](https://twitter.com/lost_martian_) – sahilgangurde08@gmail.com
<br>
<b>Krishnakant Tiwari</b> – [@Iamkkant](https://twitter.com/Iamkkant) – kkant5401@gmail.com

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
