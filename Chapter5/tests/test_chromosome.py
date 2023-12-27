import unittest

from typing import TypeVar, Tuple

from chromosome import Chromosome

T = TypeVar('T', bound='Chromosome') # for returning self

# Create a concrete subclass of Chromosome for testing
class TestChromosome(Chromosome):
    def fitness(self) -> float:
        return 0.0

    @classmethod
    def random_instance(cls) -> T:
        return TestChromosome()

    def crossover(self, other: T) -> Tuple[T, T]:
        return self, other

    def mutate(self) -> None:
        pass
    
class TestChromosomeMethods(unittest.TestCase):
    def setUp(self):
        self.chromosome = TestChromosome()

    def test_fitness(self):
        self.assertEqual(self.chromosome.fitness(), 0.0)

    def test_random_instance(self):
        self.assertIsInstance(TestChromosome.random_instance(), TestChromosome)

    def test_crossover(self):
        other = TestChromosome()
        child1, child2 = self.chromosome.crossover(other)
        self.assertEqual(child1, self.chromosome)
        self.assertEqual(child2, other)

if __name__ == '__main__':
    unittest.main()