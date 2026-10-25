# Complexity analysis

`n` is the number of list elements. These bounds exclude printing.

## Algorithms

| Algorithm     | Best case  | Worst case        |
| ------------- | ---------- | ----------------- |
| Binary Search | Θ(1)       | Θ(log n)          |
| Cocktail Sort | Θ(n)       | Θ(n²)             |
| Comb Sort     | Θ(n log n) | O(n²) upper bound |

- **Binary Search:** Best when the target is the first middle element. Otherwise, each iteration removes half the search range. An absent target above the maximum gives a longest search path.
- **Cocktail Sort:** An already sorted list needs one pass and stops because there are no swaps. Reverse-sorted distinct values require n(n-1)/2 adjacent swaps, giving quadratic time.
- **Comb Sort:** The gap is divided by 1.3 and rounded down until it reaches 1. Even sorted input needs about log n passes, each checking up to n pairs. After that, gap-1 passes behave like Bubble Sort, giving an O(n²) upper bound. I have not established a tight worst-case bound for this exact implementation.

## Inputs and timing

The five list sizes are **128, 256, 512, 1024, 2048**.

- **Best:** Ascending values from 0 to n-1. Search for the first middle element.
- **Worst:** Descending values for sorting. This is a true worst case for Cocktail Sort, but only a challenging pattern for Comb Sort. Binary Search uses ascending values and searches for n, which is absent.
- **Random:** Uniform random integers from 0 to 10\*n inclusive; duplicates are allowed. Search uses a sorted copy and one random target from the same range per size. Repeating that target does not test different random queries.

Binary Search runs 10,000 times per size. Each sort runs 5 times, using copies of identical starting values for both algorithms. The program reports mean time and the ratio to the previous size. Generation, copying, checks, and printing are all outside the timer.

## Expected growth when size doubles

- Binary Search: best time stays roughly constant; worst case adds about one iteration.
- Cocktail Sort: best time roughly doubles; worst time roughly quadruples.
- Comb Sort: best time grows slightly more than twice, following n log n. Its quadratic upper bound does not mean the reverse-sorted experiment must take four times longer.

## Example measurements

Actual results from one run. Times are in microseconds. Ratios compare size 2048 with size 1024.

| Algorithm and case           |      1024 |      2048 | Ratio |
| ---------------------------- | --------: | --------: | ----: |
| Binary Search, best          |     0.064 |     0.062 |  0.97 |
| Binary Search, random        |     0.349 |     0.450 |  1.29 |
| Binary Search, worst         |     0.447 |     0.457 |  1.02 |
| Cocktail Sort, best          |    16.383 |    35.608 |  2.17 |
| Cocktail Sort, random        | 14828.667 | 70455.567 |  4.75 |
| Cocktail Sort, worst         | 23002.317 | 94466.100 |  4.11 |
| Comb Sort, best              |   319.850 |   765.642 |  2.39 |
| Comb Sort, random            |   508.750 |  1568.275 |  3.08 |
| Comb Sort, reverse challenge |   388.400 |   951.892 |  2.45 |

The results broadly match the predictions: search grows slowly, while Cocktail Sort's worst time grows about fourfold. Comb Sort's reverse input was faster than its random input, so it should not be called a proven worst case. Small timings, computer load, and the chosen random inputs cause variation. Measurements illustrate complexity; they do not prove it.
