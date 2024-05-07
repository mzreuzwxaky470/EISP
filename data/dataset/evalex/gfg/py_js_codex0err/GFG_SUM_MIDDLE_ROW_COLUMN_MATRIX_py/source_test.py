def test():
  "--- test function ---" ;
  param = [
    ([[7, 32, 33, 35, 51, 61, 62, 68, 71, 73], [3, 10, 18, 32, 44, 56, 62, 80, 86, 91], [13, 21, 26, 31, 43, 53, 54, 59, 61, 73], [3, 9, 14, 14, 43, 46, 67, 71, 87, 99], [20, 53, 53, 72, 79, 80, 82, 84, 95, 99], [15, 21, 39, 44, 46, 48, 59, 64, 65, 70], [28, 35, 39, 41, 45, 50, 52, 61, 72, 73], [3, 15, 21, 22, 49, 49, 54, 73, 88, 98], [7, 9, 14, 16, 18, 26, 42, 45, 59, 86], [14, 21, 25, 31, 34, 45, 53, 54, 66, 82]],8,),
    ([[22, 92, 36, -94, -4, 6, -36, 78, -18, 12, 14, 54, 80, 4, -34, 4, -2, 24, 60, -14, 68, 88, -46, 82, -70, -2, 38, 76, -72, 70, -12, 24, -62, 58, 64, -92, 60, 96, -20, 0], [96, 42, -92, 70, 82, -74, -28, -64, -64, -50, -56, 92, -52, 84, 68, 2, -80, 60, -70, 6, 42, -16, 50, 86, -2, 56, 36, -90, 82, -38, 42, -66, -32, -88, 2, 48, 24, 56, 78, 90], [-86, 4, 8, 22, 92, -62, 88, -54, 50, 0, -32, -24, 38, 64, -22, -4, 30, -26, 82, 10, 4, 78, 78, 48, -42, 94, -14, -54, 24, 14, 36, 46, -16, -14, -72, -98, 30, 2, -28, -10], [-70, 44, 54, 6, 2, 66, -24, 6, 94, 16, 92, -78, -26, -36, 66, 56, -30, -50, -94, -64, 94, 82, -70, 74, 70, 88, -34, -24, -4, -62, 10, 18, -96, -22, -34, -52, 40, -50, -80, 22], [78, -70, -52, 58, 78, -6, -26, -16, -34, -42, 66, 12, -2, 30, -36, -28, 94, 64, 84, -86, -78, -62, -92, 16, 50, -50, 16, 64, -46, -92, -46, -48, -18, -86, -18, -84, 28, 22, 10, -58], [34, -86, 68, -10, -82, -28, -78, -18, -86, 22, -80, -14, 34, -80, -30, -50, 32, 84, -70, -32, 40, 62, -92, -76, 98, 24, -70, 24, 64, -92, 40, -28, -10, 38, -6, -6, -44, 50, -24, 98], [96, 62, 46, 90, 38, -36, -82, 70, -82, 2, -78, -84, -42, 92, 32, 54, 44, -50, -90, 94, 6, 38, 40, -6, -76, 98, -64, -90, 80, -2, -20, 28, 94, -52, 38, -38, 12, -78, -32, -64], [-28, -32, 66, 44, 28, 60, 58, 70, -56, 8, -82, 78, -94, -74, 60, 36, 64, 48, 60, -60, 82, 44, 52, -38, 26, -36, -90, -94, 44, 74, 84, 28, 76, 46, 4, 64, 16, 44, 72, 48], [28, 92, -64, 80, -84, 18, -82, 8, -28, -60, -50, 66, 76, 96, -54, 54, -4, -80, 72, 2, 74, -64, -48, 34, 6, -56, 6, 86, -26, -68, -30, -18, 70, 14, -70, -78, 68, 86, 40, -86], [58, 78, 76, -4, -68, 76, -10, -68, -78, -48, -82, -46, -80, -40, 42, 36, 96, 32, -10, -90, 6, -22, 22, -52, 32, 16, -58, -52, -78, -4, -54, -86, -16, 78, -66, -16, 68, 6, 66, -84], [-58, 30, 62, 70, -38, -22, -68, 98, -62, -54, 80, -38, -90, 38, -8, -36, -52, 48, -2, 82, -78, -72, -6, 96, 44, -34, 90, -2, 30, 92, 40, -18, -76, 46, -60, 36, 90, -54, 56, -24], [84, 34, -20, 4, 0, 80, 70, -82, -74, -12, -24, 72, 30, 16, 62, -44, 50, -64, 98, 58, 74, -64, -34, 82, -24, 20, 22, -34, 74, 4, 52, -8, 26, -8, 74, -26, 34, 60, 40, -24], [-46, -54, 22, 20, 70, -8, 32, 98, 94, 34, -94, -40, 24, 98, -56, 12, -28, 58, 84, -86, 98, 80, -40, -54, -30, 16, 6, 74, 72, -98, 78, -98, -62, 70, 40, -90, 82, 68, -36, -12], [26, -54, 66, 50, -78, -66, -18, 78, -78, -24, 22, 14, -42, -10, 34, -82, 36, 94, -98, 60, 52, 46, -60, -52, -42, -64, 94, -18, 66, -2, -20, -92, -70, 32, 14, 72, 58, 54, -62, 22], [-16, -14, -80, 20, -90, -10, 92, -54, -8, -32, -44, 6, -26, 66, -56, -38, -56, 86, 52, -38, 12, 12, 20, 24, 14, -30, -10, -70, 36, 64, -82, -46, 24, 26, -58, 96, 58, 96, -70, 58], [16, -90, -18, -40, 86, -98, -14, -92, -86, 24, -98, -84, 54, 64, -84, -50, 76, -34, 62, 26, 58, 42, 10, -72, 32, 92, 46, 50, 58, 66, -98, 26, -56, 56, -66, 26, -82, 0, -6, 34], [4, -2, -6, 8, -70, 30, -36, 2, -46, -86, 76, 4, -46, -20, -24, -60, -10, -20, 44, -8, -32, -4, -54, -68, 36, 84, 4, 86, -42, 0, -6, 76, 52, -10, 46, -76, -2, 72, 16, 34], [24, -80, -58, 26, 42, -42, 8, -70, 22, -86, -38, -12, -80, 46, 32, 84, 96, -76, -36, -26, -6, 46, 10, 84, -42, 52, -94, -76, -66, -44, -46, 64, -62, 50, -26, 96, -4, 20, -86, 12], [-42, 78, -32, -98, -86, 2, 54, -30, 68, 24, -40, 66, -92, -66, -48, -30, -98, -96, 88, -92, -40, -24, 52, 70, -54, 66, 18, 96, 22, 26, 46, 6, 76, -54, -74, 0, -82, -56, -60, 0], [-6, -70, 20, -88, 44, 42, 20, 34, -70, 36, 22, 24, 30, -82, 26, 62, -72, -96, 56, -64, 88, -42, 22, 64, 66, -40, 46, 20, -40, -86, 50, 16, 34, -84, -12, -30, -84, 96, -82, -40], [-62, 10, 36, -62, -62, -72, 14, -92, 10, 4, 14, 22, -94, -26, 88, -34, -16, 80, -28, 26, 42, 78, 92, -44, -32, 64, 18, 4, -34, -22, -54, 10, 58, 88, -90, 64, -90, -88, -30, -86], [18, -62, 22, -78, 16, -70, 26, 66, -2, -48, -74, 48, -44, -88, 12, 86, -50, 30, 14, 36, -28, 82, 64, -4, 10, 84, -88, 44, -98, -86, -22, 64, -22, 92, -80, -94, -42, 64, 66, -30], [94, -24, 96, 34, 36, -76, -58, 88, -54, -66, 22, 56, -4, 30, -70, -36, -52, 96, 14, 96, -56, 54, -64, -78, 82, 58, 16, -86, 62, -68, 20, -4, -92, 78, -76, 96, 14, -48, 88, -28], [40, 14, 6, -84, -76, -78, -54, 48, -56, -38, 4, -30, 6, 34, -54, -38, -82, 28, 74, 66, -66, 26, 92, -78, 78, -60, 66, -36, 18, 16, -36, 72, 76, -18, -24, 20, -4, -44, -36, -16], [98, -52, 12, 48, -28, 68, -94, 10, 20, -52, -32, 38, -76, -58, -16, -60, 32, 52, 70, -46, 48, -22, -26, 82, 48, -54, 66, 56, -46, -32, -20, 52, 82, -4, -80, -30, -22, -36, 8, 4], [82, -52, 66, 94, -4, -8, 2, -34, 32, -62, 90, -48, 60, -22, 14, -84, -24, -10, 36, 0, 88, -90, -66, -6, 60, -10, -12, -42, -96, 56, 28, -48, -80, 48, 22, -98, 98, 32, -10, 48], [-54, 2, -68, -46, -38, -46, -80, -62, 50, 12, -80, 0, -64, 4, -92, -64, -52, 64, 24, -46, 4, -98, -92, -90, -68, 88, -98, -54, -74, 50, 28, -30, -4, -48, -88, -44, -86, -10, 66, 64], [-72, 50, -8, 26, 66, -40, 72, -32, -72, 36, 18, 72, 12, 48, 70, -60, 68, 6, 94, -44, -10, -52, 2, -28, 86, 78, 76, 64, 2, -42, -22, 14, -94, 98, -46, -12, 34, -50, 76, 56], [-38, -6, 44, 46, -26, -62, -40, -80, 74, 48, 96, 8, -34, 56, 52, -46, -80, 68, 40, -34, 56, -58, 40, -54, -66, 68, 60, -72, -44, 12, -88, 6, -86, 70, 10, 62, -76, -20, 98, -54], [-86, -88, -24, 0, -96, -82, -34, 2, -84, -40, -2, -30, 92, 16, -42, 74, 40, 30, -34, -98, -34, -6, -46, 40, -78, 72, 74, -56, -82, 18, 60, -68, 60, -16, 88, 16, -28, -2, 84, -88], [66, 96, 92, 18, -58, 16, 18, 4, 18, 22, 42, 48, 14, -6, -60, -76, 62, 54, 40, -22, 76, -96, 6, 44, 24, -80, -26, -70, -90, -88, -62, -68, 22, 16, -32, -70, 22, -8, -70, 44], [-4, 16, -38, 36, 24, 58, 58, 10, -38, -12, -26, -10, 46, -16, -90, -36, -60, -36, 86, -92, 14, 38, 96, -98, -8, 76, -96, 48, -46, 32, -56, -62, -54, 86, -42, -28, 78, 12, 48, 76], [42, 80, 54, -62, 12, -64, 4, -98, -10, -48, -22, 64, 26, -2, -46, -50, 10, 70, 36, -66, 28, -50, 6, -24, 52, 74, 50, -4, -34, 58, 30, -48, 36, 40, 46, -18, 68, 76, 34, -56], [-70, 38, 8, -20, -70, -86, 96, 50, 10, -98, -56, 86, -6, 10, -30, 78, 24, 32, -98, 10, -88, 42, -52, 86, -56, 18, -26, -36, 10, 78, -96, -68, -38, -58, -8, -94, -74, 50, 50, -32], [-2, 6, -30, -4, 2, 42, -98, -66, -92, 52, 68, 96, 80, -68, -4, -96, 90, -56, -50, -30, 2, -40, -48, 44, 20, -22, -8, 36, 66, 30, -26, 0, 6, 80, 78, 2, 60, -72, 4, 94], [28, 52, -16, 80, 72, -54, -76, 0, 62, 32, -40, 32, -40, -72, 52, 24, -4, -80, -94, -46, 54, -54, -32, -76, -62, 78, -60, 72, -58, -86, -24, 46, 20, 90, -54, 38, 36, 64, 26, 60], [-18, -72, 82, -6, 66, 60, 14, 64, 6, 6, -58, -68, 22, 98, -28, 94, -58, -70, -10, 12, 84, 26, -38, 34, -42, -50, -38, 80, -42, 42, 74, -64, 56, -78, 42, -76, -10, -16, 54, 66], [-92, 82, -88, -70, -94, 82, 20, 78, 96, -2, -28, -18, -34, 32, -14, -86, -46, -58, 92, -80, 40, 48, 28, 30, 36, -92, 8, -18, -6, -90, 76, 88, -2, -12, -78, 90, 78, 12, -2, -6], [-52, -68, 72, 58, 52, 16, -68, 6, 50, -44, 96, -8, 66, -8, 68, -90, -24, -50, -42, -44, 60, -90, -46, -86, -52, 90, 96, -82, 66, 14, -4, 34, 8, 66, 6, 50, -52, 62, 60, 50], [-56, -58, -92, -6, 38, -54, 64, 32, 48, -68, 36, -34, 34, -50, 24, -80, -18, -44, -60, -64, -22, 72, 20, -30, -92, 46, 90, 92, -84, 88, -26, -42, -98, -98, 28, -92, 30, -30, -86, 10]],31,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],22,),
    ([[47, 81], [14, 25]],1,),
    ([[-38, 30], [-80, 94]],1,),
    ([[1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]],31,),
    ([[1, 6, 6, 8, 8, 15, 19, 21, 22, 26, 29, 30, 31, 32, 35, 37, 37, 40, 41, 41, 44, 46, 48, 52, 54, 54, 55, 60, 61, 61, 67, 68, 76, 77, 78, 80, 80, 81, 81, 81, 82, 83, 85, 87, 89, 91, 97, 97], [4, 5, 6, 8, 9, 13, 14, 19, 22, 23, 29, 29, 30, 35, 36, 36, 39, 40, 41, 43, 43, 44, 45, 46, 46, 51, 51, 53, 55, 57, 58, 59, 60, 60, 61, 64, 65, 68, 69, 70, 70, 75, 76, 78, 81, 82, 88, 92], [4, 5, 5, 8, 17, 18, 19, 19, 20, 20, 21, 21, 22, 23, 29, 29, 31, 32, 33, 33, 33, 34, 38, 43, 44, 45, 47, 58, 61, 66, 72, 72, 72, 74, 75, 76, 78, 78, 80, 83, 85, 86, 88, 92, 92, 96, 97, 99], [1, 3, 4, 6, 8, 9, 14, 14, 15, 15, 16, 18, 18, 20, 21, 21, 23, 23, 24, 27, 32, 33, 35, 35, 36, 43, 44, 44, 45, 47, 48, 50, 51, 51, 55, 55, 55, 55, 66, 67, 67, 70, 86, 88, 92, 93, 94, 99], [1, 2, 4, 7, 10, 10, 11, 13, 13, 15, 16, 17, 22, 31, 32, 35, 36, 37, 37, 41, 41, 43, 45, 46, 47, 50, 51, 51, 54, 55, 58, 64, 67, 68, 70, 72, 73, 76, 77, 82, 83, 84, 84, 85, 85, 89, 93, 94], [3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 15, 16, 17, 17, 21, 21, 23, 25, 26, 27, 29, 30, 32, 36, 40, 41, 43, 43, 49, 49, 57, 57, 61, 62, 68, 71, 73, 75, 81, 84, 89, 91, 92, 94, 95, 97, 97], [1, 1, 4, 16, 16, 16, 19, 24, 26, 26, 28, 31, 33, 34, 34, 35, 36, 37, 40, 52, 54, 56, 57, 62, 64, 64, 66, 70, 71, 72, 72, 73, 73, 74, 78, 81, 81, 83, 83, 85, 88, 90, 92, 93, 93, 94, 98, 99], [2, 4, 6, 8, 8, 9, 11, 14, 15, 17, 17, 20, 21, 22, 22, 28, 29, 30, 31, 31, 32, 36, 44, 47, 50, 50, 55, 59, 62, 62, 63, 66, 67, 70, 76, 76, 76, 78, 80, 80, 81, 83, 84, 86, 88, 91, 95, 97], [4, 6, 8, 10, 11, 13, 17, 17, 21, 22, 33, 33, 37, 41, 43, 45, 47, 48, 51, 52, 53, 58, 58, 58, 58, 58, 63, 65, 66, 67, 67, 68, 69, 71, 73, 75, 80, 81, 82, 82, 83, 89, 89, 94, 95, 97, 98, 99], [3, 5, 10, 11, 11, 12, 13, 17, 17, 18, 20, 23, 23, 24, 27, 31, 31, 34, 39, 39, 39, 43, 43, 44, 45, 46, 50, 51, 53, 55, 60, 61, 64, 68, 75, 75, 76, 78, 81, 82, 83, 86, 88, 93, 93, 96, 96, 98], [2, 2, 3, 6, 7, 13, 16, 21, 23, 23, 23, 24, 29, 30, 32, 35, 36, 36, 38, 39, 39, 39, 41, 42, 42, 44, 46, 51, 51, 52, 53, 64, 71, 73, 74, 80, 81, 84, 86, 86, 93, 94, 96, 96, 96, 96, 97, 99], [2, 4, 5, 12, 14, 16, 20, 22, 25, 26, 33, 34, 35, 35, 36, 40, 44, 49, 50, 50, 51, 51, 51, 52, 55, 58, 58, 59, 60, 61, 62, 64, 66, 66, 66, 72, 75, 76, 81, 82, 82, 84, 86, 89, 92, 93, 93, 96], [1, 2, 2, 3, 4, 5, 6, 7, 11, 13, 13, 15, 19, 20, 23, 26, 27, 29, 30, 30, 38, 39, 40, 40, 41, 43, 53, 57, 65, 70, 71, 78, 78, 79, 80, 81, 82, 82, 83, 87, 87, 93, 93, 96, 96, 97, 97, 98], [4, 11, 12, 18, 18, 21, 21, 27, 27, 28, 29, 33, 34, 37, 40, 41, 41, 45, 55, 56, 56, 57, 58, 58, 63, 63, 65, 65, 66, 68, 68, 69, 69, 73, 74, 78, 80, 82, 83, 83, 85, 87, 89, 92, 95, 95, 96, 97], [1, 4, 7, 7, 14, 15, 22, 24, 24, 27, 30, 32, 33, 34, 39, 39, 40, 41, 44, 48, 56, 56, 58, 59, 61, 61, 62, 63, 64, 65, 68, 69, 70, 72, 78, 78, 80, 80, 82, 83, 83, 84, 86, 87, 92, 93, 94, 94], [1, 1, 4, 5, 6, 6, 7, 9, 10, 10, 14, 16, 17, 19, 21, 24, 26, 30, 31, 32, 37, 37, 38, 40, 45, 49, 52, 52, 54, 54, 61, 61, 65, 67, 70, 72, 78, 79, 80, 82, 84, 85, 87, 88, 88, 92, 94, 97], [3, 6, 10, 10, 11, 12, 12, 13, 14, 15, 16, 18, 21, 23, 25, 27, 27, 27, 27, 30, 33, 35, 40, 41, 44, 48, 50, 50, 51, 52, 54, 54, 55, 58, 58, 58, 59, 62, 65, 69, 72, 72, 74, 74, 76, 79, 80, 98], [1, 2, 4, 4, 4, 5, 6, 7, 9, 9, 10, 12, 22, 23, 24, 26, 26, 28, 33, 35, 35, 38, 42, 44, 48, 48, 52, 54, 56, 60, 63, 68, 68, 68, 72, 75, 77, 79, 79, 82, 85, 88, 89, 91, 91, 91, 92, 93], [1, 8, 11, 13, 22, 23, 23, 26, 30, 31, 33, 34, 35, 35, 37, 39, 40, 44, 46, 46, 46, 47, 47, 47, 54, 59, 60, 60, 61, 62, 64, 66, 69, 74, 75, 77, 78, 79, 79, 82, 83, 86, 87, 92, 94, 96, 99, 99], [1, 1, 3, 8, 11, 14, 19, 20, 20, 20, 21, 24, 25, 25, 28, 34, 37, 38, 38, 39, 40, 47, 53, 54, 56, 57, 58, 62, 65, 69, 70, 70, 71, 71, 73, 76, 78, 78, 81, 84, 87, 92, 94, 94, 94, 96, 98, 99], [3, 4, 4, 15, 19, 21, 23, 26, 30, 31, 32, 34, 35, 37, 38, 41, 46, 46, 46, 51, 52, 53, 58, 63, 65, 68, 68, 68, 69, 70, 70, 70, 71, 72, 73, 74, 75, 75, 77, 80, 81, 84, 84, 86, 96, 96, 96, 98], [3, 4, 8, 9, 9, 11, 16, 19, 19, 20, 20, 23, 27, 27, 28, 30, 31, 34, 36, 40, 41, 43, 45, 46, 53, 53, 55, 58, 58, 59, 62, 63, 64, 65, 68, 68, 71, 72, 75, 78, 80, 87, 87, 88, 89, 94, 97, 99], [1, 3, 3, 10, 12, 12, 12, 12, 13, 15, 17, 18, 22, 24, 24, 28, 29, 31, 33, 33, 34, 34, 40, 43, 44, 48, 48, 49, 51, 55, 60, 63, 67, 68, 70, 72, 73, 75, 75, 77, 82, 85, 88, 91, 93, 94, 95, 98], [6, 6, 7, 8, 9, 14, 15, 18, 19, 26, 28, 28, 28, 30, 31, 33, 33, 36, 38, 39, 43, 44, 46, 48, 56, 57, 57, 60, 60, 61, 67, 69, 70, 71, 73, 74, 79, 80, 82, 84, 86, 86, 90, 92, 94, 95, 96, 98], [2, 2, 3, 9, 10, 14, 15, 15, 16, 19, 25, 26, 28, 31, 32, 33, 33, 34, 35, 41, 41, 42, 42, 43, 48, 48, 58, 59, 61, 66, 66, 69, 72, 73, 77, 78, 79, 79, 83, 86, 88, 92, 92, 92, 92, 95, 96, 97], [1, 6, 7, 8, 11, 14, 15, 16, 16, 18, 23, 23, 24, 25, 28, 29, 31, 32, 36, 38, 38, 41, 42, 43, 44, 46, 55, 55, 56, 59, 62, 64, 67, 69, 69, 70, 71, 72, 76, 81, 84, 86, 86, 87, 87, 89, 94, 95], [3, 3, 6, 10, 11, 15, 16, 18, 18, 27, 28, 28, 30, 30, 33, 34, 35, 35, 39, 43, 45, 48, 50, 51, 52, 53, 55, 62, 62, 62, 67, 68, 69, 70, 71, 72, 74, 74, 80, 81, 84, 85, 85, 86, 88, 88, 88, 96], [1, 2, 4, 5, 5, 5, 6, 12, 14, 14, 16, 16, 19, 28, 28, 29, 30, 32, 35, 36, 38, 39, 41, 47, 52, 57, 58, 58, 62, 64, 66, 71, 75, 76, 80, 81, 82, 83, 84, 85, 86, 87, 90, 91, 93, 96, 97, 98], [4, 7, 8, 10, 11, 12, 14, 17, 19, 19, 20, 24, 24, 28, 29, 29, 31, 31, 32, 33, 35, 36, 40, 42, 43, 47, 49, 53, 53, 53, 54, 54, 58, 58, 61, 64, 67, 72, 74, 79, 80, 80, 84, 86, 91, 91, 96, 97], [2, 4, 6, 6, 11, 12, 17, 19, 20, 21, 25, 26, 29, 30, 30, 31, 32, 39, 42, 42, 47, 48, 48, 49, 49, 49, 51, 55, 56, 59, 62, 65, 67, 67, 68, 68, 69, 73, 73, 76, 79, 82, 86, 87, 87, 88, 98, 98], [2, 3, 5, 7, 8, 16, 17, 18, 29, 29, 30, 31, 32, 33, 36, 38, 38, 40, 43, 45, 47, 56, 58, 59, 61, 63, 65, 65, 67, 68, 68, 69, 73, 74, 78, 80, 81, 82, 82, 89, 91, 92, 92, 94, 96, 97, 97, 98], [4, 8, 11, 12, 14, 15, 24, 27, 29, 32, 33, 36, 37, 38, 42, 46, 46, 47, 47, 49, 50, 53, 58, 58, 61, 64, 64, 65, 68, 69, 73, 74, 76, 79, 79, 82, 83, 84, 85, 89, 89, 90, 95, 95, 95, 97, 99, 99], [3, 3, 3, 5, 6, 7, 10, 13, 14, 16, 18, 23, 25, 26, 27, 31, 31, 35, 38, 41, 44, 46, 52, 57, 58, 62, 63, 63, 63, 64, 68, 69, 71, 72, 72, 76, 76, 78, 80, 83, 83, 88, 89, 90, 92, 94, 95, 98], [3, 8, 11, 15, 15, 26, 27, 29, 30, 32, 32, 37, 39, 42, 47, 49, 52, 52, 52, 53, 53, 54, 54, 59, 60, 61, 61, 62, 64, 65, 66, 66, 67, 67, 68, 69, 73, 74, 77, 79, 90, 90, 91, 91, 95, 98, 99, 99], [2, 4, 6, 8, 9, 10, 11, 15, 15, 16, 20, 21, 22, 23, 25, 26, 27, 27, 36, 38, 42, 45, 47, 47, 51, 53, 53, 55, 57, 59, 59, 62, 65, 66, 72, 73, 76, 82, 82, 83, 88, 90, 90, 91, 95, 96, 99, 99], [1, 2, 3, 6, 6, 7, 11, 16, 17, 19, 20, 23, 24, 24, 26, 28, 31, 33, 36, 37, 38, 39, 40, 40, 44, 46, 46, 51, 51, 53, 62, 62, 63, 64, 68, 69, 70, 73, 78, 78, 85, 87, 90, 91, 93, 93, 95, 98], [3, 9, 9, 11, 14, 16, 17, 18, 18, 22, 22, 25, 29, 30, 34, 35, 37, 37, 41, 42, 43, 45, 45, 52, 54, 55, 55, 57, 63, 64, 65, 68, 69, 70, 70, 71, 74, 75, 75, 77, 86, 86, 87, 93, 94, 95, 95, 99], [1, 3, 3, 10, 13, 14, 15, 18, 19, 20, 22, 23, 24, 25, 26, 32, 34, 40, 41, 41, 41, 44, 44, 46, 53, 57, 57, 59, 60, 61, 62, 63, 64, 70, 72, 72, 77, 78, 86, 88, 90, 92, 92, 93, 93, 94, 95, 98], [2, 4, 5, 7, 17, 20, 20, 21, 24, 24, 25, 25, 27, 28, 29, 29, 33, 35, 35, 35, 37, 38, 43, 43, 45, 48, 49, 52, 53, 59, 62, 64, 65, 70, 71, 72, 72, 75, 75, 86, 88, 89, 89, 91, 91, 93, 96, 97], [5, 6, 6, 9, 13, 16, 17, 18, 20, 21, 25, 26, 26, 31, 34, 43, 44, 45, 45, 47, 48, 48, 51, 51, 54, 56, 56, 57, 61, 61, 66, 67, 69, 69, 70, 72, 76, 76, 81, 83, 85, 90, 96, 96, 97, 98, 98, 99], [3, 4, 5, 6, 12, 13, 14, 14, 18, 20, 22, 24, 32, 35, 38, 38, 39, 41, 44, 48, 51, 52, 54, 55, 55, 57, 58, 59, 60, 60, 62, 64, 66, 69, 69, 74, 74, 76, 78, 79, 81, 82, 82, 82, 85, 86, 91, 99], [2, 6, 7, 8, 10, 14, 15, 15, 16, 16, 18, 21, 24, 30, 31, 32, 37, 38, 39, 41, 42, 42, 44, 45, 50, 51, 52, 53, 59, 60, 61, 61, 67, 67, 72, 73, 74, 75, 77, 79, 81, 88, 90, 91, 95, 95, 97, 98], [2, 3, 4, 7, 7, 7, 9, 15, 17, 18, 19, 20, 22, 24, 26, 26, 28, 29, 33, 36, 39, 40, 42, 43, 45, 49, 58, 61, 68, 68, 71, 75, 75, 75, 75, 76, 77, 78, 79, 80, 83, 86, 91, 94, 95, 98, 99, 99], [5, 6, 7, 10, 10, 11, 12, 14, 17, 19, 20, 24, 29, 31, 32, 35, 41, 44, 47, 47, 49, 50, 54, 57, 60, 61, 64, 66, 69, 70, 71, 72, 75, 75, 75, 77, 80, 81, 82, 88, 88, 90, 94, 97, 97, 97, 98, 99], [1, 1, 4, 6, 6, 7, 8, 11, 11, 14, 17, 18, 20, 21, 25, 29, 31, 31, 32, 38, 40, 41, 42, 44, 44, 45, 46, 51, 52, 58, 61, 62, 66, 67, 73, 74, 76, 79, 82, 84, 85, 86, 87, 90, 91, 92, 94, 97], [1, 1, 3, 4, 7, 7, 10, 11, 12, 13, 16, 24, 24, 27, 28, 29, 34, 36, 38, 39, 39, 42, 45, 48, 55, 57, 60, 62, 62, 63, 63, 69, 72, 76, 77, 78, 81, 81, 82, 83, 90, 93, 94, 94, 96, 98, 99, 99], [1, 1, 1, 1, 2, 2, 3, 7, 8, 14, 14, 19, 19, 23, 23, 25, 26, 27, 31, 43, 48, 49, 49, 50, 51, 51, 52, 55, 56, 57, 57, 57, 59, 62, 63, 63, 67, 71, 74, 74, 74, 76, 81, 84, 85, 87, 98, 98], [1, 1, 5, 9, 10, 12, 16, 18, 19, 20, 23, 26, 28, 35, 35, 36, 37, 40, 41, 41, 44, 44, 54, 57, 59, 60, 60, 60, 61, 63, 67, 74, 76, 79, 79, 84, 85, 86, 89, 89, 90, 91, 92, 92, 92, 95, 96, 98]],35,),
    ([[-18, -22, 0, 40, 84, 14, -90, 8, -52, 70, 24, 92, -22, 92, -38, -78, 76, 70, -6, -34, 68, -92, -58, -58, -58, -90, -76, 62, -46, -22, 6], [-78, 0, -42, -10, 94, -78, 26, 28, 30, 34, -68, -68, 52, 70, 86, -54, 42, 60, -34, 14, 36, 30, -64, -48, -76, -36, -78, 66, 18, 96, 2], [62, -88, 90, -32, -40, 56, 18, 96, 72, -50, 20, 72, 64, -82, 30, 66, -32, 16, 64, 96, -82, 72, -94, -48, 14, 60, 6, -78, 44, -80, 22], [-42, -86, -16, -62, 4, -30, 46, 10, 94, -12, 14, 96, -62, 68, 72, 68, -58, 2, 26, -12, 2, -16, 32, 26, 92, 64, -62, -80, -70, 76, -14], [96, 78, -4, -34, -88, 34, 50, 0, 46, 94, 14, 26, 58, -14, 82, 24, 86, 74, -8, 50, 54, -66, 46, -80, 20, 74, 2, -68, 92, -96, -2], [74, -70, -36, 76, 90, 50, 74, 78, 12, 40, 0, -8, -18, -34, -66, 86, 48, 44, 18, 96, -66, 48, 0, -36, 72, -40, 50, -32, -2, -50, 78], [18, -80, 70, -16, 34, -54, -94, -40, 60, -4, -50, -44, -56, -68, 22, -12, 54, 10, 90, -76, -28, 76, 72, -2, -78, 34, -24, 14, -80, -86, 68], [16, -88, 82, -48, -90, 36, 56, -80, -44, 40, 18, -84, -30, 40, -48, 52, 74, 18, 84, 92, 76, -26, -8, -4, 32, -92, 10, -88, -74, -58, -56], [22, 98, 12, 44, 30, 70, -60, 62, -78, -60, 80, -96, 46, 8, 26, 54, 20, -58, 80, -36, 44, -20, 18, 36, -22, 50, 90, 64, -56, 4, -28], [-6, -18, -92, -68, 20, -22, -60, -50, -72, 64, -50, 76, -36, 40, -30, 64, 96, 2, -82, 52, -50, 20, 34, 52, -24, -14, 96, 76, -48, -6, -98], [-60, 48, -82, -38, -26, 98, 56, 98, 78, -82, -92, -70, 56, -80, -46, -96, -10, -70, -88, 92, -54, 16, 88, -26, -74, 34, -56, 54, -52, 2, 72], [16, 82, -70, 42, -40, 38, 48, -86, -28, 46, -40, -30, -54, 58, 94, -54, -88, 46, 42, 84, 58, -74, 94, -2, 72, -50, 72, 36, 26, 50, -80], [-80, -34, 16, 20, -72, 86, 22, 82, -64, -38, -24, -82, -30, 2, 32, 18, -88, 82, 0, 90, -36, -92, 50, -30, -72, -20, 74, -14, -42, 52, 66], [40, 54, 42, -34, -20, 18, 88, -32, -52, -40, -8, 8, 60, 0, 22, 94, -96, -72, -76, -18, 60, -52, -98, -92, 30, 66, 76, -38, -38, 24, 70], [-82, -60, 86, 98, -42, -12, -92, -78, 92, -90, 54, 0, 8, 98, 50, 80, -24, 20, -86, 56, -86, 38, 6, -44, -24, -2, 16, -50, 36, 10, 98], [-34, 92, -52, -72, -54, 64, -48, -46, 88, -28, -56, 92, -8, -18, -70, -48, -2, -42, -76, -62, -34, 8, -22, -4, -12, -14, -26, -46, 40, 12, -84], [50, 70, -52, -86, 50, 36, -18, -82, -12, -74, -90, 14, 18, -10, 80, 24, -22, -10, -30, 92, 70, 60, 16, -18, 10, 2, 2, 18, 44, -72, -72], [54, -66, 22, 76, -34, 68, -36, -50, -32, -20, -70, 44, 56, 88, -12, -32, 42, -30, 90, -88, 30, -10, -28, -16, 40, -58, 12, -70, 12, -24, 74], [48, -36, -52, -36, 8, -20, -60, 64, 50, 94, -64, -74, -70, 40, -80, 46, 22, 94, -52, -58, -76, -36, -76, 92, -76, -92, -64, -78, -2, -20, 62], [-30, 34, 74, -48, -56, -18, -8, 88, 18, 80, -72, -52, -52, 82, -20, 58, 58, -50, 68, 26, 18, 34, -86, -8, 40, 42, 12, 92, -14, -4, -78], [-18, -80, 66, 66, -14, 16, 26, -24, 32, 24, 58, 0, 36, -76, -48, 36, 88, -18, 42, -4, 2, 48, -90, -84, 2, 92, 78, 92, -62, 4, 72], [90, -56, -48, -68, 70, -2, -94, -52, -12, 2, 64, 12, -70, 18, 28, -98, -80, 48, 34, -58, 24, 6, -60, -54, -70, 96, 88, 38, 42, -40, 18], [-2, -48, 32, 62, -42, 70, -10, -42, 20, 88, 44, -12, -46, -10, -96, 18, 44, -46, 90, -6, 74, 88, 8, -42, 26, -10, 84, -28, -12, -88, -98], [56, -64, -4, 32, 98, 12, 82, -46, 80, 16, -32, 54, 54, -28, -56, 54, 88, -46, 68, -74, 24, 4, 96, -84, 86, 14, -66, 12, -64, -86, 10], [26, -50, 72, -2, -50, -88, 96, -24, 48, 96, 26, 24, 46, 80, -70, -84, -30, 64, 44, -86, 24, -20, 12, 96, -26, 42, 88, -44, -54, -84, -66], [-28, 90, -66, 46, 16, -84, 22, -62, 20, -26, 22, 86, 40, -2, -36, 60, 90, 14, -24, 32, 66, 32, 12, 92, 22, -82, -96, 20, -64, 16, -22], [26, -80, 12, -42, -80, 72, -10, 42, 26, -32, 56, 96, -34, -14, -28, 62, -58, -36, -24, -22, -86, -48, -28, 48, -26, 26, 38, 10, -42, -8, -26], [-76, 22, 60, 88, 38, 44, -62, -68, -96, -64, 12, 42, 94, 10, 90, 68, -44, 74, -28, -86, -20, -22, -60, -78, -20, 68, -32, -40, 12, -64, 82], [60, -66, -14, -90, 40, 26, 52, -70, 92, -64, 68, 6, -84, -32, -90, -30, 18, -68, -50, 68, 54, 24, -68, -92, -32, -40, -30, 78, 60, -94, -48], [-14, -2, 72, 70, 2, 24, -54, 14, 98, -2, 70, 24, -60, -28, -72, -36, -50, -12, 60, -98, -80, -46, -88, 28, -74, -94, -28, 92, 30, -38, -8], [-78, 26, -94, -24, 14, 80, 60, -80, -28, 86, 4, 54, 88, -34, 4, -44, 18, -96, 18, -28, 90, 88, 42, 8, 66, 24, 0, -70, -78, -64, -20]],29,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],38,),
    ([[91, 17, 91, 54, 63, 43, 59, 7, 5, 73, 55, 46, 78, 60, 96, 32, 22, 66, 40, 34, 2, 48, 97, 26, 34, 17, 56, 88, 69, 30, 52, 87, 98], [84, 89, 34, 38, 49, 47, 99, 97, 48, 75, 43, 13, 7, 21, 76, 88, 18, 29, 86, 94, 89, 1, 40, 87, 94, 33, 12, 87, 38, 46, 54, 56, 79], [24, 21, 46, 88, 21, 31, 78, 91, 69, 62, 88, 88, 49, 37, 21, 30, 71, 57, 48, 1, 63, 46, 78, 80, 10, 57, 52, 31, 90, 13, 16, 12, 67], [48, 3, 74, 98, 23, 56, 27, 66, 4, 38, 14, 29, 20, 9, 84, 72, 25, 18, 98, 21, 37, 9, 34, 16, 42, 11, 14, 73, 4, 79, 22, 63, 37], [73, 26, 87, 85, 18, 14, 96, 87, 71, 41, 67, 71, 69, 61, 19, 8, 31, 64, 28, 6, 20, 1, 50, 9, 13, 42, 41, 99, 43, 75, 24, 34, 67], [40, 92, 49, 22, 85, 79, 3, 12, 66, 91, 64, 88, 85, 56, 1, 58, 2, 49, 46, 3, 69, 47, 39, 64, 97, 72, 36, 6, 97, 67, 47, 81, 50], [10, 22, 88, 26, 66, 41, 29, 55, 34, 86, 35, 31, 13, 31, 26, 5, 72, 45, 93, 86, 99, 99, 87, 91, 80, 40, 89, 44, 20, 33, 55, 42, 19], [88, 43, 80, 48, 35, 35, 80, 57, 89, 64, 10, 33, 55, 6, 76, 64, 59, 65, 62, 23, 32, 78, 45, 87, 41, 96, 54, 44, 82, 63, 14, 76, 34], [40, 32, 33, 4, 36, 81, 35, 1, 35, 22, 98, 37, 69, 69, 8, 4, 33, 61, 80, 37, 73, 45, 18, 17, 7, 38, 90, 59, 98, 20, 79, 21, 67], [15, 71, 7, 16, 55, 43, 65, 61, 11, 69, 87, 34, 62, 4, 30, 6, 10, 27, 22, 28, 18, 3, 28, 52, 58, 87, 70, 74, 66, 25, 68, 46, 73], [34, 89, 5, 16, 91, 93, 86, 19, 95, 4, 3, 71, 34, 25, 96, 86, 60, 86, 90, 72, 88, 2, 29, 91, 66, 92, 60, 34, 81, 22, 56, 90, 31], [83, 43, 58, 84, 38, 98, 3, 17, 5, 48, 50, 9, 84, 85, 1, 16, 23, 57, 30, 59, 47, 1, 59, 33, 33, 86, 82, 29, 2, 3, 2, 53, 57], [62, 77, 77, 80, 62, 72, 4, 41, 10, 97, 32, 85, 35, 70, 10, 18, 33, 93, 97, 96, 14, 54, 86, 31, 65, 45, 31, 3, 56, 85, 20, 35, 10], [54, 24, 10, 51, 45, 90, 47, 83, 6, 32, 60, 58, 74, 7, 15, 62, 47, 94, 99, 48, 12, 80, 13, 66, 52, 19, 62, 13, 7, 79, 20, 34, 44], [25, 76, 25, 5, 39, 26, 50, 69, 39, 35, 90, 80, 33, 78, 80, 62, 62, 35, 96, 67, 57, 44, 22, 52, 80, 6, 78, 24, 84, 64, 67, 3, 90], [10, 10, 92, 4, 17, 49, 6, 65, 56, 2, 46, 57, 4, 37, 37, 65, 18, 65, 92, 24, 36, 98, 86, 6, 63, 64, 9, 77, 40, 64, 32, 14, 67], [36, 12, 98, 90, 96, 94, 17, 26, 83, 26, 16, 89, 29, 98, 2, 59, 78, 14, 51, 40, 84, 1, 83, 50, 97, 65, 68, 20, 20, 48, 80, 15, 87], [26, 1, 56, 67, 76, 38, 19, 29, 90, 58, 62, 77, 12, 92, 22, 49, 44, 83, 84, 51, 25, 9, 61, 69, 1, 2, 83, 20, 34, 38, 70, 2, 32], [54, 28, 21, 94, 62, 51, 60, 43, 76, 13, 1, 45, 5, 84, 52, 21, 38, 39, 89, 9, 67, 56, 93, 45, 38, 79, 95, 42, 70, 68, 15, 52, 44], [46, 34, 89, 97, 46, 41, 55, 63, 5, 91, 95, 40, 3, 31, 65, 53, 35, 42, 8, 75, 24, 31, 59, 19, 84, 79, 60, 91, 63, 99, 83, 75, 23], [52, 96, 12, 22, 5, 84, 10, 69, 56, 10, 74, 27, 85, 92, 96, 77, 75, 89, 26, 81, 18, 73, 83, 37, 43, 4, 74, 39, 29, 75, 98, 91, 34], [74, 23, 95, 17, 90, 40, 71, 6, 98, 80, 53, 52, 48, 19, 40, 38, 14, 13, 24, 90, 25, 96, 51, 10, 38, 89, 16, 85, 51, 46, 84, 94, 50], [72, 34, 29, 54, 13, 1, 91, 39, 55, 7, 69, 60, 72, 10, 88, 35, 37, 62, 73, 5, 2, 15, 76, 4, 99, 5, 31, 19, 65, 29, 62, 82, 14], [70, 95, 44, 52, 30, 12, 29, 54, 6, 6, 61, 32, 5, 16, 53, 2, 16, 2, 85, 81, 63, 50, 2, 23, 41, 32, 61, 61, 64, 53, 22, 63, 92], [95, 62, 20, 58, 14, 38, 81, 30, 11, 59, 93, 72, 69, 73, 17, 15, 41, 81, 58, 84, 59, 73, 89, 15, 62, 81, 79, 76, 72, 82, 12, 42, 4], [46, 61, 24, 78, 8, 36, 91, 60, 87, 15, 35, 77, 14, 30, 64, 25, 16, 3, 57, 95, 14, 89, 30, 87, 47, 39, 90, 25, 82, 27, 85, 65, 81], [23, 53, 6, 29, 53, 66, 38, 15, 78, 59, 47, 91, 13, 12, 96, 8, 93, 65, 9, 85, 12, 55, 11, 89, 91, 6, 24, 56, 55, 98, 23, 78, 76], [78, 15, 32, 58, 70, 69, 8, 51, 64, 42, 79, 24, 73, 8, 38, 21, 18, 31, 89, 60, 60, 17, 87, 62, 56, 94, 59, 83, 39, 63, 72, 45, 41], [16, 71, 94, 55, 37, 40, 84, 88, 62, 15, 26, 52, 36, 31, 20, 70, 89, 1, 52, 15, 77, 12, 79, 26, 2, 75, 10, 53, 27, 63, 55, 76, 50], [42, 65, 39, 23, 69, 31, 84, 47, 68, 53, 28, 7, 10, 54, 62, 37, 61, 82, 24, 29, 69, 44, 44, 34, 95, 44, 31, 7, 21, 9, 64, 51, 20], [33, 74, 71, 30, 98, 92, 74, 50, 90, 23, 8, 90, 81, 38, 5, 12, 65, 22, 99, 44, 30, 1, 81, 82, 33, 13, 47, 52, 17, 88, 40, 91, 89], [69, 97, 51, 49, 71, 2, 43, 7, 51, 86, 25, 74, 91, 55, 42, 23, 83, 55, 73, 53, 55, 75, 93, 75, 69, 81, 6, 75, 2, 66, 51, 37, 19], [65, 39, 98, 7, 42, 20, 34, 4, 22, 20, 26, 80, 56, 70, 7, 95, 87, 49, 19, 17, 58, 65, 29, 22, 26, 15, 28, 93, 9, 16, 75, 76, 78]],20,)
        ]
  for i, parameters_set in enumerate(param):
    idx = i
    f_gold(* parameters_set)
    result = parameters_set
"-----------------"
#TESTED_PROGRAM"-----------------"
test()
