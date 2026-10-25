import random
import sys
import time

sys.setrecursionlimit(200000)


def partition(arr: list[float], low: int, high: int, ascending: bool) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        condition = (arr[j] <= pivot) if ascending else (arr[j] >= pivot)

        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_recursive(
    arr: list[float], low: int, high: int, ascending: bool
) -> None:
    if low < high:
        pivot_index = partition(arr, low, high, ascending)
        quick_sort_recursive(arr, low, pivot_index - 1, ascending)
        quick_sort_recursive(arr, pivot_index + 1, high, ascending)


def quick_sort(arr: list[float], ascending: bool = True) -> None:

    if not arr or len(arr) <= 1:
        return
    quick_sort_recursive(arr, 0, len(arr) - 1, ascending)


def is_sorted(arr: list[float], ascending: bool = True) -> bool:

    if not arr or len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):
        if ascending:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False

    return True


def generate_random_array(size: int) -> list[float]:
    return [random.uniform(-5000.0, 5000.0) for _ in range(size)]


if __name__ == "__main__":
    print(" Перевірка роботи алгоритму QuickSort")
    sizes = [1_000, 10_000, 100_000]

    for size in sizes:
        print(f"\n Тестування для масиву з {size:,} елементів ")
        original_array = generate_random_array(size)

        asc_array = original_array.copy()
        start_time = time.perf_counter()
        quick_sort(asc_array, ascending=True)
        end_time = time.perf_counter()
        asc_time_ms = (end_time - start_time) * 1000
        print(
            f"За зростанням: час = {asc_time_ms:.2f} ms | "
            f"Відсортовано коректно: {is_sorted(asc_array, ascending=True)}"
        )

        desc_array = original_array.copy()
        start_time = time.perf_counter()
        quick_sort(desc_array, ascending=False)
        end_time = time.perf_counter()
        desc_time_ms = (end_time - start_time) * 1000
        print(
            f"За спаданням:  час = {desc_time_ms:.2f} ms | "
            f"Відсортовано коректно: {is_sorted(desc_array, ascending=False)}"
        )