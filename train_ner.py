import argparse
from simpletransformers.ner import NERModel

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_data")
    parser.add_argument("test_data")

    args = parser.parse_args()

    model = NERModel("xlmroberta", "xlm-roberta-base", use_cuda=False)
    model.train_model(args.train_data)
    result, output, preds = model.eval_model(args.test_data)
