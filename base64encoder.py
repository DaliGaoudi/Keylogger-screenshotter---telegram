import base64
import sys

def main():
    if len(sys.argv) != 2:
        print('Encode a file with Base64\nUsage:\n%s filename' % sys.argv[0])
        sys.exit()

    fname = sys.argv[1]
    with open(fname, 'rb') as f:
        data = f.read()

    with open(fname + 'b64', 'wb') as f:
        f.write(base64.encodebytes(data))

if __name__ == '__main__':
    main()