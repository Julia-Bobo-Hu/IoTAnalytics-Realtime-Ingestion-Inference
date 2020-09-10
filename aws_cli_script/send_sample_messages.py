import argparse
import json

import boto3


def main():
    # Parse command line arguments
    parser, args = parse_args()

    client = boto3.client('iot-data')
    count = 0

    with open(args.datafile) as f:
        messages = json.load(f)

    for message in messages:
        response = client.publish(
            topic=args.topic,
            qos=0,
            payload=json.dumps(message))

        count += 1
        print(response)
        print('Total messages sent: {}/{}'.format(count, len(messages)))


# Read in command-line parameters
def parse_args():
    parser = argparse.ArgumentParser(description="Send sample messages to AWS IoT topic")
    parser.add_argument('-f', '--datafile',
                        required=True,
                        default='raw_data_small.json',
                        help="file containing messages")
    parser.add_argument('-t', '--topic',
                        required=True,
                        default='check-ride-iot-device-data',
                        help="topic to send messages to")

    args = parser.parse_args()
    return parser, args


if __name__ == '__main__':
    main()