"""An example of what some core functionality for a project might look like"""
import argparse
import requests

DEFAULT_WEBPAGE = "https://www.example.com"


def make_request(webpage: str = DEFAULT_WEBPAGE) -> requests.Response:
    """Make a simple request to a webpage"""
    response = requests.get(webpage, timeout=5)
    return response


def main():
    """Main functionality of core module"""
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('-w', '--webpage', help='webpage for the request',
                        default=DEFAULT_WEBPAGE)

    # Parse the arguments
    args = parser.parse_args()

    # access the 'webpage' argument and pass to make_request
    print(make_request(args.webpage))


if __name__ == '__main__':
    main()
