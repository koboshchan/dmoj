depth = [int(input()) for _ in range(4)]

"""
there are four consecutive depth readings which form a strictly increasing sequence (such as 3 4 7 9) (which we will call "Fish Rising") or
there are four consecutive depth readings which form a strictly decreasing sequence (such as 9 6 5 2) (which we will call "Fish Diving"), or
there are four consecutive depth readings which are identical (which we will call "Fish At Constant Depth").

All other readings will be considered random noise or debris, which we will call "No Fish". Your task is to read a sequence of depth readings and determine if the alarm will sound.
"""

if depth[0] < depth[1] < depth[2] < depth[3]:
    print("Fish Rising")
elif depth[0] > depth[1] > depth[2] > depth[3]:
    print("Fish Diving")
elif depth[0] == depth[1] == depth[2] == depth[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")