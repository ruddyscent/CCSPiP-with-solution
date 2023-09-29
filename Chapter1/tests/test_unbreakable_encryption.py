# tests_unbreakable_encryption.py
# unit test of unbreakable encryption
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

import unbreakable_encryption


class UnbreakableEncryptionTestCase(unittest.TestCase):
    original: str = "One Time Pad!"

    def test_restoration(self) -> None:
        key1: int
        key2: int
        key1, key2 = unbreakable_encryption.encrypt(self.original)
        result: str = unbreakable_encryption.decrypt(key1, key2)
        self.assertEqual(result, self.original)


class UnbreakableEncryptionImageTestCase(unittest.TestCase):
    original_path: str = "/workspace/Chapter1/assets/cover.png"

    def test_restoration(self) -> None:
        key1: int
        key2: int
        key1, key2 = unbreakable_encryption.encrypt_image(self.original_path)
        result: bytes = unbreakable_encryption.decrypt_image(key1, key2)

        with open(self.original_path, "rb") as img_file:
            original_bytes: bytes = img_file.read()
        
        self.assertEqual(result, original_bytes)


if __name__ == '__main__':
    unittest.main()
