
import numpy as np
from matplotlib import pyplot as plt
import cv2


def colorArea(img):
    img2 = np.copy(img)

    (img2, neighbors) = firstIteration(img2)

    (areas, img2) = secondIteration(img2, neighbors)

    centersArray = centers(img2, areas)

    return (img2, centersArray, list(areas))

def centers(img, areas):
    centers = []
    for area in areas:
        center = (int(generalM(img, 0, 1, area) / generalM(img, 0, 0,
                  area)), int(generalM(img, 1, 0, area)
                  / generalM(img, 0, 0, area)))
        centers.append(center)
    return centers

def firstIteration(img):
    counter = 1
    neighbors = {}

    for i in range(1, img.shape[0]):
        for j in range(1, img.shape[1] - 1):
            if img[i, j] != 1:
                continue
            pos = np.array([img[i - 1, j - 1], img[i - 1, j],
                                 img[i - 1, j + 1], img[i, j - 1]])
            if sum(pos) == 0:
                counter += 1
                img[i, j] = counter
                neighbors[counter] = set()
                continue
            nzero = np.any(pos)
            if nzero:
                areas = np.argwhere(pos > 1)
                if len(areas) == 1:
                    img[i, j] = pos[areas]
                else:
                    k = areas[0][0]
                    img[i, j] = pos[k]
                    for x in areas:
                        neighbors[pos[k]].add(pos[x][0])

    return (img, neighbors)


def secondIteration(img, neighbors):
    for key in reversed(neighbors.keys()):
        for area in neighbors[key]:
            img[img == area] = key
    areas = set(img.astype('int').flatten())
    areas.remove(0)

    return (areas, img)


def generalM(img, p, q, color):
    sum = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            sum += np.power(x, p) * np.power(y, q) * (img[x, y]
                    == color)
    return sum

def coinValue(seg, centers, areas):
    classifications = [1] * len(centers)
    for (k, (center, area)) in enumerate(zip(centers, areas)):
        pixel_count = np.count_nonzero(seg == area)
        if pixel_count > 4000:
            classifications[k] = 5
    return classifications


def thresholds(img, threshold):
    out = np.ones_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] >= threshold:
                out[i, j] = 0
    return out


def plot(segmentation, color, centers, file):
    plt.subplot(1, 2, 1)
    plt.imshow(segmentation, cmap='gray')
    plt.title('Segmentace')

    plt.subplot(1, 2, 2)
    plt.imshow(file)
    for center in centers:
        plt.scatter(center[0], center[1])
        print("center:", center)
    plt.title('Teziste nalezenych objektu')

    plt.show()


def segmentation(file):
    file = file.astype('float')
    green = file[:, :, 1] * 255 / (file[:, :, 0] + file[:, :, 1]
                                   + file[:, :, 2])
    green = green.astype('uint8')

    segmentation = thresholds(green, 100)
    return segmentation


def coloring(seg):
    (color, centers, areas) = colorArea(seg)
    print("color:", color)
    print("centers:", centers)
    
    classification = coinValue(color, centers, areas)
    for (c, center) in zip(classification, centers):
        print ('Na souradnici teziste', center, 'se nachazi', c)
    print ('Celkova hodnota minc: ', sum(classification))

    return (color, centers)


if __name__ == '__main__':
    file = cv2.imread('cv07_segmentace.bmp')

    seg = segmentation(file)
    (c, centers) = coloring(seg)

    plot(seg, c, centers, file)