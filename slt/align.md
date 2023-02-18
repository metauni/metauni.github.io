---
title:
    metauni Alignment Project
description:
    There are no algebraists in foxholes
---

We describe an approach to scalable mechanistic interpretability of neural networks based on the

* **Universality hypothesis**: many of the representations and algorithms encoded by neural networks are approximately universal.

This hypothesis has been articulated for example [here](https://distill.pub/2020/circuits/zoom-in/#claim-3). If this hypothesis holds for a sufficiently broad class of the computations carried out by a network, we have tools that allow us to discover approximations to those representations and algorithms, and those tools can be run at industrial scale, then interpretability could contribute to aligning advanced AI systems.

In outline, the plan has three parts:

- **Spectroscopy of Singularities:** Co-evolve a set of **devices** in tandem with experiments, for probing the **density of states** of neural networks, modelled on the role of scanning tunneling microscopies in solid state physics (talk ref). These devices are presumed to reveal information about divergences of the density of states and the singularities in level sets of the loss function that generate them.

- **Components as Concepts:** Use the spectroscopy to get information about the essential components of the exceptional divisor of the resolution of the singularities dominating phases encountered during training, and match the phase transition structure to concepts learned during training, as tracked by other probes.

- **Programs as Constructions:** By tracking the phase transitions in the network, obtain an understanding of (parts of) the final trained parameter as a function of the history of the formation and deformation of concepts encountered during training.

These ideas are grounded in **Singular Learning Theory (SLT)**, a theory of universal behaviour of learning machines based on algebraic geometry and statistics, and **Conformal Field Theory (CFT)**, a theory of universality classes of physical systems, their "representations" and the RG flows between them. Both fields have a deep relation to singularity theory, in SLT because singularities in the KL divergence cause divergences in the density of states, which determine key quantities in Bayesian learning, and in CFT due to the classification of universality classes (this is the subject of the LG/CFT correspondence). 

The plan is scoped on the order of ~10 years and presumes:

- Modest progress on pure mathematical foundations in Singular Learning Theory (SLT) and related fields
- Significant progress in a layer of "theoretical physics" between the pure theory of SLT and experiments (more on this below)
- Large scale investment in experiments and ecosystems of devices and interpretability stacks

*Authors:* Dan Murfet, you?
*Last update:* 18/2/2023

## Jargon

SLT - Singular Learning Theory
CFT - Conformal Field Theory
LG - Landau-Ginzburg
SSP - Solid State Physics
DOS - density of states

## Spectroscopy of Singularities

Divergences in the density of states are responsible for many electrical properties of materials, and detecting these divergences by indirect probes (which look for example at differential conductance) is a key experimental technique in solid state physics. There is no principled reason analogous devices cannot be constructed for learning machines. The plan depends on finding scalable devices of this kind.

Suppose we have a spectroscope. Then we can look at degenercies in the DOS for the network, or for parts of weight space encountered by training. This gives us some idea of the nature of the singularities encountered and the universality class. We match this against empirically observed behaviour (e.g. performance on a battery of tests) to infer what kind of progress was made in each phase transition. We develop a kind of spectroscope that can detect components of the resolution of singularities / via jet scheme ideas.

**Work to be done:**

- Find candidate targets (analogues of differential conductance) and experiment with measurements in toy models
- Survey applications of deep learning to microscopy, simulating materials and obtaining accurate estimates of DOS

## Concepts as Components

* **Components**: essential components of the arc scheme loosely correspond to irreducible components of the exceptional divisor of the resolution of singularities. We assume that these components can be distinguished in some form by spectroscopy, and that the components correlate with "concepts" in the following sense:
* 
* **Concepts:** we run many experiments and track simultaneously the spectroscopy and performance of the network on many probes that test specific competencies from the training distribution, designed to test the presence of "concepts". We assume that there will be some correspondence between DOS divergences and the phase transitions in training. 

A microscope probing a singularity, or a distribution of trajectories near that point in weight space, do not interact directly with the singularity but rather with a kind of "cloud" of nearby functions in function space. This means that the precise divergence of the DOS that we observe can be thought of as being determined by "subatomic particles" inside the singularity. These are the irreducible components of the exceptional divisor of the resolution of the singularity, or matrix factorisations (or representations of the associated CFT, conjecturally).

Components are like the spectrum, if the phase transitions are gradual enough most of them won't change, and we can track the changes to particular components and match that up with the conceptual changes. This gives us a picture, over training, of the programs that are being formed.

Resolution of singularities is impossible at scale, but probing the structure of the jet scheme (= low energy parts) should be possible.

## Programs as Constructions

Programs as singularities, we can test out these ideas on models of computation that we understand and build up a dictionary.

The theory in the background is via LG/CFT components of jet schemes = representations of vertex algebras, we know how that fits into universality, RG flows.

How are these programs actually executed? 

Second-order phase transitions are deformations of singularities. We have some understanding of the "symbolic content" of these deformations, from LG/CFT. It can be operationalised to build probes.

https://hep.uchicago.edu/seminars/semspr2019/zohar_komargodski.pdf
