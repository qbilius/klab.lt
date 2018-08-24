---
title: Summary of: Perceptual organization of two-dimensional patterns
datestamp: 2013-09-22 16:13:21
categories: Blog
tags: Reviews & Summaries
reviewof: Geisler & Super, 2000
reviewof_link: http://dx.doi.org/10.1037/0033-295X.107.4.677
---

In 2000, Geisler and Super proposed [a generic model for grouping two-dimensional patterns](http://dx.doi.org/10.1037/0033-295X.107.4.677) ([pdf](https://dl.dropboxusercontent.com/u/2498793/klab/Geisler_Super_2000_Perceptual_organization_of.pdf)), where observers see distinct regions based on grouping over a certain dimension (e.g., proximity in dot lattices, orientation differences for figures used by Victor Lamme and Pieter Roelfsema). Their simple algorithm manages to correctly group a wide variety of typical (textbook) Gestalt displays. However, for some reason this paper never got picked up (currently it has only 32 citations).

Background
----------

Existing texture segregation models:

-   Feature-based: extract features and cluster them
-   Filter-based: apply a filter of size or orientation, then process by a non-linearity

Limitations:

-   Segregation by shape: need to extract and use specific shapes, rather than features
-   Nonstationary structures (ones that change smoothly and systematically, e.g., contour integration): need some form of texture integration

The model
---------

**Step 1. *Receptive field matching to detect shape primitives***

**Step 2. *The total grouping difference between each pair of primitives***

*Total grouping difference:* weighted sum of various dimensions. Relative strength of each grouping principle was measured using three stimuli, varying their properties and asking participants to indicate which two of them group together. Final weights:


| **Dimension**  | **Difference measure**                         | **Weight**
| -------------- | ---------------------------------------------- | ------------
| Position       | sqrt((x\_i-x\_j)\*\*2 + (y\_i-y\_j)\*\*2)      | .147
| Size           | |log(s\_i/s\_j)|                               | 1.490
| Orientation    | |ori\_i - ori\_j|                              | .017
| Shape (form)   | matching error after the best transformation   | .327
| Symmetry       | 0 if symetric, 1 if not                        | -
| Luminance      | |log(lum\_i/lum\_j)|                           | -
| Contrast       | |log(contrast\_i/contrast\_j)|                 | -

**Step 3. *Initial transitive or nontransitive grouping using binding criterion rules***

-   *The generalized uniqueness principle:* At any time and at any level in the hierarchy, a given object (part) can be assigned to only one superordinate object (whole).
-   *Transitive grouping:* Binding indirectly such that if A and B bind, B and C bind, then A and C bind even if their grouping strength is low.
-   *Nontransitive grouping:* Binding together of parts that share some common property or cluster of properties.

To discover groups, a *binding criterion* must chosen, for example, using these rules:

-   *Stability:* groups must remain stable for a range of binding criterion values (local minima).
-   *Performance:* optimize performance in a given task.
-   *Recognition:* binding criterion should yield recognized objects or parts of objects.

**Step 4. *Transformational matching***

Find the best transformation between the groups found in Step 3. Difference is measured as the total normalized weighted Euclidean distance in the feature space between all pairs of points. Final difference is computed by finding the best transformation that minimizes this difference and applying a log, so that this difference zero or more. Objects can be transformed using:

-   translation
-   rotation
-   scaling
-   reflection
-   luminance scaling
-   contrast scaling

*Note:* A simple template matching is not good because perceptually similar shapes (a square and wiggly square) might produce a worse overlap than some perceptually dissimilar stimulus (like a triangle)). Alternatively, attribute matching could be used where properties of groups would be compared. This mechanism is not used in the model however*.*

**Step 5. *Transitive or nontransitive grouping using binding criterion rules***

Repeat (4) and (5) for *multilevel grouping* where grouping occurs over higher-level structures. Multilevel grouping prefers groups with the smallest overall grouping error.

[caption id=“attachment\_710” align=“alignnone” width=“614”][![Multilevel grouping](multilevel-1024x409.png "Multilevel grouping")](multilevel.png) **Multilevel grouping.** Figures on the left are perceived as two I’s (with serifs) even though transitive grouping would bind parts as seen on the right. Panel on the right also demonstrates that the effect is not due to closure or other single-level grouping principles. Adapted from Fig. 5 in [Geisler & Super (2000)](http://dx.doi.org/10.1037/0033-295X.107.4.677).[/caption]
