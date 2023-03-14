from kata_calculate_stats.stats import Stats

example_list = [6, 9, 15, -2, 92, 11]
# test that a list named list_of_numbers exists
def test_min_value():
    stats = Stats()
    var_min_value = stats.min_value(example_list)

    assert var_min_value == -2




