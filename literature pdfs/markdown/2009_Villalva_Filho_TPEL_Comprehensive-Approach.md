IEEE TRANSACTIONS ON POWER ELECTRONICS, VOL. 24, NO. 5, MAY 2009

## Comprehensive Approach to Modeling and Simulation of Photovoltaic Arrays

Marcelo Gradella Villalva, Jonas Rafael Gazoli, and Ernesto Ruppert Filho

***Abstract*—This paper proposes a method of modeling and sim- ulation of photovoltaic arrays. The main objective is to find the**

**parameters of the nonlinear *I–V* equation by adjusting the curve at three points: open circuit, maximum power, and short circuit.**

**Given these three points, which are provided by all commercial** **array datasheets, the method finds the best *I–V* equation for the single-diode photovoltaic (PV) model including the effect of the**

**series and parallel resistances, and warranties that the maximum** **power of the model matches with the maximum power of the real** **array. With the parameters of the adjusted *I–V* equation, one can** **build a PV circuit model with any circuit simulator by using basic** **math blocks. The modeling method and the proposed circuit model** **are useful for power electronics designers who need a simple, fast, accurate, and easy-to-use modeling method for using in simulations**

**of PV systems. In the first pages, the reader will find a tutorial on** **PV devices and will understand the parameters that compose the single-diode PV model. The modeling method is then introduced**

**and presented in details. The model is validated with experimental data of commercial PV arrays.**

***Index Terms*—Array, circuit, equivalent, model, modeling, photovoltaic (PV), simulation.**

I. INTRODUCTION
PHOTOVOLTAIC (PV) system directly converts sunlight

# Ainto electricity. The basic device of a PV system is the

PV cell. Cells may be grouped to form panels or arrays. The voltage and current available at the terminals of a PV device may directly feed small loads such as lighting systems and DC motors. More sophisticated applications require electronic converters to process the electricity from the PV device. These converters may be used to regulate the voltage and current at the load, to control the power flow in grid-connected systems, and mainly to track the maximum power point (MPP) of the device. In order to study electronic converters for PV systems, one first needs to know how to model the PV device that is attached to the converter. PV devices present a nonlinear*I*–*V* characteristic with several parameters that need to be adjusted from experi- mental data of practical devices. The mathematical model of the PV device may be useful in the study of the dynamic analysis of converters, in the study of MPP tracking (MPPT) algorithms, and mainly to simulate the PV system and its components using circuit simulators. The first purpose of this paper is to present a brief introduction to the behavior and functioning of a PV device and write its basic equations, without the intention of providing an indepth

Manuscript received September 27, 2008; revised December 16, 2008. Current version published April 17, 2009. Recommended for publication by Associate Editor K. Ngo. The authors are with the School of Electrical and Computer Engineering, University of Campinas (UNICAMP), Campinas 13083-970, Brazil (e-mail: mvillalva@gmail.com; gazoli@gmail.com; ruppert@fee.unicamp.br). Digital Object Identifier 10.1109/TPEL.2009.2013862

Fig. 1. Physical structure of a PV cell.

analysis of the PV phenomenon and the semiconductor physics. The introduction on PV devices is followed by the modeling and simulation of PV arrays, which is the main subject of this paper. Some terms used in this paper require an explanation. A PV *device* may be any element that converts sunlight into electricity. The elementary PV device is the PV *cell*. A set of connected cells form a *panel*. Panels are generally composed of series cells in order to obtain large output voltages. Panels with large output currents are achieved by increasing the surface area of the cells or by connecting cells in parallel. A PV *array* may be either a panel or a set of panels connected in series or parallel to form large PV systems. Electronic converter designers are usually interested in mod- eling PV panels (called arrays henceforth in this paper), which are the general purpose off-the-shelf PV devices available in the market. This paper focuses on PV arrays and shows how to obtain the parameters of the *I*–*V* equation from practical data obtained in datasheets. The modeling of elementary PV cells or arrays composed of multiple panels may be done with the same procedure.

### II. HOW A PV CELL WORKS

A photovoltaic cell is basically a semiconductor diode whose *p*–*n* junction is exposed to light [1], [2]. Photovoltaic cells are made of several types of semiconductors using different man- ufacturing processes. The monocrystalline and polycrystalline silicon cells are the only found at commercial scale at the present time. Silicon PV cells are composed of a thin layer of bulk Si or a thin Si film connected to electric terminals. One of the sides of the Si layer is doped to form the *p*–*n* junction. A thin metallic grid is placed on the Sun-facing surface of the semiconductor.

Fig. 1 roughly illustrates the physical structure of a PV cell.

The incidence of light on the cell generates charge car- riers that originate an electric current if the cell is short- circuited [2]. Charges are generated when the energy of the incident photon is sufficient to detach the covalent elec- trons of the semiconductor—this phenomenon depends on the semiconductor material and on the wavelength of the incident light. Basically, the PV phenomenon may be described as the absorption of solar radiation, the generation and transport of free

0885-8993/$25.00 © 2009 IEEE Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on November 06,2025 at 10:38:07 UTC from IEEE Xplore. Restrictions apply.

: COMPREHENSIVE APPROACH TO MODELING AND SIMULATION OF PHOTOVOLTAIC ARRAYS

Fig. 2. Spectral distribution of the black body radiation and the Sun radiation in

the extraterrestrial space (AM0) and on Earth’s surface (AM1.5). *Source:Moller ¨* [2].

VILLALVA *et al.*

carriers at the *p*–*n* junction, and the collection of these electric charges at the terminals of the PV device [3], [4]. The rate of generation of electric carriers depends on the flux of incident light and the capacity of absorption of the semi- conductor. The capacity of absorption depends mainly on the semiconductor bandgap, on the reflectance of the cell surface (that depends on the shape and treatment of the surface), on the intrinsic concentration of carriers of the semiconductor, on the electronic mobility, on the recombination rate, on the tem- perature, and on several other factors. The solar radiation is composed of photons of different ener- gies. Photons with energies lower than the bandgap of the PV cell are useless and generate no voltage or electric current. Pho- tons with energy superior to the bandgap generate electricity, but only the energy corresponding to the bandgap is used—the remainder of energy is dissipated as heat in the body of the PV cell. Semiconductors with lower bandgaps may take advantage or a larger radiation spectrum, but the generated voltages are lower [5]. Si is not the only, and probably not the best, semi- conductor material for PV cells, but it is the only one whose fabrication process is economically feasible in large scale. Other materials can achieve better conversion efficiency, but at higher and commercially unfeasible costs. The study of the physics of PV cells is considerably compli- cated and is out of the scope of this paper. For the purpose of studying electronic converters for PV systems, it is sufficient to know the electric characteristics of the PV device (cell, panel, and array). The manufacturers of PV devices always provide a set of empirical data that may be used to obtain the mathe- matical equation of the device *I*–*V* curve. Some manufacturers also provide *I*–*V* curves obtained experimentally for different operating conditions. The mathematical model may be adjusted and validated with these experimental curves.

### III. SOLAR RADIATION

The efficiency of a PV device depends on the spectral distri- bution of the solar radiation. The Sun is a light source whose radiation spectrum may be compared to the spectrum of a black body near 6000 K. A black body absorbs and emits electromag- netic radiation in all wavelengths. The theoretical distribution of wavelengths of the black body radiation is mathematically described by Planck’s law, which establishes the relations and interdependencies of the wavelength (or frequency), the tem- perature and the spectral distribution of the black body [5]–[7].

Fig. 2 shows the spectral distribution of the black body ra-

diation compared with the extraterrestrial and terrestrial solar radiations [2]. The study of the effect of the solar radiation on PV devices is difficult because the spectrum of the sunlight on the Earth’s surface is influenced by factors such as the variation of the temperature on the solar disc and the influence of the atmo- sphere [8]. In the extraterrestrial space, at the average distance between the Sun and the Earth, the irradiated solar energy is about 1.353 kW/m². On the Earth’s surface, the irradiation is approximately 1 kW/m² (this is a reference value only, as the net irradiation on Earth’s surface depends on many factors).

Fig. 3. Illustration of the AM1.5 path and the direct-normal and global incident

radiations on a Sun-facing surface at 37 *◦* tilt.

PV devices are generally evaluated with reference to a stan- dard spectral distribution. The American Society for Testing and Materials (ASTM) defines two standard terrestrial spectral distributions [9], [10]: the direct-normal and global AM1.5. The direct-normal standard corresponds to the incident radiation that perpendicularly reaches a Sun-facing surface directly from the Sun. The global or total standard corresponds to the spectrum of the direct and diffuse radiations. Diffuse radiation is the ra- diation influenced by the atmospheric steam and the reflection on Earth’s surface. The AM1.5 standards are defined for a PV *◦* device whose surface is tilted at 37 and faces the Sun rays. The AM initials stand for *air mass*, which means the mass of air between a surface and the Sun that affects the spectral distribution and intensity of sunlight [11]. The AM*x* number indicates the length of the path of the solar radiation through the atmosphere. With longer paths more light deviation and absorp- tion occur. These phenomena change the spectral distribution of the light received by the PV device. The length of the path of the sun rays (given in number of atmospheres) is indicated by the *x* coefficient of AM*x* defined as

<u>1</u> *x* = (1) cos*θ*z

where *θz*is the angle of the Sun with reference to the zenith, as shown in Fig. 3. A bigger *x* corresponds to a longer path and a greater air mass between the Sun and the surface of the terrestrial PV device. The standard AM1.5 distributions correspond to the spectrum of the solar radiation with a solar angle *θ*z= 48.19 *◦*.

Fig. 3 illustrates the definitions of the AM1.5 path and the direct-

normal and global radiations.

Fig. 4. Single-diode model of the theoretical PV cell and equivalent circuit of

a practical PV device including the series and parallel resistances.

||− I₀ I = I||− 1 −||
|---|---|---|---|---|
|Fig. 5. Characteristic I –V composed of the light-generated current I|pv|t||p|
||pv|t|s||
|||s|||

Fig. 5. Characteristic *I*–*V* curve of the PV cell. The net cell current *I* is

pvand the diode current *I*d.

The intensity and spectral distribution of the solar radiation depend on the geographic position, time, day of the year, climate conditions, composition of the atmosphere, altitude, and many other factors [8]. Due to the factors that influence the solar radia- tion, the AM1.5 spectral distributions are only average estimates

|rents may be expressed as I|= I|N ,I₀ = I₀|N .In|
|---|---|---|---|
||pv pv,cell|p|,cell p|
|s|||p|

that serve as references for the evaluation and comparison of PV devices. The AM1.5 distributions are used as standards in the PV industry. Datasheets generally bring information about the characteristics and performance of PV devices with respect to the so-called *standard test condition* (STC), which means an ir- radiation of 1000 W/m² with an AM1.5 spectrum at 25 *◦* C [12].

### IV. MODELING OF PV DEVICES

*A. Ideal PV Cell*
Fig. 4 shows the equivalent circuit of the ideal PV cell. The
 basic equation from the theory of semiconductors [13] that math- ematically describes the *I*–*V* characteristic of the ideal PV cell is
[ ()] <u>qV</u> *I*=*I*pv*,*cell*− I₀,*cellexp *−* 1 (2) <u>akT</u> ︸ ︷︷ ︸ *I* d where *I*pv*,*cellis the current generated by the incident light (it is directly proportional to the Sun irradiation), *I*dis the Shockley diode equation, *I₀,*cellis the reverse saturation or leakage current *−*19 of the diode, *q* is the electron charge (1.60217646 *×* 10 C), *−*23 *k* is the Boltzmann constant (1.3806503 *×* 10 J/K), *T* (in Kelvin) is the temperature of the *p*–*n* junction, and *a* is the diode ideality constant. Fig. 5 shows the *I*–*V* curve originated from (2).

*B. Modeling the PV Array* The basic equation (2) of the elementary PV cell does not represent the*I*–*V* characteristic of a practical PV array. Practical arrays are composed of several connected PV cells and the observation of the characteristics at the terminals of the PV
Fig. 6. Characteristic *I*–*V* curve of a practical PV device and the three *re-*

*markable points*: short circuit (0*,I*sc),MPP(*V*mp*,I*mp)*,* and open circuit (*V*oc*,*0).

array requires the inclusion of additional parameters to the basic equation [13] [ ()] <u>V + RsI V + RsI</u> pvexp *V*t*a R*p

(3)
where *I* and *I₀* are the photovoltaic (PV) and saturation cur- rents, respectively, of the array and *V* = *N kT/q* is the thermal voltage of the array with *N* cells connected in series. Cells connected in parallel increase the current and cells connected in series provide greater output voltages. If the array is composed of *N*pparallel connections of cells the PV and saturation cur- pv pv*,*cell p*,*cell p

(3), *R* is the equivalent series resistance of the array and *R* is the equivalent parallel resistance. This equation originates the *I*–*V* curve in Fig. 6, where three *remarkable points* are high- lighted: short circuit (0*,I*sc),MPP(*V*mp*,I*mp)*,* and open circuit (*V*oc*,*0). Equation (3) describes the single-diode model presented in
Fig. 4. Some authors have proposed more sophisticated models
 that present better accuracy and serve for different purposes. For example, in [14]–[18] an extra diode is used to represent the effect of the recombination of carriers. A three-diode model is proposed in [19] to include the influence of effects that are not considered by the previous models. For simplicity, the single- diode model of Fig. 4 is studied in this paper. This model offers a good compromise between simplicity and accuracy [20], and has been used by several authors in previous works, sometimes with simplifications but always with the basic structure com- posed of a current source and a parallel diode [12], [21]–[34]. The simplicity of the single-diode model with the method for adjusting the parameters and the improvements proposed in this paper make this model perfect for power electronics design- ers who are looking for an easy and effective model for the simulation of PV devices with power converters. Manufacturers of PV arrays, instead of the *I*–*V* equation, provide only a few experimental data about electrical and ther- mal characteristics. Unfortunately, some of the parameters re- quired for adjusting PV array models cannot be found in the manufacturer’s datasheets, such as the light-generated or PV current, the series and shunt resistances, the diode ideality con- stant, the diode reverse saturation current, and the bandgap energy of the semiconductor. All PV array datasheets bring basically the following information: the nominal open-circuit voltage (*V*oc*,*n), the nominal short-circuit current (*I*sc*,*n),the

voltage at the MPP (*V*mp), the current at the MPP (*I*mp),the open-circuit voltage/temperature coefficient (*KV*), the short- circuit current/temperature coefficient (*KI*), and the maximum experimental peak output power (*P*max*,*e). This information is always provided with reference to the nominal condition or stan- dard test conditions (STCs) of temperature and solar irradiation. Some manufacturers provide *I*–*V* curves for several irradiation and temperature conditions. These curves make easier the ad- justment and the validation of the desired mathematical *I*–*V* equation. Basically, this is all the information one can get from datasheets of PV arrays. Electric generators are generally classified as current or volt- age sources. The practical PV device presents an hybrid behav- ior, which may be of current or voltage source depending on the operating point, as shown in Fig. 6. The practical PV de- vice has a series resistance *R*swhose influence is stronger when the device operates in the voltage source region, and a paral- lel resistance *R*pwith stronger influence in the current source region of operation. The *R*sresistance is the sum of several structural resistances of the device. Fig. 1 shows the structure of a PV cell. *R*sbasically depends on the contact resistance of the metal base with the *p* semiconductor layer, the resis- tances of the *p* and *n* bodies, the contact resistance of the *n* layer with the top metal grid, and the resistance of the grid [4]. The *R*presistance exists mainly due to the leakage current of the *p*–*n* junction and depends on the fabrication method of the PV cell. The value of *R*pis generally high and some au- thors [12], [23]–[26], [29], [35]–[38] neglect this resistance to simplify the model. The value of *R*sis very low, and sometimes this parameter is neglected too [36], [39]–[41]. The *I*–*V* characteristic of the PV device shown in Fig. 6 depends on the internal characteristics of the device (*R*s, *R*p) and on external influences such as irradiation level and temperature. The amount of incident light directly affects the generation of charge carriers, and consequently, the current generated by the device. The light-generated current (*I*pv) of the elementary cells, without the influence of the series and parallel resistances, is difficult to determine. Datasheets only inform the nominal short- circuit current (*I*sc*,*n), which is the maximum current available at the terminals of the practical device. The assumption *I*sc*≈ I*pv is generally used in the modeling of PV devices because in practical devices the series resistance is low and the parallel resistance is high. The light-generated current of the PV cell

|I|+ K ∆||
|---|---|---|
|sc,n|I T||
|oc,n|V T|t|

depends linearly on the solar irradiation and is also influenced by the temperature according to the following equation [30], [42]–[44]:

<u>G</u>

||=(I I|∆ )|and K .The|
|---|---|---|---|
||pv pv,n|I T|I V|
|||n||
|pv,n||||
|||◦||
|n|n|||
|||n||

+ *K* (4) *G*

where *I* (in amperes) is the light-generated current at the nominal condition (usually 25 C and 1000 W/m²), ∆T= *T − T* (*T* and *T* being the actual and nominal tempera- tures [in Kelvin], respectively), *G* (watts per square meters) is the irradiation on the device surface, and *G* is the nominal irradiation.

The diode saturation current *I₀* and its dependence on the temperature may be expressed by as shown [42], [43], [45]–[48]: ()3 [ ()] *I₀* = *I₀,*n *T*n exp *qE*g1 *−* 1

(5)
*T ak T*n*T*

where *E*gis the bandgap energy of the semiconductor (*E*g=

1.12 eV for the polycrystalline Si at 25
*◦* C [23], [42]), and *I₀,*n is the nominal saturation current: <u>I</u> <u>sc,n</u> *I₀,*n= exp( *V /aV*) *−* 1

(6)
oc*,*n t*,*n with *V*t*,*nbeing the thermal voltage of *N*sseries-connected cells at the nominal temperature *T*n. The saturation current *I₀* of the PV cells that compose the device depend on the saturation current density of the semi- conductor (*J*, generally given in [A/cm]) and on the effective 2 0 area of the cells. The current density *J₀* depends on the intrinsic characteristics of the PV cell, which depend on several physical parameters such as the coefficient of diffusion of electrons in the semiconductor, the lifetime of minority carriers, the intrinsic carrier density, etc. [19]. This kind of information is not usually available for commercial PV arrays. In this paper, the nominal saturation current *I₀,*nis indirectly obtained from the experi- mental data through (6), which is obtained by evaluating (3) at the nominal open-circuit condition, with *V* = *V*oc*,*n, *I* =0, and *I* pv*≈ I*sc*,*n. The value of the diode constant *a* may be arbitrarily chosen. Many authors discuss ways to estimate the correct value of this constant [20], [23]. Usually, 1 *≤ a ≤* 1.5 and the choice depends on other parameters of the *I*–*V* model. Some values for *a* are found in [42] based on empirical analyses. As is given in [20], there are different opinions about the best way to choose

*a*. Because *a* expresses the degree of ideality of the diode and it is totally empirical, any initial value of *a* can be chosen in order to adjust the model. The value of *a* can be later modified in order to improve the model fitting, if necessary. This constant affects the curvature of the*I*–*V* curve and varying*a*can slightly improve the model accuracy.
*C. Improving the Model* The PV model described in the previous section can be im- proved if (5) is replaced by *I₀* = (7)
exp((*V* + *K* ∆)*/aV*) *−* 1

This modification aims to match the open-circuit voltages of the model with the experimental data for a very large range of temperatures. Equation (7) is obtained from (6) by including in the equation the current and voltage coefficients*K* saturation current *I₀* is strongly dependent on the temperature and (7) proposes a different approach to express the dependence of *I₀* on the temperature so that the net effect of the tempera- ture is the linear variation of the open-circuit voltage according the the practical voltage/temperature coefficient. This equation simplifies the model and cancels the model error at the vicinities of the open-circuit voltages, and consequently, at other regions of the *I*–*V* curve.

Fig. 7. *P* –*V* curves plotted for different values of *R*sand *R*p.

The validity of the model with this new equation has been tested through computer simulation and through comparison with experimental data. One interesting fact about the correc- tion introduced with (7) is that the coefficient *KV*from the manufacturer’s datasheet appears in the equation. The volt- age/temperature coefficient *KV*brings important information necessary to achieve the best possible *I*–*V* curve fitting for temperatures different of the nominal value.

*D. Adjusting the Model* Two parameters remain unknown in (3), which are *R*sand *R*p. A few authors have proposed ways to mathematically de- termine these resistances. Although it may be useful to have a mathematical formula to determine these unknown parameters, any expression for *R*sand *R*pwill always rely on experimental data. Some authors propose varying *R*sin an iterative process,

|s||||Fig. 7.|P –V curves plotted for different values of R|and R.|
|---|---|---|---|---|---|---|
||p|s|s p|p|||
|||s p|||||
|max,e max,m|mp mp|mp mp|||||
||max,e||||||
 incrementing*R*suntil the*I*–*V* curve visually fits the experimen- tal data and then vary *R* in the same fashion. This is a quite poor and inaccurate fitting method, mainly because *R* and *R* may not be adjusted separately if a good *I*–*V* model is desired. This paper proposes a method for adjusting *R* and *R* based on the fact that there is an only pair *{R*,*R}* that warranties that*P*max*,*m= *P* = *V I* at the (*V,I*) point of the *I*–*V* curve, i.e., the maximum power calculated by the *I*–*V* model of (3) (*P*) is equal to the maximum experimen- tal power from the datasheet (*P*) at the MPP. Conven- tional modeling methods found in the literature take care of the *I*–*V* curve but forget that the*P* –*V* (power versus voltage) curve must match the experimental data too. Works like [36] and [49] gave attention to the necessity of matching the power curve but with different or simplified models. For example, in [36], the series resistance of the array model is neglected. The relation between *R*sand *R*p, the only unknowns of (3), may be found by making *P*max*,*m= *P*max*,*eand solving the resulting equation for *R*s,asshown.
{ [ ()] <u>q Vmp+ RsImp</u> *P*max*,*m= *V*mp*I*pv*− I₀* exp *−* 1 *kT aN*s } <u>Vmp+ RsImp</u> *−* = *P*max*,*e(8) *R*p

*R*p= *V*mp(*V*mp+ *I*mp*R*s)*/* { [] <u>(Vmp+ ImpRs) q</u> *V*mp*I*pv*− V*mp*I₀* exp *N*s*a kT* }

### + VmpI₀ − Pmax,e. (9)

Equation (9) means that for any value of *R*sthere will be a value of *R*pthat makes the mathematical *I*–*V* curve cross the experimental (*V*mp*,I*mp) point.

*E. Iterative Solution of R*s*and R*p The goal is to find the value of *R*s(and hence, *R*p) that makes the peak of the mathematical *P* –*V* curve coincide with the
Fig. 8. *P*max*,* mversus *V* for several values of *R*s*>* 0.

experimental peak power at the (*V*mp*,I*mp) point. This requires several iterations until *P*max*,*m= *P*max*,*e. In the iterative process, *R*smust be slowly incremented starting from *R*s=0. Adjusting the *P* –*V* curve to match the experimental data requires finding the curve for several values of *R*sand *R*p. Actually, plotting the curve is not necessary, as only the peak power value is required. Figs. 7 and 9 illustrate how this iterative process works. In Fig. 7, as *R*sincreases, the *P* –*V* curve moves to the left and the peak power (*P*max*,*m) goes toward the experimental MPP. Fig. 8 shows the contour drawn by the peaks of the power curves for several values of *R*s(this example uses the parameters of the Kyocera KC200GT solar array [50]). For every*P* –*V* curve of Fig. 7, there is a correspond- ing *I*–*V* curve in Fig. 9. As expected from (9), all *I*–*V* curves cross the desired experimental MPP point at (*V*mp*,I*mp). Plotting the *P* –*V* and *I*–*V* curves requires solving (3) for *I ∈* [0*,I*sc*,*n] and *V ∈* [0*,V*oc*,*n]. Equation (3) does not have a direct solution because *I* = *f* (*V,I*) and *V* = *f* (*I,V*).This transcendental equation must be solved by a numerical method and this imposes no difficulty. The *I*–*V* points are easily

Fig. 9. *I*–*V* curves plotted for different values of *R*sand *R*p.

Fig. 11. *I*–*V* curve adjusted to three *remarkable points*.

|||||Fig. 12. P –V|curve adjusted to three remarkable points.|
|---|---|---|---|---|---|
|Fig. 10. P|= f (R) with I = I|and V = V|.|||

max s mp mp

obtained by numerically solving *g*(*V,I*)=*I − f*(*V,I*)=0for a set of*V* values and obtaining the corresponding set of*I* points. Obtaining the *P* –*V* points is straightforward. The iterative method gives the solution *R*s= 0.221 Ω for the KC200GT array. Fig. 8 shows a plot of*P*max*,*mas a function of*V* for several values of *R*s. There is an only point, corresponding to a single value of *R*sthat satisfies the imposed condition *P*max*,*m= *V*mp*I*mpat the (*V*mp*,I*mp) point. Fig. 10 shows a plot of *P*max*,*mas a function of *R*sfor *I* = *I*mpand *V* = *V*mp. This plot shows that *R*s= 0.221 Ω is the desired solution, in accordance with the result of the iterative method. This plot may be an alternative way for graphically finding the solution for*R*s. Figs. 11 and 12 show the *I*–*V* and *P* –*V* curves of the KC200GT PV array adjusted with the proposed method. The model curves *exactly* match with the experimental data at the three *remarkable points* provided by the datasheet: short circuit, maximum power, and open circuit. The adjusted parameters and model constants are listed in Table II.

*F. Further Improving the Model* The model developed in the preceding sections may be further improved by taking advantage of the iterative solution of*R*sand *R*p. Each iteration updates *R*sand *R*ptoward the best model solution, so (10) may be introduced in the model.
<u>Rp+ Rs</u> *I* pv*,*n= *R*p *I* sc*,*n*.* (10)

Equation (10) uses the resistances *R*sand *R*pto determine *I* pv*̸*= *I*sc. The values of *R*sand *R*pare initially unknown but as the solution of the algorithm is refined along successive iter- ations the values of *R*sand *R*ptend to the best solution and (10) becomes valid and effectively determines the light-generated current *I*pvtaking in account the influence of the series and par- allel resistances of the array. Initial guesses for *R*sand *R*pare necessary before the iterative process starts. The initial value of *R*smay be zero. The initial value of *R*pmay be given by

<u>VmpVoc,n− Vmp</u> *R*p*,*min= *−.* (11) *I* sc*,*n*− I*mp*I*mp

Fig. 14. *I*–*V* model curves and experimental data of the KC200GT solar array

2 at different temperatures, 1000 W/m.

|Fig. 13. Algorithm of the method used to adjust the I –V||model.|at different temperatures, 1000 W/m|
|---|---|---|---|
||TABLE I|||
|PARAMETERS OF THE KC200GT SOLAR ARRAY AT 25|A.M1.5, 1000 W/m|C,||

Fig. 13. Algorithm of the method used to adjust the *I*–*V* model.

*◦* 2

TABLE II PARAMETERS OF THE ADJUSTED MODEL OF THE KC200GT SOLAR ARRAY AT NOMINAL OPERATING CONDITIONS

Equation (11) determines the minimum value of *R*p, which is the slope of the line segment between the short-circuit and the maximum-power *remarkable points*. Although *R*pis still unknown, it surely is greater than *R*p*,*minand this is a good initial guess.

*G. Modeling Algorithm* The simplified flowchart of the iterative modeling algorithm is illustrated in Fig. 13.
V. VALIDATING THE MODEL
As Tables I and II and Figs. 11 and 12 have shown, the de- veloped model and the experimental data are exactly matched

Fig. 15. *I*–*V* model curves and experimental data of the KC200GT solar array

at different irradiations, 25*◦*C.

at the nominal *remarkable points* of the *I*–*V* curve, and the ex- perimental and mathematical maximum peak powers coincide. The objective of adjusting the mathematical *I*–*V* curve at the three *remarkable points* was successfully achieved. In order to test the validity of the model, a comparison with other experimental data (different of the nominal *remarkable* *points*) is very useful. Fig. 14 shows the mathematical *I*–*V* curves of the KC200GT solar panel plotted with the experi- mental data at three different temperature conditions. Fig. 15 shows the *I*–*V* curves at different irradiations. The circular markers in the graphs represent experimental (*V,I*) points extracted from the datasheet. Some points are not exactly matched because the model is not perfect, although it is exact at the *remarkable points* and sufficiently accurate for other points. The model accuracy may be slightly improved by running more iterations with other values of the constant *a*, without modifications in the algorithm.

Fig. 16 shows the mathematical *I*–*V* curves of the Solarex

MSX60 solar panel [51] plotted with the experimental data at

Fig. 16. *I*–*V* model curves and experimental data of the MSX60 solar array

2 at different temperatures, 1000 W/m.

Fig. 18. Absolute errors of the model proposed in this paper (curve A) and

2 in [23] (curve B) for the Kyocera KC200GT solar array at 25*◦*C, 1000 W/m.

Fig. 17. *P* –*V* model curves and experimental data of the MSX60 solar array

at different temperatures, 1000 W/m 2.

two different temperature conditions. Fig. 17 shows the *P −V* curves obtained at the two temperatures. The circular markers in the graphs represent experimental (*V,I*) and (*V,P*) points extracted from the datasheet. Fig. 17 proves that the model ac- curately matches with the experimental data both in the current and power curves, as expected. Figs. 18–21 show the absolute errors of the model with re- spect to the experimental data. The model prosed in this paper is compared with the modeling method of [23]. The errors pre- sented by both models are plotted on the same graphs. The model proposed in this paper is superior, especially at the vicinities of the *remarkable points*.Atthe*remarkable points* the errors are practically null.

### VI. SIMULATION OF THE PV ARRAY

The PV array can be simulated with an equivalent circuit model based on the PV model of Fig. 4. Two simulation strate- gies are possible.

Fig. 19. Absolute errors of the model proposed in this paper (curve A) and

in [23] (curve B) for the Kyocera KC200GT solar array at 75*◦*C, 1000 W/m².

Fig. 22 shows a circuit model using one current source (*I*m)

and two resistors (*R*sand *R*p). This circuit can be implemented in any circuit simulator. The value of the model current *I*mis calculated by the computational block that has *V*, *I*, *I₀*, and *I* pvas inputs. *I₀* is obtained from (5) or (7) and *I*vpis obtained from (4). This computational block may be implemented in any circuit simulator able to evaluate math functions.

Fig. 23 shows another circuit model composed of only one

current source. The value of the current is obtained by numeri- cally solving the *I*–*V* equation. For every value of *V*, a corre- sponding *I* that satisfies the *I*–*V* equation (3) is obtained. The solution of (3) can be implemented with a numerical method in any circuit simulator that accepts embedded programming. Other authors have proposed circuits for simulating PV ar- rays that are based on simplified equations and/or require lots of computational effort [24], [36], [37], [52]. A circuit-based PV

Fig. 22. PV array model circuit with a controlled current source, equivalent

resistors, and the equation of the model current (*I*m).

Fig. 20. Absolute errors of the model proposed in this paper (curve A) and

2 in [23] (curve B) for the Solarex MSX60 solar array at 25*◦*C, 1000 W/m.

Fig. 23. PV array model circuit with a controlled current source and a com-

putational block that solves the *I*–*V* equation.

Fig. 21. Absolute errors of the model proposed in this paper (curve A) and

in [23] (curve B) for the Solarex MSX60 solar array at 75*◦*C, 1000 W/m².

model is composed of a current source driven by an intricate and inaccurate equation in [24] where the parallel resistance is neglected. An intricate PSPICE-based simulation was presented in [36], where the *I*–*V* equation is numerically solved within the PSpice software. Although interesting, the approach found in [36] is excessively elaborated and concerns the simplified PV model without the series resistance. A simple circuit-based PV model is proposed in [37] where the parallel resistance is neglected. A circuit-based model was proposed based on the piecewise approximation of the *I*–*V* curve in [52]. Although interesting and relatively simple, this method [52] does not pro- vide a solution to find the parameters of the *I*–*V* equation and the circuit model requires many components.

### VII. CONCLUSION

This paper has analyzed the development of a method for the mathematical modeling of PV arrays. The objective of the method is to fit the mathematical*I*–*V* equation to the experimen- tal*remarkable points*of the*I*–*V* curve of the practical array. The method obtains the parameters of the*I*–*V* equation by using the following nominal information from the array datasheet: open- circuit voltage, short-circuit current, maximum output power, voltage and current at the MPP, and current/temperature and voltage/temperature coefficients. This paper has proposed an effective and straightforward method to fit the mathematical *I*–*V* curve to the three (*V,I*) *remarkable points* without the need to guess or to estimate any other parameters except the diode constant *a*. This paper has proposed a closed solution for the problem of finding the parameters of the single-diode model equation of a practical PV array. Other authors have tried to pro- pose single-diode models and methods for estimating the model parameters, but these methods always require visually fitting the mathematical curve to the *I*–*V* points and/or graphically extracting the slope of the *I*–*V* curve at a given point and/or successively solving and adjusting the model in a trial and error process. Some authors have proposed indirect methods to adjust the *I*–*V* curve through artificial intelligence [27], [53]–[55] and interpolation techniques [35]. Although interesting, such meth- ods are not very practical and are unnecessarily complicated and require more computational effort than it would be expected for this problem. Moreover, frequently in these models *R*sand *R*p are neglected or treated as independent parameters, which is not true if one wishes to correctly adjust the model so that the maximum power of the model is equal to the maximum power of the practical array.

An equation to express the dependence of the diode satura- tion current *I₀* on the temperature was proposed and used in the model. The results obtained in the modeling of two practical PV arrays have demonstrated that the equation is effective and per- mits to exactly adjust the *I*–*V* curve at the open-circuit voltages at temperatures different from the nominal. Moreover, the assumption *I*pv*≈ I*scused in most of previous works on PV modeling was replaced in this method by a relation between *I*pvand *I*scbased on the series and parallel resistances. The proposed iterative method for solving the unknown param- eters of the *I*–*V* equation allows to determine the value of *I*pv, which is different from*I*sc. This paper has presented in detail the equations that constitute the single-diode PV *I*–*V* model and the algorithm necessary to obtain the parameters of the equation. In order to show the practical use of the proposed modeling method, this paper has presented two circuit models that can be used to simulate PV arrays with circuit simulators. This paper provides the reader with all necessary infor- mation to easily develop a single-diode PV array model for analyzing and simulating a PV array. Programs and ready-to-use circuit models are available for download at: [http://sites.google.com/site/mvillalva/pvmodel](http://sites.google.com/site/mvillalva/pvmodel).

REFERENCES

[1] A. S. Sedra and K. C. Smith, *Microelectronic Circuits*. London, U.K.: Oxford Univ. Press, 2006. [2] H.J.Moller, ¨ *Semiconductors for Solar Cells*. Norwood, MA: Artech House, 1993. [3] A. L. Fahrenbruch and R. H. Bube, *Fundamentals of Solar Cells*.San Francisco, CA: Academic, 1983. [4] F. Lasnier and T. G. Ang, *Photovoltaic Engineering Handbook*.New York: Adam Hilger, 1990. [5] “Photovoltaic systems technology,” Universitat Kassel, Kassel, Germany, ¨

2003.
[6] L. Castaner ˜ and S. Silvestre, *Modeling Photovoltaic Systems Using* *PSpice*. New York: Wiley, 2002. [7] K.S.Krane,*Modern Physics.*2nd ed. New York: Wiley, Aug. 1995. [8] A. Guechi and M. Chegaar, “Effects of diffuse spectral illumination on microcrystalline solar cells,” *J. Electron Devices*, vol. 5, pp. 116–121,

2007.
[9] C. Riordan and R. Hulstron, “What is an air mass 1.5 spectrum? [solar cell performance calculations],” in *Proc. Conf. Record 21st IEEE Photovoltaic* *Spec. Conf.*, 1990, vol. 2, pp. 1085–1088. [10] American Society for Testing and Materials (ASTM). Reference solar spectral irradiance: Air mass 1.5. [Online]. Available: [http://rredc.nrel](http://rredc.nrel). gov/solar/spectra/am1.5/ [11] *IEEE Standard Definitions of Terms for Solar Cells*, 1969. [12] W. Xiao, W. G. Dunford, and A. Capel, “A novel modeling method for photovoltaic cells,” in *Proc. IEEE 35th Annu. Power Electron. Spec. Conf.* *(PESC)*, 2004, vol. 3, pp. 1950–1956. [13] H. S. Rauschenbach, *Solar Cell Array Design Handbook*.NewYork: Van Nostrand Reinhold, 1980. [14] J. A. Gow and C. D. Manning, “Development of a photovoltaic array model for use in power-electronics simulation studies,” *IEE Proc. Elect.* *Power Appl.*, vol. 146, no. 2, pp. 193–200, 1999. [15] J. A. Gow and C. D. Manning, “Development of a model for photovoltaic arrays suitable for use in simulation studies of solar energy conversion systems,” in *Proc. 6th Int. Conf. Power Electron. Variable Speed Drives*, 1996, pp. 69–74. [16] N. Pongratananukul and T. Kasparis, “Tool for automated simulation of solar arrays using general-purpose simulators,” in *Proc. IEEE Workshop* *Comput. Power Electron.*, 2004, pp. 10–14. [17] S. Chowdhury, G. A. Taylor, S. P. Chowdhury, A. K. Saha, and Y. H. Song, “Modelling, simulation and performance analysis of a PV array in an em-

bedded environment,” in *Proc. 42nd Int. Univ. Power Eng. Conf. (UPEC)*, 2007, pp. 781–785. [18] J. Hyvarinen and J. Karila, “New analysis method for crystalline silicon cells,” in *Proc. 3rd World Conf. Photovoltaic Energy Convers.*, 2003, vol. 2, pp. 1521–1524. [19] K. Nishioka, N. Sakitani, Y. Uraoka, and T. Fuyuki, “Analysis of multicrys- talline silicon solar cells by modified 3-diode equivalent circuit model tak- ing leakage current through periphery into consideration,” *Solar Energy* *Mater. Solar Cells*, vol. 91, no. 13, pp. 1222–1227, 2007. [20] C. Carrero, J. Amador, and S. Arnaltes, “A single procedure for helping PV designers to select silicon PV module and evaluate the loss resistances,” *Renewable Energy*, vol. 32, no. 15, pp. 2579–2589, Dec. 2007. [21] E. Koutroulis, K. Kalaitzakis, and V. Tzitzilonis. (2008). Development of a FPGA-based system for real-time simulation of photovoltaic modules, *Microelectron. J.* [Online]. [22] G. E. Ahmad, H. M. S. Hussein, and H. H. El-Ghetany, “Theoretical anal- ysis and experimental verification of PV modules,” *Renewable Energy*, vol. 28, no. 8, pp. 1159–1168, 2003. [23] G. Walker, “Evaluating MPPT converter topologies using a matlab PV model,” *J. Elect. Electron. Eng., Australia*, vol. 21, no. 1, pp. 45–55,

2001.
[24] M. Veerachary, “PSIM circuit-oriented simulator model for the nonlinear photovoltaic sources,” *IEEE Trans. Aerosp. Electron. Syst.*, vol. 42, no. 2, pp. 735–740, Apr. 2006. [25] A. N. Celik and N. Acikgoz, “Modelling and experimental verification of the operating current of mono-crystalline photovoltaic modules using four- and five-parameter models,” *Appl. Energy*, vol. 84, no. 1, pp. 1–15, Jan. 2007. [26] Y.-C. Kuo, T.-J. Liang, and J.-F. Chen, “Novel maximum-power-point- tracking controller for photovoltaic energy conversion system,” *IEEE* *Trans. Ind. Electron.*, vol. 48, no. 3, pp. 594–601, Jun. 2001. [27] M. T. Elhagry, A. A. T. Elkousy, M. B. Saleh, T. F. Elshatter, and

E. M. Abou-Elzahab, “Fuzzy modeling of photovoltaic panel equivalent circuit,” in *Proc. 40th Midwest Symp. Circuits Syst.*, Aug. 1997, vol. 1, pp. 60–63.
[28] S. Liu and R. A. Dougal, “Dynamic multiphysics model for solar array,” *IEEE Trans. Energy Convers.*, vol. 17, no. 2, pp. 285–294, Jun. 2002. [29] Y. Yusof, S. H. Sayuti, M. Abdul Latif, and M. Z. C. Wanik, “Modeling and simulation of maximum power point tracker for photovoltaic system,” in *Proc. Nat. Power Energy Conf. (PEC)*, 2004, pp. 88–93. [30] D. Sera, R. Teodorescu, and P. Rodriguez, “PV panel model based on datasheet values,” in *Proc. IEEE Int. Symp. Ind. Electron. (ISIE)*, 2007, pp. 2392–2396. [31] M. A. Vitorino, L. V. Hartmann, A. M. N. Lima, and M. B. R. Correa, “Using the model of the solar cell for determining the maximum power point of photovoltaic systems,” in *Proc. Eur. Conf. Power Electron. Appl.*, 2007, pp. 1–10. [32] D. Dondi, D. Brunelli, L. Benini, P. Pavan, A. Bertacchini, and L. Larcher, “Photovoltaic cell modeling for solar energy powered sensor networks,” in *Proc. 2nd Int. Workshop Adv. Sens. Interface (IWASI)*, 2007, pp. 1–6. [33] H. Patel and V. Agarwal, “MATLAB-based modeling to study the effects of partial shading on PV array characteristics,” *IEEE Trans. Energy* *Convers.*, vol. 23, no. 1, pp. 302–310, Mar. 2008. [34] W. Yi-Bo, W. Chun-Sheng, L. Hua, and X. Hong-Hua, “Steady-state model and power flow analysis of grid-connected photovoltaic power system,” in *Proc. IEEE Int. Conf. Ind. Technol. (ICIT’08)*, pp. 1–6. [35] K. Khouzam, C. Khoon Ly, C. Koh, and P. Y. Ng, “Simulation and real- time modelling of space photovoltaic systems,” in *Proc. IEEE 1st World* *Conf. Photovoltaic Energy Convers., Conf. Record 24th IEEE Photovoltaic* *Spec. Conf.*, 1994, vol. 2, pp. 2038–2041. [36] M. C. Glass, “Improved solar array power point model with SPICE re- alization,” in *Proc. 31st Intersoc. Energy Convers. Eng. Conf. (IECEC)*, Aug. 1996, vol. 1, pp. 286–291. [37] I. H. Altas and A. M. Sharaf, “A photovoltaic array simulation model for matlab–simulink GUI environment,” in *Proc. Int. Conf. Clean Elect.* *Power (ICCEP)*, 2007, pp. 341–345. [38] E. Matagne, R. Chenni, and R. El Bachtiri, “A photovoltaic cell model based on nominal data only,” in *Proc. Int. Conf. Power Eng., Energy Elect.* *Drives, POWERENG*, 2007, pp. 562–565. [39] Y. T. Tan, D. S. Kirschen, and N. Jenkins, “A model of PV generation suitable for stability analysis,” *IEEE Trans. Energy Convers.*, vol. 19, no. 4, pp. 748–755, Dec. 2004. [40] A. Kajihara and A. T. Harakawa, “Model of photovoltaic cell circuits under partial shading,” in *Proc. IEEE Int. Conf. Ind. Technol. (ICIT)*, 2005, pp. 866–870.

**Marcelo Gradella Villalva** was born in Campinas, Sao Paulo, Brazil, in 1978. He received the B.Sc. and ˜

M.Sc. degrees in electrical engineering in 2002 and 2005, respectively, from the University of Campinas (UNICAMP), Brazil, where he is currently working toward the Ph.D. degree. His current research interests include active filters, modeling and control of electronic converters, pho- tovoltaic energy systems, distributed generation, and artificial intelligence applied to power electronics.
**Jonas Rafael Gazoli** was born in Americana, Sao˜ Paulo, Brazil, in 1983. He received the B.Sc. in elec- trical engineering in 2008, from the University of Campinas (UNICAMP), Brazil, where he is currently working toward the M.Sc. degree. His current research interests include power elec- tronics for solar energy conversion and control strate- gies for electrical drives.

[41] N. D. Benavides and P. L. Chapman, “Modeling the effect of voltage ripple on the power output of photovoltaic modules,” *IEEE Trans. Ind.* *Electron.*, vol. 55, no. 7, pp. 2638–2643, Jul. 2008. [42] W. De Soto, S. A. Klein, and W. A. Beckman, “Improvement and validation of a model for photovoltaic array performance,” *Solar Energy*, vol. 80, no. 1, pp. 78–88, Jan. 2006. [43] Q. Kou, S. A. Klein, and W. A. Beckman, “A method for estimating the long-term performance of direct-coupled PV pumping systems,” *Solar* *Energy*, vol. 64, no. 1–3, pp. 33–40, Sep. 1998. [44] A. Driesse, S. Harrison, and P. Jain, “Evaluating the effectiveness of maximum power point tracking methods in photovoltaic power systems using array performance models,” in *Proc. IEEE Power Electron. Spec.* *Conf. (PESC)*, 2007, pp. 145–151. [45] R. A. Messenger and J. Ventre, *Photovoltaic Systems Engineering*.Boca Raton, FL: CRC Press, 2004. [46] F. Nakanishi, T. Ikegami, K. Ebihara, S. Kuriyama, and Y. Shiota, “Model- ing and operation of a 10 kW photovoltaic power generator using equiva- lent electric circuit method,” in *Proc. Conf. Record 28th IEEE Photovoltaic* *Spec. Conf.*, Sep. 2000, pp. 1703–1706. [47] J. Crispim, M. Carreira, and R. Castro, “Validation of photovoltaic elec- trical models against manufacturers data and experimental results,” in *Proc. Int. Conf. Power Eng., Energy Elect. Drives, POWERENG*, 2007, pp. 556–561. [48] K. H. Hussein, I. Muta, T. Hoshino, and M. Osakada, “Maximum photo- voltaic power tracking: An algorithm for rapidly changing atmospheric conditions,” in *Proc. IEE Proc.-Generation, Transmiss. Distrib.*,Jan. 1995, vol. 142, pp. 59–64. [49] E. I. Ortiz-Rivera and F. Z. Peng, “Analytical model for a photovoltaic module using the electrical characteristics provided by the manufacturer data sheet,” in *Proc. IEEE 36th Power Electron. Spec. Conf. (PESC)*, 2005, pp. 2087–2091. [50] KC200GT High Efficiency Multicrystal Photovoltaic Module Datasheet Kyocera. [Online]. Available: [http://www.kyocera.com.sg/products/solar/](http://www.kyocera.com.sg/products/solar/) pdf/kc200gt.pdf [51] *Solarex MSX60 and MSX64 Solar Arrays Datasheet*. (1997). [Online]. Available: [http://www.californiasolarcenter.org/newssh/pdfs/](http://www.californiasolarcenter.org/newssh/pdfs/) solarex-MSX64.pdf [52] R. C. Campbell, “A circuit-based photovoltaic array model for power system studies,” in *Proc. 39th North Amer. Power Symp. (NAPS)*, 2007, pp. 97–101. [53] T. F. Elshatter, M. T. Elhagry, E. M. Abou-Elzahab, and A. A. T. Elkousy, “Fuzzy modeling of photovoltaic panel equivalent circuit,” in *Proc. Conf.* *Record 28th IEEE Photovoltaic Spec. Conf.*, 2000, pp. 1656–1659. [54] M. Balzani and A. Reatti, “Neural network based model of a PV array for the optimum performance of PV system,” in *Proc. Ph.D. Res. Microelec-*

**Ernesto Ruppert Filho** was born in Jundia´ı, Sao˜ Paulo, Brazil. He received the B.Sc., M.Sc., and Ph.D. degrees in electrical engineering from the Univer- sity of Campinas (UNICAMP), Campinas, Brazil, in 1971, 1974, and 1982, respectively. He was engaged as a project engineer and/or con- sultant, in Brazil and abroad, for several large com- panies such as Itaipu, Petrobras, General Electric, Alstom, Copel, CPFL, and Elektro. Since 1972, he has been with the UNICAMP as a Professor and Re- searcher. He is currently a Full Professor and coordi- nates several research projects with private companies and public institutions in *tron. Electron.*, 2005, vol. 2, pp. 123–126. [55] H. Mekki, A. Mellit, H. Salhi, and B. Khaled, “Modeling and simulation Brazil. His current research interests include power electronics, superconductor of photovoltaic panel based on artificial neural networks and VHDL-current limiters, electrical power systems, distributed generation, electric ma- language,” in *Proc. 14th IEEE Int. Conf. Electron., Circuits Syst. (ICECS)*, chines, and motor drives. He has authored or coauthored many technical papers 2007, pp. 58–61. published in international journals and conferences.
