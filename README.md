Safe zero-divide
================

Everyone hates division-by-zero errors. Free yourself
of these nasty edge cases by allowing Python to sensibly
evaluate a zero division

Usage
=====

```
>>> import safedivzero
>>> hex(1 / 0)
```

No more exceptional behaviour! Continue calculating cleanly
while errors cascade to the final step, as you might in SQL,
or IEEE-754 floating point.

