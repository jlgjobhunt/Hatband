# hatband_v0.py
# This is a copy of Joshua Greenfield's original Hatband
# taken from a Jupyter Notebook before getting double whammied
# by hurricanes in Fall 2024 in Tampa Bay, FL.
# This was seemingly perfect for my project with Rochelle Gemma if it only
# had the work put into it.

hatband = {   
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

# This record ought be stored in 'prefix-?!-short'.
record = {
    'key': '?!',
    'value': 'Amazing Interobang?!',
    'hatband': 'prefix-?!-short',
    # ISO 8601 Date-Time Format: YYYY-MM-DDTHH:MM:SSZ where Z means UTC.
    # Without Z, it is the locale time, which should be avoided if the
    # hatband were to be utilized for time-series purposes. The reason
    # why UTC matters to this use-case is that after sorting each hatband
    # location's list copy, it should merge any records added after the
    # UTC datetime that the copy was made.
    'last-changed': 'YYYY-MM-DDTHH:MM:SSZ'
}

def hatband_insertL(record: dict) -> int:

    location = record['hatband']

    hatband[location].insert(0,record)

    # Returns index where record was stored.
    return 0


def hatband_insertR(record: dict) -> int:

    location = record['hatband']

    hatband[location].append(record)

    # Returns index where record was stored.
    return (len(hatband[location]) - 1)


def hatband_insertM(record: dict) -> int:

    location = record['hatband']

    location_length = len(hatband[location])

    if location_length > 2 and location_length % 2 == 0:
        hatband[location].insert(((location_length) / 2), record)
        # Returns index where record was stored.
        return (location_length) / 2
    elif location_length > 2 and location_length % 2 == 1:
        hatband[location].insert(((location_length - 1) / 2 ), record)
        # Returns index where record was stored.
        return (location_length - 1) / 2


def hatband_retrieve(location: str, key: str, index=None):
    last_index = len(hatband[location]) - 1

    if 0 > last_index:
        return {}, -1

    elif index != None:
        target = hatband[location][index]
        if target.get('key') == key:
            return target, index
        else:
            for i in range(index, last_index):
                target = hatband[location][i]
                if target.get('key') == key:
                    return target, i
                    
            if i == last_index:
                return {}, -1
    
    elif index == None:
        for i in range(last_index):
            target = hatband[location][i]
            if target.get('key') == key:
                return target, i
        
        if i == last_index:
            return {}, -1
        
