# Optical model for multilayer structures with coherent, partly coherent and incoherent layers

## Rudi Santbergen,

***** **Arno H.M. Smets, and Miro Zeman** *Photovoltaic Materials and Devices, Delft University of Technology, Mekelweg 4, 2628 CD, Delft, the Netherlands* ***

*r.santbergen@tudelft.nl*
**Abstract:** We present a novel approach for modeling the reflectance, transmittance and absorption depth profile of thin-film multilayer structures such as solar cells. Our model is based on the net-radiation method adapted for coherent calculations and is highly flexible while using a simple algorithm. We demonstrate that as a result arbitrary multilayer structures with coherent, partly coherent and incoherent layers can be simulated more accurately at much lower computational cost. ©2013 Optical Society of America **OCIS codes:** (350.6050) Solar energy; (240.0310) Thin films.

## References and links

1. E. Hecht, *Optics* (Pearson Education, 2002).
2. H. A. Macleod, *Thin-Film Optical Filters* (Taylor and Francis Group, 2010).
3. M. Born and E. Wolf, *Principles of Optics* (Pergamon Press Ltd., 1980).
4. C. C. Katsidis and D. I. Siapkas, “General transfer-matrix method for optical multilayer systems with coherent, partially coherent, and incoherent interference,” Appl. Opt. **41**(19), 3978–3987 (2002).
5. E. Centurioni, “Generalized matrix method for calculation of internal light energy flux in mixed coherent and incoherent multilayers,” Appl. Opt. **44**(35), 7532–7539 (2005).
6. J. S. C. Prentice, “Coherent, partially coherent and incoherent light absorption in thin-film multilayer structures,”
J. Phys. D Appl. Phys. **33**(24), 3139–3145 (2000).
7. M. C. Troparevsky, A. S. Sabau, A. R. Lupini, and Z. Zhang, “Transfer-matrix formalism for the calculation of optical response in multilayer systems: from coherent to incoherent interference,” Opt. Express **18**(24), 24715– 24721 (2010).
8. R. Siegel, “Net radiation method for transmission through partially transparent plates,” Sol. Energy **15**(3), 273– 276 (1973).
9. R. Santbergen, J. M. Goud, M. Zeman, J. A. M. van Roosmalen, and R. J. C. van Zolingen, “The AM1.5 <u>absorption factor of thin-film solar cells,” Sol. Energy Mater. Sol. Cells 94(5), 715–723 (2010).</u>
## 1. Introduction

Optical models for thin-film multilayer structures are used in several important applications such as design and analysis of optical coatings and thin-film solar cells. The objective of these optical models is to predict reflectance, transmittance or absorption depth profile as a function of wavelength. For accurate calculation of these parameters it is crucial that the interference between multiple internal reflections is taken into account correctly. Thus far this has been especially challenging for thin-film solar cells which typically have an absorber layer thickness on the order of the coherence length of the incident sunlight. Layers with an optical thickness less than the coherence length of the incident light cause observable interference fringes and are commonly referred to as coherent layers. Much thicker layers, that do not give rise to observable fringes, are referred to as incoherent layers. Partly coherent layers represent the intermediate case. Optical models for multilayer systems consisting of only coherent or only incoherent layers can be found in textbooks [1–3]. Models for the coherent case take into account the wave nature of light by representing it as complex amplitudes containing both amplitude and phase information. Models for the incoherent case consider only the light intensity without the phase information. However, most thin-film multilayer systems consist of both coherent and incoherent layers. A simple example is a thin anti-reflective coating, on a thick substrate. Reflectance (*R*) or transmittance (*T*) measurements of such a system show that there is interference in the coherent coating, but not in the incoherent substrate. A completely

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A262

*incoherent* simulation of such a system would fail to include interference in the coating, while a completely *coherent* simulation would show unrealistic interference in the substrate. The conventional approach to model these multilayer systems is to treat the coherent layers first, after which these are represented as interfaces in an incoherent calculation [4, 5]. This approach becomes rather involved for multilayer structures with a larger number of layers. An alternative approach is to simply treat all layers coherently and remove unrealistic interference by a suitable averaging procedure [6, 7]. The above mentioned approaches are commonly based on the transfer-matrix method [2]. We will show that the simpler net-radiation method, thus far only used for incoherent calculations [8, 9], can be used for these coherent calculations as well. By combining the coherent net-radiation method with a more efficient averaging procedure we obtained an elegant optical model for arbitrary multilayer systems consisting of coherent, partially coherent and incoherent layers.

Fig. 1. Schematic multilayer structure, with numbering convention of interfaces, layers and

electric field strength.

## 2. Coherent net-radiation method

Figure 1 shows a multilayer structure schematically. The numbering convention for interfaces

and layers is indicated. At each interface *i* = 1, 2,…*I*, four electric field strengths are defined (indicated by subscripts *a*, *b*, *c* and *d*), corresponding to electromagnetic waves propagating in left/right direction on the left/right side of the interface. These are complex amplitudes, i.e. the magnitude of this complex number represents the amplitude and the angle represents the phase of the electric field. These complex amplitudes are related by a set of linear equations. For every interface *i* there are four equations,

ì*EEia*= τ*i* −− 1(1) *i d* ï ï*ErEtEib*=+*i* >< *ia i ic* í (1) ï *EEic*= τ*i* (1) *i* + *b* ïî *EtErE* =+. *id i* >< *ia i ic*

We assume that a monochromatic plane wave with unit amplitude is incident from the left (*E1,a* = 1) and no light is incident from the right of the multilayer (*EIc* = 0). The coefficients *r* and *t* are the Fresnel amplitude coefficients of reflection and transmission calculated from the complex refractive index *N*. The subscript *>* or *<* indicates whether the light incident on the interface comes from the left or the right. The layer transmittance τi that appears in Eq. (1) indicates the change in the wave’s complex amplitude as it traverses layer *i* and is given by

τ*i*= *e* *i* δ*i*, (2)

## with complex phase

δπ*iii*= 2/, *Nd* λ (3)

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A263

and where *di* is the thickness of layer *i*. The system of linear equations given by Eq. (1) can be solved for all complex amplitudes using standard algorithms. From the obtained complex amplitudes the Poynting vector can be determined at each interface *i*

*PEH* =ℜ *, (4) *iii*()

where ℜ indicates the real part, *Ei* and *Hi* are the total resultant electric and magnetic field strength at the interface, given by

*EEE EEiiaibicid*=+=+, (5)

*HEEEEii*=−=− 00 ()(),*ai bi di c* (6) *NN* *NNii* −1

and *Hi** is the complex conjugate of *Hi*. Note that we use *E*, *H* and *P* in non-dimensional form, normalized to the incident light. In this way, from the Poynting vector the reflectance, absorptance of each layer and transmittance of the multilayer system can be easily derived

## RP =− 11

*Aiii*=− *PP*+1 (7)

## TP =I.

Also the absorption depth profile, i.e. the fraction of incident light absorbed at each depth inside the layer, can be easily found by evaluating the Poynting vector at different depths inside a layer. The advantage of the above described net-radiation method over the commonly used transfer-matrix method is that instead of using a sequence of 2 × 2 transfer matrices, all complex amplitudes are calculated at once by solving the set of linear equation given by Eq.

(1). Note that the number of equations is 4*I*, where *I* is the number of interfaces.
## 3. Incoherent layers

Thus far our treatment is completely coherent and therefore, like for any coherent approach, is not suitable for incoherent layers. We illustrate this by simulating a simple multilayer system with the following structure: glass (1 mm) / ZnO:Al (1 μm). Figure 2(a) shows the reflectance, absorptance and transmittance of this system calculated coherently. Because also the glass substrate is treated coherently, a dense pattern of interference fringes is visible. Obviously, this is not in agreement with the measured *R* and *T* (indicated by symbols), showing only broad fringes due to the thin ZnO:Al layer. In the inset of Fig. 2(a) the horizontal axis is zoomed in to show a much more narrow wavelength range. This reveals that the dense fringes caused by the substrate closely resemble a sine function. The physical reason that these dense fringes are not observed experimentally could be related to non-uniform substrate thickness or limited spectral sensitivity. A more fundamental reason is that the substrate thickness (1 mm) far exceeds the coherence length of the incident light, which for sunlight is about 1 μm [1]. This means that there is no constant phase relation between light reflected at the front and at the rear of a thick layer, which averages out these narrow interference fringes. One way to think of this is that the complex phase δi given by Eq. (3) is valid for coherent layers, but for incoherent layers a time dependent phase ϕ*(t*) should be added

δπλ*ii*() *tNd* =+ 2*i*/ ϕ(). *t* (10)

This ϕ(*t*) varies randomly on time scales much smaller than the typical measurement time scale. As a result, for multilayer structures with one or more incoherent layers the derived quantities *R* and *T* will fluctuate rapidly as well. However, typical measurements will give

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A264

time averaged and reproducible values for *R* and *T* in which the narrow interference fringes are averaged out.

1 1

0.9 0.9

||reflectance|
|---|---|
||abs. glass abs. ZnO:Al transmittance|
|0.8|0.9 1|

0.8 0.8 1 1 T, A, R (−)
0.7
0.9 T, A, R (−)0.70.9 T (−)
0.8T (−)0.8
0.6 0.6
0.7
0.6 0.6001 0.6002 0.6003 0.6004 0.70.6 0.6001 0.6002 0.6003 0.6004 wavelength (μm) wavelength (μm)
0.50.4
0.5 0.6 0.7 0.8 0.9 1
0.50.4
0.5 0.6 0.7
wavelength (μm) wavelength (μm)

(a) (b)
Fig. 2. Simulated (area) and measured (symbols) *R*, *A* and *T* of a 1 μm ZnO:Al film on glass.
 The inset shows *T* in more detail. (a) single coherent simulation (b) average of three coherent simulations (the inset shows the individual simulations with ϕ = 0°, 120° and 240° and their average). It is this time averaged value that we wish to calculate with the optical model. The
conventional method for doing this is based on combining the coherent electric field calculations and the incoherent intensity calculations [4, 5]. Especially for systems consisting of several coherent and incoherent layers this is rather complicated. A more flexible method exists in which several coherent calculations, each with a different value of ϕ, are simply averaged [6, 7]. This method does not require any incoherent calculations with intensity and more closely mimics the physical process that averages out the interference fringes. Thus far this was done by taking *random* values of ϕ (see Eq. (10). Indeed, it can be shown that a large collection of sine waves with a random phase will average out to a constant value. However, using random values has the drawback that thousands of sine waves need to be averaged to sufficiently remove the fringes. We show that the same result can be achieved with much less calculation time using *equidistant* values of ϕ instead of random ones. The inset of Fig. 2(b) illustrates how for ϕ₁ = 0°, ϕ₂ = 120° and ϕ₃ = 240° the fringes are shifted by phase ϕ*.* Obviously, the average of multiple sine waves with the phase distributed equidistantly averages out to a constant value. In the inset of Fig. 2(b) the average value is indicated by the horizontal black line. The main Fig. 2(b) shows the average value throughout the wavelength range 0.4-1.0 μm. This clearly illustrates that the dense fringes are removed everywhere and only the interference fringes of the thin ZnO:Al layer remain. This is in excellent agreement with the measured *R* and *T* (indicated by symbols). We note that the fringes shown in Fig. 2(a) in for example *R* are due to the superposition of the reflectance of the front interface and additional contributions from light bouncing up and down the glass substrate multiple times, i.e. the higher order reflections. It can be shown that the use of *n* equidistant values of ϕ assures that the interference of up to the *n* th order reflection cancels out perfectly and only the interference effects due higher orders remain. Because the intensity of the higher order reflections decreases exponentially with increasing order, accurate results can be obtained with a very limited number of simulations. To compare the accuracy of our method using equidistant values of ϕ (denoted by ‘equidistant method’) to the existing method of using random values of ϕ (denoted by ‘random method’), we compare them both to the exact solution. Figure 3 shows the deviation of both methods as a function of the number of simulations that are averaged. The deviation is defined here as the wavelength averaged deviation in both *R* and *T* for the glass / ZnO:Al structure considered above. We normalize the deviation such that the deviation is unity for the single coherent simulation with ϕ = 0° (as shown in Fig. 2(a)). By definition, both the random and equidistant method have a deviation of 1 when ‘averaging’ a single simulation. When increasing the number of

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A265

simulations in the random method, the deviation decreases, albeit slowly (red line). In this method as many as 10 4 simulations need to be averaged to reduce the deviation to 1% of the original value. On the other hand, when increasing the number of simulations in our equidistant method, the deviation from the exact solution decreases very rapidly (green line). In this case only three simulations need to be averaged to reduce the deviation below 1%. In case of 10 simulations, the equidistant method deviates from the exact solution by even less than 10 −9. This not only indicates that our equidistant method converges to the exact solution, but also that it does so much more rapidly than the existing random method. In the above example a multi-layer structure with a *single* incoherent layer was considered. The same approach can also be applied for *multiple* incoherent layers. In that case the averaging should be performed over every phase combination. Although this increases the computational cost, for the most frequently encountered multilayer systems with only a few incoherent layers the equidistant method is still many times faster than the random method.

1e−3

deviation (−) 1e−6

random <u>equidistant</u> 1e−9 0 1 2 3 4 10 10 10 10 10 nr of simulations (−)

Fig. 3. Deviation from the exact solution as a function of the number of coherent simulations

averaged. The existing method of averaging with random ϕ (red line) and our new method of averaging with equidistant ϕ (green line) are compared.

## 4. Partially coherent layers

Thus far we have considered coherent and incoherent layers, with a thickness that is respectively much smaller or much larger than the coherence length of the incident light. Partially coherent layers represent the intermediate case. The degree of coherence can be measured by the visibility *V* of the interference fringes. This visibility is defined as the amplitude of the fringes normalized by the amplitude in the coherent limit. By definition *V* = 1 in the coherent limit. With increasing layer thickness (or decreasing coherence length of the incident light) the amplitude of the fringes, and therefore *V*, gradually reduces, reaching zero in the incoherent limit. We note that the averaging has been done with equal weight for each calculation. Partial coherence could be simulated by simply attaching more weight to the calculation with ϕ = 0°. We illustrate this by simulating an hydrogenated amorphous silicon (a-Si:H) solar cell with the following structure: glass (1 mm) / ZnO:Al (1 um) / p (20 nm) / i (300 nm) / n (20) nm / Ag. Here p, i and n indicate the p-type, intrinsic and n-type a-Si:H layers. The ZnO:Al layer serves as transparent front contact and Ag serves as reflective back contact. For solar cell applications the most interesting quantity to obtain from the model is the absorptance of the absorber layer, which in this case is the intrinsic a-Si:H layer. Figure 4(a) shows this absorptance versus wavelength λ for various degrees of absorber layer coherence ranging from coherent (*V* = 1) to incoherent (*V* = 0). In all cases the glass superstrate is treated incoherently and the other layers coherently. The fringes that appear when the absorber layer is treated more coherently can be attributed to interference in this layer. These fringes appear only for λ = 550 - 800 nm because in this range the absorber layer goes from opaque to

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A266

completely transparent. The fringes at shorter wavelengths due to interference in the ZnO:Al layer are independent of the degree of coherence of the absorber layer. Such fringe patterns are also observed in measurements of solar cell reflectance or external quantum efficiency. The absorption depth profile of the absorber layer is also obtained from the simulation and is shown in Fig. 4(b) for a wavelength of 600 nm. When the absorber layer is treated coherently, the depth profile shows a strong interference pattern. This is due to the superposition of the incident wave and the wave reflected by the Ag back reflector traveling in opposite direction. When the absorber layer is treated more incoherently this pattern converges to a monotonically decreasing function. This is as expected as in the incoherent limit the depth profile is simply an exponential curve given by the Lambert-Beer law [3].

20 coherent

0.8 coherent s)λ = 600 nm
4 15

0.6
(−)
10

0.4 a−Si:H(i) incoherent
A

0.2 5
abs. rate (photons/nmincoherent 0 00

0.4 0.5 0.6 0.7 0.8 0.05 0.1 0.15 0.2 0.25 0.3 wavelength (μm) depth (μm)
(a) (b)
Fig. 4. (a) Absorptance and (b) absorption depth profile for of the absorber layer of an a-Si:H
 solar cell for various degrees of absorber layer coherence, indicated by visibility *V*. The lines represent *V* = 0.0, 0.2, 0.4, 0.6, 0.8 and 1.0.
## 5. Conclusion

In summary, we showed that the net-radiation method can be used for coherent calculations of multilayer structures. We demonstrated that by averaging only a few calculations with equidistant values of ϕ, the coherence of any layer can be removed partly or completely. This makes this relatively simple method a powerful optical design tool for multilayer structures consisting of coherent, partly coherent and incoherent layers, such as thin-film solar cells. We illustrated this method by optical simulation of an a-Si:H solar cell with various degrees of absorber layer coherence.

## Acknowledgment

The authors would like to thank Janez Krc, Sergey Solntsev and Klaus Jäger for helpful discussions. This work was funded by the Dutch STW Vidi grant of A.H.M. Smets.

|#180430 - $15.00 USD|Received 28 Nov 2012; revised 8 Feb 2013; accepted 8 Feb 2013; published 15 Feb 2013|||||
|---|---|---|---|---|---|
|(C) 2012|OSA|11 March|/ Vol.|21, No.|S2 / OPTICS|

EXPRESS A267
