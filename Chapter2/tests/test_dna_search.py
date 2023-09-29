# tests_dna_search.py
# unit test of dna_search.py
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

from enum import IntEnum
from typing import Tuple, List

import dna_search


class DnaSearchTestCase(unittest.TestCase):
    def test_linear_contains(self) -> None:
        Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
        Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
        Gene = List[Codon]  # type alias for genes

        gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

        my_gene: Gene = dna_search.string_to_gene(gene_str)

        acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
        gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

        self.assertTrue(dna_search.linear_contains(my_gene, acg))
        self.assertFalse(dna_search.linear_contains(my_gene, gat))


if __name__ == '__main__':
    unittest.main()
