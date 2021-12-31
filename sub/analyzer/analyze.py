def analyze_options(argv, keywords):

    """
    Returns a dictionary containing the optional or required input keywords as keys,
    and their values.
    """

    # argv = ["for", "14/m", "since", "last", "week", "until", "next", "month"]
    # keywords = ["for", "since", "until"]

    keyword_indexes = [index for index, keyword in enumerate(argv) if keyword in keywords]
    # keyword_indexes = [0,2,5]

    # method 1 (note: this method has a small bug)
    #keyword_slices = [keyword_indexes[i:i+2] for i in range(len(keyword_indexes))]
    # method 2
    keyword_slices = list(zip(keyword_indexes, [*keyword_indexes[1:],None]))
    # keyword_slices = [(0,2), (2,5), (5,None)]

    option_slices = [argv[slice(*s)] for s in keyword_slices]
    # option_slices = [["for", "14/m"], ["since","last","week"], ["until","next","week"]]

    options = {s[0]: ' '.join(s[1:]) for s in option_slices}
    # options = {"for": "14/m", "since": "last week", "until": "next week"}

    return options