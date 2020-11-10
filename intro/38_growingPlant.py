def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 1
    height = upSpeed
    while height < desiredHeight:
        day += 1
        height += upSpeed - downSpeed
    return day
