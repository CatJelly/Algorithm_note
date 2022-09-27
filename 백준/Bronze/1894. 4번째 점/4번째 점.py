import enum


while True:
    try:
        spot_list = list(map(float, input().split()))
        spot_list = list(spot_list[i*2:(i+1)*2] for i in range(4))
        
    except:
        break
    
    overlap_spot = ""
    for i, spot1 in enumerate(spot_list):
        for j, spot2 in enumerate(spot_list):
            if i != j and spot1 == spot2:
                overlap_spot = spot1
                spot_list.remove(spot1)
                spot_list.remove(spot2)

    middle_spot = [(spot_list[0][0] + spot_list[1][0]) / 2,
                    (spot_list[0][1] + spot_list[1][1]) / 2]
    vector = [middle_spot[0] - overlap_spot[0], middle_spot[1] - overlap_spot[1]]
    other_spot = [middle_spot[0] + vector[0],
                middle_spot[1] + vector[1]]

    print(f"{other_spot[0]:.3f} {other_spot[1]:.3f}")