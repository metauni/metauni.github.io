---
title:
    metauni Alignment Project
description:
    There are no algebraists in foxholes
---

This working document contains ideas for applying Singular Learning Theory (SLT) to AI alignment. There is an [FAQ](/align-faq). 

# The Alignment Problem

We are likely to develop beyond-human AI systems within the next few decades, [possibly much sooner](https://www.youtube.com/watch?v=CJ1DUtpiYqI).
Those systems are likely to be "agentic" (=have goals) because [agents are more capable and may even be necessary to tackle many common problems](https://gwern.net/tool-ai). 

Agentic systems are likely to be ["power-seeking"](https://80000hours.org/problem-profiles/artificial-intelligence/#power-seeking-ai) — certain instrumental goals such as power are common to almost all goal-seeking systems. 

They are also unlikely to be aligned with human values by default because [capabilities generalize faster than alignment](https://www.lesswrong.com/posts/GNhMPAWcfBCASy8e6/a-central-ai-alignment-problem-capabilities-generalization).

In short, [AI poses an existential risk to humanity](https://80000hours.org/problem-profiles/artificial-intelligence/). 

## Interpretability via Universality

A shared component of [many alignment research plans](https://www.lesswrong.com/posts/QBAjndPuFbhEXKcCr/my-understanding-of-what-everyone-in-technical-alignment-is) is [developing powerful transparency and interpretability tools](https://www.lesswrong.com/posts/nbq2bWLcYmSGup9aF/a-transparency-and-interpretability-tech-tree). If we can introspect what a system is doing and how it changes during training, we may be able to anticipate "sharp left turns", detect deception, and avoid other failure modes.

Current approaches to mechanistic interpretability [have been criticized for being ad-hoc and unscalable](https://www.alignmentforum.org/s/a6ne2ve5uturEEQK7/p/wt7HXaCWzuKQipqz3). Here, we describe an approach to scalable mechanistic interpretability of neural networks based on SLT and the

* **Universality hypothesis**: many of the representations and algorithms encoded by neural networks are approximately universal.

This hypothesis has been articulated for example [here](https://distill.pub/2020/circuits/zoom-in/#claim-3). If (1) this hypothesis holds for a sufficiently broad class of the computations carried out by a network, (2) we have tools that allow us to discover approximations to those representations and algorithms, and (3) those tools can be run at industrial scale, then interpretability could contribute to aligning advanced AI systems.

# The Plan

In outline, the plan has three parts:

- **Spectroscopy of Singularities:** Construct **devices** for probing the **density of states** of neural networks, modelled on the role of scanning tunneling microscopes in solid state physics (talk ref). These devices reveal information about divergences of the density of states and the singularities in level sets of the loss function that generate them.

- **Components as Concepts:** Use the spectroscopy to get information about the essential components of the exceptional divisor of the resolution of the singularities dominating phases encountered during training, and match the phase transition structure to concepts learned during training, as tracked by other probes.

- **Programs as Constructions:** By tracking the phase transitions in the network, obtain an understanding of (parts of) the final trained parameter as a function of the history of the formation and deformation of concepts encountered during training.

These ideas are grounded in **Singular Learning Theory (SLT)**, a theory of universal behaviour of learning machines based on algebraic geometry and statistics, and **Conformal Field Theory (CFT)**, a theory of universality classes of physical systems, their "representations" and the RG flows between them. Both fields have a deep relation to singularity theory, in SLT because singularities in the KL divergence cause divergences in the density of states, which determine key quantities in Bayesian learning, and in CFT due to the classification of universality classes (this is the subject of the LG/CFT correspondence).

This picture is in some sense a *necessary consequence* of the universality hypothesis: given the content of SLT and the relation between singularities and CFT etc., plus the presence of scaling laws, *if* there are universal representations and algorithms in neural networks then the natural explanation given what we know about mathematics and mathematical physics is something like the above.

The plan is scoped on the order of ~10 years and presumes:

- Modest progress on pure mathematical foundations in Singular Learning Theory (SLT) and related fields
- Significant progress in a layer of "theoretical physics" between the pure theory of SLT and experiments (more on this below)
- Large scale investment in experiments and ecosystems of devices and interpretability stacks

Note: Universality here does *not* mean that all training runs will learn the same representations. The term is used in the physical sense: the representations and algorithms that compute with them are in some sense scale invariant (where scale here means something like how closely you are zoomed in on a level set of the loss function).

For an outline of how mechanistic interpretability impacts alignment, see [here](https://www.lesswrong.com/posts/Jgs7LQwmvErxR9BCC/current-themes-in-mechanistic-interpretability-research).

* *Authors:* Dan Murfet, you?
* *Last update:* 18/2/2023

Jargon

* SLT - Singular Learning Theory
* CFT - Conformal Field Theory
* LG - Landau-Ginzburg
* SSP - Solid State Physics
* DOS - density of states

## Spectroscopy of Singularities

Divergences in the density of states are responsible for many electrical properties of materials, and detecting these divergences by indirect probes (which look for example at differential conductance) is a key experimental technique in solid state physics. There is no principled reason analogous devices cannot be constructed for learning machines. The plan depends on finding scalable devices of this kind. Let us call them **spectroscopes**.

We envision running such devices during a distribution of training runs of a neural network, and using them to examine the phases and phase transitions encountered. This gives us some idea of the nature of the singularities encountered and the universality class. We match this against empirically observed behaviour (e.g. performance on a battery of tests) to infer what kind of progress was made in each phase transition. It is likely to be impossible to accurately estimate the Bayesian posterior or RLCTs for very large networks, but if each phase transition only involves a smaller subset of the weight directions, then the spectroscope can look in these directions.

**Work to be done:**

- Find candidate targets (analogues of differential conductance) and experiment with measurements in toy models
- Survey applications of deep learning to microscopy, simulating materials and obtaining accurate estimates of DOS

## Concepts as Components

From SLT we know that singularities in the level sets of the loss function determine learning behaviour, and the local free energy of phases (hence the coarse grained Bayesian posterior, potentially also learning trajectories). Singularities are points, but they nonetheless have "subatomic" structure, which can be seen in various equivalent ways:

- components of the exceptional divisor of a resolution of singularities
- matrix factorisations
- representations of vertex algebras (i.e. of CFTs)

The relation among these three classes of objects is not bijective, and is mathematically complex (far from worked out, subject to various conjectures etc). But we understand enough to have a pretty good operational understanding of how trajectories governed by noise probe the jet scheme, how the geometry of the jet scheme relates to CFT, and how that relates to representations of the CFT (which in turn dominate the universal / scaling behaviour). Similarities to solid state physics suggest that the things we can measure are sufficiently closely related to the universal behaviour that experiments and devices might yield measurements that align with the theory (which in turn guides how the devices and experiments are build/designed).

Note: resolution of singularities is too hard to do exactly, but components of jet schemes are more likely to be approximately accessible. Needs checking. The LG/CFT correspondence is doing a lot of work here conceptually, TODO: explain.

Where we step outside known mathematics is in the conjecture that the **concepts gained during training** are synonymous with these "subatomic particles" of the singularities encountered during training. This can be tested by using the spectroscope to determine signatures of the former, and matching the structure of phases and phase transitions for probes along various subdistributions for the overall model (i.e. probe for understanding of modular arithmetic on "the outside" while watching the spectroscope probing the "inside").

Remark: A microscope probing a singularity, or a distribution of trajectories near that point in weight space, do not interact directly with the singularity but rather with a kind of "cloud" of nearby functions in function space. This means that the precise divergence of the DOS that we observe can be thought of as being determined by "subatomic particles" inside the singularity. These are the irreducible components of the exceptional divisor of the resolution of the singularity, or matrix factorisations (or representations of the associated CFT, conjecturally).

We refer to the history of phases and phase transitions encountered during training as the *phase structure* of the final parameter.

Note that CFT theory / LG tells us that phase transitions between CFTs are themselves often modelled by representations of CFTs / defects.

**Work to be done:**

- Clarify the theoretical role of components of exceptional divisor in Bayesian statistics
- Refine spectroscope to detect structure of components in small models
- Test for alignment between spectroscope results and external probes of actual "concept acquisition"

## Programs as Constructions

Under the Curry-Howard correspondence we learn how to think about programs as *constructions*, or to put it differently, as build up from deduction rules in logic. If we have the spectroscope, and we can use it to probe the phase structure of the final parameter, and if that matches up with the formation of concepts by external probes, then we can think of the final parameter as being *assembled* from the "subatomic pieces" / representations encountered during each phase transition.

**Work to be done:**

- We can use the existing (provisional) correspondence between programs and singularities (see [here](http://therisingsea.org/notes/MSc-Waring.pdf)) as a guide: we can see precisely how the existing notion of programs as constructions maps to the structure phase transitions and use that to bootstrap understanding in neural networks.
- Track concept evolution "on the outside" and "on the inside" and relate the dynamics of concepts (refinement, decomposition, structural formation) to DOS features as detected by spectroscope.
- Survey use of DOS in chemistry to detect formation of certain kinds of bonds
- How are these programs actually executed? 

## Renormalisation Group

A key technique for relating the spectroscope measurements, theoretical physics and mathematical theory will be RG methods (we can borrow from solid state physics for ideas).

https://hep.uchicago.edu/seminars/semspr2019/zohar_komargodski.pdf

## Questions

TODO: more on how AI itself can help with the above components

* Do mesa-optimisers have a universality class? https://astralcodexten.substack.com/p/deceptively-aligned-mesa-optimizers?s=r 
* Localisation [paper](https://arxiv.org/abs/2302.06600)
* Evidence for/against universality [paper](https://arxiv.org/abs/2302.03025)
* Searching for search [paper](https://www.lesswrong.com/posts/FDjTgDcGPc7B98AES/searching-for-search-4)

> Our ability to make lots of useful observations depends on measurement tools, or lenses, that make visible things which are invisible, either by overcoming the physical limitations of our sense organs or our cognitive limitations to interpret raw data. This can be a major bottleneck to scientific progress, a prototypical example being the invention of the microscope, which was a turning point for our ability to study the natural world. The lenses that currently exist for interpretability are still quite crude, and expanding the current suite of tools, as well as building places to explore and visualize neural networks using those tools, seems critical for making lots of high bit observations.
