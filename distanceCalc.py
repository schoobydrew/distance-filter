#https://stackoverflow.com/questions/57294120/calculating-distance-between-latitude-and-longitude-in-python/57298327#57298327
#this post has simple code to follow
# https://andrew.hedges.name/experiments/haversine/
# blog post on research and result validation
import numpy as np

def haversine(lat1,lon1, lat2,lon2):
    # dlon = lon2 - lon1
    # dlat = lat2 - lat1
    # a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
    # c = 2 * atan2( sqrt(a), sqrt(1-a) )
    # d = R * c (where R is the radius of the Earth)
    
    radius = 6373.0  # km
    dlon = np.radians(lon2 - lon1)
    dlat = np.radians(lat2 - lat1)
    a = (np.sin(dlat / 2.0)**2) + (np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * (np.sin(dlon / 2.0)**2))
    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    d = radius * c
    return d #d in kilometers
def test_haversine_singular():
    res = haversine(38.898556,-77.037852,38.897147,-77.043934)
    assert round(res,3) == .549 # expect .549 km
    res = haversine(20,20, 40,40)
    assert round(res,3) == 2928.304 # expect 2928.304 km
    res = haversine(45.46433102378706, -122.65229575257185, 45.464331774531544, -122.65169711659489)
    assert round(res,3) == .047 # expect .047 km
def test_haversine_plural():
    res = haversine(
            np.array([38.898556,20,45.46433102378706]),
            np.array([-77.037852,20,-122.65229575257185]),
            np.array([38.897147,40,45.464331774531544]),
            np.array([-77.043934,40,-122.65169711659489]))
    assert list(res.round(3)) == [.549, 2928.304, .047]
def test_haversine_one2many():
    lat1, lon1 = (32.355726, -90.158399)
    latarr = np.array([32.356315098092615, 32.355746390781164, 32.35573279614031])
    lonarr = np.array([-90.15840168239147, -90.16033823714292, -90.15659387366226])
    check = [.066, .182, .170]
    res = haversine(lat1, lon1, latarr, lonarr)
    assert list(res.round(3)) == check