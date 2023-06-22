import json
import numpy as np
import argparse

if __name__ == '__main__':

    argparser = argparse.ArgumentParser()

    argparser.add_argument('--ensemble', type=str, default='weighted')
    argparser.add_argument('--output', type=str, default='./final_submit.json')
    args = argparser.parse_args()
    np.random.seed(42)

    ensemble_type = args.ensemble
    print("ensemble type: %s" %ensemble_type)

    prob = 0.25  # w/ prob=0.4 use file2
    weight = 0.25  # weight for file2

    file1 = './submit_ttm1.json'
    file2 = './submit_ttm2.json'

    target_file = args.output
    # Open the JSON file in read mode
    with open(file1, 'r') as f:
        # Load the JSON data into a Python dictionary
        data = json.load(f)

    with open(file2, 'r') as f:
        # Load the JSON data into a Python dictionary
        data2 = json.load(f)

    for key, value in data.items():
        if key != 'results':
            pass
        else:
            for i in range(len(data['results'])):
                if ensemble_type == 'random':
                    sample = np.random.rand()
                    if sample <= prob:
                        data['results'][i]['score'] = data2['results'][i]['score']
                elif ensemble_type == 'weighted':
                    data['results'][i]['score'] = (1 - weight) * data['results'][i]['score'] + weight * data2['results'][i]['score']
                else:
                    raise NotImplementedError("Ensemble method not implemented")

    # Write the dictionary to the JSON file
    with open(target_file, "w") as f:
        json.dump(data, f)
