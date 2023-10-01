# trivial_compression.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import math

from typing import Dict, Set

class ErgonomicCompressor:
    def __init__(self, text: str) -> None:
        self.current: int = 0

        self.chars: Set[str] = set(list(text))
        self.bit_size: int = math.ceil(math.log2(len(self.chars)))
        self.mask: int = 2**self.bit_size - 1

        self.char2bit: Dict[str, int] = {char: bit for bit, char in enumerate(self.chars)}
        self.bit2char: Dict[int, str] = {bit: char for char, bit in self.char2bit.items()}
        
        self._compress(text)

    def _compress(self, text: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for char in list(text):
            self.bit_string <<= self.bit_size  # shift left bit_size bits
            self.bit_string += self.char2bit[char]
            
    def decompress(self) -> str:
        return "".join(char for char in self)
    
    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()

    def __getitem__(self, index: int) -> str:
        bit_length: int = self.bit_string.bit_length() - 1

        if index < 0 or index * self.bit_size >= bit_length:
            raise IndexError("Index out of range")
        
        bits: int = self.bit_string >> (bit_length - (index + 1) * self.bit_size) & self.mask  # get just relevant bits
        return self.bit2char[bits]
    
    def __iter__(self) -> ErgonomicCompressor:
        return self
    
    def __next__(self) -> str:
        if self.current * self.bit_size >= self.bit_string.bit_length() - 1:
            self.current = 0
            raise StopIteration
        else:
            char: str = self[self.current]
            self.current += 1
            return char


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._ergonomic_compressor = ErgonomicCompressor(gene)

    def decompress(self) -> str:
        return self._ergonomic_compressor.decompress()

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()

    @property
    def bit_string(self) -> int:
        return self._ergonomic_compressor.bit_string


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))

    original: str = "ABCA"
    compressed: ErgonomicCompressor = ErgonomicCompressor(original)
    for i, _ in enumerate(original):
        print(compressed[i])
    