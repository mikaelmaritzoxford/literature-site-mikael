**www.advmat.de www.MaterialsViews.com**

### COMMUNICATION

# Accounting for Interference, Scattering, and Electrode Absorption to Make Accurate Internal Quantum Effi ciency

# Measurements in Organic and Other Thin Solar Cells

## By George F. Burkhard, Eric T. Hoke, and

## Michael D. McGehee *

In solar cells, internal quantum effi ciency (IQE) is the ratio of the number of charge carriers extracted from the cell to the number of photons absorbed in the active layer. Because IQE measurements normalize the current generation effi ciency by the light absorp- tion effi ciency, they separate electronic properties from optical properties and provide useful information about the electrical properties of cells that external quantum effi ciency measurements alone cannot. The magnitude of the IQE is inversely related to the amount of recombination that is occurring in the cell, while the spectral shape of the curve can provide information about the effi ciency of harvesting excitons in the cell or spatial dependence of charge recombination. [1,2] Effects like multiple exciton gen- eration [3–5] and singlet exciton fi ssion [6] as well as bias-dependent photoconductivity [7] can lead to interesting spectral shapes and be detected by measuring IQEs greater than 100%. Despite its useful- ness as a characterization tool, IQE is rarely reported. When IQE is reported, absorption is frequently not measured in actual devices; this can lead to errors since refl ective electrodes induce strong interference effects that substantially affect absorption. When absorption is measured in actual devices, parasitic absorptions are almost never taken into account. We hope that by demonstrating a straightforward method of measuring IQE, it will become a standard measurement and the community may benefi t from a better understanding of how the best performing cells work. Organic photovoltaics (OPVs) and other ultra-thin solar cells [8–11] are made as a stack of materials including an active semicon- ducting layer, electrodes, and in some cases modifi er layers such as charge blocking layers and optical spacers. [12–15] The active layer is responsible for all charge generation in the cell. Typi- cally 5–10% of the incident light is absorbed in the electrodes. In many solar cells, the IQE should not vary with wavelength. Since parasitic absorption does vary with wavelength, one must account for it to observe the correct spectral shape. [1] Consequently in the general case, it is critically important to take this parasitic absorp- tion into account when calculating internal quantum effi ciency. Determining the active layer’s contribution to the total absorp- tion can be a challenge, as it generally requires optical modeling to relate the experimentally measurable total absorption to the absorption in each layer. The absorption of each layer cannot independently be measured because, due to interference effects, the optical density of the stack is not simply the sum of the optical

[*] G. F. Burkhard, E. T. Hoke, Prof. M. D. McGehee Department of Materials Science and Engineering 476 Lomita Mall, Stanford, CA, 94305 (USA) E-mail: mmcgehee@stanford.edu

##### DOI: 10.1002/adma.201000883

*Adv. Mater.*,, 3293–3297

densities of each layer. The most accurate commonly used model uses a transfer matrix formalism to calculate the interference of coherent refl ected and transmitted waves at each interface in the stack. [16,17] This calculation requires knowledge of the wavelength- dependent complex index of refraction of each material. The imaginary part, *k*, is related to the extinction coeffi cient and is responsible for absorption in a medium. The real part, *n*, deter- mines the wavelength of light of a given energy *in a material* and is important for calculating where areas of constructive and destruc- tive interference occur. Typically the optical constants are meas- ured using variable angle spectroscopic ellipsometry (VASE). [18–22] The data produced by this technique when measuring anisotropic organic materials are diffi cult to interpret and require compli- cated modeling not available to many research groups. In blended donor-acceptor fi lms, the optical properties depend strongly on morphology and therefore on processing conditions. Thus fi lms of different thicknesses, cast from different solvents, or dried for different amounts of time have different optical constants. [23,24] In such composite materials, morphology is also a function of depth due to vertical phase segregation. [24,25] In these cases the optical constants are spatially dependent and the data gathered by these methods are approximations themselves. It is not always fea- sible to use VASE to measure *n* and *k* for each fi lm, so a simpler method of determining active layer absorption is desirable. In this article we show that for typical OPVs, precise knowl- edge of the real part of the complex index of refraction of the active layer is not required for making the measurements of the active layer absorption necessary for calculating IQE. We have investigated several methods to calculate the active layer absorption using published values of the optical constants. [18–22] We propose a method that minimizes error by using an optical model to calculate the parasitic absorption (the absorption by the layers that do not contribute to photocurrent) and subtracting this from the experimentally measured total absorption. The transfer matrix method can be used to model active layer absorption, accounting for optical interference effects as well as parasitic absorption. This method calculates the refl ection and transmission at each interface as well as attenuation in each layer. [16,17]

**Figure 1a** shows the absorption in each layer as well

as the total absorption for a typical poly-3-hexylthiophene:[6,6]- phenyl-C61 -butyric acid methyl ester (P3HT:PCBM) cell as calcu- lated by this method. The optical model is limited in accuracy, however, in that it does not account for diffuse scattering and the spatially-dependent optical constants of the blend layer. The error associated with these approximations can be observed by comparing the total device absorption predicted by the model to the experimentally measured absorption spectrum (Figure 1b ); substantial differences exist at all device thicknesses.

© 2010 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

1.0
##### Parasitic Abs.

0.9 Active Abs.
##### Total Abs.

0.8
0.7
0.6
0.5
Absorption0.4

### COMMUNICATION0.3

0.2
0.1
0.0 300 400 500 600 700 800
##### Wavelength (nm)

**(b)**
**(a)**
**Figure 1. a)** Parasitic absorption, active layer absorption, and total absorption of a typical P3HT:PCBM cell (220 nm thick active layer) as calculated

by the transfer matrix optical model. **b)** Total absorptions for cells of varying thickness as calculated by the transfer matrix method compared with experimentally measured values.

The most accurate method of isolating active layer absorption we have investigated uses the transfer matrix optical model to calculate the absorptions in the various layers in the stack but only makes use of the solutions for the absorptions in the elec- trodes. Rather than using the model to predict the absorption in the active layer, we make use of the experimentally measured total absorption, which consists mainly of active layer absorp- tion. From this, we subtract the parasitic absorptions calcu- lated by the model. Because the experimentally measured total absorption is highly accurate, errors in the resulting active layer absorption are only as small as the errors in the parasitic absorp- tions. For example, even if the error in the parasitic absorption were as high as 10%, in a typical cell where the total parasitic absorption comprises 10% of the total absorption at most wave- lengths, the error in the active layer absorption would only be 1%. Typical errors are smaller than this, as we show below, so the method is generally very accurate. This robustness provides some added fl exibility in that we can loosen the requirements on the accuracy of the optical constants of the blend, which are notoriously diffi cult to measure. In fact we can make reasonable predictions of active layer absorption by estimating *n* and meas- uring *k* for the blend. **Figure 2** shows the active layer absorption using values of *n* determined by VASE as well as the absorption calculated using a constant value of *n* = 2. Both curves were gen- erated using the method that combines the modeled parasitic absorption with the experimentally measured total absorption. The absorption spectrum calculated using the approximation that *n* = 2 is in close agreement with the spectrum generated using the more accurate values of *n* measured by VASE. There is less than 1% discrepancy at wavelengths where the active layer absorbs strongly, which are the wavelengths of interest for IQE measurements. The values of the optical constants for the electrode layers are easily found in the literature, [18–22] so this means that one can produce very good IQE spectra without having to resort to any special methods of measuring *n* in the active layer.

Because our method of calculating active layer absorption allows us to estimate the real part of the index of refraction of the active layer, the only optical constant we need to measure is the imaginary part, *k*. The imaginary part of the index of refrac- tion is related to the absorption coeffi cient by

<u>8a</u> *k* = (1) 4B

where λ is the wavelength of light and α the absorption coef- fi cient. α can be determined from measurements of the trans- mission or optical density (OD) of a fi lm and its thickness,

**Figure 2 .** Active layer absorption for optimized P3HT:PCBM solar cell

calculated using the method we propose with values of n and k as meas- ured by VASE for the active layer as well as values assuming *n* = 2 at all wavelengths.

### COMMUNICATION

which can be measured using profi lometry. α is related to the optical density and the transmitted intensity by,

##### <u>(OD) In (10)</u>

" = (2) *x*

*I*−"*x* = *e* (3) *I₀*

where *I* / *I₀* is the fraction of light that remains after passing through the fi lm and *x* is the fi lm thickness. Equation ( 2 ) is useful for many off the shelf absorption spectrometers that output optical density. Equation ( 3 ) is more appropriate in con- fi gurations that output transmission such as the one used in this work. To be clear, Equation ( 3 ) describes the decay of the inten- sity of a wave as it passes through an absorbing fi lm. It does not represent the total position-dependent intensity in a device under solar illumination, which includes interference with waves transmitted and refl ected at each interface in the device. Because this equation does not describe refl ection at the inter- faces, it does not take coupling effi ciency into account. Thus it is important to take into account the refl ection/transmission at the air/substrate (glass) interface using the Fresnel equations. Without knowing, *a priori*, the value of the real part of the index of refraction of the fi lm, it is impossible to know exactly how much light is coupled into the fi lm and how much is refl ected at the fi lm-substrate interface. However, refl ection at this interface is small (approximately 2%) so it can be estimated by assuming *n* = 2 (for organics) without much loss of accuracy. We measure the total absorption using a refl ection-mode measurement inside of an integrating sphere. The use of the integrating sphere greatly enhances the accuracy of the measure- ment since a signifi cant amount of light is diffusely refl ected or scattered into waveguide modes in the glass substrate. **Figure 3** shows an absorption measurement taken with the sample inside of an integrating sphere in contrast to a more traditional refl ec- tion measurement where only the spectral refl ection is measured. The strongly scattered light escapes the device in all directions and is captured by the integrating sphere. In other refl ection mode confi gurations this light would be lost and would mistak- enly be attributed to absorption by the device. This is especially important for the short wavelengths where Rayleigh scattering is more effi cient so an error in absorption at these wavelengths can signifi cantly affect the shape of the IQE curve. While the integrating sphere is not necessary for wavelengths where the cell absorbs strongly, it is necessary to obtain the correct spectral shape across the whole absorption spectrum. The integrating sphere is quite easy to use for this type of measurement since all that is required is to compare the intensity of light in the sphere with and without the sample present. The scattering effi ciency of the sphere does not need to be characterized since it is a factor present in both measurements and is accounted for when the two intensities are divided. It is important for the sample to be much smaller than the sphere itself so that it does not present a large area for secondary absorption of light.

**Figure 4** shows an IQE curve generated for a P3HT:PCBM cell

using the method we describe. The external quantum effi ciency was measured using standard techniques. We only show IQE for wavelengths where the active layer absorbs; the calculated IQE values are less accurate for absorption below the bandgap since

**Figure 3 .** Absorption in a complete P3HT:PCBM cell as measured using a

traditional refl ection-mode absorption measurement where only specular refl ection is detected and the same measurement made using an inte- grating sphere.

the active layer absorption is close to zero and this term appears in the denominator. For practical purposes, the IQE is only rele- vant at wavelengths where the active layer absorbs signifi cantly. We have shown that in this system, the IQE spectrum is not fl at because of differences in the effi ciencies at which P3HT and PCBM excitons are harvested, however in systems where har- vesting is equally effi cient in both materials, this method pro- duces fl at IQE curves as expected. [1] These observations would not have been possible without taking parasitic absorptions into account using the method we propose.

**Figure 4 .** Internal quantum effi ciency of optimized (220 nm thick active

layer) P3HT:PCBM solar cell calculated using the method we describe to generate active layer absorption spectrum. The IQE values below the absorption onset ( > 650 nm) are less accurate because the assumption that the active layer is responsible for a majority of the absorption is no longer true (see Figure 1a ).

|www.advmat.de|1.0 0.9 0.8 0.7 0.6 n 0.5 ptio r 0.4 so b A 0.3 0.2 0.1 0.0 -0.1|
|---|---|
||3 300 (a) Total and active layer absorption of a P3HT:PCBM solar cell optimized to 220 nm active layer thickness. of a P3HT:PCBM solar cell with a 45 nm active layer. There are many instances in the literature where absorp- tion by the electrodes is ignored under the assumption that the absorption in the electrodes is insignifi cant compared to that of the active layer. To illustrate how important it is to subtract the electrode absorption, we compare the active layer absorp- tion of a typical P3HT:PCBM cell as determined by the method we propose to the measured total absorption (Figure 5a). Not only is the active layer absorption signifi cantly smaller than the total absorption but the shape is moderately different. This data is for a cell with a strongly absorbing, 220 nm thick active layer. For thinner active layers, the difference in shape is even more dramatic (Figure 5b) since more light is available to be absorbed by the electrodes in devices with weakly absorbing Intensity in device Intensity in film (2 passes)|

##### Active Layer

##### To t a l

### COMMUNICATION

400 500 600 700 800 Wavelength (nm)

(b)
**Figure 5. a) b)** Total and active layer absorption

A strategy often used when reporting IQE in the literature is to measure the absorption of the active layer alone on a glass sub- strate in transmission mode. The optical density is then doubled to take into account two optical passes caused by the refl ective metal electrode. Although this is very convenient in that it allows one to use an off-the-shelf spectrometer in transmission mode, it does not take into account interference effects, most importantly the area of low electromagnetic fi eld intensity close to the metal electrode where absorption is necessarily weak. It also ignores parasitic absorption, albeit in a different way than results from attributing 100% of the total absorption to the active layer; rather than counting parasitic absorption toward the active layer absorp- tion, it treats the electrodes as if they are lossless in that the active active layers. layer sees the full solar spectrum. **Figure 6a** shows the intensity

0.7
0.6
0.5
0.4
0.3
Intensity (I/I0)

0.2
0.1
0.0 0 50 100 150 200 250
Position in active layer (nm)

(a) (b)
**Figure 6. a)** Electric fi eld intensity for 450 nm monochromatic light vs. position in a real device and as calculated by measuring absorption in a fi lm

and doubling the optical density. **b)** Absorption spectrum of the active layer in a real device and as calculated by measuring absorption in a fi lm and doubling the optical density.

© 2010 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim *Adv. Mater.*,, 3293–3297

### COMMUNICATION

#### Acknowledgements

This work was supported by the Center for Advanced Molecular Photovoltaics (Award No KUSC1-015-21), made by King Abdullah University of Science and Technology (KAUST) E.T.H. is supported by the National Science Foundation GRFP and the Fannie and John Hertz Foundation.

Received: March 11, 2010 Published online: May 31, 2010

of 450 nm light in a device confi guration as well as in a fi lm con- fi guration when the optical density is doubled. Both interference and parasitic absorption occur in the device but not in the fi lm. Because of this, the shape of the absorption spectrum calculated by doubling the optical density of a fi lm can differ signifi cantly from the absorption spectrum in the active layer of a real device. This effect becomes more pronounced in thinner fi lms where interference effects are even more important. Figure 6b shows the absorption spectrum calculated by doubling the optical den- sity of a fi lm vs. the true active layer absorption. Internal quantum effi ciency provides detailed information about the electronic properties in solar cells including insight into things like recombination and morphology-dependent properties. We have described a method to easily measure internal quantum effi ciency that takes into account parasitic absorptions in the electrodes and/or other non-active layers in the stack. Our method is relatively insensitive to modeling error, allowing some of the optical constants used in the model to be relatively imprecise; an educated guess is suffi cient in most cases. Since this method eliminates the need for precise measurements of the active layer’s complex index of refraction using a time consuming technique, we hope that more OPV publications will include measurements of internal quantum effi ciency. This method will also be useful for all-nanocrystal solar cells and other thin fi lm technologies. A program that uses the transfer-matrix formalism to calcu- late absorption in stacks of materials is available as a Matlab script and can be downloaded free of charge at [http://mcgehee](http://mcgehee). group.stanford.edu/transfermatrix.

[ 1] G. F. Burkhard, E. T. Hoke, M. D. McGehee, *Nano Lett.***2009**, *9*, 4037. [ 2] J. A. Mikroyannidis, M. M. Stylianakis, P. Suresh, P. Balraju, G. D. Sharma, *Organic Electronics* **2009**, *10*, 1320. [ 3] R. J. Ellingson, M. C. Beard, J. C. Johnson, P. R. Yu, O. I. Micic, A. J. Nozik, A. Shabaev, A. L. Efros, *Nano Lett.***2005**, *5*, 865. [ 4] R. D. Schaller, V. I. Klimov, *Phys. Rev. Lett.***2004**, *92*, 186601. [ 5] A. J. Nozik, *Physica E* **2002**, *14*, 115. [ 6] I. Paci, J. C. Johnson, X. Chen, G. Rana, D. Popovic, D. E. David,

A. J. Nozik, M. A. Ratner, J. Michl, *J. Am. Chem. Soc.* **2006**, *128*, 16546.
[ 7] H.-Y. Chen, M. K. F. Lo, G. Yang, H. G. Monbouquette, Y. Yang, *Nat.* *Nanotechnol.***2008**, *3*, 543. [ 8] I. Gur, N. A. Fromer, M. L. Geier, A. P. Alivisatos, *Science* **2005**, *310*, 462. [ 9] A. J. Nozik, *Physica E: Low-dimensional Systems and Nanostructures* **2002**, *14*, 115. [ 10] B. A. Gregg, M. C. Hanna, *J. Appl. Phys.***2003**, *93*, 3605. [ 11] A. Maria, P. W. Cyr, E. J. D. Klem, L. Levina, E. H. Sargent, *Appl.* *Phys. Lett.***2005**, *87*, 213112. [ 12] J. Y. Kim, S. H. Kim, H. H. Lee, K. Lee, W. L. Ma, X. Gong, A. J. Heeger, *Adv. Mater.***2006**, *18*, 572. [ 13] A. W. Hains, C. Ramanan, M. D. Irwin, J. Liu, M. R. Wasielewski, T. J. Marks, *ACS Applied Materials & Interfaces* **2009**, *2*, 175. [ 14] J. Gilot, I. Barbu, M. M. Wienk, R. A. J. Janssen, *Appl. Phys. Lett.* **2007**, *91*, 113520. [ 15] B. Kang, L. W. Tan, S. R. P. Silva, *Appl. Phys. Lett.* **2008**, *93*, 133302. [ 16] L. A. A. Pettersson, L. S. Roman, O. Inganas, *J. Appl. Phys.* **1999**, *86*, 487. [ 17] P. Peumans, A. Yakimov, S. Forrest, *J. of Appl. Phys.***2003**, *93*, 3693. [ 18] J. D. Kotlarski, P. W. M. Blom, L. J. A. Koster, M. Lenes, L. H. Slooff,

*J. Appl. Phys.***2008**, *103*.
[ 19] L. Emmanouil, O. Andreas, A. Ioannis, H. Yasuhiko, *J. Appl. Phys.* **2007**, *102*, 083104. [ 20] A. B. Djurisic, C. Y. Kwong, T. W. Lau, Z. T. Liu, H. S. Kwok, L. S. M. Lam, W. K. Chan, *Appl. Opt.***2003**, *42*, 6382. [ 21] S. Yoo, W. J. Potscavage Jr, B. Domercq, S.-H. Han, T.-D. Li, S. C. Jones, R. Szoszkiewicz, D. Levi, E. Riedo, S. R. Marder, B. Kippelen, *Solid-State Electron.***2007**, *51*, 1367. [ 22] A. M. C. Ng, K. Y. Cheung, M. K. Fung, A. B. Djurisic, W. K. Chan, *Thin Solid Films* **2008**, *517*, 1047. [ 23] A. J. Moulé, K. Meerholz, *Adv. Mater.***2008**, *20*, 240. [ 24] M. Campoy-Quiles, T. Ferenczi, T. Agostinelli, P. G. Etchegoin, Y. Kim, T. D. Anthopoulos, P. N. Stavrinou, D. D. C. Bradley, J. Nelson, *Nat. Mater.***2008**, *7*, 158. [ 25] D. S. Germack, C. K. Chan, B. H. Hamadani, L. J. Richter, D. A. Fischer, D. J. Gundlach, D. M. DeLongchamp, *Appl. Phys. Lett.***2009**, *94*, 233303.

#### Experimental Section

P3HT:PCBM devices were made with the structure indium tin oxide ITO/ PEDOT:PSS/P3HT:PCBM/Ca/Al with the following thicknesses (in nm): 110/35/220/7/200. ITO substrates were purchased from Sorizon Technologies; PEDOT:PSS from Baytron; P3HT from Rieke; PCBM from NanoC; and metals from K. J. Lesker. Substrates were cleaned in an ultrasonic bath with Extran 300, rinsed in deionized water and then cleaned in acetone and isopropanol followed by 20 minutes of UV-ozone treatment. PEDOT:PSS was spin-coated and the substrates were annealed at 140 ° C for 10 minutes. They were then transferred to a nitrogen glovebox, where they remained for the duration of the fabrication process as well as for all characterizations performed. P3HT:PCBM (1:1 w/w, 25 mg/mL each) was cast from 1,2-dichlorobenzene and were allowed to slow-dry overnight. They were then thermally annealed at 110 ° C for 10 minutes. Calcium and aluminum metal electrodes were deposited in a thermal evaporator. All devices had power conversion effi ciencies greater than 4%. EQE was taken at short circuit using monochromated white light from a tungsten lamp. The white light was split with half incident on a reference silicon photodiode and the other half incident on the device being tested. The photocurrent responses of both devices were measured simultaneously as a function of wavelength. This simultaneous measurement accounts for fl uctuations in lamp intensity or changes in optics over time. EQE was calculated by comparing the photocurrent action spectrum of the device to that of a NIST traceable calibration photodiode.
