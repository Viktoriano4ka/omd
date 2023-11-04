from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFitTransform(unittest.TestCase):
    def test_animals(self):
        actual = fit_transform(['cat', 'dog', 'pig', 'pig', 'bear'])
        expected = [('cat', [0, 0, 0, 1]),
                    ('dog', [0, 0, 1, 0]),
                    ('pig', [0, 1, 0, 0]),
                    ('pig', [0, 1, 0, 0]),
                    ('bear', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_not_in(self):
        actual_raw = fit_transform(['cat', 'cat', 'bear'])
        actual = [i[1] for i in actual_raw]
        not_expected = [0, 0, 1]
        self.assertNotIn(not_expected, actual)

    def test_animals_list(self):
        actual = fit_transform(['cat'])
        self.assertIsInstance(actual, list)

    def test_exception(self):
        self.assertRaises(TypeError, fit_transform)


if __name__ == '__main__':
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities