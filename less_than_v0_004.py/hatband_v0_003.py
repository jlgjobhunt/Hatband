import math
import json
import os



def floor(x):
    return math.floor(x)

class Hatband:

    version = "v0.003"

    def __init__(self, storage_dir="hatband_storage", use_memory=False):
        self.storage_dir = storage_dir
        self.use_memory = use_memory
        if not self.use_memory:
            os.makedirs(self.storage_dir, exist_ok=True)
        self.categories = {
            # ... (Joshua Greenfield's categories definitions)
            'negative-nine-long': [],
            'negative-nine-medium': [],
            'negative-nine-short': [],
            'negative-eight': [],
            'negative-seven': [],
            'negative-six': [],
            'negative-five': [],
            'negative-four': [],
            'negative-three': [],
            'negative-two': [],
            'negative-one': [],
            'zero-long': [],
            'zero-medium': [],
            'zero-short': [],
            'one-long': [],
            'one-medium': [],
            'one-short': [],
            'two-long': [],
            'two-medium': [],
            'two-short': [],
            'three-long': [],
            'three-medium': [],
            'three-short': [],
            'four-long': [],
            'four-medium': [],
            'four-short': [],
            'five-long': [],
            'five-medium': [],
            'five-short': [],
            'six-long': [],
            'six-medium': [],
            'six-short': [],
            'seven-long': [],
            'seven-medium': [],
            'seven-short': [],
            'eight-long': [],
            'eight-medium': [],
            'eight-short': [],
            'nine-long': [],
            'nine-medium': [],
            'nine-short': [],
            'a-long': [],
            'a-medium': [],
            'a-short': [],
            'A-long': [],
            'A-medium': [],
            'A-short': [],
            'b-long': [],
            'b-medium': [],
            'b-short': [],
            'B-long': [],
            'B-medium': [],
            'B-short': [],
            'c-long': [],
            'c-medium': [],
            'c-short': [],
            'C-long': [],
            'C-medium': [],
            'C-short': [],
            'd-long': [],
            'd-medium': [],
            'd-short': [],
            'D-long': [],
            'D-medium': [],
            'D-short': [],
            'e-long': [],
            'e-medium': [],
            'e-short': [],
            'E-long': [],
            'E-medium': [],
            'E-short': [],
            'f-long': [],
            'f-medium': [],
            'f-short': [],
            'F-long': [],
            'F-medium': [],
            'F-short': [],
            'g-long': [],
            'g-medium': [],
            'g-short': [],
            'G-long': [],
            'G-medium': [],
            'G-short': [],
            'h-long': [],
            'h-medium': [],
            'h-short': [],
            'H-long': [],
            'H-medium': [],
            'H-short': [],
            'i-long': [],
            'i-medium': [],
            'i-short': [],
            'I-long': [],
            'I-medium': [],
            'I-short': [],
            'j-long': [],
            'j-medium': [],
            'j-short': [],
            'J-long': [],
            'J-medium': [],
            'J-short': [],
            'k-long': [],
            'k-medium': [],
            'k-short': [],
            'K-long': [],
            'K-medium': [],
            'K-short': [],
            'l-long': [],
            'l-medium': [],
            'l-short': [],
            'L-long': [],
            'L-medium': [],
            'L-short': [],
            'm-long': [],
            'm-medium': [],
            'm-short': [],
            'M-long': [],
            'M-medium': [],
            'M-short': [],
            'n-long': [],
            'n-medium': [],
            'n-short': [],
            'N-long': [],
            'N-medium': [],
            'N-short': [],
            'o-long': [],
            'o-medium': [],
            'o-short': [],
            'O-long': [],
            'O-medium': [],
            'O-short': [],
            'p-long': [],
            'p-medium': [],
            'p-short': [],
            'P-long': [],
            'P-medium': [],
            'P-short': [],
            'q-long': [],
            'q-medium': [],
            'q-short': [],
            'Q-long': [],
            'Q-medium': [],
            'Q-short': [],
            'r-long': [],
            'r-medium': [],
            'r-short': [],
            'R-long': [],
            'R-medium': [],
            'R-short': [],
            's-short': [],
            's-medium': [],
            's-long': [],
            'S-short': [],
            'S-medium': [],
            'S-long': [],
            't-short': [],
            't-medium': [],
            't-long': [],
            'T-short': [],
            'T-medium': [],
            'T-long': [],
            'u-short': [],
            'u-medium': [],
            'u-long': [],
            'U-short': [],
            'U-medium': [],
            'U-long': [],
            'v-short': [],
            'v-medium': [],
            'v-long': [],
            'V-short': [],
            'V-medium': [],
            'V-long': [],
            'w-short': [],
            'w-medium': [],
            'w-long': [],
            'W-short': [],
            'W-medium': [],
            'W-long': [],
            'x-short': [],
            'x-medium': [],
            'x-long': [],
            'X-short': [],
            'X-medium': [],
            'X-long': [],
            'y-short': [],
            'y-medium': [],
            'y-long': [],
            'Y-short': [],
            'Y-medium': [],
            'Y-long': [],
            'z-short': [],
            'z-medium': [],
            'z-long': [],
            'Z-short': [],
            'Z-medium': [],
            'Z-long': [],
            'symbols-long': [],
            'symbols-medium': [],
            'symbols-short': [],
            'prefix-?!-long': [],
            'prefix-?!-medium': [],
            'prefix-?!-short': [],
        }
        if not self.use_memory:
            self.load_all_hatbands()
        

    def load_all_hatbands(self):
        if self.use_memory:
            return
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

        for filename in os.listdir(self.storage_dir):
            hatband_top_level_name = filename[:-5]
            self.categories[hatband_top_level_name] = self.load_hatband_from_file(hatband_top_level_name)


    def load_hatband_from_file(self, hatband_top_level_name):
        filepath = os.path.join(self.storage_dir, f"{hatband_top_level_name}.json")
        if os.path.exists(filepath):
            with open(filepath,'r') as f:
                try:
                    data = json.load(f)
                    print(f"DEBUGGING | Loaded data from {filepath} | {data}")
                    return data
                except json.JSONDecodeError:
                    print(f"DEBUGGING | {filepath} contains invalid JSON or is empty. Returning empty list.")
                    return []
        return []

    def save_hatband_to_file(self, hatband_top_level_name, data):
        if self.use_memory:
            return
        filepath = os.path.join(self.storage_dir, f"{hatband_top_level_name}.json")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"DEBUGGING | Saved data from {filepath}:\n\n{json.dumps(data, indent=4)}\n\n")


    def _get_file_path(self, location):
        return os.path.join(self.storage_dir, f"{location}.json")
    

    def hatband_insertL(self, record):
        hatband_top_level_name = record['hatband']
        if hatband_top_level_name not in self.categories:
                self.categories[hatband_top_level_name] = []
        self.categories[hatband_top_level_name].insert(0, record)
        if not self.use_memory:
            self.save_hatband_to_file(hatband_top_level_name, self.categories[hatband_top_level_name])
        return 0

    def reset_data(self):
        self._data = {}

    def _load_data(self, file_path):
        data = []
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                print(f"Debug: Loaded data from {file_path}: {data}")
            except json.JSONDecodeError:
                print(f"Debug: Error decoding JSON in {file_path}")
        else:
            print(f"DEBUGGING | File not found | {file_path}")
        return data
        
    def _save_data(self, file_path, data):
        try:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            print(f"""DEBUGGING | Saved data to {file_path}: 
                  
                  {data}
                  
                  """)
        except Exception as e:
            print(f"DEBUGGING | Error saving data to {file_path}: {e}")


    def hatband_insertR(self, record):
        location = record['hatband']
        if self.use_memory:
            if location not in self.categories:
                self.categories[location] = []
            self.categories[location].append(record)
            return len(self.categories[location]) - 1
        else:
            file_path = self._get_file_path(location)
            data = self._load_data(file_path)
            data.append(record)
            self._save_data(file_path, data)
            return len(data) - 1


    def hatband_insertM(self, record):
        location = record['hatband']
        if self.use_memory:
            location_length = len(self.categories[location])
            print(f"Location Length: {location_length}, Type: {type(location_length)}")
            modulo_result = location_length % 2
            print(f"Modulo Result: {modulo_result}, Type: {type(modulo_result)}")
            if location_length == 0:
                index = 0
                self.categories[location].insert(index, record)
                return 0
            elif modulo_result == 0:
                index = location_length // 2
                print(f"Calculated Index: {index}")
                print(f"Index to return: {index}")
                self.categories[location].insert(index, record)
                return index
            else:
                index = location_length // 2 + 1
                print(f"Calculated Index: {index}")
                print(f"Index to return: {index}")
                self.categories[location].insert(index, record)
                return index
        else:
            file_path = self._get_file_path(location)
            data = self._load_data(file_path)
            location_length = len(data)
            print(f"Location Length: {location_length}, Type: {type(location_length)}")
            modulo_result = location_length % 2
            print(f"Modulo Result: {modulo_result}, Type: {type(modulo_result)}")
            
            if location_length == 0:
                index = 0
                data.insert(index, record)
                self._save_data(file_path, data)
                return 0
            elif location_length % 2 == 0:
                index = location_length // 2
                print(f"Calculated Index: {index}")
                print(f"Index to return: {index}")
                data.insert(index, record)
                self._save_data(file_path, data)
                return index
            else:
                index = location_length // 2 + 1
                print(f"Calculated Index: {index}")
                print(f"Index to return: {index}")
                data.insert(index, record)
                self._save_data(file_path, data)
                return index


    def hatband_retrieve(self, location, key, index=None):
        if self.use_memory:
            last_index = len(self.categories[location]) - 1

            if 0 > last_index:
                return {}, -1
            
            elif index is not None:
                target = self.categories[location][index]
                if target.get('key') == key:
                    return target, index
                else:
                    for i in range(index, last_index + 1):
                        target = self.categories[location][i]
                        if target.get('key') == key:
                            return target, i
                        
                    return {}, -1
                
            elif index is None:
                for i in range(last_index + 1):
                    target = self.categories[location][i]
                    if target.get('key') == key:
                        return target, i
                    
                return {}, -1
        else:
            file_path = self._get_file_path(location)
            data = self._load_data(file_path)
            last_index = len(data) - 1
            if 0 > last_index:
                return {}, -1
            elif index is not None:
                if index > last_index:
                    return {}, -1
                target = data[index]
                if target.get('key') == key:
                    return target, index
                else:
                    for i in range(index, last_index + 1):
                        target = data[i]
                        if target.get('key') == key:
                            return target, i
                    return {}, -1
            elif index is None:
                for i in range(len(data)):
                    target = data[i]
                    if target.get('key') == key:
                        return target, i
                return {}, -1
            
        
        
