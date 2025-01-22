from collections import defaultdict
from math import radians, atan2, sin, cos, sqrt
from typing import List

def closestLocationGPS(arr1: List[tuple], arr2: List[tuple]) -> dict:
    """
    This function takes two geo-location arrays and finds the points from the 2nd array that are closest to the points in the 1st array,
    and puts the pairs into a dictionary.

    Args: 
        arr1 (List[tuple]): base array
        arr2 (List[tuple]): array for comparison
    
    Returns:
        dict: dictionary of results, keys are from arr2 and values are from arr1
    """
    assert len(arr1) > 0 and len(arr2) > 0

    closest_location_map = defaultdict(list)
    for arr1_pair in arr1:
        lat1, lon1 = arr1_pair
        closest_distance = None
        closest_pair = None
        for arr2_pair in arr2:
            lat2, lon2 = arr2_pair

            diff_lat = radians(lat2 - lat1)
            diff_lon = radians(lon2 - lon1)

            res = sin(diff_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(diff_lon / 2) ** 2
            res = 2 * atan2(sqrt(res), sqrt(1 - res))

            if closest_distance is None:
                closest_distance = res
                closest_pair = arr2_pair
            else:
                temp_distance = closest_distance
                closest_distance = min(closest_distance, res)
                if temp_distance != closest_distance:
                    closest_pair = arr2_pair     

        closest_location_map[closest_pair].append(arr1_pair)
    
    return dict(closest_location_map)