# kiri

Branch   |[GitHub Actions](https://github.com/richelbilderbeek/kiri/actions)                                     |[![Travis CI logo](man/figures/TravisCI.png)](https://travis-ci.org)                                                |[![AppVeyor logo](man/figures/AppVeyor.png)](https://www.appveyor.com)                                                                                                                   |[![Codecov logo](man/figures/Codecov.png)](https://www.codecov.io)
---------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------
`master` |![R-CMD-check](https://github.com/richelbilderbeek/kiri/workflows/R-CMD-check/badge.svg?branch=master) |[![Build Status](https://travis-ci.org/richelbilderbeek/kiri.svg?branch=master)](https://travis-ci.org/richelbilderbeek/kiri) |[![Build status](https://ci.appveyor.com/api/projects/status/jv76errjocm5d5yq/branch/master?svg=true)](https://ci.appveyor.com/project/richelbilderbeek/babette-on-windows/branch/master)|[![codecov.io](https://codecov.io/github/richelbilderbeek/kiri/coverage.svg?branch=master)](https://codecov.io/github/richelbilderbeek/kiri/branch/master)
`develop`|![R-CMD-check](https://github.com/richelbilderbeek/kiri/workflows/R-CMD-check/badge.svg?branch=develop)|[![Build Status](https://travis-ci.org/richelbilderbeek/kiri.svg?branch=develop)](https://travis-ci.org/richelbilderbeek/kiri)| .                                                                                                                                                                                       |[![codecov.io](https://codecov.io/github/richelbilderbeek/kiri/coverage.svg?branch=develop)](https://codecov.io/github/richelbilderbeek/kiri/branch/develop)

This will be our Python version of the ancient game of Mastermind.

## Libraries

 * [PyGame](https://www.pygame.org/wiki/GettingStarted)

## The Game
* The codemaker picks 4 pegs out of the six different colours and place them behind the visor. You're allowed to place multile pegs in one colour.
* The codebreaker (this is you!) places four pegs on the first row.
* Now the codemaker uses the red/black pins to state how many pegs are both the right colour AND in the right place.
* Uses the white pins to state pegs in the right colour but in the wrong place.
* The codebreaker guesses again accordingly and continues to do so in as little turns as possible until the code is broken.

