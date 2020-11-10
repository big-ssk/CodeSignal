def chessBoardCellColor(cell1, cell2):
    return (sum(map(ord, cell1 + cell2))) % 2 == 0
