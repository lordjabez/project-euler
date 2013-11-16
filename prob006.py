for n in range(100, 101):
    _nums = range(1, n + 1)
    _sum = sum(_nums)
    _squares = (i * i for i in _nums)
    _sumofsquares = sum(_squares)
    _squareofsum = _sum * _sum
    _delta = _squareofsum - _sumofsquares
    print(n, _delta)


    