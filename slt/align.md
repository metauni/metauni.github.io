---
title:
    metauni Alignment Plan
description:
    Lightning unenlightened
---

This document contains a research plan leading to applications of Singular Learning Theory (SLT) to AI alignment. There is an [FAQ](/align-faq). 

# Interpretability via Universality

We describe an approach to scalable interpretability of neural networks based on SLT and the

* **Universality hypothesis**: many of the representations and algorithms encoded by neural networks are approximately universal.

This hypothesis has been articulated for example [here](https://distill.pub/2020/circuits/zoom-in/#claim-3). If (a) this hypothesis holds for a sufficiently broad class of the computations carried out by a network (b) we have tools that allow us to discover approximations to those representations and algorithms, and (c) those tools can be run at industrial scale, then interpretability could contribute to aligning advanced AI systems.

We do not expect that our approach will work unless the problem can be effectively subdivided. Thus we further assume the

* **Locality hypothesis**: in order to understand the final trained parameter, it (a) suffices to understand the set of phases and phase transitions encountered during training and (b) the set of relevant degrees of freedom for each phase transition is "small enough".

Typically the overall training loss does not undergo phase transitions for large models, so this hypothesis has to be understood quite carefully: see the section on the Locality Hypothesis below.

Under these hypotheses, the plan has three parts:

- **Spectroscopy of Singularities:** Construct devices for probing the *density of states* of neural networks, modelled on the role of scanning tunneling microscopes in [solid state physics](https://youtu.be/xnMEfgbSKNs). These devices reveal information about divergences of the density of states caused by singularities in level sets of the loss function in large scale systems, comparable in complexity to large neural networks.

- **Substructure and Semantics:** Use the spectroscopic probe to get substructural information about the singularities dominating phases encountered during training, and use information from those probes to measure how that substructure changes during phase transitions. Match the signatures of these changes to concepts learned during training ("semantics") as tracked by other probes.

- **Programs as Constructions:** Making use of the alignment between substructural changes in the singularities and semantics across training, and the structure of the network, obtain an understanding of the final trained network.

These ideas are grounded in **Singular Learning Theory (SLT)**, a theory of universal behaviour of learning machines based on algebraic geometry and statistics, and **Conformal Field Theory (CFT)**, a theory of universality classes of physical systems, their "representations" and the RG flows between them. Both fields have a deep relation to singularity theory, in SLT because singularities in the KL divergence cause divergences in the density of states, which determine key quantities in Bayesian learning, and in CFT due to the classification of universality classes (this is the subject of the [LG/CFT correspondence](http://therisingsea.org/notes/talk-lgcft.pdf)).

The plan is scoped on the order of ~10 years and presumes:

- Modest progress on pure mathematical foundations in Singular Learning Theory (SLT) and related fields
- Significant progress in a layer of "theoretical physics" between the pure theory of SLT and experiments (more on this below)
- Large scale investment in experiments and ecosystems of devices and interpretability stacks

For an outline of how mechanistic interpretability impacts alignment, see [here](https://www.lesswrong.com/posts/Jgs7LQwmvErxR9BCC/current-themes-in-mechanistic-interpretability-research). From "[Searching for search](https://www.lesswrong.com/posts/FDjTgDcGPc7B98AES/searching-for-search-4)":

> Our ability to make lots of useful observations depends on measurement tools, or lenses, that make visible things which are invisible, either by overcoming the physical limitations of our sense organs or our cognitive limitations to interpret raw data. This can be a major bottleneck to scientific progress, a prototypical example being the invention of the microscope, which was a turning point for our ability to study the natural world. The lenses that currently exist for interpretability are still quite crude, and expanding the current suite of tools, as well as building places to explore and visualize neural networks using those tools, seems critical for making lots of high bit observations.

Jargon

* SLT - Singular Learning Theory
* CFT - Conformal Field Theory
* LG - Landau-Ginzburg
* SSP - Solid State Physics
* DOS - density of states

## Spectroscopy of Singularities

Divergences in the density of states are responsible for many electrical properties of materials, and detecting these divergences by indirect probes (which look for example at differential conductance) is a key experimental technique in solid state physics. There is no principled reason why analogous devices cannot be constructed for large-scale learning machines and there are clear paths to building them. Let us call them **spectroscopic probes**.

We assume that the true loss `L` is a sum of **sublosses** `L_i`, which we may view as arising from subdistributions of the true distribution (instances of addition within GPT's larger training/test set, for example). During training `w_0, w_1, ... ` we track the performance of the network on each of these sublosses, and sample checkpoints `w_{c0}, w_{c1}, ... ` at points of interest which include phase transitions in the sublosses. These checkpoints are passed to a separate analytics system which uses the spectroscopic probe to analyse the neighbourhood of each checkpoint.

**Work to be done:**

- Find candidate targets (analogues of differential conductance) and experiment with measurements in toy models
- Survey applications of deep learning to microscopy, simulating materials and obtaining accurate estimates of DOS
- Relation of phase transition in sublosses to overall Bayesian posterior

**References:**

- C. Kittel "Solid state physics" 8th edition ([link](http://metal.elte.hu/~groma/Anyagtudomany/kittel.pdf)).
- Talk on solid state physics and SLT ([video](https://youtu.be/xnMEfgbSKNs)).

## Substructure and Semantics

The spectroscopic analysis of these checkpoints is correlated with **semantic development** in the network, as measured by an independent set of probes of performance on tests separate from the primary training objective (or sublosses). We conjecture that there is a relationship between the structure of the semantic development (e.g. logical structure) and the substructure of the singularities, as reflected in the spectroscopic analysis.

This substructure is well-understood mathematically, and already plays some role in solid state physics (although is perhaps not fully developed even there). While singularities are points, they nonetheless have "internal" structure (one might say "subatomic" structure) which can be seen in various equivalent ways:

- (essential) components of the exceptional divisor of a resolution of singularities
- matrix factorisations
- representations of vertex algebras (i.e. of CFTs) associated to jet schemes

The relation among these three classes of objects is complex, and a full understanding is not critical to designing substructural spectroscopic probes. However, the theory does suggest that stochastic processes near a singularity are probing the jet scheme, and therefore that quantities involved in scaling (i.e. "universal" quantities) should be sensitive to this substructure.

**Work to be done:**

- Clarify the theoretical role of components of exceptional divisor in Bayesian statistics
- Refine spectroscope to detect structure of components in small models
- Work with solid state physicists to find analogues of substructural probes in that domain
- Test for alignment between spectroscope results and external probes of actual "concept acquisition"

**Notes:**

- A microscope probing a singularity, or a distribution of trajectories near that point in weight space, do not interact directly with the singularity but rather with a kind of "cloud" of nearby functions in function space. This means that the precise divergence of the DOS that we observe can be thought of as being determined by "subatomic structure".
- Resolution of singularities is too hard to do exactly, but components of jet schemes are more likely to be approximately accessible.

## Programs as Constructions

Under the Curry-Howard correspondence we learn how to think about programs as *constructions*, or to put it differently, as build up from deduction rules in logic. If we have the spectroscope, and we can use it to probe the phase structure of the final parameter, and if that matches up with the formation of concepts by external probes, then we can think of the final parameter as being *assembled* from the "subatomic pieces" / representations encountered during each phase transition.

**Work to be done:**

- We can use the existing (provisional) correspondence between programs and singularities (see [here](http://therisingsea.org/notes/MSc-Waring.pdf)) as a guide: we can see precisely how the existing notion of programs as constructions maps to the structure phase transitions and use that to bootstrap understanding in neural networks.
- Track concept evolution "on the outside" and "on the inside" and relate the dynamics of concepts (refinement, decomposition, structural formation) to DOS features as detected by spectroscope.
- Survey use of DOS in chemistry to detect formation of certain kinds of bonds
- How are these programs actually executed? 

## Notes

### The Locality Hypothesis

A Scanning Tunnelling Microscope (STM) is sensitive to divergences in the density of states *scaled by the wavefunction at a position in space*. This localisation in space plays a key role in how the tool is used to interpret the behaviour of systems in solid state physics, because it exponentially reduces the number of degrees of freedom to which the probe is sensitive (some would say that's more or less what space *is*). 

The most serious obstacle to building spectroscopic probes of singularities in large neural networks is that it is prohibitively difficult to estimate the Bayesian posterior near a singular point in a large-dimensional model. We need *localisation procedures* for reducing the number of degrees of freedom we need to care about (e.g. by freezing all but a small number of directions and doing MCMC or variational inference in the others). 

There are two keys sources of localisation:

* **Network architecture:** e.g. layers, or in Transformers, heads.
* **Phase structure:** if the transition `P1 -> P2` between phases involves significant changes in only a small fraction of the weights, then we can localise the spectroscopic probe in these directions.

The latter is inspired by viewing the set of phases encountered during training as a kind of emergent spatial direction. The need to leverage the second kind of localisation is the key reason why we do **not** propose to directly study the final weights / singularity of a trained large neural network.

**References**:

* [paper](https://arxiv.org/abs/2302.06600)

## Where is the mechanism?

The substructural information, tracked across phases during training, by itself does not consistute a *mechanistic* understanding of the neural network, since it doesn't for example necessarily say anything about how information is passed from entity to entity between layers in a Transformer. It is supposed that, however, the information provided by the spectroscope is a foundation for that kind of higher-level reasoning.

### Renormalisation Group

A key technique for relating the spectroscope measurements, theoretical physics and mathematical theory will be RG methods (we can borrow from solid state physics for ideas).

https://hep.uchicago.edu/seminars/semspr2019/zohar_komargodski.pdf

## Questions

* Do mesa-optimisers have a universality class? https://astralcodexten.substack.com/p/deceptively-aligned-mesa-optimizers?s=r 
* Evidence for/against universality [paper](https://arxiv.org/abs/2302.03025)
