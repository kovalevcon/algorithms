# The problem of covering the set. It is necessary to select the stations covering the maximum of all states.
# Asymptotic complexity (O) = n**1


def find_max_coverage(states, radio_stations):
    """
    :type states: set
    :type radio_stations: set
    :rtype: set
    """
    final_stations = set()
    while states:
        best_station = None
        states_covered = set()
        for station, states_for_station in radio_stations.items():
            # print(station, states_for_station)
            covered = states & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states -= states_covered
        final_stations.add(best_station)

    return final_stations


states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az'])
}


founded_stations = find_max_coverage(states_needed, stations)
print(founded_stations)

