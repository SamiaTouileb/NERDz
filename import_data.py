import tarfile
import argparse

class Data(object):
    def __init__(self, lang, data):
        self.lang = lang
        self.data = data
        self.length = len(self.data)

    def __getitem__(self, x):
        return self.data[x]

    def to_conll(self, outfile):
        with open(outfile, "w") as out:
            for sent, anns in self.data:
                for token, ann in zip(sent, anns):
                    out.write("{}\t{}\n".format(token, ann))
                out.write("\n")

class NER_Dataset(object):

    def __init__(self, data_dirs):
        self.data_dirs = data_dirs
        self.datasets = {}
        for data_dir in self.data_dirs:
            self.add_tar_data(data_dir)

    def add_tar_data(self, data_dir):
        data = []
        tar = tarfile.open(data_dir, "r:gz")
        for member in tar.getmembers():
            f = tar.extractfile(member)
            if f is not None:
                #dataset = []
                sent, sent_anns = [], []
                for line in f.readlines():
                    line = line.decode("utf8")
                    if line.strip() == "":
                        data.append((sent, sent_anns))
                        sent, sent_anns = [], []
                    else:
                        ltok, ann = line.strip().split("\t")
                        lang, tok = ltok.split(":", 1)
                        sent.append(tok)
                        sent_anns.append(ann)
                #data.append(dataset)
        self.datasets[lang] = Data(lang, data)

    def combine_data(self, comb_strategy="concat"):
        """
        concat: simply concatenate all datasets
        subsample: subsample the largest datasets
        oversample: oversample the smallest datasets
        random: randomly choose
        """
        final_data = []
        if comb_strategy == "concat":
            for lang, dataset in self.datasets.items():
                final_data.extend(dataset.data)
        if comb_strategy == "subsample":
            smallest = 100000000000
            for dataset in self.datasets.values():
                if dataset.length < smallest:
                    smallest = dataset.length
            for lang, dataset in self.datasets.items():
                final_data.extend(dataset.data[:smallest])
        if comb_strategy == "oversample":
            largest = 0
            for dataset in self.datasets.values():
                if dataset.length > largest:
                    largest = dataset.length
            for lang, dataset in self.datasets.items():
                oversample_num = largest / dataset.length
                i = int(oversample_num)
                f = oversample_num % 1
                extra = int(f * dataset.length)
                for oversample in range(i):
                    final_data.extend(dataset.data)
                final_data.extend(dataset.data[:extra])

        self.combined_data = Data("combined", final_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", nargs="+", default=["ar", "mt", "he", "fa", "ur"])

    args = parser.parse_args()

    for lang in args.langs:
        tardir = "panx_dataset/{}.tar.gz".format(lang)
        dataset = NER_Dataset([tardir])
        dataset.datasets[lang].to_conll("data/{}.txt".format(lang))

    dataset = NER_Dataset(["panx_dataset/{}.tar.gz".format(lang) for lang in args.langs])
    dataset.combine_data("oversample")
    dataset.combined_data.to_conll("data/combined-oversample.txt")

    dataset.combine_data("undersample")
    dataset.combined_data.to_conll("data/combined-undersample.txt")
