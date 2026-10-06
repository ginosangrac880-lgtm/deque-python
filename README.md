# Algorithms and Data Structures

Учебный проект по структурам данных и алгоритмам на Python.

## Реализованные структуры данных

- Dynamic Array
- Linked List
- Deque
- AVL Tree

## Алгоритмы сортировки

- Bubble Sort
- Quick Sort

## Тесты

Для всех структур данных и алгоритмов написаны автоматические тесты с использованием `unittest`.

Файлы тестов:

- `test_dynamic_array.py`
- `test_linked_list.py`
- `test_deque.py`
- `test_avl_tree.py`
- `test_sorting.py`

## CI

В проекте настроен GitHub Actions.

При каждом push или pull request автоматически запускаются все тесты.

Workflow:

`.github/workflows/ci.yml`

## Запуск тестов

```bash
python -m unittest discover -v
