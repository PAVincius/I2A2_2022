# Entropy and Information Entropy

## Entropy :fire: :cool:

Entropy can be thought of as a measurement of the energy between two objects. If we call it A and B of some arbitrary, but identical objetcs, the energy they have can be stored between them in a variety of different states. There are probabilistic measurements of which state are likely to happen next between the two objects based on how the energy is distributed.

If the two objects are the same we have this distribution:


Imagine that we have A and B, and all the energy they have is stored in A, this is called Low Entropy, because the energy is concentrated, and High Entropy means that the energy is distributed evenly.

In real life, in a system with A and B objects, which A has more energy than B, there's a chance of an interaction between these two to results in the A getting energy. But this is so small that just never happens.

Hence an object losses its energy to the evironment or to another object with less energy than it. It's about the flow of energy between something that possess some energy.

## Information Theory

A subfield of mathematics and it's foundational concept is the quantification of the amount of information in things like events, more likely to measure how much surprise there is in a event. If the event is unlikely to happen, that's called a Low Probability event.

The more unlikely the event, more information will be necessary to represent them as normal events.

## How's it calculated?

We can calculate the amount of information by using the formula:

$information(x) = -log( p(x) )$

Where log() is the base-2 logarithm and p(x) is the probability of the event x.

We can also calculate the entropy for a random variable :sunglasses:!

In that case we call that we are calculating the information entropy or simply entropy. And as you could guess, this is a analogy from the term entropy from physics.

The intuition for entropy is that it is the average number of bits required to represent or transmit an event drawn from the probability distribution for the random variable. The formula to calculate entropy in a random variable is:

$H(X) = -sum(each k in K p(k) * log(p(k)))$

**OBS: the log function uses base 2.**

The greater value of entrop will be when all the events are likely to happen and the lowest would be if it has an event with a probability of 1.0(100%).

