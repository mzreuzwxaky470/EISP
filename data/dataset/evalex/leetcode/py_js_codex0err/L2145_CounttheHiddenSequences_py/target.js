function f_gold(differences, lower, upper) {
    var num = mi = mx = 0;
    for (var d of differences) {
        num += d;
        mi = Math.min(mi, num);
        mx = Math.max(mx, num);
    }
    return Math.max(0, upper - lower - (mx - mi) + 1);
}

