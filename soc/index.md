# Shadows of Computation

Welcome to Shadows of Computation. This online course covers the foundations of category theory, which is used by computer scientists to abstract computing systems to reveal their intrinsic mathematical properties. This course is targeted towards those who are mathematically inclined, and interested in learning how category theory can be used in theoretical computer science.

There is also a secondary aim of the course: to teach how to present theoretical ideas. Two of the lectures will be about lecturing, and students will be encouraged to present a short talk at the end of the course, covering an extension of the ideas presented in the lectures.

This course will be taught at [metauni](https://metauni.org), using Roblox for the 3D virtual environment and voice chat and Discord for community.

* **Time**: starting October 10 2022, weekly 1.5 hour lectures on Mondays 19:30-21:00 AEST, weekly 1 hour exercise sessions Wednesdays 20:00 AEST. The class will run for 9 weeks.
* **Location**: [Moonlight Forest](https://www.roblox.com/games/start?placeId=8165217582&launchData=pocket:Moonlight%20Forest%201), a 3D virtual world built in Roblox, which is part of [metauni](https://metauni.org). At metauni we write on blackboards (which retain their contents when you leave) and talk using position-based voice chat (people far away can't hear you). We also use the [metauni Discord](https://discord.gg/9yBaAxPSK8) for communication outside of Roblox. See the [instructions](https://metauni.org/posts/instructions/instructions) for how to set up spatial audio.

> **Important**: _you must have spatial voice set up (before you join a lecture) to hear other people speaking_.

* **Goal**: to introduce the beauty of category theory in a concrete way which reveals the philosophical ideas, the links to and between foundations, mathematics, and theoretical computer science. By concrete, we mean that we will not be telling you these ideas and insisting you accept them, but instead we will let the mathematics do the talking.
* **Resources**: the textbook is the excellent textbook E. Rhiel "[Category Theory in context](https://math.jhu.edu/~eriehl/context.pdf)", which is available freely online. Other resources for the computer science component will be used and referenced throughout the course. An example of the ideas we will explore can be found here: "[Theorems for free](https://people.mpi-sws.org/~dreyer/tor/papers/wadler.pdf)".

Organisers:
* [Will Troiani](https://williamtroiani.github.io/Mathematics.html) ([Fleetwood_Obdurate](https://www.roblox.com/users/2312973422/profile) on Roblox) and [Billy Snikkers](https://billy-price.github.io/web/) ([blinkybill](https://www.roblox.com/users/2293079954/profile) on Roblox), neither with PhDs in category theory.

**Subscribe to the mailing list** to receive updates on future classes (if you keep an eye on the `#shadows-of-computation` channel in the metauni Discord, no need to sign up here).

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/adminmetauni" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/adminmetauni', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><p><label for="tlemail">Enter your email address to get updates on Shadows of Computation:</label></p><p><input type="text" style="width:140px" name="email" id="tlemail" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /><p><a href="https://tinyletter.com" target="_blank">powered by TinyLetter</a></p></form>

## Course content

Each lecture will be 1.5hr. In the schedule below, the references are given after the section number, eg `R 1.3` refers to Section 1.3 of Category Theory in Context. The lecturer is given in brackets, `(B)` means Billy and `(W)` means Will (subject to change).

* **Lecture 1:** Making subtle ideas apparent `(W) R 1.1`.
* **Lecture 2:** Structure preservation `(B) R 1.3`.
* **Lecture 3:** Naturality/how to present mathematics 1 `(W) R 1.4`.
* **Lecture 4:** Limits `(B) R 3.1, 3.2`.
* **Lecture 5:** The untyped and the simply typed λ-calculus `(B) R 1.2, 3.3` [Lectures on the Curry-Howard Isomorphism](https://disi.unitn.it/~bernardi/RSISE11/Papers/curry-howard.pdf).
* **Lecture 6:** The category of λ-terms and the Curry-Howard correspondence `(W)` ([Gentzen-Mints-Zucker Duality](https://arxiv.org/abs/2008.10131).
* **Lecture 7:** The Yoneda Lemma `(W) R 2.2`.
* **Lecture 8:** Monads/how to present mathematics 2 `(W) R 5.1`.
* **Lecture 9:** Moggi's Notions of Computation `(W)` [Notions of Computation and Monads](https://www.cs.cmu.edu/~crary/819-f09/Moggi91.pdf).

<!-- All videos can be found in [the PRGM playlist](). -->

## Exercise Sessions

We encourage learning by doing. Each week there will be assigned exercises for you to practice and better your understanding of the lecture content with your peers. There will be a regular exercise session on Wednesdays at 20:00 AEST in [Moonlight Forest](https://www.roblox.com/games/start?placeId=8165217582&launchData=pocket:Moonlight%20Forest%201), where you can get help from Billy, Will, or another experienced tutor.

It's hard to pick a time that works for every timezone, so it is also encouraged for you to schedule your own times to meet with other students for a study/exercise session.

## Exercise Sheets

Exercise sheets will appear here and also in the discord channels for each week.

- **Week 1:** [Exercises](./Exercises/Week1.pdf)
- **Week 2:** [Exercises](./Exercises/Week2.pdf)
<!-- - **Week 3:** [Exercises](./Exercises/Week3.pdf) -->

## Pre-requisites

High school algebra plus a little bit of linear algebra (a basic familiarity with finite dimensional complex vector spaces). More precisely, you should have experience working with linear transformations and bases. You should know

* The definition of a linear transformation, 
* The definition of a basis for a finite dimensional complex vector space.

In particular, we assume no familiarty nor experience with coding whatsoever.

You should also be comfortable with functions and terms like [domain](https://en.wikipedia.org/wiki/Domain_of_a_function), [codomain](https://en.wikipedia.org/wiki/Codomain), [image and preimage](https://en.wikipedia.org/wiki/Image_(mathematics)), [injective, surjective, bijective](https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection), [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product). If you want to brush up, here are some modules from Khan Academy that cover the necessary background:

* [Introduction to Algebra](https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra)
* [Polynomial expressions, equations and functions](https://www.khanacademy.org/math/algebra-home/alg-polynomials)
* [Matrices](https://www.khanacademy.org/math/algebra-home/alg-matrices) up to "Row-echelon form and Gaussian elimination"
* [Basic set operations](https://www.khanacademy.org/math/statistics-probability/probability-library/basic-set-ops/v/intersection-and-union-of-sets).
* [Functions](https://www.khanacademy.org/math/algebra-home/alg-functions).

For tablet and microphone recommends see the [hardware](https://www.metauni.org/posts/instructions/hardware) page.

## Registration

Registration is now open. Here is the registration process:

1. Follow Steps 1 and 2 of the [instructions](https://metauni.org/posts/instructions/instructions) to setup your Roblox and Discord accounts.
2. Open the metauni Discord server and post in the `#soc-registration` channel with your Roblox username and how you want people to refer to you. This is mainly for your classmates, so you may wish to include a brief description of your interests and reasons for attending the class, and any links to personal webpages or Twitter accounts you want people to see. No pressure though, your Roblox username is enough (for administration purposes we need to know the connection between Discord accounts and Roblox usernames).
3. Join the [metauni Roblox group](https://www.roblox.com/groups/13108882/metauni#!/about). This way we can give you permission to write on the blackboards throughout metauni.

## Foundations Seminar

Every two weeks we also host the foundations seminar, which will run immediately after the Shadows of Computation lecture, at 21:00 AEST. [Click here for details](https://metauni.org/foundations/). The first seminar will be on the 17th of October at 21:00 AEST.