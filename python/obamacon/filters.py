from PIL import Image

def load_img(img): 
    image =  Image.open(img)
    return image

def show_img(img):
    print(img)
    img.show(title=None)

def save_img(img, filename):
    img.save(filename)


def obamicon(img):
    # image into data
    data = img.getdata()
    final = []
    # change data in different rgb
    for p in range(0, len(data)):
        if sum(data[p]) < 182:
            final.append((0, 51, 76))
        elif sum(data[p]) < 364:
            final.append((217, 26, 33))
        elif sum(data[p]) < 546:
            final.append((112, 150, 158))
        else:
            final.append((252, 227, 166))
    # turn back into img
    img.putdata(final)
    return img

test = load_img("test.jpg")
trial = obamicon(test)
show_img(trial)

