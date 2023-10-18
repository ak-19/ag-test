import json
from unittest import TestCase as TC, main
from FileHandler import FileHandler
from Optimizer import Optimizer

class TestOptimizer(TC):

    def test_base_case(self):
        """Base test case as provided in the problem statement"""        
        data = FileHandler('./test-data/input-1.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_total_value = 16650
        self.assertEqual(expected_total_value, optimized_data['total_value'], 'Base Test case failed')

    def test_case_2(self):
        """Test case with multiple solutions and priority choice"""
        data = FileHandler('./test-data/input-2-2-solutions.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_data = None
        with open('./test-data/output-2-2-solutions.json', 'r') as f: expected_data = json.load(f)
        self.assertEqual(expected_data, optimized_data, 'Test case with multiple solutions and priority choice failed')

    def test_case_3(self):
        """Test case with duplicate names, should raise error"""
        data = FileHandler('./test-data/input-3-duplicates.json', '').load_data()
        with self.assertRaises(Exception) as context:
            Optimizer(data['items'],  data['total_space'])

    def test_case_4(self):
        """Test case with cycle dependencies, should raise error"""
        data = FileHandler('./test-data/input-4-cycle-error.json', '').load_data()
        with self.assertRaises(Exception) as context:
            Optimizer(data['items'],  data['total_space'])      

    def test_case_5(self):
        """Test case with 4 items, take 3 that make up to 49"""
        data = FileHandler('./test-data/input-5.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_total_value = 49
        self.assertEqual(expected_total_value, optimized_data['total_value'], 'Base Test case failed')

    def test_case_6(self):
        """Test case with 4 items, take 2 that make up to 46"""
        data = FileHandler('./test-data/input-6.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_total_value = 46
        self.assertEqual(expected_total_value, optimized_data['total_value'], 'Base Test case failed')   

    def test_case_7(self):
        """Test case with 20 items, that make up to 119"""
        data = FileHandler('./test-data/input-7.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_total_value = 119
        self.assertEqual(expected_total_value, optimized_data['total_value'], 'Base Test case failed')   

    def test_case_8(self):
        """Test case with 30 items, that make up to 119"""
        data = FileHandler('./test-data/input-8.json', '').load_data()
        optimized_data = Optimizer(data['items'],  data['total_space']).get_result()
        expected_total_value = 164
        self.assertEqual(expected_total_value, optimized_data['total_value'], 'Base Test case failed')                        
            
if __name__ == '__main__':
    main()