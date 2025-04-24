from sphere import Sphere
from cube import Cube
from cylinder import Cylinder
import random

def generate_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
    if shape_type == 'Sphere':
        radius = random.randint(1, 10)
        return Sphere(radius)
    elif shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)
    elif shape_type == 'Cube':
        side = random.randint(1, 10)
        return Cube(side)

def create_shape_manually():
    print("Choose a shape:")
    print("1. Sphere")
    print("2. Cylinder")
    print("3. Cube")
    choice = input("Choose the number (1-3): ")

    if choice == '1':
        radius = float(input("Write radius: "))
        return Sphere(radius)
    elif choice == '2':
        radius = float(input("Write radius: "))
        height = float(input("Write height: "))
        return Cylinder(radius, height)
    elif choice == '3':
        side = float(input("Write the side length: "))
        return Cube(side)
    else:
        print("Error")
        return None

if __name__ == "__main__":
    main()
    def main():
        print("Choose the option: ")
        print("1. Generate Random Shapes")
        print("2. Enter Shapes Manually")
        mode = input("Choose an option: ")

        shapes = []

        if mode == '1':
            count = int(input("How many shapes do you want to generat? "))
            shapes = [generate_random_shape() for _ in range(count)]
        elif mode == '2':
            count = int(input("How many shapes do you want to enter? "))
            for _ in range(count):
                shape = create_shape_manually()
                if shape:
                    shapes.append(shape)
        else:
            print("Error")
            return

        print("Shape Information:")
        for i, shape in enumerate(shapes, 1):
            print(f"Shape {i}: {shape.__class__.__name__}")
            print(f"  Surface Area: {shape.surface_area():.2f}")
            print(f"  Volume: {shape.volume():.2f}\n")
