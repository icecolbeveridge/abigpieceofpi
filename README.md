# A Big Piece of Pi
A 1D Monte Carlo approach to calculating pi

Apparently, [Matt Parker is planning to calculate pi on the moon](https://www.youtube.com/watch?v=nGtVej1Qx5Y) -- which, I'm sure we can all agree, is a worthwhile and useful endeavour. We do these things, not because they are hard, but because they are ridiculous.

Anyway, Matt's suggested 2D Monte Carlo strikes me as *ludicrously* inefficient for a space mission, even for terrible Python code. Wouldn't it make much more sense to do with just one random variable? Special bonus, we can use his [absolute favourite method for calculating the area of a triangle](https://en.wikipedia.org/wiki/Heron%27s_formula)!

Usage: just call 

    python hero.py

... and it'll run 10,000 iterations for you. Enjoy!
