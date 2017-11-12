from PIL import Image


def encrypt(message_image, host_image, out_image='encrypted.png'):
    """
        :param message_image: Message Image to be hide inside the host Image
        :type message_image: image-like (png, jpeg, ...)
        :param host_image: Image to hide the message image in
        :type host_image: image-like(png, jpeg, ...)
        :param out_image: file to store the encrypted image in
        :type out_image: String
    """
    msg = Image.open(message_image)
    img = Image.open(host_image)
    if msg.size[0] > img.size[0] or msg.size[1] > img.size[1]:
        print("Error: Message image size must be smaller than or equal to the host image.")
    msg_data = msg.load()
    img_data = img.load()
    for i in range(msg.size[0]):
        for j in range(msg.size[1]):
            if msg_data[i, j][0] == 0:
                # pixel is black
                if img_data[i, j][0] % 2 == 0:
                    # red value is even so change it to odd
                    img_data[i, j] = (img_data[i, j][0] + 1, img_data[i, j][1], img_data[i, j][2])
            else:
                # pixel is white
                if img_data[i, j][0] % 2 != 0:
                    # red value is odd so change it to even
                    img_data[i, j] = (img_data[i, j][0] - 1, img_data[i, j][1], img_data[i, j][2])
    img.save(out_image)



if __name__ == '__main__':
    encrypt('./m.png', './o.png', 'out.png')
