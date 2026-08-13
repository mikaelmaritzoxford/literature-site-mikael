# Multilayer optical calculations

##### Steven J. Byrnes

Current affiliation: Charles Stark Draper Laboratory, Cambridge, Massachusetts, USA

Contact: steven.byrnes@gmail.com

January 1, 2021

Abstract

When light hits a multilayer planar stack, it is reflected, refracted, and absorbed in a way that can be derived from the Fresnel equations. The analysis is treated in many textbooks, and implemented in many software programs, but certain aspects of it are difficult to find explicitly and consistently worked out in the literature. Here, we derive the formulas underlying the transfer-matrix method of calculating the optical proper- ties of these stacks, including oblique-angle incidence, absorption-vs-position profiles, and ellipsometry parameters. We discuss and explain some strange consequences of the formulas in the situation where the incident and/or final (semi-infinite) medium are absorptive, such as calculating T > 1 in the absence of gain. We also discuss some implementation details like complex-plane branch cuts. Finally, we derive modified formulas for including one or more “incoherent” layers, i.e. very thick layers in which interference can be neglected. This document was written in conjunction with the “tmm” Python software package, which implements these calculations.

## arXiv:1603.02720v5 [physics.comp-ph] 30 Dec 2020

### Contents

1 Introduction 3

2 Wave propagation 3

2.1 What is complex refractive index?..................... 4
2.2 Explicit E, H, and k for s-polarization and p-polarization........ 4
3 Single-interface reflection and transmission amplitudes 5

3.1 Waves coming from both sides....................... 5
4 Multilayer thin films 6

4.1 Complex amplitudes for reflection and transmission. ........... 6
4.2 Ellipsometric parameters ........................... 7
4.3 Calculating Poynting vector......................... 7
4.4 T (transmitted power) and R (reflected power).............. 8
4.4.1 Counter-intuitive results when the initial medium is absorptive. 9
4.5 Absorbed energy density ........................... 9
5 Branch cuts 10

6 Thick “incoherent” films 11

6.1 Introduction .................................. 11
6.2 Calculation method .............................. 11
6.3 Absorption profile, Coherence length.................... 12
7 Acknowledgments 13

AAppendix: Sign convention for reflection amplitude 14

BAppendix: R and Twith an absorptive starting medium 15

B.1 Accounting for this effect in the incoherent calculation.......... 17
CAppendix: Stimulated emission 18

DAppendix: Branch cuts 18

D.1Computer implementation.......................... 18
D.2Case that Im n > 0, Re n > 0....................... 19
D.3Case that Im n = 0, Re n > 0....................... 20
D.3.1 Case Im n = 0, Re n > 0, Total internal reflection ........ 20
D.3.2 Case Im n = 0, Re n > 0, Normal refraction........... 20
D.4Case that Im n < 0, Re n < 0....................... 20
D.5Everything else................................ 20

### 1 Introduction

I originally wrote these notes to record and explain the calculations implemented by the “tmm” (short for “transfer matrix method”) Python software package: See [https://pypi.python.org/pypi/tmm](https://pypi.python.org/pypi/tmm). The derivations (at least through Sec. 4) can be found, in whole or part, in quite a few textbooks and references. I found Bo Sernelius’s lecture notes¹ an especially useful starting point. Apart from my tmm program, there are many other programs that calculate some or all of the same formulas. 2 I have done a few consistency checks between my program and others. They tend to agree perfectly except in the tricky (and somewhat unusual) case of calculating reflected power or transmitted power when the semi-infinite incom- ing and/or outgoing medium has a complex index of refraction. I assume non-magnetic (µ = µ₀) and isotropic (as opposed to birefringent) materials throughout the document.

### 2 Wave propagation

We assume our structure is a stack of one or more smooth planar layers, such as a flat piece of glass with an antireflective coating on top. The interfaces between layers are all normal to ˆz, and everything is uniform in the x and y directions. We assume the wavevector of the light is in the x–z plane. (Or just along ˆz if it’s normal-incidence). The “forward” direction (direction that normally-incident incoming light is traveling) is +zˆ. All sinusoidally-oscillating quantities are given as complex numbers; to get the actual value at any particular time, multiply by e −iωt and take the real part. The electric field at any given point is a superposition of the forward-moving and backwards-moving electromagnetic waves:

E(r) = E⁰fe ikf·r + E⁰be ikb·r

(1)
Here, kfand kbare the [angular] wavevectors for forward- and backwards-moving waves; E⁰ f and E⁰ b are some constant vectors; and E(r) is the complex electric field at any given point r within a certain layer. The y-components of the kfand kbare zero because, like I said above, the wavevector is assumed to be in the x–z plane. The x- components of kfand kbare always real, because we are assuming it’s a plane wave, so the light intensity is uniform along the x and y directions. However, the z component might be complex, representing a wave that is attenuating as it travels through the stack, due to absorption. The wavevectors is related to the [complex] index of refraction n by:

2πn 2πn ˆ sin θ) ˆ sin θ) (2)

||k = (zˆ cos θ + x|, k = (−zˆ cos θ + x|
|---|---|---|
|1 2|f vac|b vac|

λ λ

[http://people.ifm.liu.se/boser/elma/–especially](http://people.ifm.liu.se/boser/elma/–especially) lecture 13 I have a list at: [http://sjbyrnes.com/multilayer-film-optics-programs/](http://sjbyrnes.com/multilayer-film-optics-programs/)

where θ is the angle from the normal, and λvacis the vacuum wavelength. That means n sin θ is always a real number, but n cos θ might not be. This is consistent with Snell’s law: nisin θi= njsin θj(3)

i.e., n sin θ should be the same real number in every layer. Snell’s law is the same as saying that the component of k in the x − y plane is the same in each layer.
##### 2.1 What is complex refractive index?

When the refractive index is complex, the imaginary part is sometimes called “extinc- tion coefficient”. The larger it is, the more quickly light gets absorbed as it tries to travel through the material. Negative extinction coefficient corresponds to stimulated emission. Extinction coefficient, like refractive index, is a unitless number. It should NOT be confused with “molar extinction coefficient” or “mass extinction coefficient” in chemistry, which are not unitless. 3 For real-world materials, the extinction coefficient, like the refractive index, is different at different frequencies. Again, with the conventions used here, Im n > 0 means absorption and Im n < 0 means stimulated emission.

2.2 Explicit E, H, and k for s-polarization and p-polarization As usual, s-polarization is where the E-field points in the y-direction, and p-polarization is where the H-field points in the y-direction. There is no difference between s and p-polarization for normal-incident light. However, the way our sign conventions work, the reflection amplitude for a normal-incidence wave is given with the opposite sign depending on whether you call it “s” or “p“! For s-polarization, our sign convention is based on the direction of the E-field—e.g., if two waves have E pointing parallel, then their amplitudes have the same sign. Whereas for p-polarization, our sign convention is based on the direction of the H-field. Half of textbooks use the opposite sign convention for p from this one, so don’t be surprised to see discrepancies between different sources. See Appendix A for further discussion. Maxwell’s equations imply that H =
µ0 1ω k × E for a plane wave. [This works even if k and/or E is a complex vector.] Therefore the explicit E, H, k are:

s-polarization

2πn 2πn ˆ), (− cos θˆz + sin θxˆ)

|k =|(cos θˆz + sin θx|k =|
|---|---|---|
|f|vac|b vac|
|||b b|
|f|f|b b|

λ λ Ef= Efyˆ, E = E yˆ H ∝ nE (− cos θxˆ + sin θˆz), H ∝ nE (cos θxˆ + sin θˆz) (4)

3 However, if you know one you can figure out the other. See [https://en.wikipedia.org/w/index.php?title=Mathematical_descriptions_of_opacity&oldid=695422502](https://en.wikipedia.org/w/index.php?title=Mathematical_descriptions_of_opacity&oldid=695422502).

and

p-polarization

2πn 2πn ˆ) ˆ)

|k =|(cos θˆz + sin θx|, k =|(− cos θˆz + sin θx|
|---|---|---|---|
|f|vac|b|vac|
|f|f|b b|b b|

λ λ E = E (− sin θˆz + cos θxˆ), E = E (− sin θˆz − cos θxˆ) Hf∝ nEfyˆ, H ∝ nE yˆ (5)

### 3 Single-interface reflection and transmission am- plitudes

If you have the interface between two layers 1 and 2, and shine light from 1, then there are three relevant wave amplitudes: The incident amplitude (Efon the layer 1 side), the reflected amplitude (Ebon the layer 1 side), and the transmitted amplitude (Efon the layer 2 side). The reflection coefficient r is the ratio of reflected amplitude to incident amplitude, and the transmission coefficient t is the ratio of transmitted amplitude to incident amplitude. To derive the equations for r and t (“The Fresnel Equations”), we start with Eqs. (4-

5) on both sides of the interface, with Ef= E₀,Eb= rE₀ on the starting side and Ef= tE₀,Eb= 0 on the destination side. Then we plug in the boundary conditions for E and H: Hx y z x y z

|,H|,H ,E|,E, and n²E||are all continuous across the boundary. Two|||
|---|---|---|---|---|---|---|
|x|y z|x y||z|||
|f b||f|b||z z|z z|
 clarifications: (1) These boundary conditions refer to components of the total fields E=E + E and H = H + H; (2) The criterion is actually that B and D are continuous across the boundary, but I just rephrased it in terms of H and E using µ = µ₀,ǫ = n²ǫ₀. Readers may check the algebra themselves, or refer to any optics textbook; traveling from medium 1 into medium 2:
n₁ cos θ₁ − n₂ cos θ₂ n₂ cos θ₁ − n₁ cos θ₂ r s=, rp= n₁ cos θ₁ + n₂ cos θ₂ n₂ cos θ₁ + n₁ cos θ₂ 2n₁ cos θ₁ 2n₁ cos θ₁ t s=, tp= (6) n₁ cos θ₁ + n₂ cos θ₂ n₂ cos θ₁ + n₁ cos θ₂

##### 3.1 Waves coming from both sides

A slight extension is to have waves incoming from both sides of the interface at once. Say they have amplitudes (at the interface) of Ef 1,Eb1,Ef 2,Eb2(forwards in medium 1, backwards in 1, forwards in 2, backwards in 2). These are related by

||E = E r₁₂ + E|E = E t₁₂ + E|
|---|---|---|
|ab ab|b1 f 1|f 2 f 1|

b2t₂₁,b2r₂₁ (7)

where t,r are transmission and reflection going from layer a into b. Intuitively, each of the outgoing waves is a superposition of the reflected amplitude of one of the incoming

waves, plus the transmitted amplitude of the other incoming wave. More formally, we could derive these from scratch using the electromagnetic boundary conditions, but it’s easier to note that we already know two situations that satisfy the boundary conditions: (Ef 1,Eb1,Ef 2,Eb2) = (1,r₁₂,t₁₂, 0) and (0,t₂₁,r₂₁, 1). Both of these satisfy (7), and therefore so does any linear combination / superposition of those two situations—which includes all possible combinations of incoming waves.

### 4 Multilayer thin films

##### 4.1 Complex amplitudes for reflection and transmission

##### Layer 3

##### v =t w =0

3 3

##### Layer 2

v₂ w₂"forwards" "backwards"

##### Layer 1

v₁ w₁

1 r Layer 0 +z direction

Figure 1 – Sample stack with N = 4 (two finite layers between two semi-infinite layers).

The labels next to the small arrows indicate wave amplitudes.

Now we have N materials, numbered 0, 1,...,N − 1, where the first (“0”) and last (“N − 1”) layer are semi-infinite. Light with amplitude 1 is in layer 0, heading towards layer 1 (Fig. 1). At the interface between the (n − 1)st and nth material, let vnbe the amplitude of the wave on the nth side heading forwards (away from the boundary), and let wnbe the amplitude on the nth side heading backwards (towards the boundary). (Fig. 1.) ((v₀,w₀) are undefined, while vN −1= t and wN −1= 0.) We define

δ n≡ (thickness of layer n)(kzfor the forward-traveling wave in layer n) (8)

i.e., δncharacterizes the phase [and when kzis complex, also the absorption] that comes from passing through layer n. Now from Eq. (7) we get:
= n

|v|(v e )t|+ w|r|
|---|---|---|---|
|n+1|n iδ|n,n+1|n+1 n+1,n|
|n −iδ|n+1 n+1,n|n|iδ n,n+1|
|a,b|b,a|a,b b,a|a,b b,a|

w e n = w t + (v e n

)r (9)
where ra,band ta,bare reflection and transmission for light heading from layer a into layer b. Using the identities r = −r and t t − r r = 1 (which follow from Eqs. (6)), we can transform these into: () () vnvn+1 = Mn(10) wnwn+1

for n = 1,...,N − 2, where ( −iδ ) () e n 0 1 rn,n+11 Mn≡iδ n (11) 0 e rn,n+11 tn,n+1

Now we want the matrix relating the waves entering the structure to the waves exiting,

i.e.: ( ) ( )
1 ˜ t = M. (12) r 0

M ˜ is given by: () M ˜ = M₁M₂ · · · M N −2(13) 1 1 r0,1 t 0,1r0,11 Combining these two equations allows r and t to be written in terms of the four entries of the matrix M˜ : ( ) () ( ) 1 M˜00M˜01t = ˜ ˜ (14) r M₁₀ M₁₁ 0

##### t = 1/M˜00, r = M˜10/M˜00(15)

So now we know how to calculate r and t for an arbitrary multi-layer thin film. (And incidentally, it is straightforward from here to also calculate vnand wnfor every n.)

##### 4.2 Ellipsometric parameters

If we know r and r, we can also calculate the two parameters measured in ellipsometry:

|s t|||
|---|---|---|
||−1 p s|p s|

ψ ≡ tan (|r /r |), ∆ ≡ phase(−r /r) (16)

where “phase” means complex phase angle. However, I found that different textbooks have different definitions. So you may need to flip the signs, add or subtract π/2, etc.

##### 4.3 Calculating Poynting vector

The next few sections relate to power flows and power absorption: The goal is to be able to generate graphs like Fig. 2. The relevant equations are somewhat hard to find (without typos) in the literature, but I verified them by various consistency checks, such as continuity across interfaces when appropriate, agreement with R and T in simple cases, etc. I will start by deriving the expression for the normal component of the Poynting vector S, i.e. S · zˆ. This dot-product represents the net power flowing forward through the structure at a given point. We compute it as a unitless fraction of the total incoming power. Start with s-polarization, using Eq. (4):

|ˆ + E E y|ˆ y|||
|---|---|---|---|
|f|b|||
|f|∗|b f∗ b∗|f|

E = H ∝ nE (− cos θxˆ + sin θˆz) + nE (cos θxˆ + sin θˆz) 1 S · ˆz = Re[zˆ · (E × H)] ∝ Re[(E + E)(E − Eb)n cos θ] (17)

absorption Local **INCOMING** **LIGHT** Poynting vector

n=2.2+0.2i n=1 n=3.3+0.3i n=1

Figure 2 – Sample calculation of local absorption and Poynting vector in a two-layer struc-

ture with air on both sides (refractive indices written below the graph).

I am really only interested in power flow as a fraction of incoming power. The incoming power is what you would get with Ef= 1,Eb= 0. So here is the final result: [] Re (n)(cos θ)(E + E)(Ef− Eb) f∗ b∗ s-polarization: S · ˆz = (18) Re [n₀ cos θ₀]

##### Next, p-polarization, from Eq. (5):

E = Ef(− sin θˆz + cos θxˆ) + Eb(− sin θˆz − cos θxˆ)

|ˆ + nE y nE|ˆ y|||
|---|---|---|---|
|f|b ∗|∗ f∗|b∗ f|

H ∝ 1 S · zˆ = Re[zˆ · (E × H)] ∝ Re[(cos θ) (E − E)(E + Eb)n] (19) 2

Again we normalize to incident power: [] Re (n)(cos θ

|)(E + E|)(E|− E )|
|---|---|---|
|∗ f|b f∗|b∗|
||∗ ∗|∗|

p-polarization: S · zˆ = (20) Re [n₀ cos θ₀]

(If I omitted parentheses somewhere, it’s because cos(θ) = (cos θ).)

##### 4.4 T (transmitted power) and R (reflected power)

To get the formula for T, the fraction of power transmitted, we simply take Eqs. (18),(20) and apply it to the final medium by plugging in Eb= 0 (no light is flowing backwards in the final layer): 2Re [n cos θ] s-polarization: T = |t| (21) Re [n₀ cos θ₀] ∗ 2Re [n cos θ] p-polarization: T = |t| (22) ∗ Re [n₀ cos θ₀]

where T is the fraction of power transmitted and t = Ef/E₀ is the transmission am- plitude. 4 The formula for R is just what you expect:

R = |r| 2 (23)

4.4.1 Counter-intuitive results when the initial medium is absorptive When the initial medium is absorbing, these formulas give very strange results. Most strikingly, you can get T > 1 in the absence of stimulated emission, and you can get R + T > 1 or R + T < 1 for an interface between two semi-infinite media. The issue more specifically is that the power entering the first layer of the stack (called power_entering in the tmm software) is not necessarily equal to 1 − R, as one would expect (energy 1 moving forwards, minus energy R moving backwards). I explain and discuss this in Appendix B. Quick summary of Appendix B: The difference between power_entering and 1 − R—which can only happen when the starting medium is absorptive—is related to an excess or deficit of absorption just before the first interface, arising from interference between the incoming and reflected waves. In other words, R and T are normalized to incoming power far from the interface, extrapolated to the interface assuming exponen- tial decay; but due to the interference, that extrapolation is inaccurate. So the actual power at the interface may be higher or lower than the power-normalization factor.
##### 4.5 Absorbed energy density

Next, absorbed energy density at a given depth. In principle this has units of [power]/[volume], but we can express it as a multiple of incoming light power density on the material, which has units [power]/[area], so that absorbed energy density has units of 1/[length]. This is the negative derivative (with respect to distance) of the S · zˆ expressions above. Differentiating is straightforward, using Ef(z) ∝ e ikz z and Eb(z) ∝ e −ikz z. (Reminder: kz= 2πn cos θ/λvac.) The result is:

|Ef+ Eb| 2 Im [n cos(θ)kz] s-polarization: a(z) = Re [n₀ cos θ₀] [ ∗ ( 2 2 )] Im n cos(θ) kz|Ef− Eb| − kz∗|Ef+ Eb| p-polarization: a(z) = ∗ (24) Re [n₀ cos θ₀]

Within a given layer, absorption is an analytical function:

a(z) = A₁e 2z Im(kz) + A₂e −2z Im(kz) + A₃e 2iz Re(kz) + A ∗ 3 e −2iz Re(kz)

4 In some references, the complex conjugation for p-polarization is omitted, but I’m very confident it’s correct. Usually the incident and final media are non-absorbing, e.g. air, so cos θ is real and it doesn’t matter whether you conjugate θ or not.

where:

Im [n cos(θ)kz]2 s-polarization : A₁ = |w| Re [n₀ cos θ₀] Im [n cos(θ)kz]2 A₂ = |v| Re [n₀ cos θ₀] Im [n cos(θ)k]

||z ∗||
|---|---|---|
|z|∗|2|
||∗||
|z|∗|2|
||∗||
|z||∗ ∗|
||∗||

A₃ = vw Re [n₀ cos θ₀] 2 Im [k] Re [n cos(θ)] p-polarization : A₁ = |w| Re [n₀ cos θ₀] 2 Im [k] Re [n cos(θ)] A₂ = |v| Re [n₀ cos θ₀] −2 Re [k] Im [n cos(θ)] A₃ = vw Re [n₀ cos θ₀]

where v = Ef(0) and w = Eb(0). (For the purpose of this section, z = 0 is the start of the layer in question. n₀ and θ₀ refer as usual to the incident semi-infinite medium; remember, we are calculating absorption per unit incident power.)

### 5 Branch cuts

Snell’s law gives θi= arcsin(n₀ sin(θ₀)/ni). However, the arcsine function is ambiguous– it has branch cuts in the complex plane. How do we get the right θ? There are actually only two non-equivalent choices. If θ is one solution, then π −θ is the other. You may recognize that we are choosing which of the two waves in medium i is called “forward-traveling” and which one is called “backward-traveling”. How do we make the right choice? Good news: In the intermediate, finite-thickness layers, the choice actually doesn’t matter. We solve for both the forward- and backward-traveling waves, so it doesn’t matter which wave has which name. The two choices of θiwill switch viwith wi, but won’t affect observable quantities like reflectance, absorption, etc. Bad news: The choice of θ versus π − θ does matter very much in the starting semi-infinite layer (where the “forward-traveling” wave amplitude is set to 1), and in the final semi-infinite layer (where the “backwards-traveling” wave amplitude is set to

0). In these layers, we need to choose θ correctly. More bad news: If you do the naive thing, θi= arcsin(n₀ sin(θ₀)/ni), you do not always wind up the right θi. It depends on how arcsine is defined in your programming language of choice (branch cuts are inherently arbitrary). For example, Python/SciPy wants to choose the wrong θ for the final layer during total internal reflection. Therefore I recommend you always check whether θ or π − θ is the right choice—see Appendix D for the specific criteria.

### 6 Thick “incoherent” films

##### 6.1 Introduction

That finishes the discussion of thin-film interference. Next, thick films. Here we are interested in hybrid structures containing both thick and thin layers (or even just thick layers). Light loses its coherence when traveling through the thick layers—i.e., the Fabry–P´erot fringes are so close together that they cannot be resolved by the experi- mental measurement, due to factors such as random thickness variations, propagation angle variations, and/or wavelength variations. Instead of seeing the fringes, you just see the average. I reiterate that an incoherent analysis is never strictly necessary. If incoherence comes from having a variety of wavelengths / angles / thicknesses, the obvious way to proceed is to do many coherent simulations across a variety of wavelengths / angles / thicknesses and then average the results. However, the incoherent analysis is a convenient shortcut when appropriate. In the tmm software approach, there are two types of layers: Coherent layers (treated as in the sections above), and incoherent layers. Generally, a layer should be treated as incoherent only if it is much much larger than the light wavelength, and if you have strong reason to believe that Fabry–P´erot fringes within that layer are getting averaged out. As soon as light enters an incoherent layer, its phase information is thrown out, and only its intensity is remembered. This approach does not allow partial coherence, it’s all or nothing! If that’s not good enough, you can always fall back on the universally- valid method of running coherent simulations and averaging the results, as mentioned above. 5

##### 6.2 Calculation method

||Layer 6 = Incoherent layer 3|V =T|W =0|
|---|---|---|---|
|Layer 5||||
|= Stack 1 Layers 2 & 3|Layer 4 = Incoherent layer 2|V₂|W₂|
|= Stack 0|Layer 1 = Incoherent layer 1|V₁|W₁|
||Layer 0 = Incoherent layer 0|1|R|

3 3

Figure 3 – Variable definitions related to the incoherent calculation program. A “stack”

is one or more consecutive coherent layers. Note the three numbering systems: Each layer has a layer index, each incoherent layer has an incoherent layer index, and each stack has a stack index. Vi,Wiare power flows (note the capital letters, not to be confused with the amplitudes vi,wiin Fig. 1).

We have a number of incoherent layers 0,1,...,N − 1. Let Vibe the forward propaga-

5 There are more sophisticated methods for dealing with incoherence than the simple one used here; see Refs. [1, 2] for example.

tion power and Wibe the backwards power at the beginning of the ith incoherent layer. (Capital letters to distinguish from v,w, the amplitudes in the coherent algorithm, see previous section.) Let Xiand Yibe forward and backwards power at the end of the ith incoherent layer. (Xiand Yiare not explicitly calculated in the tmm software.) Let Ti,jbe transmissivity from the ith to jth incoherent layer (where j = i ± 1, and Ri,jthe reflectivity. Then:

##### Yi= XiRi,i+1+ Wi+1Ti+1,i

Vi+1= XiTi,i+1+ Wi+1Ri+1,i () () () Xi1 1 −Ri+1,iVi+1 =. (25) Yi Ti,i+1Ri,i+1Ti+1,iTi,i+1− Ri+1,iRi,i+1Wi+1

Let Pibe the fraction of light that passes successfully through layer i (in a single pass) without getting absorbed, calculated by

4π Im[n

||||cos θ|]|
|---|---|---|---|---|
||−αd||i|i|
||i||||
|n|i i i|i|vac i i i|i+1,i|
|i,i+1|i|i,i+1|i+1,i i,i+1|i+1,i|

i P = e, α = (26) λ

where diis the layer thickness. Then: () () () V 1/P 0 X = (27) W 0 P Y

Define the matrices L by () () 1 1/P 0 1 −R Ln= (28) T 0 P R T T − R Ri,i+1

for n = 1,...,N −1. Now we want the matrix relating the powers entering the structure to the powers exiting, i.e.: () () 1 T = L˜. (29) R 0

Then the formula for L˜ is () () 1 1 −R1,0L˜ ˜ ˜ = L₁L₂ · · · L00L01 LN −1=

|||N −1|
|---|---|---|
|0,1 1,0 0,1|1,0 0,1||
||00|10 00|

T0,1R0,1T1,0T0,1− R1,0R0,1L₁₀ ˜ L₁₁ ˜

T = 1/L˜, R=L˜ /L˜ (30)

##### 6.3 Absorption profile, Coherence length

Absorption as a function of depth for incoherent layers is not implemented in the tmm software; this section explains why. Calculating the absorption profile within an “incoherent” layer is not simple to do correctly. If you look up close, the absorption as a function of position would be oscillatory near an interface due to interference between the incoming and outgoing beams; with the oscillations gradually dying down into a smooth exponential farther

away from the interface. The “coherence length” describes how far from the interface you need to go before the oscillations die down. For example, if the incoherence is caused by using a not-quite-monochromatic light source, the coherence length would be related to the bandwidth of the light. If you are only interested in calculating the total amount of light absorbed in each layer, it turns out that you do not need to know the coherence length!! More precisely, the coherence length does not affect the total absorption in (and transmission through) an incoherent layer under two assumptions (which are usually satisfied): (1) The co- herence length is large compared to a wavelength; (2) The coherence length is small compared to the layer thickness. This is an example of the more general mathematical fact that when you have sinusoidal oscillations that gradually die away, ∫their integral is independent of the

|∞ ikx|−αx|
|---|---|
|0||

precise decay properties. Here is an example: e e dx = −ik1+α ≈ −1ik; the integral is approximately independent of α as long as α ≪ k, i.e. as long as the decay length is much larger than the oscillation length. That’s the reason that you are not prompted to input coherence lengths in any of the calculations above. On the other hand, if you want to calculate absorption as a function of depth in an incoherent layer, you do need to know exactly what the coherence length is. It is generally hard to know a coherence length quantitatively. Therefore absorption as a function of depth is not implemented for incoherent layers in the tmm software. If you want to see absorption as a function of depth for an incoherent layer, you need to use the coherent program and average over slightly varying wavelengths / thicknesses / angles (as appropriate).

### 7 Acknowledgments

I thank Francis Loignon-Houle, John Honig, Fernando Stefani, Noah Rubin, Yinsheng Guo, Omer Luria, Fatemeh Edalatfar, Akira Okumura, and especially Mikhail Kats for helpful feedback and corrections.

### References

[1] B. Harbecke. Coherent and incoherent reflection and transmission of multilayer structures. Applied Physics B, 39(3):165–170, 1986. [2] Charalambos C. Katsidis and Dimitrios I. Siapkas. General transfer-matrix method for optical multilayer systems with coherent, partially coherent, and incoherent interference. Applied Optics, 41(19):3978, 2002. [3] Bertil Nistad and Johannes Skaar. Causality and electromagnetic properties of active media. Physical Review E, 78(3):036603, 2008. [4] Yi-Fan Chen, Peer Fischer, and Frank W. Wise. Negative refraction at optical fre- quencies in nonmagnetic two-component molecular media. Physical Review Letters, 95(6):067402, 2005.

### A Appendix: Sign convention for reflection am- plitude

A common point of confusion for students is the sign convention for reflection amplitude in the Fresnel equations. For p polarization in particular, half of textbooks use one sign convention, the other half use the opposite one. 6 The confusion more specifically is that it does not seem like it should be a convention (i.e., arbitrary choice) at all! After all, light interferes with its reflection. So the relative phase between light and its reflection does not seem like it should be arbitrary; it should have a right and wrong answer. We start by asking: why is there a sign convention in the first place? The electric field vector of a wave is unambiguous, but if we want to write that vector as a scalar amplitude times a unit vector, then there are two ways to do that, because we can flip the sign of both the amplitude and the unit vector. So two ways of formulating the equations are (cf. Eq. (5)):

##### Convention A (p-polarization) Convention B (p-polarization)

Ef= Ef(− sin θˆz + cos θxˆ) Ef= Ef(− sin θˆz + cos θxˆ) ˆ)

|E = E|(− sin θˆz − cos θx||ˆ)|E = E|(sin θˆz + cos θx|
|---|---|---|---|---|---|
|b|b|f|b|b|b|
||||b|||
|||b f||||

Again, the vectors E and E are the same for everyone, but different conventions will give different signs for E, and hence different signs for scalar quantities like the reflection amplitude E /E. For a concrete example, consider light in air reflecting off glass at normal incidence. The electric field switches sign (changes phase by π), while the magnetic field keeps the same sign (changes phase by 0). Related to this, there are two ways to define the relative phase of oppositely-propagating light beams, the one based on whether the magnetic field is in phase or not (“Convention A”), and the one based on whether the electric field is in phase or not (“Convention B”). These two conventions line up with the two possible signs of rp. In Convention A, rp> 0 for light in air reflecting off glass at normal incidence; in Convention B, rp< 0 in the same situation. At normal incidence, there is a compelling reason to prefer Convention B: This is the convention based on whether or not the electric field of the incident and reflected light are in phase. The electric field is generally more important for light-matter interaction than the magnetic field. Relatedly, this gives rs= rpat normal incidence, which neatly agrees with the fact that s and p are equivalent at normal incidence. (Everyone uses the same sign convention for rs.) However, at glancing angle, there is an equally compelling reason to prefer Conven- tion A! At glancing angle, light and its reflection are traveling in the same direction, so there is a unique and natural way to say whether the waves are in or out of phase at the interface. For example, if r = −1 at glancing angle, then that intuitively suggests that

6 For example, the following textbooks use “Convention A” (as defined shortly): Jackson (Eq. (7.41)), Hecht (Eq. (4.38)), Zangwill (Eq. (17.34)); whereas the following textbooks use “Convention B”: Feynman Lectures on Physics (Eq. 33.8), Griffiths (3rd edition, Eq. (9.109)), Lipson-Lipson-Lipson (Eq (5.42)).

the reflected light is equal and opposite the incident light, so we expect destructive in- terference at the interface (both zero electric field and zero magnetic field). Convention A agrees with that expectation. Again, there is no right or wrong convention, but we still have to pick one. So in this document we use Convention A.

### B Appendix: R and T with an absorptive start- ing medium

In this section, we discuss in more detail how we are defining R and T, and why this can lead to unexpected results like T > 1 when the starting medium is absorptive. As shown in Fig. 4, I define R and T by the following operation:

- Assume that the light starts out a large distance L behind the first interface, with power P₁ flowing towards the interface.
- The light travels the distance L, bounces off, then travels the same big distance L back through the initial medium, at which point it now has power P₂...
2αL

- R is defined by R = e P₂/P₁, in the limit L → ∞. (The exponential factor here cancels out the absorption in the initial medium, so that this limit exists.) (We don’t really need L → ∞; all that really matters is that L is big enough that it is beyond the area where the incoming and outgoing beams have coherent interference.)
- Similarly, let P₃ be the flowing away from the last interface (immediately after the interface)...
αL

- T is defined as T = e P₃/P₁, in the limit L → ∞.
+z

z=0

ted

Incoming

+✁ |z|/2 –✂ |z|/2

#### |E(z)|~e |E(z)|~r e

+ |z| –✄ |z|

#### P(z) ~ e P(z) ~ R e

Figure 4 – How the reflected power R is defined. Electric field E and power transported P

are shown.

(Are these good ways to define R and T ? Well, it depends on what you’re trying to do. For example, if you are putting an antireflective coating on tinted glass, these are great definitions. They make it very easy to calculate the overall reflection and transmission. My incoherent tmm calculation is based on situations like that. So, I like these definitions, although I admit that they are not the only possible definitions.) We obviously expect R = |r| 2 here (as usual), and that’s correct with this definition. The interesting thing—which had me confused at first—is that the normalized Poynting vector passing through the first interface is not necessarily equal to (1 − R), as one would expect (energy 1 moving forwards minus energy R moving backwards). Likewise, it is possible to have R + T 6= 1 for an interface between two semi-infinite media. This strange situation only comes up when the starting semi-infinite medium is absorbing. Why does this happen? To get the exact formulas for Poynting vector at the initial interface, called power_entering in the program, we just plug into the normal Poynting vector formula with Ef= 1 and Eb= r, to get:

s-polarization:

Re [n₀ cos θ₀(1 + r ∗

)(1 − r)] Im[n₀ cos θ₀]
power entering = = (1 − R) + 2 Im[r] Re [n₀ cos θ₀] Re[n₀ cos θ₀]

p-polarization:

Re [n₀ cos θ₀ ∗ (1 + r)(1 − r ∗ )] Im[n₀ cos θ 0∗ ∗] power entering = ∗ = (1 − R) − 2 Im[r] Re [n₀ cos θ₀] Re[n₀ cos θ₀] The first term is what we expect, the second term is strange. We naively expect the Poynting vector for z < 0 in Fig. 4 to satisfy

S(z) · ˆz = e α|z| − Re −α|z| [formula for without wave interference] (31)

where the first term comes from the incoming wave and the second term from the reflected wave. It is fine to demand this when the beams do not overlap, but we CANNOT use this expression in the “Interference here” triangle region of Fig. 4. Instead, there is interference between the forward- and backward-moving waves, which causes oscillations in the absorption profile (“hot-spots” and “nodes”) (see Fig. 2), so there are corresponding oscillations in the Poynting vector (it’s a bit hard to see them in Fig. 2 but they’re there). A bit of extra energy is flowing from the nodes to the nearby hot-spots. Thanks to these oscillations, the Poynting vector right at the edge before the start of the structure may not be 1 − R. If r is real, then there is a node or hot-spot of absorption right at the interface. It turns out that this sort of corresponds to having an integer number of oscillatory cycles, so the oscillations do not affect the power passing through the interface. R + T = 1 is still valid. But if r is complex, then you have an extra bit of absorption, or deficit of absorption, compared to the non-oscillating baseline expectation of Eq. (31). Instead of R + T = 1, the formula is:

R + T ± (extra bit or deficit of absorption from how the oscillations cut off) = 1

Again, this comes from the fact that R is defined by Eq. (31), which is not valid when there is interference. To verify that R = |r| 2 is the correct expression to use, we use the Poynting vector formula, plugged in at an arbitrary depth z < 0, using Ef= exp(2πinz cos θ/λvac) and Eb= r exp(−2πinz cos θ/λvac). I’ll just do the s-polarized case:

|Re[n₀ cos θ₀(E|+ E|)(E − E|)]|||
|---|---|---|---|---|---|
||f∗|b∗ f|b|||
|−4πz Im[n|cos θ]/λ|2 4πiz Re[n|+4πz Im[n cos θ|cos θ]/λ]/λ|)|

S(z) · ˆz = Re[n₀ cos θ₀] () = e 0 0 vac − |r| e 0 0 vac + () Im[n₀ cos θ₀] 0 0 vac + 2 Im[re] Re[n₀ cos θ₀]

The first term corresponds exactly to Eq. (31) with R = |r| 2, and the second term is a sinusoidal oscillation corresponding to interference. When the beams stop overlapping (i.e., below the triangle in Fig. 4), the oscillation term goes away but the other term remains. In the program, I use the variable “power_entering” to describe the net power entering the structure, i.e. the Poynting vector at the front of the first layer. For an interface between two semi-infinite media with light coming from just one side, power_entering is always equal to T. When the incident semi-infinite medium has real refractive index, power_entering is always equal to 1 − R.

B.1 Accounting for this effect in the incoherent calcula- tion One of the things I want to compute in the incoherent calculation is how much light gets absorbed in each layer. Part of that absorption is the “extra” absorption due to the oscillation cut-off at the interface. At the interface between two incoherent layers, say 0 and 1, let’s say the power flows on the two sides are Pf,0,Pf,1,Pb,0,Pb,1, where f and b stand forward-moving and backward-moving. The important thing to remember is that the net power actually crossing the interface is exactly Pf,0T₀₁ − Pb,1T₁₀. Why? Because the transmitted light beams have no funny corrections due to oscillations; they have nothing to coherently interfere with them. Therefore, the “extra” absorption near the interface, not accounted for in the ex- ponential decay of the waves, is exactly equal to
(Pf 0− Pb0) − (Pf 0T₀₁ − Pb1T₁₀) = Pf 0(1 − R₀₁ − T₀₁)

extra near-interface absorption on the 0 side, and likewise

##### Pb1(1 − R₁₀ − T₁₀)

extra near-interface absorption on the 1 side.

### C Appendix: Stimulated emission

With stimulated-emission (a.k.a. “gain” or “active”) media, there is a possibility for confusion. It turns out that Maxwell’s equations always have a unique finite steady- state solution, and the algorithm described herein will always find this solution. But this solution may be unphysical! There is, after all, another possibility: The system may be unstable, with fields exponentially growing (until the gain saturates). So you can find various papers exploring surprising aspects of Fresnel reflection and refrac- tion with gain—but where the results are all nonsense, because they are exploring unphysical solutions. A very helpful paper in this area is Ref. [3]. The same paper also explains why knowing n at one wavelength is not enough infor- mation to do a multilayer fresnel analysis when the initial or final layer has stimulated emission: The whole wavelength-vs-n dispersion is required to figure out which choice of arcsine to use (cf. Section 5). If a medium has gain at λ₁ but loss at λ₂, it can require you to use the unexpected choice of arcsine even at λ₂! An example along those lines is constructed in Ref. [4], where a certain dielectric function at a certain wavelength has negative refraction, even though it has (at that wavelength) neither negative permittivity nor negative permeability nor gain.

### D Appendix: Branch cuts

Snell’s law gives θi= arcsin(n₀ sin(θ₀)/ni). However, the arcsine function is ambiguous– it has branch cuts. How to get the right θ?? Remember here, nimay be an arbitrary complex number, ideally the program will work even for unusual cases like negative- index materials (Re n < 0) or stimulated-emission media (Im n < 0). Actually, we never care about θ itself, just sin θ and cos θ. The sine has no ambi- guity: n₀ sin θ₀ sin θi= ni The cosine is more problematic, because there are two choices consistent with Snell’s law: √ 1 2 2 cos θi= ± n i − (n₀ sin θ₀) ni Do we want the + or −?? In other words, we can pick between two angles θ and π − θ. See Section 5 for an explanation of what the choice really means, and more impor- tantly, why it only matters in the starting and ending semi-infinite layers, but doesn’t matter in the intermediate, finite-thickness layers.

##### D.1 Computer implementation

I do not recommend using θi= arcsin(n₀ sin(θ₀)/ni) and hoping to wind up with the right θ. That often works, but not always, at least not always in all program- ming languages. It depends on details of the arcsine branch cut implementation. In Python/SciPy, I found that this gives the wrong θifor total internal reflection when

θ₀ > 0. Even if it seems to always work, you are vulnerable to things like rounding er- rors pushing you to the other side of the branch cut, or changes in the arcsine definition when you upgrade your software, or whatever—it’s not a robust solution. A much better idea is to calculate θ = arcsin(n₀ sin(θ₀)/ni), then check that this is the right angle (using the criteria below), and if not, use π − θ instead. (As mentioned above, you only need to check the starting and ending semi-infinite layers.)

D.2 Case that Im n > 0, Re n > 0 For an absorbing material (Im n > 0), a clear requirement is that Im(n cos θ) > 0. That way, Im kz> 0, so the Efwave in the medium decays rather than amplifying. Another clear requirement is that R > 1 or T < 0 cannot occur. This translates to Re[n cos θ] ≥ 0 for s-polarization and Re[n cos θ
∗] ≥ 0 for p-polarization. This amounts to the same thing as saying that the Poynting vector associated with an Efwave should point forward not backwards. Important question: Are these two “clear requirements” consistent with each other. Yes! Theorem: If we choose the θ with Im(n cos θ) > 0, then it will also be true that Re[n cos θ] > 0. Proof: As above, √ nicos θi= ± n² i − (n₀ sin θ₀) 2

Given that Im ni> 0 and Re ni> 0, it follows that Im n² i > 0. Since n₀ sin θ₀ is real (the wave intensity is assumed to be uniform in the lateral direction), (n²i− (n₀ sin θ₀) 2 ) also has a positive imaginary part. Therefore, its square root is in the first or third quadrant of the complex plane. That finishes the proof. Theorem: If we choose the θ with Im(n cos θ) > 0, then it will also be true that Re[n cos θ ∗] > 0. Proof: ∗√ ∗ni 2 2 Re[nicos θi∗] = Re[nicos θi] = ± n i − (n₀ sin θ₀) ni Let φ with 0 < φ < π/2 be the complex phase of ni. We have

n ∗ i arg = −2φ ni

Using the fact that (n₀ sin θ₀) 2 is a nonnegative real number,

arg n²i= 2φ, 2φ ≤ arg(n²i− (n₀ sin θ₀) 2 ) < π

If we choose the square-root with positive imaginary part, √ φ ≤ arg n² i − (n₀ sin θ₀) 2 < π/2

Therefore, [ ∗√] n i 2 2 −π/2 < −φ ≤ arg n i − (n₀ sin θ₀) < −2φ + π/2 < π/2 ni

##### That finishes the proof.

D.3 Case that Im n = 0, Re n > 0 As before,
√ 1 2 2 cos θi= ± n i − (n₀ sin θ₀) ni There are three cases: Total internal reflection where n₀ sin θ₀ > niand cos θiis pure imaginary; the ordinary case where n₀ sin θ₀ < niand cos θiis pure real, and the boundary case where n₀ sin θ₀ = niand cos θi= 0. The third one has no ambiguity because cos θi= − cos θi. Let’s look at the other two cases.

D.3.1 Case Im n = 0, Re n > 0, Total internal reflection Here, Re[nicos θi] = 0 and Re[n
∗ i cos θ i∗] = 0, so no need to worry about the sign of the Poynting vector or R > 1 or T < 0. The only requirement is that the wave decay rather than amplify, i.e. Im(nicos θi)>0

D.3.2 Case Im n = 0, Re n > 0, Normal refraction Here, Im(nicos θi) = 0, so we get no information from whether the wave is decaying or amplifying.i i
∗

|The only criterion is Re[n|cos θ] > 0 and Re[n|cos θ] > 0 (meaning the||
|---|---|---|---|
||i i|∗ i i∗||
||||i i|

i i∗ Poynting vector points forward, R < 1, T > 0). In this case it simplifies to n cos θ > 0.

D.4 Case that Im n < 0, Re n < 0 This is not stimulated emission, despite Im n < 0. It is absorption. [Remember, with Re n < 0, the direction the wave is “really moving” (the direction of the Poynting vector) is opposite the direction of the wavevector. When Im n < 0, the wave is amplifying in the direction of the wavevector, so it’s “really” decaying.] Therefore the required criteria are the same as for ordinary absorbing media with Im n > 0 and Re n > 0: Im(n cos θ) > 0 (the Efwave decays rather than amplifies), Re[n cos θ] ≥ 0 for s-polarization and Re[n cos θ
∗] ≥ 0 for p-polarization (the Efwave carries energy forwards and R < 1 and T > 0.)√ If we flip the sign of ni, we do not affect n² i − (n₀ sin θ₀) 2, so we do not affect cos θi(up to a possible sign-flip) nor do we affect (nicos θi) (up to a possible sign- flip). Therefore the proof is exactly the same as before that the two requirements are consistent with each other.

##### D.5 Everything else

As mentioned above, active media cannot be analyzed in this way, because knowing n at one wavelength is not enough information to determine which solution is which—see Ref. [3]. There are other cases too, like n = 0, which I have not looked into.
