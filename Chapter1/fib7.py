# fib7.py
# Implementing the Fibonacci sequence using Binet's formula shown at
# https://en.wikipedia.org/wiki/Fibonacci_sequence
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

phi: float = (1 + 5 ** 0.5) / 2

def fib7(n: int) -> int:
    return int(round(phi**n / 5**0.5))

if __name__ == '__main__':
    print(fib7(5))
    print(fib7(50))