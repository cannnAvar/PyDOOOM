from wad_data import WADData

class DoomEngine:
    def __init__(self, wad_path="wad/DOOM.WAD") -> None:
        self.wad_path = wad_path
        self.on_init()
        
    def on_init(self):
        self.wad_path = WADData(self, map_name="E1M1")

if __name__ == "__main__":
        doom = DoomEngine()