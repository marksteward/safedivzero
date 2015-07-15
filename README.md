Safe zero-divide
================

Everyone hates division-by-zero errors. Free yourself
of these nasty edge cases by allowing Python to meaningfully
evaluate a zero division.

Usage
=====

```
>>> import safedivzero
>>> 1 / 0
```

No more exceptional behaviour! Continue calculating cleanly,
throwing errors to the wayside, as you might in SQL, bash,
or IEEE-754 floating point. Follow in the great programming
tradition of **good enough**.

FAQ
===

Why does 0/0 not work?
----------------------

Ask the [mathematicians][https://en.wikipedia.org/wiki/Indeterminate_form]. If you're trying to get the mean
of an empty set, the answer is probably None.
