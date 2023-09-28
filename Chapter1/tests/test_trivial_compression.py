# tests_fib.py
# unit test of trivial compression
# Copyright 2023 Kyungwon Chun
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

import unittest

from sys import getsizeof

import trivial_compression


class TrivialCompressionTestCase(unittest.TestCase):
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
        
    def test_restoration(self) -> None:
        compressed: trivial_compression.CompressedGene = trivial_compression.CompressedGene(self.original)
        self.assertEqual(self.original, compressed.decompress())

    def test_efficiency(self) -> None:
        original_bytes: int = getsizeof(self.original)

        compressed: trivial_compression.CompressedGene = trivial_compression.CompressedGene(self.original)
        compressed_bytes: int = getsizeof(compressed.bit_string)

        self.assertLess(compressed_bytes, original_bytes)


class ErgonomicCompressorTestCase(unittest.TestCase):
    original: str = "I am a boy."

    def test_restoration(self) -> None:
        compressed: trivial_compression.ErgonomicCompressor = trivial_compression.ErgonomicCompressor(self.original)
        self.assertEqual(self.original, compressed.decompress())

    def test_efficiency(self) -> None:
        original_bytes: int = getsizeof(self.original)

        compressed: trivial_compression.ErgonomicCompressor = trivial_compression.ErgonomicCompressor(self.original)
        compressed_bytes: int = getsizeof(compressed.bit_string)

        self.assertLess(compressed_bytes, original_bytes)

    def test_getitem(self) -> None:
        compressed: trivial_compression.ErgonomicCompressor = trivial_compression.ErgonomicCompressor(self.original)
        for i, _ in enumerate(self.original):
            self.assertEqual(compressed[i], self.original[i])

    def test_iteration(self) -> None:
        compressed: trivial_compression.ErgonomicCompressor = trivial_compression.ErgonomicCompressor(self.original)
        for i, char in enumerate(compressed):
            self.assertEqual(char, self.original[i])


if __name__ == '__main__':
    unittest.main()
