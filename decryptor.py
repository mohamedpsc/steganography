from PIL import Image


def decrypt(image, out='decrypted.png'):
    """
        :param image: Path to image-like (png, jpeg, ...) to be decrypted
        :type image: String
        :param out: Name of the file to store the decrypted image in
        :type out: String
    """
    img = Image.open(image)
    img_data = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img_data[i, j][0] % 2 == 0:
                # red value is even so change it to white pixel
                img_data[i, j] = (255, 255, 255)
            else:
                # red value is odd so change it to black pixel
                img_data[i, j] = (0, 0, 0)
    img.save(out)


if __name__ == '__main__':
    decrypt('./Test cases/111111.png')
