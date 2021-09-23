import tarfile

class NER_Dataset(object):

    def __init__(self, data_dirs):
        self.data_dirs = data_dirs
        self.data = {}
        for data_dir in self.data_dirs:
            self.add_tar_data(data_dir)

    def add_tar_data(self, data_dir):
        data = []
        tar = tarfile.open(data_dir, "r:gz")
        for member in tar.getmembers():
            f = tar.extractfile(member)
            if f is not None:
                dataset = []
                sent, sent_anns = [], []
                for line in f.readlines():
                    line = line.decode("utf8")
                    if line.strip() == "":
                        dataset.append((sent, sent_anns))
                        sent, sent_anns = [], []
                    else:
                        ltok, ann = line.strip().split("\t")
                        lang, tok = ltok.split(":", 1)
                        sent.append(tok)
                        sent_anns.append(ann)
                data.append(dataset)
        self.data[lang] = data


dataset = NER_Dataset(["panx_dataset/eu.tar.gz"])
