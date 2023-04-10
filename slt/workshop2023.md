---
title:
    Singularities against the Singularity
description:
    Workshop on SLT and Alignment
---

This is the webpage for the 2023 conference "Singularities against the Singularity" in Berkeley, CA. For further information see the [announcement](https://www.lesswrong.com/posts/HtxLbGvD7htCybLmZ/singularities-against-the-singularity-announcing-workshop-on) and the page for [Registration](https://docs.google.com/forms/d/e/1FAIpQLSfehQkokQeTd9KzRRhw9QsjNB25iOuTOrEeA-V93OW0zsUnlg/viewform?usp=sf_link).


## The Primer

The aim of the Primer is to give a general introduction to Singular Learning Theory (SLT) and related areas of mathematics and physics, with the aim of providing a foundation for theoretical and experimental work on AI alignment. More concretely, we aim to explain the **Free Energy Formula** derived by Watanabe, what its terms mean, how to apply it to understand the phase structure of a learning machine, and how to derive intuition for the resulting picture from physics.

| Time          | Monday | Tuesday | Wednesday | Thursday | Friday |
|---------------|--------|---------|-----------|----------|--------|
| 9:00-10:00     | Welcome / SLT High 1 | SLT High 2 | SLT High 3 | SLT High 4 | SLT High 5 |
| 10:30-11:00    | break  | break   | break     | break    | break  |
| 11:00-12:00    | SLT Low 1 | SLT Low 2 | SLT Low 3 | SLT Low 4 | SLT Low 5 |
| 12:00-1:30     | lunch  | lunch   | lunch     | lunch    | lunch  |
| 1:30-3:00      | Physics 1 | Physics 2 | Physics 3 | Physics 4 | Physics 5 |
| 3:00-3:30      | break  | break   | break     | break    | break  |
| 3:30-4:30      | Alignment 1 | Alignment 2 | Mech interp 1 | Mech interp 2 | Wrapup |

Each day is organised around a general theme, with the final day culminating in a sketch of the derivation of the Free Energy Formula.

* **Monday**: Introduction
* **Tuesday**: Phases and phase transitions
* **Wednesday**: Geometry and RLCTs
* **Thursday**: Loss landscape
* **Friday**: The Picture

### SLT High Road

The SLT "high road" explains the conceptual toolkit and how to use it to reason about learning machines, leaving the proofs and details for later ("just tell me why it's useful to know this").

* **SLT High 1** (*Dan Murfet*): Welcome and introduction, survey of the Primer
* **SLT High 2** (*Dan Murfet*): Phases, free energy formula, phase transitions in `n` and the true distribution
* **SLT High 3** (*Edmund Lau*): Definitions of and intuitions for the RLCT, volume codimension, `E[nL_n(w)]`, examples
* **SLT High 4** (*Edmund Lau*): Myths, SGD is not Langevin, Flatness, Laplace, etc
* **SLT High 5** (*Dan Murfet*): Complex vs simple, logic of phase transitions, effective learning curves, "phase structure is geometry of level sets"

### SLT Low Road

The SLT "low road" looks at detailed examples and calculations and sketches of how the mathematical theory fits together ("show me how it works in an example").

* **SLT Low 1** (*Edmund Lau*): Introduction to Bayesian probability, Bayesian posterior and model selection, regular vs singular
* **SLT Low 2** (*Liam Carroll*): Phase transitions in toy ReLU networks
* **SLT Low 3** (*Zhongtian Chen*): Introduction to Algebraic Geometry I, resolution of singularities
* **SLT Low 4** (*Dan Murfet*): Introduction to Algebraic Geometry II, singularities and Density of States
* **SLT Low 5** (*Zhongtian Chen*): Sketch of derivation of Free Energy Formula (i.e. p.31 of gray book)

### Physics

* **Physics 1** (*Jesse Hoogland*): The Physics of Intelligence: from Classical to Singular Learning Theory
* **Physics 2** (*Jesse Hoogland*): Statistical mechanics, Boltzmann distribution, free energy, phases and phase transitions
* **Physics 3** (*Dan Murfet*): Density of states in solid state physics, van Hove singularities
* **Physics 4** (*Jesse Hoogland*): Singularities and nonlinear dynamics (following e.g. Strogatz)
* **Physics 5** (*??*): Critical phenomena and universality (speaker TBC)

### Alignment and Mechanistic Interpretability

* **Alignment 1**
* **Alignment 2**
* **Mech interp 1**
* **Mech interp 2**

### References

* For thermodynamics, we recommend Callen, H. B. (1985). Thermodynamics and an introduction to thermostatistics (2nd ed.). John Wiley & Sons.

* The [metauni SLT seminar](https://www.metauni.org/slt).
* The [SLT for Alignment](https://www.metauni.org/slt/align) page.

# Week 2

The second week of the workshop is for discussing open problems, collaboration and more mathematical details beyond the introductions in the first week.

* (*Liam Carroll*) The MCMC life
* (*Dan Murfet*) Programs as Singularities - structure vs structure
* Open Problem sessions
* Toy Models of Superposition
* Analytic to algebraic for 1-layer tanh (?)
* Exercise sessions
* The plan
* Singular structure inference vs circuit inference (e.g. [causal scrubbing](https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing), [looking for circuits](https://www.alignmentforum.org/posts/XNjRwEX9kxbpzWFWd/200-cop-in-mi-looking-for-circuits-in-the-wild)).
