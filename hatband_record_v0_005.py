# hatband_record_v0_005.py

class Record:

    version = "v0.005"

    def __init__(self, content_chunk):
        if len(content_chunk) < 5:
            raise ValueError("Content chunk must be at least 5 characters long.")

        self.content_chunk = content_chunk
        self.short_index_key = self._generate_short_index_key()
        self.medium_index_key = self._generate_medium_index_key()
        self.long_index_key = self._generate_long_index_key()
        self.value = content_chunk

    def _generate_short_index_key(self):
        """Generates a short index key."""
        return self._derive_key(self.content_chunk, length=5)
    
    def _generate_medium_index_key(self):
        """Generates a medium index key."""
        return self._derive_key(self.content_chunk, length=25)
    
    def _generate_long_index_key(self):
        """Generates a long index key."""
        return self._derive_key(self.content_chunk, length=50)
    
    def _derive_key(self, content_chunk, length):
        """Derives a key of the specified length."""
        if len(content_chunk) >= length:
            return content_chunk[:length]
        else:
            return content_chunk
    
    def to_dict(self):
        return {
            'short_index_key': self.short_index_key,
            'medium_index_key': self.medium_index_key,
            'long_index_key': self.long_index_key,
            'value': self.value
        }
    


