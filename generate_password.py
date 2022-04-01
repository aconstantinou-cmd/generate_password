import argparse
import random
import os


def main():
    parser = argparse.ArgumentParser(description='Generate random password')
    parser.add_argument('-l', '--length', type=int, help='length of password')
    parser.add_argument('-f', '--file', help='file to save password')
    args = parser.parse_args()
    if args.length:
        password = generate_password(args.length)
        print(password)
        if args.file:
            save_password(args.file, password)
    else:
        print('No length specified')


def generate_password(length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
    return ''.join(random.choice(chars) for _ in range(length))


def save_password(file, password):
    with open(file, 'w') as f:
        f.write(password)
    print('Password saved to file: {}'.format(os.getcwd() + '/' + file))


if __name__ == '__main__':
    main()

