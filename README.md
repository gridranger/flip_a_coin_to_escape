# Flip A Coin To Escape
Python implementation of Coins on a Chessboard riddle.

Features:
* board size can be set or left random
* layout of the coins could be set or left random
* key could be placed manually or randomly
* result drawing could be turned on/off

Expected result is something like this:
```
INFO:root:Board size 8×8; key is hidden at 40.
INFO:root:The coin to flip is the one at square 31.
INFO:root:Successful check, key was found at: 40
INFO:root:

*: key location; @: coin to flip
+----+----+----+----+----+----+----+----+
|1  0|0  1|1  2|0  3|0  4|0  5|1  6|1  7|
+----+----+----+----+----+----+----+----+
|1  8|0  9|0 10|0 11|1 12|0 13|1 14|0 15|
+----+----+----+----+----+----+----+----+
|1 16|0 17|0 18|0 19|0 20|0 21|1 22|0 23|
+----+----+----+----+----+----+----+----+
|1 24|0 25|1 26|1 27|1 28|0 29|1 30|0  @|
+----+----+----+----+----+----+----+----+
|1 32|0 33|1 34|1 35|0 36|1 37|1 38|1 39|
+----+----+----+----+----+----+----+----+
|1  *|1 41|1 42|1 43|0 44|1 45|0 46|0 47|
+----+----+----+----+----+----+----+----+
|1 48|1 49|0 50|1 51|1 52|1 53|1 54|1 55|
+----+----+----+----+----+----+----+----+
|1 56|0 57|1 58|0 59|0 60|1 61|1 62|1 63|
+----+----+----+----+----+----+----+----+
```