from kata_calculate_stats.stats import Stats

example_list = [6, 9, 15, -2, 92, 11]
# test that a list named list_of_numbers exists
def test_min_value():
    stats = Stats()
    assert stats.min_value(example_list) == -2

def test_max_value():
    stats = Stats()
    assert stats.max_value(example_list) == 92


