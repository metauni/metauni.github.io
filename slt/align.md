---
title:
    SLT for Alignment
description:
    Lightning unenlightened
---

Leveraging the concepts of singularity theory, this program aims to discover the geometric and logical structures underlying the computations that determine a model's knowledge, allowing for a deeper understanding of the network's behavior and its consequences. By identifying and studying phase transitions encountered during training, which are large-scale changes in structure and symmetry, we hope to uncover the deep structure of knowledge and computations contained within these networks, leading to a new view of the fundamental nature of programs and more effective interpretability tools.

We focus on phase transitions because (a) there is good evidence they are present in the training process of these networks and relate to the concepts represented in the network and (b) the divergences present at a phase transition should imply the existence of easily measured signals reflecting the aforementioned geometric and logical structures, which are otherwise invisible. The problem is to locate these transitions, learn how to probe them, and how to infer from those probes the underlying structures.

# Interpretability via Universality

We describe an approach to scalable interpretability of neural networks based on SLT and the

* **Universality hypothesis**: many of the representations and algorithms encoded by neural networks are approximately universal.

This hypothesis has been articulated for example [here](https://distill.pub/2020/circuits/zoom-in/#claim-3). If (a) this hypothesis holds for a sufficiently broad class of the computations carried out by a network (b) we have tools that allow us to discover approximations to those representations and algorithms, and (c) those tools can be run at industrial scale, then interpretability could contribute to aligning advanced AI systems.

We do not expect that our approach will work unless the problem can be effectively subdivided. Thus we further assume the

* **Locality hypothesis**: in order to understand the final trained parameter, it (a) suffices to understand the set of phases and phase transitions encountered during training and (b) the set of relevant degrees of freedom for each phase transition is "small enough".

Typically the overall training loss does not undergo phase transitions for large models, so this hypothesis has to be understood quite carefully: see the section on the Locality Hypothesis below.

Under these hypotheses, the plan has two parts:

- **Spectroscopy of Singularities:** Construct devices for probing the *density of states* of neural networks, modelled on the role of scanning tunneling microscopes in [solid state physics](https://youtu.be/xnMEfgbSKNs). These devices reveal information about divergences of the density of states caused by singularities in level sets of the loss function in large scale systems, comparable in complexity to large neural networks.

- **Substructure and Semantics:** Use the spectroscopic probe to get substructural information about the singularities dominating phases encountered during training, and use information from those probes to measure how that substructure changes during phase transitions. Match the signatures of these changes to concepts learned during training, capabilities detected, and other evaluations.

These ideas are grounded in **Singular Learning Theory (SLT)**, a theory of universal behaviour of learning machines based on algebraic geometry and statistics, and **Conformal Field Theory (CFT)**, a theory of universality classes of physical systems, their "representations" and the RG flows between them. Both fields have a deep relation to singularity theory, in SLT because singularities in the KL divergence cause divergences in the density of states, which determine key quantities in Bayesian learning, and in CFT due to the classification of universality classes (this is the subject of the [LG/CFT correspondence](http://therisingsea.org/notes/talk-lgcft.pdf)).

The plan is scoped on the order of ~10 years and presumes:

- Modest progress on pure mathematical foundations in Singular Learning Theory (SLT) and related fields
- Significant progress in a layer of "theoretical physics" between the pure theory of SLT and experiments (more on this below)
- Large scale investment in experiments and ecosystems of devices and interpretability stacks

For an outline of how mechanistic interpretability impacts alignment, see [here](https://www.lesswrong.com/posts/Jgs7LQwmvErxR9BCC/current-themes-in-mechanistic-interpretability-research). 

Jargon

* SLT - Singular Learning Theory
* CFT - Conformal Field Theory
* LG - Landau-Ginzburg
* SSP - Solid State Physics
* DOS - density of states

## Spectroscopy of Singularities

> In such models, knowledge to be discovered from examples corresponds to a singularity -- S. Watanabe

The learning behaviour of singular models is dominated by the geometry of singularities. Moreover, the structure of phases and phase transitions encountered during training are dominated by singularities of level sets of the loss function. We can build scalable devices that provide useful signatures of these singularities, and thus of the "knowledge" they contain.

The motivating example of this working in practice is solid state physics. Divergences in the density of states are responsible for many electrical properties of materials, and detecting these divergences by indirect probes (which look for example at differential conductance) is a key experimental technique. There is no principled reason why analogous devices cannot be constructed for large-scale learning machines. Let us call them **spectroscopic probes**.

We assume that during training a series of points of interest are identified `w_0, w_1, ... ` and that these checkpoints are passed to a separate analytics system which uses the spectroscopic probe to analyse the neighbourhood of each checkpoint. How are these checkpoints selected? The general idea is to track a wide range of metrics across training, and watch them for phase transitions. These transitions contribute checkpoints.

* **Sublosses:** The true loss `L` could be a sum of **sublosses** `L_i`, which we may view as arising from subdistributions of the true distribution (instances of addition within GPT's larger training/test set, for example).

* **Evaluations:** There is likely to be a growing library of open source evaluations of LLM performance (see OpenAI's [Eval]s(https://github.com/openai/evals)).

* **Latent knowledge:** it is possible to extract from middle layers representations that are indicate an [understanding of logical structure](https://www.lesswrong.com/posts/L4anhrxjv8j2yRKKp/how-discovering-latent-knowledge-in-language-models-without) in text.

**Work to be done:**

- Find candidate targets (analogues of differential conductance) and experiment with measurements in toy models
- Survey applications of deep learning to microscopy, simulating materials and obtaining accurate estimates of DOS
- Relation of phase transition in sublosses to overall Bayesian posterior

**References:**

- C. Kittel "Solid state physics" 8th edition ([link](http://metal.elte.hu/~groma/Anyagtudomany/kittel.pdf)).
- Talk on solid state physics and SLT ([video](https://youtu.be/xnMEfgbSKNs)).

## Substructure and Semantics

Interpretability is about the relationship between *knowledge in singularities* and *knowledge humans have of the world*. To produce a Rosetta stone which allows us to translate between these two languages, the spectroscopic analysis of the checkpoints is compared with **semantic development** in the network, as measured by an independent set of probes of performance on tests separate from the primary training objective (or sublosses). We conjecture that there is a close relationship between the structure of the semantic development (e.g. logical structure) and the substructure of the singularities, as reflected in the spectroscopic analysis. Tracking this relationship in detail across all checkpoints is the "Rosetta stone". 

This substructure is well-understood mathematically, and already plays some role in solid state physics (although is perhaps not fully developed even there). While singularities are points, they nonetheless have "internal" structure (one might say "subatomic" structure) which can be seen in various equivalent ways:

- (essential) components of the exceptional divisor of a resolution of singularities
- matrix factorisations
- representations of vertex algebras (i.e. of CFTs) associated to jet schemes

The relation among these three classes of objects is complex, and a full understanding is not critical to designing substructural spectroscopic probes. However, the theory does suggest that stochastic processes near a singularity are probing the jet scheme, and therefore that quantities involved in scaling (i.e. "universal" quantities) should be sensitive to this substructure.

**Remark:** While it is a fact that knowledge to be discovered from data corresponds to a singularity of the KL divergence, or loss function, and the geometry of that singularity governs the learning process, it is *not* yet clear mathematically that substructure of the singularity corresponds to structure of that knowledge in any human-interpretable way. This is an open research problem.

**Work to be done:**

- Clarify the theoretical role of components of exceptional divisor in Bayesian statistics
- Refine spectroscope to detect structure of components in small models
- Work with solid state physicists to find analogues of substructural probes in that domain
- Test for alignment between spectroscope results and external probes of actual "concept acquisition"

**Notes:**

- A microscope probing a singularity, or a distribution of trajectories near that point in weight space, do not interact directly with the singularity but rather with a kind of "cloud" of nearby functions in function space. This means that the precise divergence of the DOS that we observe can be thought of as being determined by "subatomic structure".
- Resolution of singularities is too hard to do exactly, but components of jet schemes are more likely to be approximately accessible (see the jet scheme lectures [here](https://metauni.org/slt/)).
- See [emergent capabilities](https://openreview.net/forum?id=yzkSU5zdwD).

### Programs as Singularities

For interpretability to succeed you need the right model for the computations within a network. Circuits or TMs or lambda terms are the wrong model; a new view of programs may be required. We understand how to represent traditional programs (e.g. Turing machines) as singularities in learning machines (see [here](http://therisingsea.org/notes/MSc-Waring.pdf)). That means that we can test the above ideas in a situation where we have the ground truth, by attempting to reverse-engineer structure of programs from structure of their singularities.

### The Locality Hypothesis

A Scanning Tunnelling Microscope (STM) is sensitive to divergences in the density of states *scaled by the wavefunction at a position in space*. This localisation in space plays a key role in how the tool is used to interpret the behaviour of systems in solid state physics, because it exponentially reduces the number of degrees of freedom to which the probe is sensitive (some would say that's more or less what space *is*). 

The most serious obstacle to building spectroscopic probes of singularities in large neural networks is that it is prohibitively difficult to estimate the Bayesian posterior near a singular point in a large-dimensional model. We need *localisation procedures* for reducing the number of degrees of freedom we need to care about (e.g. by freezing all but a small number of directions and doing MCMC or variational inference in the others). There are three keys sources of localisation:

* **Network architecture:** e.g. layers, or in Transformers, heads.
* **Phase structure:** if the transition `P1 -> P2` between phases involves significant changes in only a small fraction of the weights, then we can localise the spectroscopic probe in these directions.

Note that when we speak of phases, we mean with respect to the sublosses discussed above. Firstly, because the overall loss does not undergo (discrete) phase transitions in large neural network training, and secondly because we only expect strong localisation for phase transitions in the sublosses.

# Why should mathematicians work on Alignment?

Take it from Demis Hassabis, [CEO of DeepMind](https://www.lesswrong.com/posts/SbAgRYo8tkHwhd9Qx/deepmind-the-podcast-excerpts-on-agi#_Avengers_assembled__for_AI_Safety__Pause_AI_development_to_prove_things_mathematically):

> I always imagine that as we got closer to the sort of gray zone that you were talking about earlier, the best thing to do might be to pause the pushing of the performance of these systems so that you can analyze down to minute detail exactly and maybe even prove things mathematically about the system so that you know the limits and otherwise of the systems that you're building. At that point I think all the world's greatest minds should probably be thinking about this problem. So that was what I would be advocating to you know the Terence Tao’s of this world, the best mathematicians. Actually I've even talked to him about this—I know you're working on the Riemann hypothesis or something which is the best thing in mathematics but actually this is more pressing.

> Our ability to make lots of useful observations depends on measurement tools, or lenses, that make visible things which are invisible, either by overcoming the physical limitations of our sense organs or our cognitive limitations to interpret raw data. This can be a major bottleneck to scientific progress, a prototypical example being the invention of the microscope, which was a turning point for our ability to study the natural world. The lenses that currently exist for interpretability are still quite crude, and expanding the current suite of tools, as well as building places to explore and visualize neural networks using those tools, seems critical for making lots of high bit observations -- From "[Searching for search](https://www.lesswrong.com/posts/FDjTgDcGPc7B98AES/searching-for-search-4)"
