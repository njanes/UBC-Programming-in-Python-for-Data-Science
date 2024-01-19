def test_col_div():
    from div_int64 import col_div
    import pandas as pd

    # data dictionary
    data = {
        "Employee": [1, 2, 3, 4],
        "Salary": [60000, 75000, 80000, 55000],
        "Orders": [15, 20, 10, 18],
    }

    # create helper data from dictionary
    helper_data = pd.DataFrame(data)

    # test col_div() fucntion
    test = col_div(helper_data, "Salary", 100)
    assert test.shape == (4, 3)
    assert list(test["Salary"]) == [600, 750, 800, 550]
