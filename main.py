def test_extend_list():
    user_data_science = [15, 23, 43, 56]
    user_machine_learning = [13, 23, 56, 42]

    watched = []
    watched = user_data_science.copy()
    watched.extend(user_machine_learning)
    # final list has duplicated elements
    print(watched)

def test_set():
    user_data_science = {15, 23, 43, 56}
    user_machine_learning = {13, 23, 56, 42}
    # a set has no duplicated element
    # set has no index access/no order
    watched_union = user_machine_learning | user_data_science
    watched_intesec = user_machine_learning & user_data_science
    watched_diff = user_machine_learning - user_data_science
    watched_exclusive = user_machine_learning ^ user_data_science
    print(watched_exclusive)
    for user in watched_exclusive:
        print(user)


if __name__ == "__main__":
    test_set()
