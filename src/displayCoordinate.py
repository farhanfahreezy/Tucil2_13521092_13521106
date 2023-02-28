import matplotlib.pyplot as plt

def displayCoordinate(arrayCoordinate, c1, c2):
    # c1 dan c2 adalah 2 koordinat yang akan digaris
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Masukin semua koordinat ke diagram
    for i in range(len(arrayCoordinate)):
        x, y, z = arrayCoordinate[i]
        ax.scatter(x, y, z, c='g',s=1)

    # Buat garis diantara c1 dan c2
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    ax.scatter(x1, y1, z1, c='r',s=10)
    ax.scatter(x2, y2, z2, c='r',s=10)
    ax.plot([x1, x2], [y1, y2], [z1, z2], c='r')

    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')
    plt.show()