##### i An update to this article is included at the end

Solar Energy 80 (2006) 78–88 www.elsevier.com/locate/solener

# Improvement and validation of a model for photovoltaic array performance

### W. De Soto, S.A. Klein*, W.A. Beckman

Solar Energy Laboratory, University of Wisconsin-Madison, 1500 Engineering Drive, Madison, WI 53706, USA

Received 20 December 2004; received in revised form 21 June 2005; accepted 21 June 2005 Available online 16 August 2005

Communicated by: Associate Editor Arturo Morales-Acevedo

Abstract

Manufacturers of photovoltaic panels typically provide electrical parameters at only one operating condition. Pho- tovoltaic panels operate over a large range of conditions so the manufacturer!s information is not sufficient to determine their overall performance. Designers need a reliable tool to predict energy production from a photovoltaic panel under all conditions in order to make a sound decision on whether or not to incorporate this technology. A model to predict energy production has been developed by Sandia National Laboratory, but it requires input data that are normally not available from the manufacturer. The five-parameter model described in this paper uses data provided by the manufac- turer, absorbed solar radiation and cell temperature together with semi-empirical equations, to predict the current–volt- age curve. This paper indicates how the parameters of the five-parameter model are determined and compares predicted current–voltage curves with experimental data from a building integrated photovoltaic facility at the National Institute of Standards and Technology (NIST) for four different cell technologies (single crystalline, poly crystalline, silicon thin film, and triple-junction amorphous). The results obtained with the Sandia model are also shown. The predictions from the five-parameter model are shown to agree well with both the Sandia model results and the NIST measurements for all four cell types over a range of operating conditions. The five-parameter model is of interest because it requires only a small amount of input data available from the manufacturer and therefore it provides a valuable tool for energy predic- tion. The predictive capability could be improved if manufacturer!s data included information at two radiation levels. ! 2005 Elsevier Ltd. All rights reserved.

Keywords: Photovoltaic cells; PV cells; Performance; I–V curves; Prediction; Solar energy

1. Introduction
temperature, the solar incidence angle and the load resis- tance. Manufacturers typically provide only limited The electrical power output from a photovoltaic operational data for photovoltaic panels, such as the panel depends on the incident solar radiation, the cell open circuit voltage (Voc), the short circuit current (Isc), the maximum power current (Imp) and voltage (Vmp), the temperature coefficients at open circuit volt- * Corresponding author. Tel.: +1 608 263 5626; fax: +1 608 age and short circuit current (bV ocand aIsc, respectively), 262 8464/9. and the nominal operating cell temperature (NOCT). E-mail address: klein@engr.wisc.edu (S.A. Klein). These data are available only at standard rating

0038-092X/$ - see front matter ! 2005 Elsevier Ltd. All rights reserved. doi:10.1016/j.solener.2005.06.010

W. De Soto et al. / Solar Energy 80 (2006) 78–88 79
Nomenclature

|a|ideality|factor|parameter|M|air mass modifier at SRC and air mass 1.5|
|---|---|---|---|---|---|
||a ! N|n kT /q (eV)||NOCT|nominal operating cell temperature (K)|
|a|ideality factor parameter at SRC (eV)|||n|ideality factor|
|AM|air mass|||n|diode factor (in King!s model)|
|b|coefficients for incidence angle modifier in|||N|number of cells in series|
||Eq. (13)|||P|predicted power (W)|
|E|energy bandgap (eV)|||P|maximum power (W)|
|E G|energy (1.121 eV for silicon) (eV) total irradiance on horizontal surface (W/ m²)|bandgap|at reference|q R R|electron charge (1.60218E–19 Coulomb) ratio of beam radiation on tilted surface to that on a horizontal surface series resistance (X)|
|G|beam component of total irradiance on hor- izontal surface (W/m²)|||R R|series resistance at SRC (X) shunt resistance (X)|
|G|diffuse horizontal surface (W/m²)|component|of total|R S|shunt resistance at SRC (X) total absorbed irradiance (W/m²)|
|G|irradiance at SRC (1000 W/m²) (W/m²)|||S|total absorbed irradiance at SRC (W/m²)|
|I|current (A)|||T|cell temperature (K)|
|I|light current (A)|||T|cell temperature at SRC (K)|
|I|light current at SRC (A)|||V|voltage (V)|
|I|current at maximum power point (A)|||V|voltage at maximum power point (V)|
|I|current at maximum power point at SRC|||V|voltage at maximum power point at SRC|
||(A)||||(V)|
|I|diode reverse saturation current (A)|||V|open circuit voltage at SRC (V)|
|I I|diode reverse saturation current at SRC (A) short circuit current at SRC (A)|||a|temperature coefficient for maximum power current (A/K)|
|k K|Boltzmann!s constant (1.38066E–23 J/K) glazing extinction coefficient (1/m)|||a|temperature coefficient for short circuit cur- rent (A/K)|
|K|incidence angle modifier at beam incidence angle h|||b b|slope of the panel (") open voltage temperature coefficient (V/K)|
|K K|incidence angle modifier for diffuse compo- nent incidence angle modifier for ground reflected component|||e h h|material band gap energy (eV) incidence angle, angle between the beam of light and the normal to the panel surface (") angle of refraction (")|
|L|thickness of transparent cover (m)|||q|ground reflectance|
|M|air mass modifier|||s(h)|transmittance of glazing system at angle h|

defined as ref s I c

|a coefficients for air mass modifier in Eq. (17)||n refractive index|
|---|---|---|
|0–4|||
|ref||I|
|||D|
|0–5||s|
|g||mp|
|||beam|
|||s|
|b||s,ref|
|||sh|
|d||sh,ref|
|ref||ref|
|||c|
|L L,ref||c,ref|
|mp||mp|
|mp,ref||mp,ref|
|o o,ref sc,ref||oc,ref|

0–4

g;Treftemperature

irradiance on

I mp

I sc

sa V oc sa,d

sa,g r

conditions (SRC), for which the irradiance is 1000 W/m² and the cell temperature (Tc) is 25 "C (except for the NOCT which is determined at 800 W/m² and an ambi- ent temperature of 20 "C). These conditions produce high power output, but are rarely encountered in actual operation. The results of this study were obtained using panel performance at SRC. Accurate, reliable, and easy to apply methods for predicting the energy production of photovoltaic panels are needed to identify optimum photovoltaic systems. The model developed by King (2000) and King et al. (1998, 2004) accurately predicts energy production with an algebraically simple model, but it requires parameters that are normally not avail- able from the manufacturer. A database of the model

parameters for many different array types is provided by Sandia National Laboratories (2002). A model that uses the only data provided by manufacturers to predict energy production is presented in this paper.

2. The current–voltage relationship for a photovoltaic device The electrical power available from a photovoltaic (PV) device can be modeled with the well known equiv- alent circuit shown in Fig. 1 (Duffie and Beckman, 1991; Nelson, 2003). This circuit includes a series resistance and a diode in parallel with a shunt resistance. This

80 W. De Soto et al. / Solar Energy 80 (2006) 78–88

||||, I|, I,|
|---|---|---|---|---|
|Fig. 1. Equivalent model.|circuit representing|the five-parameter|ref o,ref sc,ref|L,ref|

circuit can be used either for an individual cell, for a module consisting of several cells, or for an array con- sisting of several modules (Duffie and Beckman, 1991). The current–voltage relationship at a fixed cell tem- perature and solar radiation for the circuit in Fig. 1 is expressed in Eq. (1). Five parameters must be known in order to determine the current and voltage, and thus the power delivered to the load. These are: the light cur-

|rent I, the diode reverse saturation current I|, the series||
|---|---|---|
|L|o||
|s|sh|mp,ref mp,ref|

resistance R, the shunt resistance R, and the modified ideality factor a defined in Eq. (2). hi <u>V þIRs V þ IRs</u> I¼IL# Ioea# 1 # ð1Þ Rsh

where <u>N n kTs I c</u> a ! ð2Þ q

The electron charge q, and Boltzmann!s constant k are known, nIis the usual ideality factor, Nsis the number of cells in series and Tcis the cell temperature. The power produced by the PV device is the product of the current and voltage. Ideally, a PV panel would always operate at a voltage that produces maximum power. Such operation is possi- ble, approximately, by using a maximum power point tracker (MPPT). Without an MPPT the PV panel oper- ates at a point on the cell I–V curve that coincides with the I–V characteristic of the load. It is this second situ- ation (i.e., no MPPT) that is the focus of this investigation.

2.1. The reference parameters To evaluate the five parameters in Eq. (1), five inde- pendent pieces of information are needed. In general, these five parameters are functions of the solar radiation incident on the cell and cell temperature. Reference val- ues of these parameters are determined for a specified operating condition such as SRC. Three current–voltage pairs are normally available from the manufacturer at SRC: the short circuit current, the open circuit voltage and the current and voltage at the maximum power point. A fourth piece of information results from recog-
nizing that the derivative of the power at the maximum power point is zero. Although both the temperature coefficient of the open circuit voltage (bV oc) and the tem- perature coefficient of the short circuit current (aIsc) are known, only bV ocis used to find the five reference param- eters. aIscis used when the cell is operating at conditions other than reference conditions. The five parameters appearing in Eq. (1) correspond- ing to operation at SRC are designated: a Rs,ref, and Rsh,ref. To determine the values of these parameters, the three known I–V pairs at SRC are substituted into Eq. (1) resulting in Eqs. (3)–(5). For short circuit current: I = I,V =0 !" <u>I sc;ref Rs;refI R</u> I sc;ref¼ IL;ref# Io;refe aref# 1 #<u>sc;ref s;ref</u>ð3Þ Rsh;ref

For open circuit voltage: I = 0, V = Voc,ref !" 0¼IL;ref# Io;refe <u>V oc</u> aref <u>;ref</u> # 1 # <u>Voc;ref</u> ð4Þ Rsh;ref

At the maximum power point: !" I=I,V=V <u>V mp;ref þ</u> a <u>I mp;ref Rs;ref</u> I mp;ref¼ IL;ref# Io;refe ref # 1

<u>Vmp;refþ Imp;refRs;ref</u> # ð5Þ Rsh;ref

The derivative with respect to power at the maximum power point is zero. # # <u>dðIV Þ</u># ## <u>dI</u> # ## ¼ Imp# Vmp¼ 0 ð6aÞ dVmpdVmp

where dI/dVjmpis given by #<u>V mpþI mp Rs</u> ## <u>#Io</u> ea# <u>1</u> <u>dI</u>a Rsh dV #mp ¼ 1 þ <u>I</u> <u>o</u> <u>R</u> <u>s</u> e <u>V mpþ</u> a <u>I mp Rs</u> þ <u>R</u> <u>s</u> ð6bÞ a Rsh

The temperature coefficient of open circuit voltage is given by

<u>oV</u> ## <u>V # V</u> l V oc¼ ## ≈<u>oc;ref oc;Tc</u>ð7Þ oTI ¼0Tref# Tc

To evaluate lV ocnumerically, it is necessary to know Voc;Tc, the open circuit voltage at some cell temperature near the reference temperature. The cell temperature used for this purpose is not critical since values of Tc ranging from 1 to 10 K above or below Trefprovide essentially the same result. Voc;Tccan be found from Eq. (4) if the temperature dependencies for parameters I o, IL, and a, are known. The shunt resistance, Rshwas assumed to be independent of temperature. Therefore, in order to apply Eq. (7), it is necessary to obtain expres- sions for the temperature dependence of the three parameters a, Ioand, IL. The dependence of all of the parameters in the model on the operating conditions is considered in the following section.

2.2. Dependence of the parameters on operating conditions From the definition of a, the modified ideality factor is a linear function of cell temperature (assuming nIis independent of temperature) so that: <u>a Tc</u> ¼ ð8Þ a refTc;ref where Tc,refand arefare the cell temperature and modi- fied ideality factor for reference conditions, while Tc and a are the cell temperature and modified ideality fac- tor parameter for the new operating conditions. Messenger and Ventre (2004) present an equation from diode theory for the diode reverse saturation current, Io. The ratio of their equation at the new oper- ating temperature to that at the reference temperature yields: !" "#3 ! #
## # ## I oTc1 EgEg ¼ exp # ð9Þ I o;refTc;refk T #TrefT #T c

where k is Boltzmann!s constant and Egis the material band gap. The values of the material band gap energies at 25 "C for the four cell types investigated in this study can be found in Table A.1. Egexhibits a small tempera- ture dependence (Van Zeghbroeck, 2004) which, for sil- icon, can be represented as indicated in Eq. (10) where Eg;Tref¼ 1:121 eV for silicon cells. Eq. (10) was used for all of the cells considered in this study. The value of Eg;Trefused for the triple junction amorphous cell type was 1.6 eV.

<u>Eg</u> ¼ 1 # 0:0002677ðT # Tref10Þ Eg;Tref

The light current, (IL), is nearly a linear function of inci- dent solar radiation. Some pyranometers in fact use the short circuit current of a solar cell as a measure of the incident solar radiation. The light current (IL) is ob- served to depend on the absorbed solar irradiance (S), the cell temperature (Tc), the short circuit current tem- perature coefficient (aIsc), and the air mass modifier

(M). The light current ILfor any operating conditions is assumed to be related to the light current at reference conditions by <u>S M</u> I L¼ ½IL;refþ aIscðTc# Tc;refÞ) ð11Þ S refMref where S

|, M, I|, T|are the parameters at refer-||
|---|---|---|---|
|ref ref|L,ref c,ref|L|c|
||||ref|
 ence conditions, while S, M, I, and T are the values for specified operating conditions. When using Eq. (11) to find the reference parameters, S = S and M = Mref. The air mass modifier is assumed to be a function of the local zenith angle and is discussed below. The information needed to determine the reference parameters is now complete. Eqs. (3)–(7) relate the
model to the known reference conditions. To evaluate Eq. (7) it is necessary to include the temperature depen- dence of a, Ioand ILas given by Eqs. (8)–(11). The simultaneous solution of these equations is facilitated with a non-linear equation solver, such as EES (Klein,

2005). The final task to complete the model is to investigate the operating condition dependence of the series resis- tance Rs, and the shunt resistance, Rsh. The series resis- tance impacts the shape of current and voltage curve near the maximum power point. This effect is seen in
Fig. 2 in which the current–voltage curves for the
 single-crystalline cell at SRC conditions have been plot- ted for series resistance values that are 20% greater and 20% lower than the value determined at reference condi- tions using Eqs. (1)–(11). The effect on the I–V curve is small and, although methods of adjusting Rsas a func- tion of operating conditions have been investigated (De Soto, 2004), Rsis assumed constant at its reference value, R in this study. s,ref The shunt resistance (Rsh) controls the slope of the I– V curve at the short circuit condition; large shunt resis- tances result in a horizontal slope. Fig. 3 shows the effect of halving and doubling the shunt resistance determined using Eqs. (1)–(11) for the single-crystalline cell at stan- dard radiation conditions. The shunt resistance appears to change with absorbed solar radiation for all of the cells although the effect is most noticeable for cell types that have a relatively small shunt resistance at SRC, such as the triple junction amorphous cell. If experimen- tal data were generally available at more than one solar radiation value, it would be possible to develop a rela- tion between the shunt resistance and absorbed radia- tion. However, this information is not normally available. Schroder (1998) indicates that the shunt resis- tance is approximately inversely proportional to the
Fig. 2. Effect of series resistance for the single crystalline cell at
 standard rating conditions.
Þð

Fig. 3. Effect of shunt resistance for the single crystalline cell at

standard rating conditions.

short-circuit current (and thus radiation) at very low light intensities. An observation apparent from an exam- ination of the slopes of the I–V curves at short circuit conditions based on the experimental data from NIST is that the effective shunt resistance increases (and the slope thus decreases) as absorbed radiation is reduced. This behavior is observed for all cell types but it is most observable for the triple-junction amorphous cell type. Eq. (12), in which the shunt resistance is inversely pro- portional to absorbed radiation, is empirically proposed to describe this effect. The model specification is now complete. <u>RshSref</u> ¼ ð12Þ Rsh;refS

3. The incidence angle modifier, Ksa The incidence angle h is the angle between the beam solar radiation and the normal to the panel surface. The incidence angle is directly involved in the determination of the radiation incident on the surface of the PV device. In addition, the incidence angle affects the amount of solar radiation transmitted through the protective cover and converted to electricity by the cell. As the incidence angle increases, the amount of radiation reflected from the cover increases. Significant effects of inclination occur at incidence angles greater than 65". The effect of reflection and absorption as a function of incidence angle is expressed in terms of the incidence angle modifier, Ksa(h) defined as the ratio of the radia- tion absorbed by the cell at some incidence angle h di- vided by the radiation absorbed by the cell at normal incidence. The short circuit current is linearly dependent on the absorbed radiation. The incidence angle is depen-
dent on the panel slope, location and on time. Panels that are mounted on a vertical surface, for example, exacerbate the incidence angle effects because much of the annual beam solar radiation strikes the panel sur- face at angles greater than 65". Nevertheless, vertically mounted panels are of interest because of the applicabil- ity of this orientation to installation on building fac¸ades. The experimental data that are available to validate the model presented in this paper were taken on a vertical surface. King et al. (1998) provides a cell-specific correlation for the incidence angle modifier in the form shown in Eq. (13). Coefficients for many cell types have been determined by Sandia National Laboratories (2002). Coefficients for the PV modules tested by NIST were determined by Fanney et al. (2002b) and these coeffi- cients are provided in Table A.1. However, an alterna- tive form for K (h) was developed for use with the sa five-parameter model that does not require specific experimental information.

5 KsaðhÞ¼X bih i ð13Þ i¼0

The incidence angle modifier for a PV panel differs somewhat from that of a flat-plate solar collector in that the glazing is bonded to the cell surface, thereby elimi- nating one air–glazing interface and the glazing surface may be treated so as to reduce reflection losses. Sjerps- Koomen et al. (1996) have shown that the transmission of this cover system can be well-represented by a simple air–glass model. Eqs. (14) and (15), based on Snell!s and Bougher!s laws as reported in Duffie and Beckman (1991), are used to calculate the incidence angle modifier for one glass–air interface. The angle of refraction (h ) isr determined from Snell!s law

h r ¼ arc sinðn sin hÞð 14Þ

where h is the incidence angle and n is an effective index of refraction of the cell cover. A good approximation of the transmittance of the cover system considering both reflective losses at the interface and absorption within the glazing is "# ! 2 2 sðhÞ¼e #ðKL= cos hr Þ 1 # <u>1 sin₂ðhr# hÞ</u> þ <u>tan₂ðhr# hÞ</u> 2 sin ðhrþ hÞ tan ðhrþ hÞ

ð15Þ

where K is the glazing extinction coefficient and L is the glazing thickness. In this study the value of K is assumed to be 4 m #1, the value for ‘‘water white’’ glass and the glazing thickness is assumed to be 2 mm, a reasonable value for most PV cell panels. The refractive index is set to 1.526, the value for glass. To obtain the incidence angle modifier (Ksa), Eq. (15) needs be evaluated for incidence angles of 0" and h. The

ratio of these two transmittances yields the incidence an- gle modifier:

<u>sðhÞ</u> KsaðhÞ¼ ð16Þ sð0Þ

Separate incidence angle modifiers are needed for beam, diffuse, and ground-reflected radiation, but each can be calculated in the same way. Average angles for isotropic diffuse and ground-reflected radiation are provided as a function of the slope of the panel in Fig. 5.4.1 of Duffie and Beckman (1991). Although these average angles for diffuse radiation were obtained for thermal collectors, they were found to yield reasonable results for PV systems. A plot of the incidence angle modifier calculated using Eqs. (14)–(16) as a function of incidence angle is shown in Fig. 4. The incidence angle modifiers deter- mined from Eq. (13) for the four cell types with the coef- ficients provided by Fanney et al. (2002b) are also shown in Fig. 4 with dotted lines. The plots are all similar. Dif- ferences are apparent at high incidence angles, but the incident radiation is normally low at these high angles and the uncertainty in the experimental values of the incidence angle modifier is larger at these conditions. The triple-junction amorphous cell type uses a thin poly- mer cover while the other three cell types employ a glass cover. The parameters for K, L and n used for glass are likely not appropriate for the polymer cover, but the cal- culated cell performance for the conditions investigated was not found to be sensitive to these parameter values. The advantage of Eqs. (14)–(16) is that it eliminates the need for specific incidence angle modifier constants which are not generally available from the manufac- turer. This method of estimating the incidence angle modifier is used in all of the following results for the five-parameter model.

4. The air mass modifier, M Air mass is the ratio of the mass of air that the beam radiation has to traverse at any given time and location to the mass of air that the beam radiation would traverse if the sun were directly overhead. Selective absorption by species in the atmosphere causes the spectral content of irradiance to change, altering the spectral distribution of the radiation incident on the PV panel. King et al. (1998) developed an empirical relation to account for air mass: X 4 <u>M</u> ¼ aiðAMÞ
i ð17Þ Mref 0

where AM is the air mass and is approximately given by King et al. (1998).

AM ¼ <u>1</u> ð18Þ cosðhZÞþ0:5057ð96:080 # hzÞ #1:634

In Eq. (17) a, a, a, a, and a are constants for differ- ent PV materials which are available for many cell types 0 1 2 3 4

from Sandia National Laboratories (2002). These con- stants were also determined for the cells tested by NIST as reported by Fanney et al. (2002b). The NIST coeffi- cients are listed for the four different cell types in Table

A.1 and used to plot the air mass modifier as a function of zenith angle for the four cell types in Fig. 5. The air mass modifiers for all cell types except the triple junction cell type are nearly the same for zenith angles between 0" and 75". Zenith angles greater than 75" are generally associated with low solar radiation values and thus the differences observed in the air mass modifiers for large angles are not important. It was found that if one set of air mass constants is chosen and used for all cell types there is little difference in the results compared to using a different air mass modifier relation for each cell type. Consequently, the air mass modifier for the poly-
Fig. 4. Incidence angle modifier, Ksa, as a function of incidence

angle, h, calculated using Eqs. (14)–(16) (solid line). The dotted

|Fig. 5. Air|mass modifier,|, as a function|of zenith|
|---|---|---|---|
|angle, h, calculated using Eq. (17) with the coefficients for each||||
|cell type listed in Table A.1.||||

lines are the incidence angle modifiers calculated using Eq. (13) with the coefficients for each cell type provided in Table A.1.

M/Mref z

Since the ratio of S/Srefis needed for further calcula- tions, Eq. (19) is more conveniently represented as:

S GbGdð1 þ cos bÞ ¼ RbeamKsa;bþ Ksa;d S refGrefGref2 <u>G ð1 # cos bÞ</u> þ qKsa;gð21Þ Gref2

where Grefis the radiation at SRC conditions (1000 W/m²) at normal incidence so that (sa)ncancels out.

crystalline cell was used for all following results obtained with the five-parameter model.

5. Absorbed radiation, S The major factor affecting the power output from a PV device is the solar radiation absorbed on the cell sur- face, S, which is a function of the incident radiation and the incidence angle. Radiation data are not normally known on the plane of the PV panel, so it is necessary to estimate the absorbed solar radiation using horizontal data and incidence angle information. The total ab- sorbed irradiance S consists of beam, diffuse, and ground reflected components. Eq. (19) provides an approximate method of estimating the absorbed radia- tion, S, assuming that both diffuse and ground-reflected radiation are isotropic (Duffie and Beckman, 1991): !
<u>ð1 þ cos bÞ</u> S ¼ðsaÞnGbRbeamKsa;bþ GdKsa;d 2 " <u>ð1 # cos bÞ</u> þ GqKsa;gð19Þ 2

In Eq. (19), q is the ground reflectance, b is the slope of the panel, Ksa,bis the incidence angle modifier at the beam incidence angle, Ksa,dand Ksa,gare the incidence angle modifiers at effective incidence angles for isotropic diffuse and ground-reflected radiation, and Rbeamis the ratio of beam radiation on a tilted surface to that on a horizontal surface. The NIST data that were used to test the validity of the model included measurements of GT, the solar radiation incident on the vertical PV array surface. However, the beam, diffuse and ground-reflected com- ponents were not measured so it was necessary to estimate these radiation components in order to determine the incidence angle modifiers in Eq. (19). Employing the same assumptions used for Eq. (19), the solar radiation on the array surface can be expressed as:

<u>ð1 þ cos bÞ ð1 # cos bÞ</u> GT¼ GbRbeamþ Gdþ Gqð20Þ 2 2 Values of GTwere available from the measurements on the vertical (b = 90") surface. Rbeamis a time dependent geometric factor provided in Duffie and Beckman (1991). The ground reflectance, q, was assumed to be

0.2. The only unknown in Eq. (19) is the diffuse fraction, Gd/G since Gb=G#Gd. The Erb!s hourly diffuse frac- tion correlation (Duffie and Beckman, 1991) was used to estimate Gd/G as a function of the clearness index. Eq. (19) was solved to determine the clearness index and thus the total radiation and beam and diffuse components on a horizontal surface corresponding to the measured value of the radiation on the vertical surface.
6. Validation of the five-parameter model The data used for this study were provided by Fan- ney et al. (2002a) from a building integrated photovol- taic facility at the National Institute of Standards and Technology (NIST) in Gaithersburg, Maryland. The experimental data provide, at five-minute intervals, one year (1 January 2000–31 December 2000) of meteorolog- ical data, and measured cell temperatures along with current and voltage values for four different photovol- taic cell technology types installed on a vertical surface. The four different cell technologies are: single-crystal- line, poly-crystalline, silicon thin film, and triple- junction amorphous. The solid lines in Fig. 6 show typical results at 4 dif- ferent operating conditions calculated for the single- crystalline cells with the five-parameter model presented in this paper. Also shown in Fig. 6 are the NIST exper- imental data (open circles) and the results obtained with the King model (closed circles). A summary of the King model is provided in the Appendix. The maximum power values measured by NIST and determined by
Fig. 6. Current vs voltage for the single-crystalline cell type
 predicted by the five-parameter model (solid lines), the King model (closed circles) and measured by NIST (open circles) for four operating conditions and the SRC condition (dotted line).

the King and five-parameter models at SRC conditions and at the 4 operating conditions are shown in Table

1. Figs. 7–9 and Tables 2–4 show similar information for the other three cell types. Note that the reference parameters for all four cell types were determined at the SRC operating condition, 1000 W/m² and 25 "C. Differences between the experimental data and the calcu- lated values occur as a result of limitations in the cell model itself, as well as in the methods used to calculate absorbed radiation, incidence angle modifier and air mass modifier. In addition, there are uncertainties inher- ent in the experimental data. Figs. 6–8 show excellent agreement between the cur- rent–voltages points determined by the five-parameter model and NIST data. The King model shows slightly better agreement with the data but this behavior is ex- pected since the model requires many measurements over a wide range of conditions to determine the model Fig. 8. Current vs voltage for the silicon thin film cell type
predicted by the five-parameter model (solid lines), the King parameters. It is interesting to note that, at points where model (closed circles) and measured by NIST (open circles) for four operating conditions and the SRC condition (dotted line).

Table 1

Maximum power values from NIST measurements and the

|Maximum|power|from NIST|measurements|and the|
|---|---|---|---|---|
|King and five-parameter models for the single-crystalline cell|||||
|type|||||
|Solar|Temperature|Maximum power [W/m²]|||
|[W/m²]|["C]|NIST|King Five-parameter||
|1000.0|25.0|133.4|133.4 133.4||
|882.6|39.5|109.5|111.4 110.6||
|696.0|47.0|80.1|82.0 82.4||
|465.7|32.2|62.7|61.1 61.0||
|189.8|36.5|23.8|22.5 22.3||

|Fig. 9. Current|vs|voltage for the|triple junction|cell type|
|---|---|---|---|---|
|predicted by the five-parameter model (solid lines), the King|||||
|model (closed circles) and measured by NIST (open circles) for|||||
|four operating conditions. (Note: results are for 2 panels in series.)|||||
|Table 2|||||
|Maximum|power values|from NIST|measurements|and the|
|King and type|five-parameter|models for|the poly-crystalline|cell|
|Solar|Temperature|Maximum power [W/m²]|||
|[W/m²]|["C]|NIST|King Five-parameter||
|1000.0|25.0|125.8|125.8 125.8||
|882.6|39.5|106.8|109.3 105.6||
|696.0|47.0|77.4|79.1 78.1||
|465.7|32.2|56.6|56.9 55.8||
|189.8|36.5|21.2|18.5 20.6||

Fig. 7. Current vs voltage for the poly-crystalline cell type

predicted by the five-parameter model (solid lines), the King model (closed circles) and measured by NIST (open circles) for four operating conditions and the SRC condition (dotted line).

|86|||W. De Soto et al. / Solar Energy 80 (2006) 78–88||
|---|---|---|---|---|
|Table 3|||||
|Maximum King and five-parameter models for the silicon thin film cell type|power|from NIST|measurements|and the|
|Solar|Temperature|Maximum power [W/m²]|||
|[W/m²]|["C]|NIST|King Five-parameter||
|1000.0|25.0|104.0|104.0 104.0||
|882.6|39.5|83.7|87.3 85.5||
|696.0|47.0|59.9|62.3 62.3||
|465.7|32.2|40.8|43.2 44.3||
|189.8|36.5|14.4|15.7 16.3||

King!s model, does not require parameters that need values to be predetermined by additional experiments. The pre- dictions from the five-parameter model are shown to agree well with both the King model results and the NIST measurements for all four cell types over a range of operating conditions. The differences between the experimental data and the five-parameter model could be reduced if additional experimental data, e.g., I–V curves at two radiation levels, were used to determine the reference parameters.

Acknowledgements

We would like to thank the Graduate Engineering

Table 4

Research Students (GERS) for their financial support Maximum power values from NIST measurements and the

|Maximum|power|from NIST|measurements|and|
|---|---|---|---|---|
|King and five-parameter models for the triple junction amor- phous cell type|||||
|Solar|Temperature|Maximum power [W/m²]|||
|[W/m²]|["C]|NIST|King|Five-parameter|
|1000.0|25.0|115.8|115.8|115.8|
|882.6|39.5|94.2|98.9|100.8|
|696.0|47.0|78.5|81.2|76.8|
|465.7|32.2|51.7|57.8|61.2|
|189.8|36.5|22.6|25.4|22.0|

and Hunter Fanney and Mark Davis from the National Institute of Standards and Technology (NIST) for providing the data we used to validate the models. We especially wish to thank Mark Davis for his help and in- sight. We would also like to thank Michae¨l Kummert for his help in transforming the data to a convenient form.

the experimental data and five-parameter results differ, such as the maximum power points for triple-junction cell in Fig. 9, the King model and five-parameter models tend to agree fairly well. The agreement could be im- proved if manufacturers were to provide two different I–V curves (one for low irradiance and one for high irra- diance) instead of just one. The two curves could be used to generate an improved set of reference parameters (aref, IL,ref, Io,ref, Rs,ref, Rsh,ref).

7. Conclusion The five-parameter model presented in this paper uses only data provided by the manufacturer with semi-empirical equations to predict the cell I–V curve (and thus the power) for any operating condition. The model requires a one-time calculation of the five param- eters (aref, Io,ref, IL,ref, Rs,ref, and Rsh,ref) at reference con- ditions. These values are then used with in the model to calculate the parameters at other operating conditions, making it possible to predict the power output at any operating conditions. Comparisons with experimental data provided by NIST (Fanney et al., 2002a) have shown that the five-parameter model can be an accurate tool for the prediction of energy production for single- junction cell types. The five-parameter model uses only data provided by the manufacturer, and in contrast to
Appendix. King’s model

King!s model shown in Eqs. (A.1)–(A.9), calculates the short circuit current (Isc), current and voltage at the maximum power point (Impand Vmp, respec- tively), the currents at two intermediate points (Ixand I xx), and the open circuit voltage (Voc). !"!" I sc¼ Isc;ref <u>M</u> ½1 þ aIscðTc# Tc;refÞ) <u>GbKsaðhÞþGd</u> MrefGref ðA:1Þ I mp¼ Imp;ref½coEeþ c₁E²)½1 þ aIðTc# Tc;refÞ) ðA:2Þ !" e $~ mp 2e<u>aIscþ aImp</u> I x¼ Ix;ref½c₄Eeþ c₅E) 1 þ ðTc# Tc;refÞ 2 ðA:3Þ I xx¼ Ixx;ref½c₆Eeþ c₇E 2e

)½1 þ a₁mpðTc# Tc;refÞ) ðA:4Þ
2 Vmp¼ Vmp;refþ c₂NsdðTcÞ lnðEeÞþc₃Ns½dðTcÞ lnðEeÞ) þ bV mpEeðTc# Tc;refÞð A:5Þ

Voc¼ Voc;refþ NsdðTcÞ lnðEeÞþbV ocEeðTc# Tc;refÞ ðA:6Þ Pmp¼ ImpVmpðA:7Þ

E ¼ <u>I</u> <u>sc</u> ðA:8Þ e I ½1 þ a ðT # T Þ) sc;ref Isc c c;ref <u>n</u> <u>D</u> <u>kTc</u> dðTcÞ¼ q ðA:9Þ

Coefficients c0–7and nD, the diode factor, are given in Table A.1.

Table A.1 Values provided by NIST for the different cell types Type of cell Silicon thin film Single-crystalline Poly-crystalline Three-junction amorphous

|Type of cell||Silicon thin film|Single-crystalline|Poly-crystalline|Three-junction amorphous|
|---|---|---|---|---|---|
|At reference conditions||||||
|P|(W)|103.96|133.40|125.78|57.04|
|I (A)||5.11|4.37|4.25|4.44|
|V|(V)|29.61|42.93|41.50|23.16|
|I|(A)|4.49|3.96|3.82|3.61|
|V|(V)|23.17|33.68|32.94|16.04|
|NOCT (K)||316.15|316.85|316.45|311.05|
|Temperature coefficients||||||
|a (A/K)||0.00468|0.00175|0.00238|0.00561|
|a =I|(1/K)|0.000916|0.000401|0.000560|0.001263|
|a (A/K)||0.00160|#0.00154|0.00018|0.00735|
|a =I|(1/K)|0.000358|#0.000390|0.000047|0.002034|
|b (V/K)||#0.12995|#0.15237|#0.15280|#0.09310|
|b =V|(1/K)|#0.004388|#0.003549|#0.003682|#0.004021|
|b (V/K)||#0.13039|#0.15358|#0.15912|#0.04773|
|b =V King model parameters determined by NIST (Sjerps-Koomen et al., 1996)c [http://www.sandia.gov/pv/docs/Database.htm|(1/K](http://www.sandia.gov/pv/docs/Database.htm|(1/K))|#0.005629|#0.004560|#0.004830 –c₇ were obtained from Sandia|#0.002976|
|a₀||0.938110|0.935823|0.918093|1.10044085|
|a₁||0.062191|0.054289|0.086257|#0.06142323|
|a₂||#0.015021|#0.008677|#0.024459|#0.00442732|
|a₃||0.001217|0.000527|0.002816|0.000631504|
|a₄||#0.000034|#0.000011|#0.000126|#1.9184E#05|
|b₀||0.998980|1.000341|0.998515|1.001845|
|b₁||#0.006098|#0.005557|#0.012122|#0.005648|
|b₂||8.117E#04|6.553E#04|1.440E#03|7.25E#04|
|b₃||#3.376E#05|#2.730E#05|#5.576E#05|#2.916E#05|
|b₄||5.647E#07|4.641E#07|8.779E#07|4.696E#07|
|b₅||#3.371E#09|#2.806E#09|#4.919E#09|#2.739E#09|
|c₀||0.9615|0.9995|1.0144|1.072|
|c₁||0.0368|0.0026|#0.0055|#0.098|
|c₂||0.2322|#0.5385|#0.3211|#1.8457|
|c₃||#9.4295|#21.4078|#30.2010|#5.1762|
|c₄||0.967|0.9980|0.9931|1.059|
|c₅||0.033|0.0020|0.0069|#0.059|
|c₆||1.12|1.159|1.104|1.188|
|c₇||#0.120|#0.159|#0.104|#0.188|
|n||1.357|1.026|1.025|3.09|
|Other parameters||||||
|N||40|72|72|22|
|E (eV) at 25 "C||1.12|1.12|1.14|1.6|

mp,ref sc,ref oc,ref mp,ref mp,ref

Isc Isc sc;ref Imp Imp mp;ref V oc V ococ;ref V mp V mpmp;ref 4

D

s g

References Fanney, A.H., Davis, M.W., Dougherty, B.P., 2002b. Short- term characterization of building-integrated photovoltaic De Soto, W., 2004. Improvement and validation of a model for panels. In: Proceedings of the Solar Forum, Sunrise on the photovoltaic array performance. M.S. Thesis, Mechanical Reliable Energy Economy, ASES, Reno, NV, June 15–19. Engineering, University of Wisconsin-Madison. King, D.L., 2000. Sandia!s PV Module Electrical Performance Duffie, J.A., Beckman, W.A., 1991. Solar Engineering of Model (Version, 2000). Sandia National Laboratories, Thermal Processes, second ed. John Wiley & Sons Inc., Albuquerque, NM, September 5. New York. King, D.L., Kratochvil, J.A., Boyson, W.E., Bower, W.I., 1998. Fanney, A.H., Dougherty, B.P., Davis, M.W., 2002a. Evaluat-Field Experience with a New Performance Characterization ing building integrated photovoltaic performance models. Procedure for Photovoltaic Arrays presented at the 2nd In: Proceedings of the 29th IEEE Photovoltaic Specialists World Conference and Exhibition on Photovoltaic Solar Conference (PVSC), May 20–24, New Orleans, LA. energy Conversion, Vienna, Austria, July 6–10.

King, D.L., Boyson, W.E., Kratochvil, J.A., 2004. Photovoltaic Sandia National Laboratories, 2002. Database of Photovoltaic array performance model, Sandia Report No. SAND2004-Module Performance Parameters. Available from: <http:// 3535 available from US Department of Commerce, www.sandia.gov/pv/docs/Database.htm>.

|Schroder,|D.K., 1998.|Semiconductor|Material and|Device|
|---|---|---|---|---|
|Characterization, second ed. John Wiley & Sons Inc., New|||||
|York.|||||
|Sjerps-Koomen, E.A., Alsema, EA., Turkemburg, W.C., 1996.|||||
|A simple model for PV module reflection losses under field|||||
|conditions. Solar Energy 57 (6), 421–432.|||||
|Van Zeghbroeck,|B.,|2004. Principles|of Semiconductor||
|Devices. ~bart/book/book/chapter2/ch2_3.htm>.|Available|from: <[http://ece-www.colorado.edu/|||](http://ece-www.colorado.edu/|||)

National Technical Information Service, 5285 Port Royal Schroder, D.K., 1998. Semiconductor Material and Device Rd, Springfield, VA 22161. Klein, S., 2005. EES—Engineering Equation Solver, F-Chart Software. Available from: <www.fchart.com>. Messenger, R.A., Ventre, J., 2004. Photovoltaic Systems Engineering, second ed. CRC Press LLC, Boca Raton, FL. Nelson, J., 2003. The Physics of Solar Cells. Imperial College Press, London.

## <u>Update</u> Solar Energy

##### Volume 81, Issue 1, January 2007, Page 150

##### DOI: <u>[https://doi.org/10.1016/j.solener.2006.05.001](https://doi.org/10.1016/j.solener.2006.05.001)</u>

Solar Energy 81 (2007) 150 www.elsevier.com/locate/solener

#### Erratum

Erratum to ‘‘Improvement and validation of a model for photovoltaic array performance’’ [Solar Energy 80 (2006) 78–88]

### W. De Soto, S.A. Klein*, W.A. Beckman

Solar Energy Laboratory, University of Wisconsin-Madison, 1500 Engineering Drive, Madison, WI 53706, USA

Available online 23 August 2006

We apologize to readers of Solar Energy Journal for this There is a sign error in Eq. (6a). The corrected equations error. should appear as !! <u>dðIV Þ</u>!! <u>dI</u>!! ! ¼ Impþ Vmp¼ 0 ð6aÞ dVmpdV !mp

DOI of original article: 10.1016/j.solener.2005.06.010 * Corresponding author. Tel.: +1 608 263 5626; fax: +1 608 262 8469. E-mail address: klein@engr.wise.edu (S.A. Klein).

0038-092X/$ - see front matter ! 2006 Elsevier Ltd. All rights reserved. doi:10.1016/j.solener.2006.05.001
