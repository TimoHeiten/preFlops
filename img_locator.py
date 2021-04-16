import os

class PreFlop:

    def __init__(self, dir_name):
        self.name = dir_name
        self.root = os.path.join("img-src", dir_name)
        self.items = os.listdir(self.root)

    def __iter__(self):
        with_path = [(img_name, os.path.join(self.root, img_name)) for img_name in self.items]
        return iter(with_path)

    def __str__(self):
        return ",".join(iter(self)) + "- from -" + self.root

    def get_columns(self):
        return len(self.items)


cold_4b = PreFlop('Cold 4B')
rfi = PreFlop('RFI')
vs_3b = PreFlop('vs 3B')
vs_4b = PreFlop('vs 4B')
vs_rfi = PreFlop('vs RFI')

all_flops = [cold_4b, rfi, vs_3b, vs_4b, vs_rfi]
rows = len(all_flops)
