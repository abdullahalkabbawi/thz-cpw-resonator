# Literature Notes: Reducing intrinsic loss by surface treatment and deep etching

**Paper Title:** Reducing intrinsic loss in superconducting resonators by surface treatment and deep etching of silicon substrates
**Authors:** A. Bruno, G. de Lange, S. Asaad, K. L. van der Enden, N. K. Langford, L. DiCarlo (Delft University of Technology)
**Published:** February 2015 (arXiv preprint / Applied Physics Letters)
**Relevance to MSc Project:** High. This is a foundational experimental demonstration of using deep reactive-ion etching (DRIE) to create the exact trench geometries we are simulating. It provides physical context for how these structures are actually fabricated and proves that trenches push quality factors above 1 Million.

---

## 1. Experimental Achievement
*   **Material:** Niobium Titanium Nitride (NbTiN) CPW resonators on Silicon substrates.
*   **Goal:** Achieve internal quality factors ($Q_i$) greater than 1 Million in the *quantum regime* (millikelvin temperatures and single-photon excitation energies).
*   **Performance:** Achieved $Q_i > 1\text{ M}$ routinely, and up to **2 Million** by combining deep etching with chemical surface treatments.

---

## 2. The Two-Pronged Mitigation Strategy
The authors recognized that Two-Level System (TLS) defects reside at the interfaces. They attacked the two most lossy interfaces using two different techniques:

### A. The Metal-Substrate (MS) Interface: Chemical Treatment
*   **Problem:** Native silicon oxides (Si-O bonds) and silanol groups (Si-OH) under the metal host a massive density of TLS defects.
*   **Solution:** Before depositing the superconducting metal, they dipped the silicon in Hydrofluoric acid (HF) to strip the native oxide. Immediately after, they baked the substrate in a **hexamethyldisilazane (HMDS)** atmosphere. 
*   **Result:** HMDS acted as a primer that prevented the silicon from re-oxidizing before the metal was deposited, resulting in a pristine, low-loss metal-substrate boundary.

### B. The Substrate-Air (SA) Interface: Deep Etching (Trenches)
*   **Problem:** The exposed silicon surface in the CPW gaps also grows a native oxide layer that interacts heavily with the electric field.
*   **Solution:** They used **Deep Reactive-Ion Etching (DRIE)** using the Bosch process (alternating SF$_6$ etching and C$_4$F$_8$ passivation) to physically dig trenches into the gaps.
*   **Trench Geometry:** They achieved highly anisotropic trenches up to **80 µm deep**. They noted an under-etch of ~1 µm (the trench cuts slightly underneath the metal) and sidewall scalloping (roughness of ~100 nm) due to the Bosch process.
*   **Result:** Displaced the lossy substrate-vacuum interface far away from the regions of highest electric field intensity, significantly boosting $Q_i$.

---

## 3. Power and Temperature Dependence
The authors confirmed that TLS defects were the dominant loss mechanism by looking at the physical behavior of the resonators:
*   **Power Dependence:** At high powers, the electric field saturates the TLS defects, and $Q_i$ increases. At single-photon powers, TLS defects are unsaturated and absorb energy, lowering $Q_i$.
*   **Temperature Dependence:** As temperature increases from 15 mK to 400 mK, $Q_i$ actually *increases*. This is because thermal energy begins to thermally excite and "depolarize" the TLS defects, preventing them from absorbing microwave photons.

---

## 4. Key Takeaways for Our MSc Project

1.  **Fabrication Reality:** Our Lumerical simulation assumes perfectly vertical, smooth walls. Bruno *et al.* show that real DRIE trenches have **sidewall scalloping** (roughness) and **under-etching** (cutting under the metal). We can mention this in our thesis discussion as a limitation of our idealized Lumerical model and an area for future simulation work.
2.  **Etch Depth Alignment:** Bruno *et al.* physically etched to 80 µm to achieve their results. This sits perfectly alongside Calusine *et al.* ($10g$) and our chosen 50 µm depth, reinforcing that deep trenches on the order of 50-80 µm are the experimental standard.
3.  **MS vs SA Interface Management:** This paper beautifully highlights that you can't just etch trenches to fix everything. Trenches fix the SA interface in the gaps, but you still need chemical treatments (like HMDS) to fix the MS interface under the metal. This dual-approach is an excellent talking point for the conclusion of the thesis.
