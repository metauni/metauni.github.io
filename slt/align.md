---
title:
    metauni Alignment Plan
description:
    There are no algebraists in foxholes
---

We sketch an approach to scalable mechanistic interpretability of neural networks based on the following hypothesis:

* **Universality hypothesis**: some of the representations and algorithms encoded by neural networks are approximately universal.

If this hypothesis holds for a sufficiently broad class of the computations carried out by a network, and we have tools that allow us to discover approximations to those representations and algorithms, then interpretability could be an effective foundation for aligning AI systems.

We begin with a high level sketch of the plan. This presumes familiarity with various concepts from statistical learning theory, physics, etc., see the Background section eblow. The ingredients:

* **Devices:** we assume that it is possible to build probes that are sensitive to the density of states in parts of the parameter space encountered by the neural network during training, and that these probes ("microscopes") . Using these devices we test the relation between theoretical predictions about DOS in toy models.

* **Concepts as components**: Essential components of the arc scheme loosely correspond to irreducible components of the exceptional divisor of the resolution of singularities, which are roughly speaking .

* **Semantics:** Connections between microscope measurements and grounded concepts we care about, for example by tracking performance on a battery of probes and tests on sub-distributions.

* **Dynamics**: Track how concepts form and combine, the computational process itself

## Background

In physics, critical points refer to the specific conditions at which a system undergoes a phase transition. Many systems near a critical point exhibit a property called scale invariance, and their mathematical description falls into specific categories known as universality classes which group together systems that display similar characteristics. Here 

- The relation between learning behaviour and jet schemes,
- Renormalisation Group methods (following SSP) and the LG/CFT correspondence.

Conformal field theory (CFT) plays a crucial role in understanding and describing the behavior of systems near critical points. CFT is a powerful mathematical framework that provides a way to understand the behavior of quantum field theories in two dimensions. By characterizing the critical behavior of a system within a specific universality class using CFT, physicists can make predictions about the system's behavior at critical points and beyond. This has significant implications for a wide range of fields, including condensed matter physics, statistical mechanics, and high-energy physics.

## Jargon

SLT - Singular Learning Theory
CFT - Conformal Field Theory
LG - Landau-Ginzburg
SSP - Solid State Physics
DOS - density of states

## Devices

By analogy with scanning tunneling microscopes in solid state physics (ref, ref), we assume that it is possible to construct "devices" (software) which 

Suppose we have a spectroscope. Then we can look at degenercies in the DOS for the network, or for parts of weight space encountered by training. This gives us some idea of the nature of the singularities encountered and the universality class. We match this against empirically observed behaviour (e.g. performance on a battery of tests) to infer what kind of progress was made in each phase transition. We develop a kind of spectroscope that can detect components of the resolution of singularities / via jet scheme ideas.

## Concepts as components

A microscope probing a singularity, or a distribution of trajectories near that point in weight space, do not interact directly with the singularity but rather with a kind of "cloud" of nearby functions in function space. This means that the precise divergence of the DOS that we observe can be thought of as being determined by "subatomic particles" inside the singularity. These are the irreducible components of the exceptional divisor of the resolution of the singularity, or matrix factorisations (or representations of the associated CFT, conjecturally).

Components are like the spectrum, if the phase transitions are gradual enough most of them won't change, and we can track the changes to particular components and match that up with the conceptual changes. This gives us a picture, over training, of the programs that are being formed.

## Semantics

Programs as singularities, we can test out these ideas on models of computation that we understand and build up a dictionary.

The theory in the background is via LG/CFT components of jet schemes = representations of vertex algebras, we know how that fits into universality, RG flows.

How are these programs actually executed? 

Second-order phase transitions are deformations of singularities. We have some understanding of the "symbolic content" of these deformations, from LG/CFT. It can be operationalised to build probes.
