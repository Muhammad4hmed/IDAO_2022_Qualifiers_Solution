from sys import getsizeof
import yaml
import pandas as pd
import gc
from pathlib import Path
from baseline import prepare_model
from baseline import read_pymatgen_dict
import os
# import time
# import psutil
# process = psutil.Process(os.getpid())


def main(config):
    model = prepare_model(
        float(config["model"]["cutoff"]), float(config["model"]["lr"])
    )
    model.load_weights(config['checkpoint_path'])
    dataset_path = Path(config['test_datapath'])
    struct = {item.name.strip('.json'): read_pymatgen_dict(
        item) for item in (dataset_path/'structures').iterdir()}
    # print(process.memory_info().rss/(1024*1024))
    private_test = pd.DataFrame(
        columns=['id', 'structures'], index=struct.keys())
    private_test = private_test.assign(structures=struct.values())
    preds = []
    i = 0
    # start = time.time()
    for st in private_test.structures:
        preds.append(model.predict_structure(st)[0])
        i += 1
        if i % 250 == 0:
            gc.collect()
            # print(process.memory_info().rss/(1024*1024))
    private_test = private_test.assign(predictions=preds)
    # private_test = private_test.assign(
    #     predictions=model.predict_structures(private_test.structures))
    # gc.collect()
    private_test[['predictions']].to_csv('./submission.csv', index_label='id')
    # print(time.time()-start)
    # print(process.memory_info().rss/(1024*1024))


if __name__ == '__main__':
    with open("config.yaml") as file:
        config = yaml.safe_load(file)
    main(config)
