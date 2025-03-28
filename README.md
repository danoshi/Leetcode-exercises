# LeetCode Solutions and Course Exercises

Within this repository, you'll discover a collection of LeetCode problems that I've tackled, along with a README detailing my thought process for each one.

Additionally, I've included exercises from various courses focused on learning data structures and algorithms. In the README, I strive to provide explanations for these exercises, accompanied by illustrative code demonstrating the algorithms or data structures discussed.

1. Inside the `ArrayExercise` folder, you'll encounter various types of array problems that require solving specific challenges.

2. The `MathExercise` folder contains mathematical problems for exploration.

3. Within the `Sorting and Searching` folder, you'll discover problems related to sorting and searching, all of which I've solved.

4. Moving on to `StringsExercise`, this section encompasses a diverse range of solved problems centered around string manipulation and related topics.

5. Lastly, in the `frontendmasters` folder, you'll find solved exercises along with detailed descriptions focusing on data structures and algorithms.







## Test Results

```
============================= test session starts ==============================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0 -- /opt/hostedtoolcache/Python/3.12.9/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/Leetcode-exercises/Leetcode-exercises
configfile: pyproject.toml
plugins: cov-6.0.0
collecting ... collected 71 items

tests/array_problems/test_best_time_to_buy_and_sell_stock_ll.py::TestSolution::test_max_profit_a PASSED [  1%]
tests/array_problems/test_contains_duplicate.py::TestSolution::test_containsDuplicate PASSED [  2%]
tests/array_problems/test_height_checker.py::TestSolution::test_heightChecker PASSED [  4%]
tests/array_problems/test_intersection_of_two_arrays_ll.py::TestSolution::test_intersect PASSED [  5%]
tests/array_problems/test_max_consecutive_ones.py::TestSolution::test_findMaxConsecutiveOnes PASSED [  7%]
tests/array_problems/test_move_zeroes.py::TestSolution::test_moveZeroes PASSED [  8%]
tests/array_problems/test_plus_one.py::TestSolution::test_plusOne_multiple_digits_no_carry PASSED [  9%]
tests/array_problems/test_plus_one.py::TestSolution::test_plusOne_multiple_digits_with_carry PASSED [ 11%]
tests/array_problems/test_plus_one.py::TestSolution::test_plusOne_single_digit_no_carry PASSED [ 12%]
tests/array_problems/test_plus_one.py::TestSolution::test_plusOne_single_digit_with_carry PASSED [ 14%]
tests/array_problems/test_remove_duplicates_from_sorted_array.py::TestSolution::test_removeDuplicates PASSED [ 15%]
tests/array_problems/test_remove_element.py::TestSolution::test_removeElement PASSED [ 16%]
tests/array_problems/test_replace_elements_with_greatest_element_on_right_side.py::TestSolution::test_replaceElements PASSED [ 18%]
tests/array_problems/test_rotate_array.py::TestSolution::test_rotate PASSED [ 19%]
tests/array_problems/test_single_number.py::TestSolution::test_singleNumber PASSED [ 21%]
tests/array_problems/test_sort_array_by_parity.py::TestSolution::test_sortArrayByParity PASSED [ 22%]
tests/array_problems/test_squares_of_a_sorted_array.py::TestSolution::test_sortedSquares PASSED [ 23%]
tests/array_problems/test_two_sum.py::test_two_sum PASSED                [ 25%]
tests/array_problems/test_two_sum.py::test_two_sum_no_solution PASSED    [ 26%]
tests/frontendmasters/test_algorithms_pathfinding_dijkstra.py::TestSolution::test_pathfinding PASSED [ 28%]
tests/frontendmasters/test_algorithms_recursion.py::TestSolution::test_recursion PASSED [ 29%]
tests/frontendmasters/test_algorithms_searching_binary_search.py::TestSolution::test_binarysearch PASSED [ 30%]
tests/frontendmasters/test_algorithms_searching_linear_search.py::TestLinearSearch::test_linear_search PASSED [ 32%]
tests/frontendmasters/test_algorithms_searching_linear_search.py::TestLinearSearch::test_linear_search_empty_list PASSED [ 33%]
tests/frontendmasters/test_algorithms_searching_linear_search.py::TestLinearSearch::test_linear_search_multiple_elements PASSED [ 35%]
tests/frontendmasters/test_algorithms_searching_linear_search.py::TestLinearSearch::test_linear_search_single_element PASSED [ 36%]
tests/frontendmasters/test_algorithms_sorting_bubble_sort.py::TestSolution::test_bubble_sort PASSED [ 38%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_duplicates_array PASSED [ 39%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_empty_array PASSED [ 40%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_large_numbers PASSED [ 42%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_mixed_numbers PASSED [ 43%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_negative_numbers PASSED [ 45%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_reverse_sorted_array PASSED [ 46%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_single_element_array PASSED [ 47%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_sorted_array PASSED [ 49%]
tests/frontendmasters/test_algorithms_sorting_heap_sort.py::TestSolution::test_unsorted_array PASSED [ 50%]
tests/frontendmasters/test_algorithms_sorting_insertion_sort.py::TestSolution::test_insertion_sort PASSED [ 52%]
tests/frontendmasters/test_algorithms_sorting_merge_sort.py::TestSolution::test_mergesort PASSED [ 53%]
tests/frontendmasters/test_algorithms_sorting_quick_sort.py::TestSolution::test_quicksort PASSED [ 54%]
tests/frontendmasters/test_algorithms_sorting_radix_sort.py::TestSolution::test_radixSort PASSED [ 56%]
tests/frontendmasters/test_algorithms_tree_traversal_breadth_first.py::TestSolution::test_breadthFirstTreeTraversals_iterative PASSED [ 57%]
tests/frontendmasters/test_algorithms_tree_traversal_breadth_first.py::TestSolution::test_breadthFirstTreeTraversals_recursion PASSED [ 59%]
tests/frontendmasters/test_algorithms_tree_traversal_depth_first.py::TestSolution::test_inorder_traversal PASSED [ 60%]
tests/frontendmasters/test_algorithms_tree_traversal_depth_first.py::TestSolution::test_postorder_traversal PASSED [ 61%]
tests/frontendmasters/test_algorithms_tree_traversal_depth_first.py::TestSolution::test_preorder_traversal PASSED [ 63%]
tests/frontendmasters/test_data_structures_arrays_array_list.py::TestSolution::test_add PASSED [ 64%]
tests/frontendmasters/test_data_structures_graphs.py::TestSolution::test_find_most_common_title PASSED [ 66%]
tests/frontendmasters/test_data_structures_linked_lists_singly_linked.py::TestSolution::test_linkedlist PASSED [ 67%]
tests/frontendmasters/test_data_structures_probabilistic_bloom_filter.py::TestBloomFilter::test_absence PASSED [ 69%]
tests/frontendmasters/test_data_structures_probabilistic_bloom_filter.py::TestBloomFilter::test_add_and_contains PASSED [ 70%]
tests/frontendmasters/test_data_structures_probabilistic_bloom_filter.py::TestBloomFilter::test_false_positive PASSED [ 71%]
tests/frontendmasters/test_data_structures_trees_avl_tree.py::TestSolution::test_add PASSED [ 73%]
tests/frontendmasters/test_data_structures_trees_avl_tree.py::TestSolution::test_balance PASSED [ 74%]
tests/frontendmasters/test_data_structures_trees_avl_tree.py::TestSolution::test_serialize PASSED [ 76%]
tests/frontendmasters/test_data_structures_trees_avl_tree.py::TestSolution::test_to_json PASSED [ 77%]
tests/frontendmasters/test_data_structures_trees_binary_search_tree.py::TestTree::test_add PASSED [ 78%]
tests/frontendmasters/test_data_structures_trees_binary_search_tree.py::TestTree::test_create_correct_tree PASSED [ 80%]
tests/frontendmasters/test_data_structures_trees_trie.py::TestSolution::test_create_trie PASSED [ 81%]
tests/math_problems/test_find_numbers_with_even_number_of_digits.py::TestSolution::test_findNumbers PASSED [ 83%]
tests/math_problems/test_fizz_buzz.py::TestSolution::test_fizzBuzz PASSED [ 84%]
tests/math_problems/test_power_of_three.py::TestSolution::test_isPowerOfThree PASSED [ 85%]
tests/math_problems/test_roman_to_integer.py::TestSolution::test_romanToInt PASSED [ 87%]
tests/sorting_searching_problems/test_check_if_n_and_its_double_exist.py::TestSolution::test_checkIfExist PASSED [ 88%]
tests/sorting_searching_problems/test_duplicate_zeros.py::TestSolution::test_duplicateZeros PASSED [ 90%]
tests/sorting_searching_problems/test_merge_sorted_array.py::TestSolution::test_merge PASSED [ 91%]
tests/sorting_searching_problems/test_valid_mountain_array.py::TestSolution::test_validMountainArray PASSED [ 92%]
tests/string_problems/test_first_unique_character_in_a_string.py::TestSolution::test_firstUniqChar PASSED [ 94%]
tests/string_problems/test_reverse_integer.py::TestSolution::test_reverse PASSED [ 95%]
tests/string_problems/test_reverse_string.py::TestSolution::test_reverseString PASSED [ 97%]
tests/string_problems/test_valid_anagram.py::TestSolution::test_isAnagram PASSED [ 98%]
tests/string_problems/test_valid_palindrome.py::TestSolution::test_palindrom PASSED [100%]

---------- coverage: platform linux, python 3.12.9-final-0 -----------
Name                                                                                  Stmts   Miss  Cover
---------------------------------------------------------------------------------------------------------
src/array_problems/best_time_to_buy_and_sell_stock_ll/solution.py                         9      0   100%
src/array_problems/contains_duplicate/solution.py                                        21      0   100%
src/array_problems/height_checker/solution.py                                            12      0   100%
src/array_problems/intersection_of_two_arrays_ll/solution.py                             11      0   100%
src/array_problems/max_consecutive_ones/solution.py                                      14      0   100%
src/array_problems/move_zeroes/solution.py                                               28      1    96%
src/array_problems/plus_one/solution.py                                                  14      0   100%
src/array_problems/remove_duplicates_from_sorted_array/solution.py                       20      7    65%
src/array_problems/remove_element/solution.py                                            18      0   100%
src/array_problems/replace_elements_with_greatest_element_on_right_side/solution.py      10      0   100%
src/array_problems/rotate_array/solution.py                                              14      0   100%
src/array_problems/single_number/solution.py                                              9      0   100%
src/array_problems/sort_array_by_parity/solution.py                                      11      0   100%
src/array_problems/squares_of_a_sorted_array/solution.py                                  8      0   100%
src/array_problems/two_sum/solution.py                                                   10      0   100%
src/frontendmasters/algorithms/pathfinding/dijkstra/solution.py                          49      2    96%
src/frontendmasters/algorithms/recursion/solution.py                                     15      1    93%
src/frontendmasters/algorithms/searching/binary_search/solution.py                       30     12    60%
src/frontendmasters/algorithms/searching/linear_search/solution.py                        7      0   100%
src/frontendmasters/algorithms/sorting/bubble_sort/solution.py                           13      0   100%
src/frontendmasters/algorithms/sorting/heap_sort/solution.py                             26      0   100%
src/frontendmasters/algorithms/sorting/insertion_sort/solution.py                        12      0   100%
src/frontendmasters/algorithms/sorting/merge_sort/solution.py                            22      0   100%
src/frontendmasters/algorithms/sorting/quick_sort/solution.py                            20      0   100%
src/frontendmasters/algorithms/sorting/radix_sort/solution.py                            29      0   100%
src/frontendmasters/algorithms/tree_traversal/breadth_first/solution.py                  27      0   100%
src/frontendmasters/algorithms/tree_traversal/depth_first/solution.py                    27      0   100%
src/frontendmasters/data_structures/arrays/array_list/solution.py                        23      1    96%
src/frontendmasters/data_structures/graphs/solution.py                                   22      0   100%
src/frontendmasters/data_structures/linked_lists/singly_linked/solution.py               66     15    77%
src/frontendmasters/data_structures/probabilistic/bloom_filter/solution.py               15      0   100%
src/frontendmasters/data_structures/trees/avl_tree/solution.py                           95      8    92%
src/frontendmasters/data_structures/trees/binary_search_tree/solution.py                 38      1    97%
src/frontendmasters/data_structures/trees/trie/solution.py                               38      1    97%
src/math_problems/find_numbers_with_even_number_of_digits/solution.py                    14      0   100%
src/math_problems/fizz_buzz/solution.py                                                  16      0   100%
src/math_problems/power_of_three/solution.py                                             10      1    90%
src/math_problems/roman_to_integer/solution.py                                           12      0   100%
src/sorting_searching_problems/check_if_n_and_its_double_exist/solution.py               16      2    88%
src/sorting_searching_problems/duplicate_zeros/solution.py                               12      0   100%
src/sorting_searching_problems/merge_sorted_array/solution.py                             7      0   100%
src/sorting_searching_problems/valid_mountain_array/solution.py                          13      1    92%
src/string_problems/first_unique_character_in_a_string/solution.py                        8      1    88%
src/string_problems/reverse_integer/solution.py                                          13      1    92%
src/string_problems/reverse_string/solution.py                                           15      0   100%
src/string_problems/valid_anagram/solution.py                                            13      1    92%
src/string_problems/valid_palindrome/solution.py                                         13      8    38%
---------------------------------------------------------------------------------------------------------
TOTAL                                                                                   945     64    93%


============================== 71 passed in 0.71s ==============================
```

[![Coverage](https://img.shields.io/badge/Coverage-93.23%25-brightgreen)]()
