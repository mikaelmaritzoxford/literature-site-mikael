PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS Prog. Photovolt: Res. Appl. 2003; 11:333–340 (DOI: 10.1002/pip.496)

### ResearchGeneral Temperature

## Dependence of Solar Cell Performance and Implications

## for Device Modelling

Martin A. Green* ,y Centre of Excellence for Advanced Silicon Photovoltaics and Photonics, University of New South Wales, Sydney 2052, Australia

Solar cell performance generally decreases with increasing temperature, fundamen- tally owing to increased internal carrier recombination rates, caused by increased carrier concentrations. The temperature dependence of a general solar cell is inves- tigated on the basis of internal device physics, producing general results for the tem- perature dependence of open-circuit voltage and short-circuit current, as well as recommendations for generic modelling. Copyright # 2003 John Wiley & Sons, Ltd.

### RECOMBINATION IN SOLAR CELLS

he main temperature dependence in solar cells arises from variation of the open-circuit voltage with temperature. This voltage results from a balance between the overall recombination rate of carriers

# Tin the cell and the photogeneration rate.

Recombination in the cell generally occurs by three main processes: through defect levels, by Auger processes, or radiatively. 1,2 Defect recombination generally is well described by the Shockley–Read–Hall formula: 2,3

U ¼ np= tpoðn þ n₁Þþtnoðp þ p₁Þ ð1Þ

where U is the total recombination rate per unit volume, n and p are electron and hole carrier concentrations, n₁ and p₁ are parameters determined by the energy level of the defect state, and tnoand tpoare effective lifetime parameters determined by the capture cross-section of the defect for electrons and holes, respectively. In doped regions of a cell, say an n-type region doped with NDdopants per unit volume, under low injection, Equation (1) reduces to:

#### U ¼ np= tpoðNDþ n₁Þþtnop₁ ð2Þ

* Correspondence to: M. A. Green, Centre of Excellence for Advanced Silicon Photovoltaics and Photonics, University of New South Wales, Sydney 2052, Australia. y E-mail: m.green@unsw.edu.au Contract/grant sponsors: Australian Government Federation Fellowship; Australian Research Council.
Received 17 January 2003 Copyright # 2003 John Wiley & Sons, Ltd. Revised 31 March 2003

1099159x, 2003, 5, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.496](https://onlinelibrary.wiley.com/doi/10.1002/pip.496) by <Shibboleth>-member@ox.ac.uk, Wiley Online Library on [24/11/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

334 M. A. GREEN

since p, the minority carrier concentration, is small. Hence, recombination is proportional to the np product. Under arbitrary injection level, space charge neutrality allow the solutions:

|~|qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi|.||
|---|---|---|---|
|n ¼ N|þ N þ 4np|2|ð3aÞ|
|~|qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi|.||
|p ¼ N|þ N þ 4np|2|ð3bÞ|

D D 2

D D 2

Substituting into Equation (1) shows that U again depends on the np product, approaching a square-root dependence as this product increases to large values. In junction depletion regions, differentiating the denominator of Equation (1) shows that the strongest recom- bination² occurs when:

qffiffiffiffiffiffiffiffiffiffiffiffiffiffipffiffiffi n ¼ tno=tponp ð4aÞ

qffiffiffiffiffiffiffiffiffiffiffiffiffiffipffiffiffi p ¼ tpo=tnonp ð4bÞ

Hence, the strongest recombination in the depletion region again depends on the np product, approaching a square-root dependence for defect levels near midgap, where both n₁ and p₁ are small. Auger recombination rates 1,2 are given by:

#### U ¼ npðCnnn þ CpppÞð 5Þ

Again, in quasi-neutral regions, Equation (3) shows that recombination depends on the np product, changing from a linear to a 3/2 power dependence as injection level increases. In junction depletion regions, Auger recombination rates dramatically reduce and can be neglected compared with bulk rates. Radiative recombina- tion rates are given by:

#### U ¼ Bnp ð6Þ

where B is the radiative recombination coefficient and so radiative recombination depends linearly on the np product in both bulk and depletion regions, in both low and high injection. This establishes the importance of the np product in determining recombination in the cell, regardless of recombination process. This product can be expressed generally as: 2,3

≥ 2<u>qðp nÞ</u> np ¼ nieexp ð7Þ kT

where nieis the effective intrinsic carrier concentration, T is device temperature, kT/q is the thermal voltage 1–3

and ðp nÞ is the separation between the electron and hole quasi-Fermi potentials. On open-circuit, this separation at the cell junction will equal the open-circuit voltage of the cell, if there are no internally circulating currents within the cell. Such effects can be incorporated as second-order in the following. From the np product in the junction region, not only can recombination in this region be calculated, but also throughout the device, in terms of diffusion lengths, surface recombination velocity and the like. 1–3 It follows that the junction np product is a key parameter in determining recombination throughout the device, and hence the open-circuit voltage and cell temperature dependence.

Copyright # 2003 John Wiley & Sons, Ltd. Prog. Photovolt: Res. Appl. 2003; 11:333–340

SOLAR CELL TEMPERATURE DEPENDENCE 335

### GENERAL FORMULATION

This suggests that the output current I of a solar cell can be formulated very generally as described below in terms of the np product at the junction or, more conveniently, in terms of a closely related function, ~, defined as:

#### ~ ¼ np expðEg=kT Þ=n²ieð8Þ

where Egis the bandgap appropriate to the recombination process of interest. In terms of the quasi-Fermi poten- tial separation at the junction or internal voltage V, this gives:

X N I¼ILðV; TÞ AiðV ÞT g i f i ð~iÞð 9Þ i¼1

where ILrepresents the sum of the light and much smaller thermally generated current collected by the cell, and the second term represents the recombination current from N different sources, for generality. Each of the latter components depends primarily on the junction np product, as previously discussed or equivalently, the para- meter ~, through the appropriate function f (this can be a general function, but is a simple linear or square-root function in the limiting cases previously noted). In the general case, there will usually be second-order additional dependencies on temperature and voltage. These second-order dependencies will arise from such effects as temperature and voltage dependencies of other semiconductor parameters, such as diffusion lengths and surface recombination velocities or voltage dependen- cies, such as changing depletion region widths or fields or injection-level-dependent parametric values. As well as through the general V and T dependence of IL, such dependencies are accommodated in Equation (9) by assuming their effect can be modelled for each recombination current component as the product of a general voltage-dependent term AiðV Þ and a power of the temperature. Given the second-order nature of these pro- cesses, this modelling should be sufficiently flexible to describe a range of possible processes over the generally small temperature ranges of practical interest.

### OPEN-CIRCUIT VOLTAGE

At open-circuit I ¼ 0, and the light plus thermally generated currents and recombination currents balance. In this case, ~isimplifies to:

~ i¼ exp ðqVocEgiÞ=kT ð10Þ

where Egiis the bandgap appropriate to the given recombination component. Equating the currents and differentiating gives:

|@I dV|X dA dV|||
|---|---|---|---|
|L oc|i|oc g i|g i i i|
||i¼1 g i i|oc i|gi 2|
||i|||

@IL L oc N i oc gigi 1 þ ¼ T fiþ g Ai iT fi @T @V dT dV dT ≥ i df qðV E =qÞ q dVoc1 dEgi þ A T ~ þ ð11Þ d~ kT kT dT kT dT

Defining:

i

|x A T|~ ðdf =d~ Þ||
|---|---|---|
|N i¼1 i i g|i i i||
|N i¼1 i g|i i i|Prog. Photovolt: Res. Appl. 2003; 11:333–340|

< x > ¼ ð12Þ A Ti~ ðdf =d~ Þ

Copyright # 2003 John Wiley & Sons, Ltd.

as the weighted value of the parameter of interest gives:

~ < Ego > kT gf d~ kT dILf d~ Voc þ < > < > <u>dVoc</u>q q ~ df qILdT ~ df ¼ ~ ð13Þ dT kT 1 dA f d~ kT @ILf d~ T 1 þ < > < > q A dV ~ df qIL@V ~ d f

where Egoi¼ EgiT ðdEgi=dT Þð 14Þ

is the bandgap relevant to the recombination process of interest, extrapolated linearly from the temperature of interest to 0 K. From what follows, it can be shown that the weighting involved in Equation (12) is weighting by the con- tribution of the individual recombination processes to the total at open-circuit, when each contribution is divided by its associated ideality factor (actually, the ‘raw’ ideality factor, as discussed later). As discussed subsequently, the last term in the numerator and the last two terms of the denominator generally will be small. Neglecting such second-order terms, Equation (13) reduces to:

< Ego> kT f d~ <u>dVoc</u>q Vocþ q < g ~ df > ¼ ð15Þ dT T

Equation (15) is similar to an expression derived elsewhere under far more restricted conditions, but postulated to hold more generally [1]. Over a limited temperature range, it predicts an approximately linear temperature dependence of open-circuit voltage with temperature with a 0 K intercept equal to < Ego>=q þðkTav=qÞ < g ðf =~Þ d~=df >, where Tavis the average temperature over the given range. Some insight into typical values of the second order parameters in Equation (13) can be obtained by consid- ering the ‘local ideality factor’ near open-circuit of a diode, as above. This is the value of ideality factor that allows an equation of the form: I L¼ IonexpðqVoc=nockT Þð 16Þ

to be satisfied, if ILis varied. The value of noccan be obtained from such ‘intensity–Voc’ or ‘suns–Voc’ plots as:

n oc¼ðqIL=kT Þ=ðdIL=dVocÞð 17Þ

Evaluating nocwith the earlier formulation gives: ~ f d~ kT 1 dA f d~ noc¼< > 1 þ < > ð18Þ ~ df q A dV ~ df

The numerator, appearing frequently in Equation (13), can be identified as the ‘raw’ value of the ideality factor (equal to unity for low-injection bulk recombination, to two for this recombination when defect mediated in high injection or for recombination in depletion regions, when the function f is the linear function or square- root function, respectively). The second term in the denominator describes the modification to the raw value due to the second-order effects of changing voltage, previously mentioned. In crystalline devices, the most pronounced of these voltage effects occur in junction depletion regions owing to reduction in field strength with increasing voltage. At low field strengths, this reduction increases recombi- nation by increasing the volume within the depletion region where carrier concentrations are close to the ideal value of Equation (4). This gives a positive (dA/dV) term and, as found by many authors, 4–6 reduces the asso- ciated value of the ideality factor by as much as 10% below its ‘raw’ value of 2. This term would have a similar impact on the temperature dependence of open-circuit voltage, if junction recombination were the dominant

contributor to recombination at open-circuit. At high field strengths, field enhanced recombination can be strong at low voltages, but is weakened as voltage increases. This gives negative (dA/dV), enhancing the ideality factor above 2, and similarly enhancing the voltage temperature dependence. The remaining ‘second-order’ terms in Equation (13) involve the light-generated current, IL. The term in the denominator can be expressed in terms of a shunt resistance defined as:

#### RSH¼1=ð@IL=@V Þð 19Þ

This term will be negligible, provided this shunt resistance is much higher than the cell incremental resistance (nockT/qIL), which would normally be the case. This term accommodates not only physical shunts, but effects such as decreased carrier collection in amorphous silicon solar cells, due to decreasing depletion layer fields with increasing bias. The third term in the numerator depends on the normalised temperature dependence of IL, and will be negligible in magnitude compared with the second. Equation (15) is therefore expected to be quite accurate for all solar cells, regardless of the recombination process involved. To reduce temperature sensitivity, Vochas to be as high as possible. The limit is obtained when recombination in the cell is dominated by radiative recombination. In this case: 7,8

~ 3 2 <u>I</u> <u>L</u> <u>h c</u> Voc¼ Eg=q ðkT =qÞ ln 2 ð20Þ 2pqkTEG

Inserting numerical values for silicon² using the standard Global Air Mass 1 5 spectrum normalised to 100 mW/cm² intensity gives, at 300 K: "# ~ <u>43 0 Eg</u> 2 Eg=q Voc¼ 242 9mVþ 25 85 mV ln þ 25 85 mV lnð1=REQEÞð 21Þ I L11242

where ILis available current² in mA/cm² for photon energies above a threshold energy Eg, expressed in eV. The ideal value of this offset is 242 9 mV for material of a 300 K threshold equal to the silicon bandgap (1 1242 eV), decreasing slightly for smaller thresholds, but increasing for larger-threshold material. The final term in Equation (21) accommodates practical cases where only a fraction of the recombination is radiative, as discussed below. Combined with Equations (13) or (15), this shows that larger-bandgap material fundamentally has a larger absolute value of the voltage sensitivity. However, when normalised by the actual value of the voltage, the situa- tion reverses. This explains the often suggested lower temperature sensitivity of higher-bandgap cells. The other important factor is the quality of the cell, as characterised by its radiative external quantum effi- ciency (REQE). For Equation (21) to apply, this is defined rather carefully as the fraction of recombination within the cell represented by the re-emission of photons of energy higher than Eg. Internal radiative efficiency, defined as the fraction of primary recombination events that are radiative, will be appreciably higher. For the best silicon cells with Vocof 720 mV, the value deduced from Equation (21) for REQE is 0 2%, slightly lower than experimental EQE⁹ of about 0 6%, primarily due to the overriding impor- tance of sub-bandgap emission in actual silicon light emitters. Repeating this calculation for GaAs, using Eg¼ 1 424 eV and IL¼ 30 5 mA/cm², gives an ideal Vocof 264 mV below the bandgap compared with the experimental value of 1 022 eV for the record device, 9 corresponding to REQE of 0 48%. Values for other tech- nologies are likely to be appreciably lower, but will improve with improving device and materials technology. Temperature sensitivity of Vocwill decrease with these improvements, although values better than about 1 mV/ C are not feasible for high-performance devices for unconcentrated sunlight.

### SHORT-CIRCUIT CURRENT

The short-circuit current of a solar cell generally increases with increasing temperature, owing to decreasing band- gap and correspondingly increased band-to-band absorption coefficient across the spectrum. The actual current

output can be regarded as the product of the ideal current ILg, determined by the cell’s bandgap, and a collection fraction fCfor this current. The normalised temperature sensitivity of the short-circuit current then becomes:

|1 dI|dI dE 1|1 df|
|---|---|---|
|sc|Lg g|c|
|sc|Lg g|c|

¼ þ ð22Þ I dT I dE dT f dT

Both contributing terms are usually positive, although the second can be calculated only for specific materials and device designs. The first is independent of such issues, apart from the temperature sensitivity of the material’s bandgap. For Si and GaAs, respectively, using values for this parameter of 0 273 meV/ Cand 0 39 meV/ C gives values of normalised Iscsensitivity due to the first term of 167 and 550 ppm/ C, respectively. The higher value for the higher-bandgap material results from its photon response cut-off lying in a part of the spectrum where more photons are available, together with the higher sensitivity of the bandgap to temperature. The former is a general feature for bandgaps less than 2 eV, apart from the influence of absorption bands in the photon spec- trum. The higher temperature sensitivity of the bandgap for high bandgaps is not a general property, depending more on the mechanical properties of the lattice, such as its thermal expansion coefficient. Experimental values of short-circuit current sensitivity for silicon are generally much higher than these cal- culated values, while those for GaAs are only marginally higher. This suggests the importance of the increased absorptance of indirect gap material with increasing temperature, since cells made from such material struggle to absorb and collect the available carriers.

### FILL FACTOR

Fill factors depend on a range of cell parameters, including current and voltage operating levels, cell ideality factors and parasitic series and shunt resistances. Voltage dependence of ILcan further complicate fill factor dependencies. As such, it is difficult to derive generic formulae for the temperature sensitivity of this parameter. The present author has derived an accurate approximate formula for the specific case where neither the para- sitic series and shunt resistances vary strongly with temperature nor does the single ideality factor assumed to describe the device’s performance. In this case: 10

≥ 1 dFF 1 dVoc1 ’ð1 1 02FFoÞ ð23Þ FF dT VocdT T

to about 5% accuracy over a reasonable range of voltages, where FFois the ideal value of the fill factor, in the absence of series and shunt resistance effects. This ideal value is determined solely by Vocand the ideality fac- tor. The first bracketed term in Equation (23) tends to reduce the fill factor temperature sensitivity by a factor of about six, compared with that of the voltage, while the second term approximately doubles it, resulting in a final sensitivity about three times lower. Equation (23) describes the fill factor sensitivity of experimental silicon devices quite accurately. However, in less-developed technologies, such as amorphous silicon or nanocrystalline dye cells, cell performance often is measured to be relatively temperature insensitive. This is due to a fill factor that increases with increasing tem- perature, due to decreasing resistance effects or increasing ‘mobility-lifetime’ products within the collection region for amorphous silicon cells. These effects must significantly inhibit low-temperature performance for this beneficial effect to be large. The effect may be augmented in amorphous silicon by the annealing at high temperatures of light-induced degradation that affects primarily the fill factor.

### MODELLING IMPLICATIONS

Since, in reasonably well-developed technologies, the temperature sensitivity of the open-circuit voltage is responsible for 80–90% of the overall temperature sensitivity, it is important to model this variation correctly.

This becomes particularly important in studies that seek to optimise parameters such as device bandgaps by generic modelling over a wide temperature range. Modelling when unity ideality factor is involved generally assumes that low-injection bulk recombination is the dominant recombination process, which provides a link to the device physics. Difficulties can arise, however, when an attempt is made to model experimental devices more realistically, such as by including non-unity ideality factors. This tends to weaken links to the underlying physics, leading to possible systematic errors in modelling. For example, in a recent optimisation study of polycrystalline tandem cell designs, 11 the dark or recombina- tion currents of the cells were modelled by expressions of the form: ~ <u>qV</u> I R¼ Ionexp ð24Þ nkT

where a quite reasonable value of ideality factor of 1 5 was used to reflect the generally higher value of this factor in polycrystalline material. The parameter Ionwas chosen by fitting the open-circuit voltages predicted from Equation (24) to the best experimental polycrystalline devices over a range of different bandgaps at 25 C. In a two-stage process, this resulted in an expression for Ionof the form, previously suggested by Fan [12]: ~ g<u>Eg</u> I on¼ AT exp ð25Þ mkT

with g ¼ 3, where a value of m ¼ 2 was chosen as giving a reasonable fit to experimental data. While this pro- cedure seems quite reasonable, applying the previous analysis results in the expression: 12

~ <u>nEg gnkT</u> mq Vocþ q <u>dVoc</u> ¼ ð26Þ dT T

Comparing this with the simplified form of Equation (15), determined by very general device physics, Equa- tion (26) is in agreement with the most significant terms only if n/m is a little higher than unity. Selecting n/m equal to 0 75 will result in an unintended systematic underestimation of the temperature dependence of solar cell performance, particularly for cells made from large bandgap material. 11

As an example, for the highest bandgap CdTe devices studied, 11 Equation (26) predicts a normalised tem- perature sensitivity of open-circuit voltage of 1465 to 1543 ppm/ C compared with experimental values of 2400 to 3700 ppm/ C. 13–15 Even for the lower-bandgap silicon devices, temperature sensitivity is underes- timated unintentionally by at least a factor of two. Since temperature sensitivities were one of the issues studied in the earlier work, 11 this must weaken some of its conclusions. Comparing Equations (26) and (15), on the basis of physical principles, better agreement would be expected if m were chosen so that n/m ¼ E

|||/E, where E|is the value of E|linearly extrapolated from operating tem-|
|---|---|---|---|---|
|i 11||go g|go go|g g|

peratures to 0 K. For both Si and GaAs, E is 7–8% higher than E. Hence, if the underlying physics is taken into account, m should be constrained to have a value of close to n, say n/1 07. If only the temperature depen- dencies arising from n variation are taken into account, following the physics through¹² shows that g should be chosen as 3/n. In the previous work, these changes would correspond to fitting the experimental data in Figure 1 of Coutts et al. by a line of flatter slope. Using the suggested values, temperature coefficients of open-circuit voltage between 3170 and 3279 ppm/ C are calculated for the CdTe devices and 3912 to 4098 ppm/ C for the thin-film Si devices, in better agreement with experimental expectations. 13–16

### CONCLUSIONS

The temperature sensitivity of a general solar cell is discussed by reference to the underlying physics. The importance of the electron–hole product in determining recombination throughout the device regardless of

recombination process is established. This leads to a very general formulation of the temperature sensitivity of device open-circuit voltage, accounting for 80–90% of the temperature sensitivity in devices not unduly constrained by resistance or other fill factor losses. Surprisingly, absolute open-circuit voltage temperature sensitivities would be expected to increase with increasing bandgap, although normalised values should show the opposite trend. The normalised short-circuit current sensitivity arises from the general trend towards decreasing bandgap with increasing temperature, increasing the number of photons of usable energy. This is augmented by the ten- dency to increase of the fraction of suitable photons that actually contribute to cell output current, due mainly to stronger absorption, although improved values of other key parameters, such as diffusion lengths, could also help. The first contribution shows a general increase with increasing bandgap, for practical values of the latter, while the second seems to be strongest for the more weakly absorbing devices, such as bulk silicon cells and cells using thin amorphous silicon layers. In the absence of temperature-sensitive resistances or decreasing car- rier collection probabilities with increasing bias, the fill factor temperature sensitivity is determined by that of the open-circuit voltage, but normalised values are about three times weaker than those for this voltage. The importance of the electron–hole product in determining overall temperature sensitivity provides some constraints on appropriate expressions for modelling the performance of generic devices. Apparently sensible choices in this area can lead to errors in the modelled temperature sensitivities, and an unintentional systematic bias in the conclusions from modelling.

Acknowledgements

I thank the reviewers of this paper for suggestions that have improved its clarity. I also acknowledge the support of an Australian Government Federation Fellowship and the support of the Centre of Excellence for Advanced Silicon Photovoltaics and Photonics by the Australian Research Council.

### REFERENCES

1. Green MA. Solar Cells: Operating Principles, Technology and System Applications. Prentice-Hall: New Jersey, 1982. (reprinted version available from author)
2. Green MA. Silicon Solar Cells: Advanced Principles and Practice. Bridge Printery: Sydney, 1995. (available from author.)
3. Sze SM. Physics of Semiconductor Devices. Wiley: New York, 1981.
4. Sah CT, Noyce RN, Shockley W. Carrier generation and recombination in p–n junction and p–n junction characteristics. Proceedings of the IRE 1957; 45: 1228.
5. Nussbaum A. Physica Status Solidi (a) 1973; 19: 441.
6. McIntosh KR, Altermatt PP, Heiser G. Depletion-region recombination in silicon solar cells: when does mDR¼ 2?, Proceedings of the 16th EC PVSEC, Glasgow, 2000; 251–254.
7. Shockley W, Queisser HJ. Detailed balance limit of efficiency of p–n junction solar cells. Journal of Applied Physics 1961; 32: 510–519.
8. Green MA. Solar Cells. In Advanced Semiconductor Devices, Sze SM (ed.). Wiley: New York, 1998; 473–530.
9. Green MA, Zhao J, Wang A, Reece PJ, Gal M. Efficient silicon light emitting diodes. Nature 2001; 412: 805–808.
10. Green MA, Emery K, Blakers AW. Silicon solar cells with reduced temperature sensitivity. Electronics Letters 1982; 2: 97–98.
11. Coutts TJ, Emery KA, Ward JS. Modeled performance of polycrystalline thin-film tandem solar cells. Progress in Photovoltaics Research and Applications 2002; 10: 195–203.
12. Fan JCC. Theoretical temperature dependence of solar cell parameters. Solar Cells 1986; 17: 309–315.
13. Kropski B, Strand T, Hansen R, Powell R, Sasala R. Technical evaluation of Solar Cells, Inc. CdTe module and array at NREL. Conference Record 25th PVSC, 1996; 969–972.
14. King DL, Kratochvil JA, Boyson WE. Temperature coefficients for PV modules and arrays: measurement methods, difficulties and results. Proceedings of the 26th PVSC, Anaheim, September/October 1997; 1183.
15. King DL. Sandia Photovoltaic Module Database, 2002. www.Sandia.gov/pv/pvc.htm
16. Emery K, Burdick J, Caiyem Y, Dunlavy D, Field H, Kroposki B, Moriarty T, Ottoson L, Rummel S, Strand T, Wanlass MW. Temperature dependence of photovoltaic cells, modules and systems. Proceedings of the 25th PVSC, Anaheim, September/October 1996; 1275.
