---
title:
    metauni Alignment FAQ
---

## FAQ

**Question:** Is SLT relevant to AI alignment?

**Answer:** *tldr* Yes, but also relevant to capabilities. *Caveat emptor*.

(*Dan Murfet*'s personal views here) First some caveats: although we are optimistic SLT can be developed into theory of deep learning, it is not currently such a theory and it remains possible that there are fundamental obstacles. Putting those aside for a moment, it is plausible that phenomena like scaling laws and the related emergence of capabilities like in-context learning can be understood from first principles within a framework like SLT. This could contribute both to capabilities research and safety research.

*Contribution to capabilities.* Right now it is not understood why Transformers obey scaling laws, and how capabilities like in-context learning relate to scaling in the loss; improved theoretical understanding could increase scaling exponents or allow them to be engineered in smaller systems. For example, some empirical work already suggests that certain data distributions lead to in-context learning. It is possible that theoretical work could inspire new ideas. Thermodynamics wasn't necessary to build steam engines, but it *helped to push the technology to new levels of capability* once the systems became too big and complex for tinkering.

*Contribution to alignment.* Broadly speaking it is hard to align what you do not understand. Either the aspects of intelligence relevant for alignment are universal, or they are not. If they are not, we have to get lucky (and stay lucky as the systems scale). If the relevant aspects are universal (in the sense that they arise for fundamental reasons in sufficiently intelligent systems across multiple different substrates) we can try to understand them and use them to control/align advanced systems (or at least be forewarned about their dangers) and be reasonably certain that the phenomena continue to behave as predicted across scales. This is one motivation behind the work on properties of optimal agents, such as Logical Inductors. SLT is a theory of universal aspects of learning machines, it could perhaps be developed in similar directions.

*Does understanding scaling laws contribute to safety?*. It depends on what is causing scaling laws. If, as we suspect, it is about phases and phase transitions then it is related to the nature of the structures that emerge during training which are responsible for these phase transitions (e.g. concepts). A theory of interpretability scalable enough to align advanced systems may need to develop a fundamental theory of abstractions, especially if these are related to the phenomena around scaling laws and emergent capabilities.

Our take on this has been partly spelled out in the [Abstraction seminar](https://metauni.org/abstraction/). We're trying to develop existing links in mathematical physics between renormalisation group flow and resolution of singularities, which applied in the context of SLT might give a fundamental understanding of how abstractions emerge in learning machines. One best case scenario of the application of SLT to alignment is that this line of research gives a theoretical framework in which to understand more empirical interpretability work.

The utility of theory in general and SLT in particular depends on your mental model of the problem landscape between here and AGI. To return to the thermodynamics analogy: a working theory of thermodynamics isn't necessary to build train engines, but it's probably necessary to build rockets. If you think the engineering-driven approach that has driven deep learning so far will plateau before AGI, probably theory research is bad in expected value. If you think theory isn't necessary to get to AGI, then it may be a risk that we have to take.

Summary: In my view we seem to know enough to get to AGI. We do not know enough to get to alignment. Ergo we have to take some risks.
