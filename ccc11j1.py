"""
TroyMartian, who has at least 3 antennae and at most 4 eyes;
VladSaturnian, who has at most 6 antennae and at least 2 eyes;
GraemeMercurian, who has at most 2 antennae and at most 3 eyes.
"""

antennae = int(input())
eyes = int(input())

if antennae >= 3 and eyes <= 4:
    print("TroyMartian")
if antennae <= 6 and eyes >= 2:
    print("VladSaturnian")
if antennae <= 2 and eyes <= 3:
    print("GraemeMercurian")