def test_char_del():
    from char_delete import char_del
    import pandas as pd

    # data dictionary
    data = {
        "Car": ["Car1", "Car2", "Car3", "Car4", "Car5"],
        "Lap Time (s)": ["86", "91", "89", "88", "87"],
        "Top Speed (km/h)": ["153", "163", "157", "155", "154"],
    }

    # create helper data from dictionary
    helper_data = pd.DataFrame(data)

    # test char_del() fucntion
    test = char_del(helper_data, ["Car", "Top Speed (km/h)"], ["C", "1"])
    assert test.shape == (5, 3)
    assert list(test["Car"]) == ["ar", "ar2", "ar3", "ar4", "ar5"]
    assert list(test["Top Speed (km/h)"]) == ["53", "63", "57", "55", "54"]
