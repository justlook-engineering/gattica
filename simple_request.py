# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""

import requests
import argparse

# Initialize the PyTorch REST API endpoint URL.
PyTorch_REST_API_URL = 'http://127.0.0.1:5000/predict'


def predict_result(sequence):
    # Initialize image path
    # image = open(image_path, 'rb').read()
    payload = {"seq": sequence}
    print(payload)

    # Submit the request.
    headers = {'Content-Type': 'application/json'}
    r = requests.post(PyTorch_REST_API_URL, json=payload, headers=headers)
    response = r.json()
    print(response)
    # Ensure the request was successful.
    # if r['success']:
    #     print(r)
    #     # Loop over the predictions and display them.
    #     # for (i, result) in enumerate(r['predictions']):
    #     #     print('{}. {}: {:.4f}'.format(i + 1, result['label'],
    #     #                                   result['probability']))
    # # Otherwise, the request failed.
    # else:
    #     print('Request failed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classification demo')
    # parser.add_argument('--arr', type=list, help='Array of items sequence')
    parser.add_argument('-l','--list', nargs='+', type=int, help='<Required> Set flag', required=True)
    # parser.add_argument('--nargs', nargs='+')
    args = parser.parse_args()
    predict_result(args.list)
