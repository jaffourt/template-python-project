# This is the main entry point of the module

# Import the required functions, classes, etc. from the module
from . import core

# Define the API of the module
__all__ = ['core']


def main():
    print('Hello, world!')


# Run the main function when the module is run directly
if __name__ == '__main__':
    main()
