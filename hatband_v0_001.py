version = "v0.0001"

class Hatband:

    def __init__(self):
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


    def hatband_insertL(self, record):
        location = record['hatband']
        self.categories[location].insert(0, record)
        return 0


    def hatband_insertR(self, record):
        location = record['hatband']
        self.categories[location].append(record)
        return len(self.categories[location]) - 1


    def hatband_insertM(self, record):
        location = record['hatband']
        location_length = len(self.categories[location])
        if location_length > 2 and location_length % 2 == 0:
            self.categories[location].insert(int((location_length) / 2), record)
            return int(location_length / 2)
        elif location_length > 2 and location_length % 2 == 1:
            self.categories[location].insert(int((location_length - 1) / 2), record)
            return int((location_length - 1) / 2)
        

    def hatband_retrieve(self, location, key, index=None):
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
        
