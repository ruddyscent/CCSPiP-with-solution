import unittest

from typing import Tuple, TypeVar

from genetic_algorithm import GeneticAlgorithm
from chromosome import Chromosome


T = TypeVar('T', bound='TestChromosome') # for returning self

# Create a concrete subclass of Chromosome for testing
class TestChromosome(Chromosome):
    def fitness(self) -> float:
        return 0.0

    @classmethod
    def random_instance(cls) ->  T:
        return TestChromosome()

    def crossover(self, other: T) -> Tuple[T, T]:
        return self, other
    
    def mutate(self) -> None:
        pass

class TestGeneticAlgorithmMethods(unittest.TestCase):
    def setUp(self):
        self.population = [TestChromosome() for _ in range(10)]
        self.ga = GeneticAlgorithm(self.population, threshold=1.0, max_generations=100, mutation_chance=0.01, crossover_chance=0.7, selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)

    def test_init(self):
        self.assertEqual(self.ga._population, self.population)
        self.assertEqual(self.ga._threshold, 1.0)
        self.assertEqual(self.ga._max_generations, 100)
        self.assertEqual(self.ga._mutation_chance, 0.01)
        self.assertEqual(self.ga._crossover_chance, 0.7)
        self.assertEqual(self.ga._selection_type, GeneticAlgorithm.SelectionType.TOURNAMENT)

    def test_pick_roulette(self):
        parents = self.ga._pick_roulette([1.0 for _ in range(10)])
        self.assertIn(parents[0], self.population)
        self.assertIn(parents[1], self.population)

    def test_pick_tournament(self):
        parents = self.ga._pick_tournament(5)
        self.assertIn(parents[0], self.population)
        self.assertIn(parents[1], self.population)

if __name__ == '__main__':
    unittest.main()