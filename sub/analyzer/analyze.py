from .config import OPTIONS

def analyze(argv):

    """
    Analyzes the command line arguments
    Returns a tuple containing the command, name and options.
    """

    if len(argv) == 0:
        raise Exception("No input given.")

    [command, *rest] = argv

    if command not in OPTIONS.keys():
        raise Exception(f"Invalid subcommand: {command}")

    keywords = OPTIONS[command]
    try:
        name = analyze_name(rest, keywords)
        options = analyze_options(rest, keywords)
    except: #IndexError
        raise Exception(f"Invalid command: {' '.join(argv)}")
        # TODO: Handle IndexError in helper functions.
    

    return (command, name, options)
        

def keyword_indexes(argv, keywords):
    return sorted([index for index, keyword in enumerate(argv) if keyword in keywords])

def analyze_name(argv, keywords):

    """
    Returns the name of the subscription.
    """

    # argv = ["netflix.com", "for", "14/m", "since", "last", "week", "until", "next", "month"]
    # keywords = ["for", "since", "until"]
    name = argv[0:keyword_indexes(argv, keywords)[0]]
    return ' '.join(name) #analyze_options ignores name


def analyze_options(argv, keywords):

    """
    Returns a dictionary containing the optional or required input keywords as keys,
    and their values.
    """

    # argv = ["for", "14/m", "since", "last", "week", "until", "next", "month"]
    # keywords = ["for", "since", "until"]
    kw_indexes = keyword_indexes(argv, keywords)
    # kw_indexes = [0,2,5]

    # method 1 (note: this method has a small bug)
    #keyword_slices = [kw_indexes[i:i+2] for i in range(len(kw_indexes))]
    # method 2
    keyword_slices = list(zip(kw_indexes, [*kw_indexes[1:],None]))
    # keyword_slices = [(0,2), (2,5), (5,None)]

    option_slices = [argv[slice(*s)] for s in keyword_slices]
    # option_slices = [["for", "14/m"], ["since","last","week"], ["until","next","week"]]

    options = {s[0]: ' '.join(s[1:]) for s in option_slices}
    # options = {"for": "14/m", "since": "last week", "until": "next week"}

    return options

