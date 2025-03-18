# hatband_record_v0_009.py

class Record:
    """
    Represents a data record with generated index keys.

    Attributes:
        content_chunk (str): The content of the record.
        short_index_key (str): A short index key (first 5 characters).
        medium_index_key (str): A medium index key (first 25 characters).
        long_index_key (str): A long index key (first 50 characters).
        value (str): The content of the record.
    """

    version = "v0.009"

    def __init__(self, content_chunk):
        if len(content_chunk) < 5:
            raise ValueError("Content chunk must be at least 5 characters long.")

        self.content_chunk = content_chunk
        self.value = content_chunk
        self.short_index_key = self._generate_short_index_key()
        self.medium_index_key = self._generate_medium_index_key()
        self.long_index_key = self._generate_long_index_key()
        
        if len(content_chunk) >= 50:
            self.key = self.long_index_key
        elif len(content_chunk) >= 25:
            self.key = self.medium_index_key
        else:
            self.key = self.short_index_key
        

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
        """
        Derives a key of the specified length by truncating the content chunk.
        
        Args:
            content_chunk (str): The content chunk to derive the key from.
            length (int): The desired length of the key.

        Returns:
            str: The derived key.
            
        Raises:
            ValueError: If the length is invalid.
        
        """
        if length < 0:
            raise ValueError("Length must be a non-negative integer.")

        if len(content_chunk) >= length:
            return content_chunk[:length]
        else:
            return content_chunk
    
    def to_dict(self):
        return {
            'short_index_key': self.short_index_key,
            'medium_index_key': self.medium_index_key,
            'long_index_key': self.long_index_key,
            'value': self.value,
            'key': self.key
        }
