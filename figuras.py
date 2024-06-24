def draw_square(size):
    for i in range(size):
        for j in range(size):
            print('*', end=' ')
        print()

def draw_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print('*', end=' ')
        print()

def draw_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '* ' * i)

def draw_rhombus(diagonal):
    for i in range(1, diagonal // 2 + 2):
        print(' ' * (diagonal // 2 - i + 1) + '* ' * i)
    for i in range(diagonal // 2, 0, -1):
        print(' ' * (diagonal // 2 - i + 1) + '* ' * i)

if __name__ == "__main__":
    print("Cuadrado:")
    draw_square(5)
    print("\nRectángulo:")
    draw_rectangle(7, 3)
    print("\nTriángulo:")
    draw_triangle(5)
    print("\nRombo:")
    draw_rhombus(7)
