# Open-source integrated optical modelling with RayFlare

*∗†*, Nicholas Ekins-Daukes Department of Physics, Imperial College London, London SW7 2AZ, United Kingdom School of Photovoltaics and Renewable Energy Engineering, UNSW Sydney, NSW 2052, Australia

outline framework

Phoebe Pearce *∗* *∗* *†*

***Abstract*—RayFlare is a new Python 3 extension which aims to integrate multiple optical modelling methods in one easy-to-**

**use environment. The resulting code is capable of modelling a** **wide range of solar cells with a variety of light management structures across length scales, such as planar anti-reflection**

**coatings, distributed Bragg reflectors, large-scale textured sur- faces such as pyramids, and nanoscale diffraction gratings.**

**The methods currently included are three-dimensional ray- tracing, the transfer-matrix method (TMM), rigorous coupled-**

**wave analysis (RCWA) and a matrix framework for coupling multiple methods across one structure. The output provided**

**includes absorption/generation profiles, so the results can be used straightforwardly in electrical solvers. Calculations can be**

**performed easily across wavelengths, using either custom-defined material parameters or Solcore’s database to provide the correct**

**optical constants to the relevant solvers. The modular framework** **means it is easy to add functionality, and the code is fully open- source and free to use.**

***Index Terms*—multi-junction solar cells, light trapping, optical modelling, RCWA, TMM, ray-tracing**

I. INTRODUCTION
Modelling is integral to the design and optimization of solar cells, and many programs and packages, both commercial and free to use, are available to aid in the design of different

|Fig. 1.|Schematic|of the matrix|with the labels|of|
|---|---|---|---|---|
|redistribution matrices describing reflection and transmission at the different|||||
|surfaces.|||||

kinds of devices. However, challenges can arise in optical modelling when dealing with structures which involve very different length scales (e.g with feature sizes ranging from nanometres to hundreds of microns) and different types of structures which perhaps cannot be (efficiently) modelled using the same method. For some situations, the OPTOS [1], [2] or GenPro4 [3] framework is useful to combine multiple modelling methods in a flexible way. These methods require the optical structure to be divided into separate parts: the front surface, the bulk, and the back surface. The front and back interfaces may be made up of several layers, or be textured, the reflection and transmission for different angles of incidence can be calculated. The OPTOS method itself is straightforward, and essentially amounts to matrix multipli- cation. For both interfaces, using a suitable optical method (e.g. TMM, ray-tracing, RCWA, or analytical expressions), a matrix must be constructed which describes how light incident on the interfaces is redistributed into other angles, or absorbed. In two dimensions, this will relate some polar angle *θ* *in*to one or more *θout*, with the matrix elements describing what fraction of incident light goes to each outgoing angle. This can be expanded to three dimensions by including an azimuthal angle *φ* [1]. However, OPTOS does not include any methods for com- puting the redistribution matrices, only the code to perform the matrix multiplication (which is available freely). On

the other hand, GenPro4 also performs integrated wave- optical/ray-tracing methods, but is not free or open-source. The motivation behind the development of RayFlare is to provide a way of using the well-established matrix framework more easily, integrated directly with methods to actually com- pute the redistribution matrices, while making it possible for more advanced users to also extend the code and incorporate their own methods for calculating these matrices.

## II. BACKGROUND

RayFlare is an integrated version of several existing codes, including ones developed by the Quantum Photovoltaics Group at Imperial College as well as open-source code from other sources. It is designed to work closely with Solcore [4], an open-source Python package for modelling both optical and electrical properties of semiconductor devices, especially solar cells. Solcore already incorporates several optical mod- elling methods, including simple Beer-Lambert absorption, a transfer-matrix model and an interface with *S⁴*, a package for performing rigorous coupled-wave analysis (RCWA) [5]; RayFlare is intended as an extension which focuses purely on developing the optical modelling capabilities. The transfer-

978-1-7281-0494-2/19/$31.00 ©2019 IEEE Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on July 01,2026 at 10:51:23 UTC from IEEE Xplore. Restrictions apply.

matrix model included is largely based on the tmm Python package [6], which was vectorized for faster use in Solcore, in addition to other modifications which allow for the calculation of absorption profiles in partially incoherent stacks. The ray- tracing code used is a novel implementation which is designed to work with any continuous surface provided it can be represented by a Delaunay triangulation in Python through a series of *x*, *y*, *z* coordinates. RayFlare is intended as a companion package to Solcore, producing compatible output for solar cell simulations based on RayFlare’s optical results.

## III. OUTLINE OF THE MODEL

Fig. 1 shows some of the key features of the modified

OPTOS framework used for RayFlare, Three-dimensional hemispherical space is divided into angular channels in both the polar (*θ*) and azimuthal (*φ*) directions. The angle dis- cretization is performed according to the method in [1], where the spacing of the bins is chosen so that the area of the bins projected onto the *x*-*y* plane is approximately equal. This means that different incident polar angles *θ* have different numbers of corresponding *φ* bins. RayFlare is intended for structures with textured surfaces which are parallel to one another, i.e. each texture is confined to a plane. The power fraction in each angular bin, *P* (*θi,φj*), at any point within the simulation is represented by a vector:

⎛ ⎞ *P* (*θ₁,φ₁*) ⎛ ⎞ ⎜ *P* (*θ₁,φ₂*) ⎟ 1 ⎜ ⎟ ⎜ ⎟ ⎜.. ⎟ ⎜ 0 ⎟ *→−* *v* = ⎜⎜. ⎟ ⎟=⎜⎜ 0 ⎟⎟ (1) ⎜ *P* (*θ₂,φ₁*) ⎟ ⎜. ⎟ ⎜ ⎟ ⎝. ⎠ ⎜.. ⎟. ⎝. ⎠ 0 *P* (*θn,φm*)

The equation above shows, after the second equals sign, a specific example of a *→−* *v* vector for normally incident light. The *→−* *v* vectors are always relative to unity incident power. For each surface, *R*, *T* (see equation 5) and *A* (see equation

6) matrices can be computed, which describe the angular distribution of light reflected back into the half-plane of the incident light, the angular distribution of light transmitted into the other half-plane, and light absorbed in each layer of a surface, respectively. Absorption in the bulk, which is assumed to be thick enough compared to the wavelength of incident light that interference effects can be neglected, can be calculated very straightforwardly according to the Beer-Lambert law, ac- counting for the increased path length of light which has been scattered into non-normal angles:
⎛ *−αd/* cos*θ* ⎞ *e*1*...* 0
⎜......... ⎟
*D* = ⎝ ⎠ (2)

*··· e* *−αd/* cos*θn*

Once all the matrices have been computed, the power vectors as the light propagates through the structure (see the labelling used in Fig. 1) can be calculated iteratively:

*⃗vf*1*,l*= *Tf*1*⃗v₀* *⃗vb*1*,l*= *Dvf*1*,l* *⃗vb,l*= *Rf,*2*⃗vb,l* 2 1 *⃗vf*2*,l*= *Dvb*2*,l*

(3)
*⃗v₀* = *⃗vf*2*,l* *⃗vf*1*,l*+1= *Tf*1*⃗v₀* ...

Here, the *l* index refers to which pass of light through the cell is being considered: *l* =1refers to the light travelling downwards from the front of the cell through the bulk and back up again the first time. By iterating equations 3, we track the power flows∑using *i*=*k* the *⃗v* vectors; the total power remaining is given by*i*=1(*⃗v*)*i*where *k* is the total number of (*θ,φ*) bins, and the calculation is iterated until the total power is below some small threshold amount. However, we would also like to track where power is absorbed, reflected, and transmitted:

*i*=*k i*=*k* *A* = ∑ (*⃗v*) *−* ∑ ( *⃗v*) *down,l f₁,l i b₁,l i* *i*=1 *i*=1 ∑ *i*=*k*∑*i*=*k* *Aup,l*= (*⃗vb*2*,l*)*i−* (*⃗vf*2*,l*)*i* *i*=1 *i*=1 (4) *⃗vr,l*= *Tb*1*⃗vf*2*,l* *⃗vt,l*= *Tf*2*⃗vb*1*,l* *⃗aback,l*= *Af*2*⃗vb*1*,l* *⃗a* = *A ⃗v* *front,l b*1 *f*2*,l*

Here, the *A* values refer to power absorbed in the bulk on the downwards and upwards parts of a pass through the cell, while *⃗vrl*and *⃗vtl*describe light escaping away from the front surface of the cell (reflection) and into the medium behind the cell (transmission), respectively. The *⃗a* vectors describe how much light is absorbed in each layer in the front and back stack. These values are computed at each wavelength and for each pass *l* through the structure. This means it is possible to see how much light is absorbed in each part of the cell in each pass, and also how much light is reflected/transmitted; for instance, it may be relevant to see the contributions of direct reflection during the first interaction of light with the front surface of the cell (*⃗vr,*0) compared with escape reflection due to light incident from the inside of the cell escaping through the front surface (*⃗vr,i*for any *i>*0). To find the total reflected or transmitted power at each wavelength, the *⃗vr,l*and *⃗vr,l* matrices can be summed over both the *l* index and over all the angular channels, to give the reflected and transmitted power at each wavelength. Similarly, *⃗afront,l*and *⃗aback,l*can be summed over the pass index and the layer index to find

⎛ ⎞ *p*((*θ ,φ*) *→* (*θ ,φ*)) *p*((*θ ,φ*) *→* (*θ ,φ*))*... p*((*θn,φm*) *→* (*θ ,φ*)) ⎜ *p*((*θ₁,φ₁*) *→* (*θ₁,φ₂*)) *p*((*θ₁,φ₂*) *→* (*θ₁,φ₂*))*... p*((*θn,φm*) *→* (*θ₁,φ₂*)) ⎟ *R,T* = ⎜ ⎟ (5)
⎝...... ⎠
... *p*((*θ₁,φ₁*) *→* (*θn,φm*)) *p*((*θ₁,φ₂*) *→* (*θn,φm*))*... p*((*θn,φm*) *→* (*θn,φm*))

⎛ ⎞ *p*((*θ ,φ* 1 1) *→ Alayer* 1) *p*((*θ ,φ* 1 2) *→ Alayer* 1)*... p*((*θn,φm*) *→ Alayer* 1) ⎜ *p*((*θ₁,φ₁*) *→ Alayer* 2) *p*((*θ₁,φ₂*) *→ Alayer* 2)*... p*((*θn,φm*) *→ Alayer* 2) ⎟ *A* = ⎜ ⎟ (6)
⎝...... ⎠
... *p*((*θ₁,φ₁*) *→ Alayer k*) *p*((*θ₁,φ₂*) *→ Alayer k*)*... p*((*θn,φm*) *→ Alayer k*)

the total power absorbed in the whole front and back stack at each wavelength. Due to the way the matrices describing the front and back texture are coupled using a bulk matrix *D* (eq. 2) which is very simple to calculate, it is extremely fast computationally to change the thickness of the bulk structure and recalculate the absorption. Similarly, if one of the textures is changed, only the matrices corresponding to that surface need to be recalculated; this way, different textures and bulk thicknesses can be combined without having to repeat a computationally intensive simulation of the whole structure.

IV. INVESTIGATING A PEROVSKITE/SHJ TANDEM CELL WITH INTEGRATED TMM/RAY-TRACING

To illustrate the power of the matrix framework in com- bination with integrated TMM/ray-tracing, a tandem cell consisting of a Cs-Br perovskite with a bandgap of 1.65 eV [7] on top of a silicon hetero-junction (SHJ) cell with Fig. 2. Layer structure of a perovskite/silicon hetero-junction tandem cell. In terms of the matrix framework, the layers deposited on top of the bulk a bandgap of 1.1 eV [**?**] is considered. The full stack is silicon, including the perovskite, make up the front surface and the a-Si/ITO shown in Fig. 2 and the layer thicknesses are given inlayers make up the back surface. The silver back layer is treated as the Table I. We consider unpolarized light (an equal mixture semi-infinite transmission medium in the TMM calculations. of *s* and *p* polarization) which is normally incident on the front surface of the cell. The c-Si is assumed to have a *◦* regular pyramidal texture, with an elevation angle of 55, on both sides, onto which the top layers including a 440 nm perovskite layer are conformally deposited, following the cell TABLE I design in [8]. The total thickness of the front layers (aroundTHICKNESSES OF EACH LAYER IN THE PEROVSKITE/SHJ STRUCTURE

|SHOWN IN|FIG.2.THE REFERENCES INDICATE THE SOURCE USED FOR|||
|---|---|---|---|
|THE OPTICAL CONSTANTS|||; IF THESE SOURCES CONTAIN MULTIPLE|
|VALUES|, THE NOTES COLUMN CLARIFIES WHICH VALUES WERE USED OR WHICH OPTICAL CONSTANTS WERE ASSUMED|||
|Material||Thickness|Notes|
|MgF₂ [9]||100 nm||
|IZO [10]||110 nm|r (O₂)=0.10%, annealed|
|SnO₂||10 nm|Assumed n =2, κ =0at all λ|
|C [11]||15 nm||
|LiF [4]||1 nm||
|Perovskite [7]||440 nm|CsBr 10 %, 1:2|
|Spiro-TTB||12 nm|Assumed n = 1.65, κ =0at all λ|
|a-Si (n) [?]||6.5 nm||
|a-Si (i) [?]||6.5 nm||
|c-Si [4]||260 μm||
|a-Si (i) [?]||6.5 nm||
|a-Si (p) [?]||6.5 nm||
|ITO [4]||240 nm||
|Ag [12]||semi-infinite||

700 nm) is relatively small compared to the typical size ofSHOWN IN FIG.2.THE REFERENCES INDICATE THE SOURCE USED FOR pyramid textures on silicon (with base length on the order of, several microns). Thus, we make the assumption that we can. treat the front surface using ray-tracing as a single surface with infinitesimal thickness, with reflection and transmission probabilities calculated using TMM according to the layers on the surface. In this case, we have ignored the height of 60 the pyramids when calculating the absorption in the bulk c-Si (thickness 260 *μ*m).

*A. Calculating lookup tables using TMM*
Fig. 3 shows the results of TMM calculations across rele-

- *◦*
vant wavelengths and incidence angles from 0 to 90 for the front stack including the perovskite layer, both for incidence from the front (a-c) and rear (d-f) of the stack. These calcula- tions assume a surface made of planar layers. The calculations for incidence from inside the structure take into account the

Fig. 4. Example of a redistribution matrix, in this case the matrix *Rb,*1at

1000 nm for the perovskite/SHJ stack.

|information|(along with|the polarization|of the|light and|
|---|---|---|---|---|
|the wavelength)|is then|used to look|up the probabilities||
|of reflection (for a simple interface without additional layers, the Fresnel|and transmission|in|TMM lookup|table|
|equations|can also be|used directly).|The algorithm|then|

the

Fig. 3. a) Reflection and b) transmission of the front stack, and c) absorption

in the perovskite layer across wavelengths and angles, for light incident from outside on the front of the cell and light incident from the Si bulk. Similar absorption data is also stored for the other layers in the stack, but not shown here because the absorption is very low compared to the perovskite layer.

d)-f) show the same information but for light incident from inside the cell on the back of the front stack. fact that the light is incident from a medium with a non-unity refractive index (in this case, we have ignored the imaginary part of the refractive index for the Si incidence medium). In
Fig. 3a we can see that the direct reflection for light incident
 from air on the MgF₂ is low, except for extremely grazing incidence. In Fig. 3b (transmission) and c (absorption) we can clearly see where the perovskite is absorbing (*<* 750 nm) and where it is transparent. For light incident from the Si, we can clearly see total internal reflection occurring in Fig. 3d for wavelengths where the perovskite is non-absorbing.
*B. Calculating the redistribution matrices* The redistribution matrix is calculated by considering a total of 1 million rays in a Monte Carlo ray-tracing simulation. With the angular discretization chosen, this corresponded to 770 rays for each incident combination of *θ* and *φ*.25 different points of incidence on the unit cell were considered, with the incident rays equally divided between these points. The ray-tracing algorithm checks if a ray incident from a specific direction at a point on the unit cell intersects the surface (in this case, a pyramid), and at which angle. This
decides whether the ray is reflected or transmitted according to these probabilities. The algorithm keeps checking if the ray will intersect with the surface until it passes into the bulk below or above the surface, at which point the outgoing global angle is recorded. For an absorbing surface, the ray can also be absorbed; in this case, the local incidence angle is also stored (so that the absorption profile can be calculated). The ray-tracing method, whether used with the Fresnel equations or a lookup table, is inherently stochastic; rays can be reflected, absorbed, or transmitted, with probabilities taken from the lookup tables (or determined through the Fresnel equations). If lookup tables are used, there may be more than one layer in the stack in which the light can be absorbed; however, it is not necessary to choose which layer the absorption takes place in stochastically, since these probabilities are calculated exactly from the TMM. Thus, when a ray is absorbed, the program checks in the lookup table what the probability of absorption per layer is (for the correct wavelength, side of approach, polarization and local incidence angle) and stores this information. At the end of the simulation, a matrix can then be generated relating the global incidence angle in terms of (*θ,φ*) bins to the probability of absorption in each layer. However, because the absorption probabilities per layer are determined analytically using TMM while the R and T probabilities are generated stochastically, the situation can arise that (e.g. for a two-layer stack) *R* + *T* + *Alayer*+ *Alayer̸* =1exactly. Thus, when generating the final matrices at the end of each wavelength loop, the total number of rays which are not reflected or

|Fig. 5.|Absorption per layer, and direct and escape reflection, calculated||||
|---|---|---|---|---|
|using the|matrix|with redistribution|computed|with|
|integrated ray-tracing and TMM. Non-absorbing layers (κ included.|||=0) are not||

formalism matrices

|transmission,|and absorption|probabilities.|The absorption|
|---|---|---|---|
|profile on the incidence angle on the surface; however, in the case of a textured sheet, the local (θ|from|the A parameters ) and global (θ|and k depends ) incidence|

Fig. 6. Absorbed energy density with depth at different wavelengths for the

perovskite/SHJ stack.

transmitted (i.e. must therefore have been absorbed) is stored, so that the fraction of absorbed rays *Abs* is known for each global incidence angle. This is then ∑ used to scale the *n* *layers* absorption fractions per layer, so that*i*=1*Ai*= *Abs*. One of the redistribution matrices calculated for the per- ovskite/SHJ structure (specifically, matrix *Rb,*1at *λ* = 300 nm) is shown in Fig. 4.

*C. Calculating absorption profiles in integrated TMM/Ray-* *tracing* In the transfer matrix method, the absorption profile within a given layer can be expressed analytically [6]: *a*(*z*)=*A₁e²*
*z* Im(*kz*) + *A₂e* *−*2*z* Im(*kz*)

2*iz* Re(*k*) *∗ −*2*iz* Re(*k*)

(7)
+ *A₃e* *z* + *A₃e* *z*

Here, *A₁* and *A₂* are real parameters, while *A₃* and *kz* (the *z*-component of the wavevector, *kz*=2*πn*cos*θ/λvac*) are complex. These parameters depend on the wavelength, polarization and incidence angle; physically, *A₁* describes the

Fig. 7. Illustration of the global incidence angle *θg* and local incidence angle

*θ* *l*for a surface with V-grooves.

amplitude of the forward-travelling wave at the front of a layer, *A₂* the amplitude of the backwards-travelling wave at the back of the layer, and *A₃* gives the thin-film interference terms. When the lookup table is computed prior to ray-tracing, these parameters are stored along with the overall reflection,

calculated*z*

*l g* angles are generally not identical, as illustrated in Fig. 7. The redistribution matrices consider global incident and outgoing angles, but to calculate the absorption profiles we must be able to relate global to local incidence angles. Thus, during ray-tracing, for each absorbed ray, the local incidence angle is binned and stored. At the end of the ray-tracing procedure, the absorption profile for each local incidence angles corre- sponding to a global incidence angle can then be weighted to generate an overall absorption profile for that global incidence angle. Clearly, the absorption profile at different parts in the textured surface will be different, depending on the local incidence angle; thus we are really calculating an absorption profile averaged over one ray-tracing unit cell. With the absorption profile, we can see where light is absorbed within the layers, and generate the necessary in- put for e.g. a Poisson drift-diffusion (PDD) or depletion approximation (DA) solver when investigating the electrical properties of the cell, for instance using Solcore. The absorption profile in the bulk for each pass can be calculated similarly, by considering the power fraction of the incoming light travelling through each (*θ*, *φ*) channel, and calculating the absorption profile according to:

*dI*(*z*) *d−αz/* cos*θα−αz/* cos*θ* *a*(*z*)=*−* *dz* = *− dz*(*I₀e*)= cos *θ I⁰* *e*

(8)
where *I₀* is the power fraction in the angle bin just after interaction with a surface, before bulk absorption, and *α* is the absorption coefficient at the relevant wavelength. The total bulk profile is then given by the sum of all the different contributions for light travelling at different *θ*.

*D. Results*
Fig. shows the reflection (subdivided into direct and
 escape reflection), transmission, and absorption per layer in

the perovskite/SHJ structure. The implied photocurrents for the perovskite and c-Si, calculating by multiplying the absorp- tion in the relevant layer by the photon flux and integrating over wavelengths, are also shown. We can see that there is significant transmission into the c-Si at energies above the perovskite bandgap, which leads to the current in the top cell being limiting. Direct reflection is very low at all wavelengths, which is consistent with the low front surface reflection seen in Fig. 3a. However, there is significant escape reflection due to light incident from inside the cell escaping through the front surface at long wavelengths (where the perovskite is transparent); this is consistent with the high transmission seen for incidence angles below the critical angle in Fig. 3e. Similarly, at wavelengths near the c-Si bandgap there are clear transmission losses into the silver back surface. At short wavelengths, the front IZO and *C₆₀* layers also absorb a significant amount of light, further reducing the current in the perovskite junction.

Fig. 6 shows the absorption profiles within the front surface

layers at three different wavelengths over a ray-tracing unit cell calculated using the TMM/ray-tracing method. At 300 nm, we clearly see the parasitic absorption in the IZO, and very sharp absorption profiles in the C₆₀ and perovskite; almost all the incident photons are absorbed within the first *≈* 100 nm of perovskite. At 540 nm, there is much less parasitic absorption in the IZO and C₆₀, and the absorption profile in the perovskite is much less sharp, with photons still being absorbed towards the back of the layer. Finally, at 1200 nm, the perovskite is transparent, but we see some absorption in the thin a-Si layes and the C₆₀.

*E. Investigating different structures*
Fig. 8 shows the absorption in the bulk c-Si for the structure
 discussed in the previous section, the same structure with a perfect planar mirror (100 % reflection at all wavelengths) behind the c-Si instead of a pyramidal texture, and the structure with pyramids on both sides but the c-Si thickness increased by 100 *μ*mto360*μ*m. Since the redistribution

|[1] N. Tucher, J. Eisenlohr, P. Kiefel, O. Hohn,|||¨ H. Hauser, M. Peters,|||
|---|---|---|---|---|---|
|C. Muller, ¨|J. C. Goldschmidt, and B. Blasi,||¨ “3D optical simulation|||
|formalism|OPTOS for|textured silicon|solar cells,”|Optics Express,||
|vol. 23, //www.osapublishing.org/abstract.cfm?URI=oe-23-24-A1720|no. 24, p.|A1720, 2015.|[Online].|Available:|https:|
|[2] J. Eisenlohr, N. Tucher, O. Hohn,||¨ H. Hauser, M. Peters, P. Kiefel,||||
|J. C. Goldschmidt, propagation and absorption in thick textured optical sheets,” Optics|and|B. Blasi, ¨|“Matrix formalism|for|light|
|Express, [https://www.osapublishing.org/abstract.cfm?URI=oe-23-11-A502|vol](https://www.osapublishing.org/abstract.cfm?URI=oe-23-11-A502|vol). 23, no.|11, p. A502,|2015. [Online].|Available:||
|[3] R.|Meguro, Optical|T. Suezaki,|G.for Koizumi,|K. Yamamoto,||
|andSantbergen, M. Zeman, T.“GenPro4||Model|Solar Cell Simulation|||
|and Its|Application to|Multijunction|Solar Cells,”|IEEE Journal||
|of Photovoltaics, Available: [http://ieeexplore.ieee.org/document/7866819/|vol](http://ieeexplore.ieee.org/document/7866819/|vol). 7,|no. 3, pp.|919–926, may|2017. [Online].||
|[4] D. Alonso-Alvarez,|´ T. Wilson, P. Pearce, M. Fuhrer,||¨|D. Farrell, and||
|N. Ekins-Daukes, modelling solar cells and semiconductor materials,” Journal of Compu- tational Electronics, vol. 17, no. 3, pp. 1099–1123, sep 2018. [Online]. Available: [http://link.springer.com/10.1007/s10825-018-1171-3|“Solcore:|a](http://link.springer.com/10.1007/s10825-018-1171-3|“Solcore:|a) multi-scale,|Python-based|library|for|
|[5] V. Liu|and S. Fan,|“S4: A free|electromagnetic|solver|for|
|layered|periodic structures,”|Computer|Physics|Communications,||
|vol. 183, [http://dx.doi.org/10.1016/j.cpc.2012.04.026|no](http://dx.doi.org/10.1016/j.cpc.2012.04.026|no). 10, pp.|2233–2244,|2012. [Online].|Available:||
 matrices for a perfect mirror are trivial (matrix *R* is the identity matrix, all entries of *T* and *A* are zero) This shows that a perfect planar mirror performs slightly worse than the textured back surface, meaning the additional scattering from the pyramidal surface outweighs non-perfect reflection. As expected, increasing the c-Si thickness while not changing the surface textures increases absorption near the band edge.
V. CONCLUSIONS & OUTLOOK
RayFlare, a new optical modelling package for Python, has been introduced, outlining the underlying methods and illustrating how it can be used to investigate a perovskite/Si tandem cell. This demonstrates the power and flexibility of the approach, and the value of an integrated model com- bining existing matrix frameworks with methods for calcu- lating redistribution matrices such as TMM, ray-tracing and RCWA. RayFlare is available in full on GitHub: github.com/ qpv-research-group/rayflare.

Fig. 8. Comparison of the absorption in the bulk Si layer for three different

cases: a perfect back mirror with 100% reflectivity at all wavelengths, the textured back surface as considered in Figures 5 and 6, and the same textured back surface with the thickness of the bulk Si increased by 100 *μ*mto360*μm*

The matrix multiplication has been implemented so that it is straightforward to stack multiple bulk layers with a front and back matrix on top of one another; the transmission through the top structure can be used as input to the next bulk section and vice versa. This can be useful if multiple thick layers are present in a structure. Further improvements will mainly focus on speed, user- friendliness and thorough documentation of the code.

ACKNOWLEDGEMENTS

P. Pearce would like to acknowledge EPSRC CASE spon-
sorship from IQE plc. NJED gratefully acknowledges support from a Royal Society Industry Fellowship. We are grateful to Diego Alonso Alvarez ´ for useful discussions regarding Python.

REFERENCES [1] N. Tucher, J. Eisenlohr, P. Kiefel, O. Hohn, ¨ H. Hauser, M. Peters,

[6] S. J. Byrnes, “Multilayer optical calculations,” pp. 1–20, mar 2016. [Online]. Available: [http://arxiv.org/abs/1603.02720](http://arxiv.org/abs/1603.02720) [7] J. Werner, G. Nogay, F. Sahli, T. C. J. Yang, M. Brauninger, G. Christ-¨ mann, A. Walter, B. A. Kamino, P. Fiala, P. Loper, ¨ S. Nicolay,

Q. Jeangros, B. Niesen, and C. Ballif, “Complex Refractive Indices of Cesium-Formamidinium-Based Mixed-Halide Perovskites with Optical Band Gaps from 1.5 to 1.8 eV,” *ACS Energy Letters*, vol. 3, no. 3, pp. 742–747, 2018.
[8] F. Sahli, J. Werner, B. A. Kamino, M. Brauninger, ¨ R. Monnard,

B. Paviet-Salomon, L. Barraud, L. Ding, J. J. Diaz Leon, D. Sacchetto,
G. Cattaneo, M. Despeisse, M. Boccard, S. Nicolay, Q. Jeangros,
B. Niesen, and C. Ballif, “Fully textured monolithic perovskite/silicon tandem solar cells with 25.2% power conversion efficiency,” *Nature* *Materials*, vol. 17, no. 9, pp. 820–826, 2018. [Online]. Available: [http://dx.doi.org/10.1038/s41563-018-0115-4](http://dx.doi.org/10.1038/s41563-018-0115-4)
[9] L. V. Rodr´ıguez-de Marcos, J. I. Larruquert, J. A. Mendez, and J. A. ´ Aznarez, “Self-consistent optical constants of MgF2, LaF3, and CeF3 ´ films,” *Optical Materials Express*, vol. 7, no. 3, p. 989, mar 2017. [Online]. Available: [https://www.osapublishing.org/abstract.cfm?URI=](https://www.osapublishing.org/abstract.cfm?URI=) ome-7-3-989 [10] M. Morales-Masis, S. Martin De Nicolas, J. Holovsky, S. De Wolf, and C. Ballif, “Low-Temperature High-Mobility Amorphous IZO for Silicon Heterojunction Solar Cells,” *IEEE Journal of Photovoltaics*, vol. 5, no. 5, pp. 1340–1347, 2015. [11] S. L. Ren, Y. Wang, A. M. Rao, E. McRae, J. M. Holden, T. Hager,

K. A. Wang, W. T. Lee, H. F. Ni, J. Selegue, and P. C. Eklund, “Ellipsometric determination of the optical constants of C 60 (Buck- minsterfullerene) films,” *Applied Physics Letters*, vol. 59, no. 21, pp. 2678–2680, 1991.
[12] Y. Jiang, S. Pillai, and M. A. Green, “Realistic Silver Optical Constants for Plasmonics,” *Scientific Reports*, vol. 6, no. 1, p. 30605,

2016. [Online]. Available: [http://www.nature.com/articles/srep30605](http://www.nature.com/articles/srep30605)
