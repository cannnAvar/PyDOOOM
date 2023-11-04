from wad_reader import WadReader


class WADData:
    def __init__(self, engine) -> None:
        self.read = WadReader(engine.wad_path)
        self.read.close()