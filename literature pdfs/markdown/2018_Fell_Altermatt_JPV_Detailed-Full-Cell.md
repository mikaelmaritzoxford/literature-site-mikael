IEEE JOURNAL OF PHOTOVOLTAICS, VOL. 8, NO. 6, NOVEMBER 2018

## A Detailed Full-Cell Model of a 2018 Commercial PERC Solar Cell in Quokka3

### Andreas Fell

### and Pietro P. Altermatt

***Abstract*—An unprecedented detailed model of a full-size pas- sivated emitter and rear cell (PERC) solar cell design, as manu-**

**factured at a current Trina Solar production-line during ramp-up, is presented. Combining a newly proposed multidomain approach**

**with the multiscale skin-concept of Quokka3, the 15.6 cm*×*15.6 cm three-dimensional cell geometry including the details of the emit-**

**ter skins can thoroughly be solved within a single simulation. The** **multidomain approach uses an inner and two edge domains as irre- ducible symmetry elements, each containing the unequal front and**

**rear pitch, the dashed rear contacts, as well as part of the busbars** **and consequently the full finger resistance. The full-cell current density is then determined by simple area-averaging, opposed to**

**the more complicated common approach of coupling it with a dis- tributed network model. The multiscale skin approach enables to**

**model all emitter parts of the PERC cell in detail (accounting for dopant profiles, front surface recombination, Fermi–Dirac statis-**

**tics, etc.), whereas the other skin regions can still be described by** **their lumped properties, i.e., *R*sheetand *J₀*/*S*eff. A complete set of carefully established electrical and optical input parameters as**

**well as a detailed loss breakdown is presented, providing fellow re-** **searchers with a point of reference for modeling a state-of-the-art** **PERC solar cell in 2018.**

***Index Terms*—Full-cell, modeling, PERC, Quokka, silicon, simulation, solar cell.**

I. INTRODUCTION
HE ultimate way to simulate a silicon solar cell would be

# Tto solve the well-established semiconductor differential

equations for the full-size three-dimensional (3-D) geometry. However, this would presently require a computer cluster and many hours [1]. Therefore, the common approach to model solar cells is to solve the semiconductor differential equations within a small “unit cell” domain. Large-scale effects, such as metal grid resistance, busbar shading, and edge recombination, are not covered in such a domain. The most accurate approximation to include full-size effects has been to connect such unit cell

Manuscript received May 9, 2018; revised June 20, 2018; accepted July 31,

2018. Date of publication August 17, 2018; date of current version October 26,
2018. The work of A. Fell was supported by the European Commission through the Marie-Curie fellowship “Quokka Maturation.” *(Corresponding author:* *Andreas Fell.)*
A. Fell is with the Fraunhofer Institute for Solar Energy Systems, Freiburg
79110, Germany, and also with the AF Simulations, March 79232, Germany (e-mail:, andreas.fell@ise.fraunhofer.de).

P. P. Altermatt is with the Trina Solar, State Key Laboratory of PV Sci-
ence and Technology, Changzhou 213031, China (e-mail:, pietro.altermatt@ trinasolar.com). Color versions of one or more of the figures in this paper are available online at [http://ieeexplore.ieee.org](http://ieeexplore.ieee.org). Digital Object Identifier 10.1109/JPHOTOV.2018.2863548

simulations within a SPICE model, an approach applied already in the 1970s [2] and later, e.g., in [3] and [4]. The SPICE model is fed with the *IV* curves of possibly various different “unit cell” domains from the inner and the edge part of the cell. Other ways of including large-scale effects are simplifications to, e.g., a lumped series resistance, scaling of the current density, and an external diode property. Often, at least some of these large- scale effects are even neglected. These simplifications reduce the level of detail and accuracy, and thus the predictive power of the simulations. A notable exception exists with Griddler [5], which rigorously solves a distributed diode network representing a full-size solar cell including its metallization, at the expense of lumping multidimensional semiconductor transport effects into quasi-1-D two-diode circuits. Recently, Quokka3 was presented to be capable of discretiz- ing and electrically solving an entire full-cell geometry in 3-D including the metal layers. This became possible by the “skin concept,” where the near-surface regions are treated as lumped boundary conditions to the quasi-neutral bulk carrier transport, omitting the fine discretization required within a full detailed model [6], [7]. The lumped skins are characterized mainly by their sheet resistance *R*sheetand recombination property *J₀,*skin. Yet, Quokka3 can still account for the detailed physics of a skin by employing a “multiscale” approach, where the semiconduc- tor differential equations are solved in 1-D within the skin and are consistently coupled as an extended boundary condition to the 3-D bulk solver [6]. It is therefore now practically possible to accurately solve full-size geometries with low complexity in 3-D (like 156 mm Al-BSF cells), including detailed skin properties,

i.e., equivalent to a full detailed cell model. However, compu- tational demand is substantial, and still prohibitively high on standard hardware for more complex geometries, e.g., PERC cells with dashed rear contacts or IBC cells. This paper presents a “multidomain” approach (originally in- troduced in [8]) to enhance the capabilities for full-cell modeling of Quokka3 further: Three (or if necessary more) domains can be combined for modeling a front- and rear-contacted cell with H-pattern metallization. This enables solving, e.g., a full-size PERC solar cell with dashed rear-contacts and unequal front and rear contact pitches in practical computing times (*<*hours). In this way, a wide range of effects relevant for PERC cells can be modeled within a single simulation domain: from the details of the emitter skin losses (e.g., Auger and surface recombina- tion), over medium-scale effects (e.g., 3-D spreading resistance effects at the local rear dash contacts), up to full-cell effects (e.g., edge effects).
2156-3381 © 2018 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [http://www.ieee.org/publications](http://www.ieee.org/publications) standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on March 02,2026 at 13:36:56 UTC from IEEE Xplore. Restrictions apply.

Fig. 2. Detailed view of edge domain 1 for the investigated PERC cell, high-

lighting the different front and rear contact pitch, the dashed rear contacts, and the inclusion of the finger resistance*.*

TABLE I COMPARISON OF EXPERIMENTAL (MEDIAN OVER 2000 CELLS) AND (BASELINE)SIMULATED IV PARAMETERS OF A TRINA PERC CELL DURING RAMP-UP,HENCE NOT FULLY REPRESENTING COMMERCIAL CELLS

Fig. 1. Sketch of an H-pattern five busbar cell design (quarter symmetry, not

to scale), showing the three domains of the multidomain approach.

The new capabilities are showcased on a recent production- line Trina PERC cell. The input parameters are derived by independent measurements on test-structures, and carefully calibrated against the final cell characteristics. Details of how to establish the lumped-parameter optical model of Quokka3, a detailed loss breakdown, and the complete set of (lumped) input parameters are given.

### II. MULTIDOMAIN FULL-CELL MODEL

The multidomain approach of this paper can be considered an extreme case of the unit-cell simulations + SPICE approach described in the introduction. Enabled by the performance of Quokka3, much larger domains compared with the common unit cell domain can be used. Most decisively, the domains span over half a busbar-pitch, thus fully including the current-transport through the metal fingers and its accompanying potential drop, as well as busbar recombination and shading. Furthermore, it gives more freedom for different front- and rear contact pitches, using the least-common-multiplier to derive the total domain width. This is in contrast with common unit cell simulations, where almost always the pitches are adjusted to 1/1, 1/2 (and rarely 3/4) ratios. In this case, 3.5 front metal fingers (105 total) and 6.5 lines of rear dashed contacts (195 total) define the width of the domains. The three large domains comprise an inner domain (domain 0) and two edge domains: perpendicular to the fingers with or without a redundant line (domain 1), and parallel to the fingers (domain 2), see Figs. 1 and 2. Using the well-justified assump- tion that the busbar has a constant potential which equals the applied potential, i.e., neglecting busbar resistance, the electri- cal network simplifies to the summation of the currents from the areas represented by the respective domains at a given ap- plied voltage. For ease-of-use and overall consistency, Quokka3 can automatically construct the domains from the user-defined full-cell geometry with an H-pattern metallization and inter- nally perform the current summation. Therefore, the inputs are the same as defining the full-cell geometry, with simply an ad- ditional option whether to use the multidomain approach. This enables a straightforward variation of all input parameters in- cluding the geometry, with the decisive benefit of computational

demand being reduced to a practical level compared with solv- ing the actual full-size domain. Note that an approximation implied by the multidomain model is that the four corners of the cell are represented by two adjacent edge domains, which however incurs very small errors [3].

### III. APPLICATION EXAMPLE:INDUSTRIAL PERC CELL

*A. Electrical and Optical Cell Properties* The multidomain approach is applied to a production-line Trina Solar cell during ramp-up. The efficiency is only close to 21% because it was fabricated during ramp-up, and therefore this cell does not represent the cells sold by Trina, but en- abling us to disclose more details. The various input parameters required for the simulations were carefully derived from dedi- cated test structures, see Table II in the Appendix for a summary. Our simulations simultaneously match the manufactured cell *IV* parameters, the reflection, and external quantum efficiency (EQE) closely, see Table I and Fig. 3, meaning that a highly predictive model is achieved. We note that thereby this paper provides a complete (lumped) input parameter set describing a (close-to) state-of-the-art industrial PERC cell in 2018. This is to our knowledge the best available parameter set to date to

FELL AND ALTERMATT: DETAILED FULL-CELL MODEL OF A 2018 COMMERCIAL PERC SOLAR CELL IN QUOKKA3

Fig. 3. SunSolve fitted to measured reflection *R*, the resulting simulated front

film absorption *A*front, the derived *T*ext, and EQE comparison between measure- ment and Quokka3 simulation.

describe a recent commercial PERC cell, and thus provides an update to the 2014 PERC model published in [9]. To derive the generation rate, Quokka3’s *T*ext*− Z* optical model is used [10]. Fitting well in scope with the skin concept, the inputs for this model are lumped optical parameters of the cell, mainly the transmission through the front surface *T*ext, and light trapping quantified via the path-length enhancement factor

*Z*. In this paper, we choose to input internal optical properties of the various skins, from which Quokka3 internally calculates *Z* for each combination of front and rear skins using the analytical model of Brendel *et al*. [11]. Most notably, this enables us to account for the spatially varying light-trapping performance of the device due to the different internal reflectivity of the different rear regions as follows:
1) the poorly reflecting localized contacts;
2) the well-reflecting passivated area covered by Al-paste;
3) the even higher reflecting Ag-paste area. In this way, we increase the predictive power of the model
as it can consider the changes in current for varying rear cell design in addition to shading from the front metal grid. In con- trast with using a static generation profile, the *T*ext*− Z* model further comes with the benefits of supporting quantum effi- ciency simulations, thickness variation, and even temperature variation within Quokka3 using a fixed set of optical input parameters [10]. To derive *T*extand the internal optical properties of the skins, we set up detailed optical simulations of the three different cell areas in the optical simulator SunSolve from PV lighthouse [12], [13], being careful in replicating the measured reflection of the cells under investigation. *T*extis then determined by one minus the measured reflectance (corrected to exclude metal), linearly extrapolating in the long wavelengths to exclude the escape reflection, and adding the front film absorption from the SunSolve results for the short wavelengths. The SunSolve results further contain the light-trapping performance of the device, which can be quantified by the path- length enhancements factor *Z*. In a subsequent step, we find the

Fig. 4. Light trapping quantified by *Z* comparing SunSolve results with the

analytical model used in Quokka3.

lumped internal optical properties by fitting the analytical model [11] implemented in Quokka3 to match the known *Z*, see Fig. 4. In the analytical model, we first fix the internal front reflectance to an average reflectance of 0.93 and a specular reflectance of 0.62, as proposed in [11] for a typical random-pyramid textured surface with antireflection coating. Agreement with the SunSolve results is achieved with a physically meaningful trend of the average rear reflectance between the different regions, as well as their Lambertian fraction: the contacted Al-BSF areas have a relatively low reflectance but high scattering, whereas the Al- and Ag-covered passivated areas scatter less but have a higher reflectance, see Fig. 4. Employing those values within the complete cell simulation overestimates *J*scby only *∼*0.3 mA/cm². Possible reasons are neglecting the effect of parasitic internal absorption at the front contacts and free carrier absorp- tion in the heavily doped areas. However, both reduce the light- trapping performance only slightly [14]. We therefore adjust the average internal front reflectance down to 0.85 to match the experimental *J*sc. This value is similar to the value evaluated in UNSW PERL cells in staggered pyramids [15] and may well be realistic for the random textures of mass-fabricated PERC cells. In Fig. 3, a comparison between the final simulated and mea- sured EQE is shown, which shows a very good agreement for all wavelengths and thus validates the optical model established for this cell. The noncontacted part of the emitter skins, i.e., the n+ as well as the noncontacted n++ emitter regions, are modeled using the experimentally measured doping profiles and the silicon re- combination properties given in [1]. Modeling the noncontacted emitter regions in detail is useful for a detailed loss analysis, and in this case also for considering the significant current collection losses in the 300 *µ*mwiden++ emitter regions, which are rather wide to ensure alignment with the screen- printing metallization. It is sensible to model the contacted skins (contacted part of the emitter and the rear local BSFs) as well as the rear-passivation using lumped parameters (*J₀,*skin and *R*sheet). This is due to substantially larger uncertainties of the detailed inputs and highlights the flexibility of Quokka3’s

Fig. 5. Detailed power loss breakdown at maximum power point of the investigated PERC cell. Within a single multidomain and multiscale simulation, a wide

range of loss details is quantified. Note that the results deviate from the baseline model in that worst-case edge recombination [16] is assumed.

multiscale modeling approach, which allows to individually set the modeling type of the different skins. We note that the actual volumetric shape of the local rear contacts has to be simplified to a planar rectangular area due to the cuboidal mesh type in Quokka3. Any deviation arising from that simplification can be considered to be effectively “lumped” into the *J₀,*skinof the rear contacts. We model edge losses for two extreme cases of no and “worst- case” edge recombination. Worst-case means assuming edge SRV’s at thermal velocity, accounting for both the edge of the quasi-neutral bulk region, as well as within the space-charge- region as a result of the emitter reaching to the edge. For the “baseline” input parameters, which are compared with exper- imental results, we assume no edge recombination, as some degree of passivation is expected during cell processing, which likely renders edge recombination losses insignificant. For the loss breakdown in Section III-B, we assume worst-case edge re- combination instead, for the sake of illustrating the large range of losses being accessible via a single simulation. The reader is referred to [16] for details on the assumptions and the imple- mentation of edge recombination in Quokka3, and to [8] for an edge loss study of the investigated PERC cell.

*B. Loss Breakdown* Finally, we present a power loss breakdown of the investi- gated PERC cell. The breakdown is based on the free energy loss analysis (FELA) [17], which is an automatic output of Quokka3. The FELA is extended with approximate optical power losses by multiplying the respective current density loss with the maxi- mum power point voltage. Here, we choose the worst-case edge recombination scenario to illustrate the convenience of the mul- tidomain approach to additionally determine the edge power losses: It is directly computed by comparing the total terminal power density with the one from the inner, i.e., edge-effect-free,
domain. Within an actual full-cell simulation in contrast, the quantification of edge losses is not straightforward, because a suitable edge-effect-free reference simulation would need to be established in addition. In Fig. 5, the loss breakdown is plotted, highlighting the un- precedented scale of detail achieved within a single simulation. It ranges from large-scale effects like edge losses to resolving the losses within the emitters by Quokka3’s multiscale approach. Overall, the cell is well balanced with no single loss channel be- ing obvious to have the dominating potential for improvement. Regarding optics, shading is the dominant loss followed by escape of light at the front, but which is smaller in the module due to total internal reflection. On the electrical side, the bulk losses dominate both in terms of recombination via the boron-oxygen (BO) defect SRH recom- bination and transport losses, making it a candidate for further optimization, e.g., by an improved deactivation of the BO defect and cleaner processing to avoid metal contaminants. The bulk transport losses may be improved by improved cell geometry (smaller pitches), which however requires further simultane- ous improvements in finger width and contact recombination to not adversely increase their respective losses. We note further that the losses within the local n++ emitter are not negligible, mainly caused by the large width (300 *µ*m). Thus, an improved alignment technology allowing a smaller width is desirable.

### IV. CONCLUSION

The multidomain approach proposed in this paper and im- plemented in Quokka3 enables to model a full-size PERC cell accounting for a wide range of effects conveniently within a single simulation setup and within practical computing times. While such a range of effects had been possible to model before, it did require multiple software tools and high effort. This paper

FELL AND ALTERMATT: DETAILED FULL-CELL MODEL OF A 2018 COMMERCIAL PERC SOLAR CELL IN QUOKKA3

TABLE II ELECTRO-OPTICAL INPUT PARAMETERS FOR THE TRINA SOLAR PRODUCTION-LINE PERC CELL IN AIR (DURING RAMP-UP); ADEVICE TEMPERATURE OF 25 °C IS ASSUMED ALONG WITH THE LATEST SI MATERIAL MODELS [1], [9]

brings such complete cell simulations to a status where it can be routinely included in many modeling tasks. The approach is showcased on a recent production-line PERC cell of Trina Solar (during ramp-up, not representing commonly fabricated cells) for which a complete and consistent input parameter set is carefully derived to match the experimental cell characteristics. The established PERC model in Quokka3 thus has an unprecedented accuracy and predictive power by a single simulation setup fully accounting for:

1) the detailed physics of the emitters, i.e., the interplay of the doping profile with the various recombination mech- anisms (Auger, inactive phosphorus SRH and surface SRH), assuming state-of-the-art physical models (Fermi- Dirac carrier statistics, no quasi-neutral assumption, ...);
2) the actual metal and contact geometry (unequal front and rear contact pitch and dashed rear contacts);
3) the accurate distributed resistance effect of the metal grid and the emitter sheet resistance;
4) 3-D carrier transport within the bulk to the localized dashed rear contacts;
5) busbar effects (localized recombination and shading);
6) edge effects (edge geometry, edge recombination);
7) wavelength-dependence of the optics, i.e., supporting quantum-efficiency simulations and varying spectral irradiance;
8) different optical properties of the different rear regions. The careful calibration of electrical and optical properties
and overall accuracy of the modeling approach is evidenced by a simultaneous match to the measured reflection, EQE, and light *JV* parameters, giving confidence to its predictive power. A detailed loss breakdown of the investigated PERC cell is presented, showing that recombination in the base region is dominating the overall recombination losses, but that also recombination within the n++ part of the emitter can be fur- ther reduced, and recombination at the metal contacts is sig- nificant. It is emphasized, however, that the loss analysis alone is not sufficient for deciding where and how to reduce losses most efficiently; the reduction of losses with design changes must be modeled instead. This is so because large losses are not necessarily easily reduced. The complete (lumped) input parameter set, given in the Ap- pendix, is to our knowledge the best available parameter set to date to describe a commercial PERC cell, which fellow re- searchers are invited to use as a point of reference.

APPENDIX

### See Table II.

REFERENCES

[1] P. P. Altermatt, “Models for numerical device simulations of crystalline silicon solar cells—A review,” *J. Comput. Electron.*, vol. 10, no. 3, pp. 314– 330, 2011. [2] C. R. Fang and J. R. Hauser, “A two dimensional analysis of sheet resis- tance and contact resistance effects in solar cells,” in *Proc. 13th Photovolt.* *Spec. Conf.*, Washington, DC, USA, 1978, pp. 1306–1311. [3] G. Heiser, P. P. Altermatt, and J. Litsios, “Combining 2D and 3D device simulation with circuit simulation for optimising high-efficiency silicon solar cells,” in *Simulation of Semiconductor Devices and Processes*.New York, NY, USA: Springer, 1995, pp. 348–351. [4] J. Dicker, J. O. Schumacher, W. Warta, and S. W. Glunz, “Analysis of one- sun monocrystalline rear-contacted silicon solar cells with efficiencies of

22.1%,” *J. Appl. Phys.*, vol. 91, no. 7, pp. 4335–4343, 2002.
[5] J. Wong, “Griddler: Intelligent computer aided design of complex solar cell metallization patterns,” in *Proc. 39th Photovolt. Spec. Conf.*,Tampa, FL, USA, 2013, pp. 933–938. [6] A. Fell, J. Schon, M. C. Schubert, and S. W. Glunz, “The concept of skins ¨ for silicon solar cell modeling,” *Sol. Energy Mater. Sol. Cells*, vol. 173, pp. 128–133, 2017. [7] R. Brendel, “Modeling solar cells with the dopant-diffused layers treated as conductive boundaries,” *Prog. Photovolt., Res. Appl.*, vol. 20, no. 1, pp. 31–43, 2012. [8] A. Fell and P. P. Altermatt, “Detailed 3D full-cell modeling in Quokka3: quantifying edge and solder-pad losses in an industrial PERC Cell,” *AIP J.* *Phys.*, Silicon PV 2018, Lausanne, Switzerland, doi: 10.1063/1.5049246. [9] A. Fell *et al.*, “Input parameters for the simulation of silicon solar cells in 2014,” *IEEE J. Photovolt.*, vol. 5, no. 4, pp. 1250–1263, Jul. 2015. [10] A. Fell, K. R. McIntosh, and K. C. Fong, “Simplified device simulation of silicon solar cells using a lumped parameter optical model,” *IEEE J.* *Photovolt.*, vol. 6, no. 3, pp. 611–616, May 2016. [11] R. Brendel, M. Hirsch, R. Plieninger, and J. J.H. Werner, “Quantum ef- ficiency analysis of thin-layer silicon solar cells with back surface fields and optical confinement,” *IEEE Trans. Electron Devices*, vol. 43, no. 7, pp. 1104–1113, Jul. 1996. [12] PV Lighthouse, SunSolve. 2018. [Online] Available: [https://pvlighthouse](https://pvlighthouse). com.au/sunsolve. Accessed on: Apr. 1, 2018. [13] M. D. Abbott, K. R. McIntosh, and B. Sudbury, “Optical loss analysis of pv modules,” in *Proc. Eur. Photovolt. Sol. Energy Conf.*, 2016, pp. 976–979. [14] Y. Yang *et al.*, “Combining ray tracing with device modeling to evalu- ate experiments for an optical analysis of crystalline Si solar cells and modules,” *Energy Procedia*, vol. 124, pp. 240–249, 2017. [15] A. G. Aberle *et al.*, “Limiting loss mechanisms in 23% efficient silicon solar cells,” *J. Appl. Phys.*, vol. 77, no. 7, pp. 3491–3504, 1995. [16] A. Fell *et al.*, “Modeling edge recombination in silicon solar cells,” *IEEE*

*J. Photovolt.*, vol. 8, no. 2, pp. 428–434, Mar. 2018.
[17] R. Brendel, S. Dreissigacker, N. P. Harder, and P. P. Altermatt, “Theory of analyzing free energy losses in solar cells,” *Appl. Phys. Lett.*, vol. 93, no. 17, 2008, Art. no. 173503.

Authors’ photographs and biographies not available at the time of publication.
