## RAPID AND ACCURATE DETERMINATION OF SERIES RESISTANCE AND FILL FACTOR LOSSES IN

## INDUSTRIAL SILICON SOLAR CELLS

S. Bowden and A. Rohatgi.
School of Electrical and Computer Engineering Georgia Institute of Technology Atlanta GA 30332–0250 USA Email: bowden@ece.gatech.edu

ABSTRACT: Lower than ideal fill factors (FF) are caused by parasitic series (Rs) and shunt (Rshunt) resistances, and non-ideal diode properties. The challenge is to quantify the FF losses quickly, simply and without ambiguity. Extracting the parameters by fitting the illuminated or dark measured data with the double diode equation is inaccurate since the externally apparent Rs is not constant; it varies with illumination level and electrical load. It is shown that the variations in Rs are not a second order effect only noticeable in laboratory cells, but that the variations are even more important in industrial solar cells and many methods underestimate Rs. It is also common to estimate the cause of FF loss by visual inspection of the IV curve, but this also leads to a misinterpretation of loss mechanisms. A very high Rs affecting 10% of the cell causes a slope at short circuit current that is very similar in appearance to a cell with low Rshunt, and that a high Rs affecting 50% of the cell appears similar to high second diode saturation current. A superior method to measure Rs at the maximum power point is to shade the cell to 0.1 suns and measure open circuit voltage and short circuit current. Using this extra data with standard one sun measurements also, and reveals non-ohmic contacts. measures the average diode ideality factor, Rshunt Keywords: Characterization – 1: Modelling – 2: Series Resistance – 3.

1. INTRODUCTION The fill factors (FF) of commercial solar cells are lower than ideal primarily due series resistance (Rs), which will become larger as substrate size increases. However, in both laboratory and production cells, the fill factor is not solely limited by the Rs but also by effects such as low shunt resistance and non-ideal diode parameters. Separating out the effects of the various losses is essential for diagnosing fabrication problems. A cell production line additionally requires a very fast measurement of the cell parameters if they are to be at all useful. Ideally such methods would be taken from the one sun IV curve so that no extra measurements need to be taken. However, the one sun illumination curve alone has insufficient data to separate out the losses [1].
2. CURVE FITTING TO DARK AND ILLUMINATED IV CURVES. Simple one-dimensional models of solar cells (such as PC1D) have a single constant resistor in series with the <u>cell, as shown in Figure 1.</u>
Rs n = 1 n = 2 R sh JL J01 J02

Figure 1: Double diode model of the cell.

The cell in Figure 1 is described by the following equation when illuminated. The extra –1 terms of the ideal diode equation are irrelevant at the current levels involved.

*J* = *JL*− *J₀₁*exp⎜⎛ *s* *J₀₂* exp⎜⎛ *s s* *q*(*V* + *JR*) ⎟⎞ − *q*(*V* + *JR*) ⎟⎞ − *V* + *JR* ⎝ *kT* ⎠ ⎝ 2*kT* ⎠ *Rshunt* In the dark, JL is equal to zero, the current flows into the cell and the equation is:

*J* = *J₀₁*exp⎜⎛ *s* *J₀₂* exp⎜⎛ *s s* *q*(*V* − *JR*) ⎟⎞ + *q*(*V* − *JR*) ⎟⎞ + *V* − *JR* ⎝ *kT* ⎠ ⎝ *kT* ⎠ *Rshunt*

Using the equations it should be possible to fit the measured data to extract the parameters Rs, Rshunt, J₀₁ and J₀₂ assuming they are constant. Parameter fitting has been done with various levels of sophistication to improve extraction speed and to cope with the effects of measurement noise: see [2] [3] and references therein. However, Rs is not constant but is a function of J, an effect even more pronounced in commercial cells. This leads to errors in extraction as shown below.

3. MODELLING THE EFFECT OF DISTRIBUTED SERIES RESISTANCE The externally seen Rs of a solar cell is composed of a variety of internal resistances. In a typical commercial solar cell the dominant resistances are: contact resistance (Rc), resistance of the busbars (Rbb), finger resistance (Rf), and lateral conduction in the emitter, (Remitter). For screen- printed cells, the contribution of the rear contact is minimal due to the full metal coverage and low base resistivity. The relative importance of each resistor is dependent on the current flow in the cell. If the current paths were identical at all bias levels it would be possible to describe Rs by a single constant value. However a cell is a network of diodes and resistors causing variations in the path the current flows, which produce variations in the externally measured Rs. The fraction of current flowing through a resistor determines its contribution to the externally measured Rs. In commercial silicon solar cells, points near the contact pads will have a much lower Rs than those at the end of high resistivity screen-printed fingers. Processing errors with breaks in fingers or incompletely printed sections further increase the distributed nature of To examine the effects of distributed Rs, a model Rs. described below is used where part of the cell is affected by Rs and part of the cell is not. There exist more complicated models for distributed Rs [4] but the model used here simplifies the discussion.

|cell with Rs & double diode fit Rs = ΔV/J|cell with no Rs|
|---|---|
|0 0.1 0.2 0.3 0.4 0.5 voltage (V) affecting half the cell (R Figure 2: Cell with a medium R s = 3 Ω, C = 0.5). The rounding at the maximum point appears very similar to a cell with a high J₀₂ yet it is caused. s The actual R is calculated from the voltage difference s between the ideal curve and the R affected curve at each s current level as shown below. Also shown is the R s The effect of distributed R is quite different in the s dark and light cases. In the light case the current is generally generated uniformly across the device and must be conducted to the contacts. In the dark case the current is conducted along the most favourable conduction path. Regions of higher resistivity (a section that is not printed or regions between the contacts) are bypassed so the apparent seen externally is much lower in the dark case than in the illuminated case. Additionally in the dark case the region of the curve that is affected by R is a different s region of the curve to that affected in the illuminated case. Illuminated Rs Dark Rs 0102030|0.6 s in the|

15 **current (mA)** 10

solely by R

dark case.

Rs

Figure 1: solar cell in which only part of the cell is affected

by Rs. In the dark the JL elements are removed and the current direction is reversed so it flows into the cell.

In the model of Figure 1, Rs affects only part of the cell. The proportion of the cell affected by the high Rs is denoted by C. Varying C between zero (no part of the cell affected by Rs) and one (all the cell is affected by Rs) shows how a distributed Rs affects final IV curve. The two diodes are identical with J₀₁ of 1.5 × 10 -12 A/cm² and a Jsc of 35 mA/cm². The corresponding currents are adjusted according to the area specified by C. To further simplify the discussion Rshunt and J₀₂ are set to zero. Setting Rs to zero gives the ideal cell curve without the effects of Rs. The cell Rs at each current level is calculated from the difference between the curves as shown in Figure 2.

3.1. Rs affects entire cell The simplest case is where Rs affects the entire cell so that C = 1 and the elements of region B are removed. RsJ₀₁ J₀₂
<u>(Ωcm²) (A/cm²) (A/cm²)</u> Actual 1 1.5e-12 0 Illuminated fit 0.998 1.51e-12 0 Dark fit 1 1.5e-12 0 Dark/Light difference 1--

The table above shows that with C = 1 the model reduces to the traditional example with a constant Rs. In this case the Rs is constant for both the illuminated and dark cases at 1 Ω.

The “Dark/Light difference” measures Rs from:

*Rs*= <u>dark sc oc</u>, <u>V (I) − V</u> *I* *sc* where Vdark(Isc) is the voltage of the cell in the dark at a current level equivalent to Isc.

1.8
1.6
1.4
1.2 1
0.8
0.6 **Extrernal Rs (ohm)**
0.4
0.2 0
**current (mA)**

Figure 3: The internal resistance is constant but varies

externally. Imp = 33 mA/cm².

RsJ₀₁ J₀₂ (Ωcm²) (A/cm²) (A/cm²) Actual 1 1.5e-12 0 Illuminated fit 0.54 1.1e-12 4.8e-12 Dark fit 0.2 1.5e-12 0 Dark/Light difference 0.16--

3.3. Rs Appears Like Low Rshunt. Another possibility is where a very high resistance affects a small portion of the cell but the rest of the cell is relatively unaffected. This happens where there is
3.2. Series resistance appears like high J₀₂. The next case considered is where a large section of the cell is affected by a high Rs. This corresponds to a cell with wide finger spacing and a high emitter sheet resistivity. Portions near the fingers will have much lower Rs that those equidistant from the fingers. The points show the double diode fit. While the double diode equation fits the curve accurately it does not correctly describe the physical mechanisms within the cell.

incomplete printing with interruptions in the grid lines or coincide. The translation of Voc(shaded) by the same amount areas of the cell where there is no metallisation at all. gives the point marked with a cross in the figure above. This lies on the IV curve of the cell if there was no Rs.

||I (-0.5)|
|---|---|
|0 0.1 0.2 0.3 0.4 0.5 0.6||
|voltage (V) affecting a small portion of Figure 4: Cell with a high R s = 150 Ω, C = 0.1). The resulting IV curve looks s just like a cell with a low R but again the effect is due shunt = 30 mA/cm² mp The double diode fit in the above curve gives R = s 1.2e-12, J₀₂ = 1.5e-8 A/cm². R =200 Ωcm². shunt Despite being affected solely by R the curve is very s similar in appearance to that affect by a low R. shunt J₀₁ J₀₂ s (A/cm²) (A/cm²) (Ωcm²)|V = -0.5 only extra data needed for R and I sc needed for R shunt by the current. V oc (|
|Actual 1.1 1.5e-12 0 Illuminated fit 0 1.2e-12 1.5e-8 Dark fit 0.0013 1.4e-12 7e-14 Dark/Light difference 0.06 - - EASURING THE IV C URVE WITHOUT R S Given the problems with determining R from fitting s routines, an alternative is required that measures R at the s maximum power point. The simplest are the J V sc oc|R = s I sc (full) The ideal level of shading is s 5.2. Measurement of R|
|curve[5][6] or the Suns V curve[7]. These are equivalent oc so long the cell J is proportional to the light intensity, a sc situation that is commonly true and easily verified. The J V curve relies on the principle of sc oc superposition, i.e. that in the absence of R the illuminated s IV curve is simply the dark diode curve shifted by J. sc and J are unaffected by R. V Additionally the cell V oc sc s oc is unaffected by R since no current is drawn. For the s current, as long as the R is less 10 Ωcm² there is no affect s on J [8]. While the J V curve is not influenced sc sc oc it is still affected by R and J₀₂. shunt RACTICAL I MPLEMENTATION A measurement system requires speed, reliability and simplicity. There are a number of variations depending on|R = shunt I and V oc V oc (full|

**translated**

**0.1 sun curve**
Isc(full)

VA,Isc(full)-Isc(shaded)

**1 sun**

15 **current (mA)** 10

0 I sc(shaded)

<u>0.1 sun</u> V V oc(shaded) oc(full)
Figure 5: The open circles are the measured data points.

The three points on the fully illuminated curve are already measured during the normal IV curve measurement. The s measurement are the cell Voc under shading. The point in reverse bias is only.

The series resistance is simply the difference in voltage between the ideal curve and the real curve divided

− *V* *shaded*) *A* − *Isc*(*shaded*)

The level of shading only needs to be approximate. *I* *mp*= *Isc*( *full*) − *Isc*(*shaded*)so that R is reported at the maximum power point.

shunt The shunt resistance is simply the slope of the IV curve in reverse bias, with a reverse bias voltage of 0.5 V:

0.5
( −0.5)− *Isc*(*shaded*) While it is possible to use the one sun data, the measurement is more accurate in the shaded case since Rs has a smaller effect at lower light intensities and the current difference is more obvious.

5.3. Measurement of the Ideality Factor The cell ideality factor is defined in a variety of
the cell (R

solely to Rs. J

0.01 Ω, J₀₁ R
4. M

|from R||different ways. In this case it is defined as the average||
|---|---|---|---|
|by R||ideality factor between the maximum power point (MPP) and is denoted by n.||
|5. P the specifics of the system and the degree of automation||Looking at the data of Figure 5 in a different way gives a good measure of the ideality factor from MPP to V||
|required.||If n > 1, there is a high junction leakage current due to either a high J₀₂ or low R|. It is not easy to determine|
|5.1. Measurement of Series Resistance||which. An n < 1 indicates a non-ohmic contact, typically||
|To add to an existing system that already measures the||an extra diode at the rear contact. By itself n is a useful||
|full IV curve, all that is needed is to shade the cell to about||diagnostic tool.||
|10% light intensity and then measure the cell I||So long as the level of shading corresponds to about||
|V|. From the argument above the shaded curve can|MPP the n factor can be used to determine the fill factor of||
|be translated upwards so that the two I||the cell without the effects of R|[9].|

s s

|n =|− V|⋅ q|
|---|---|---|
|ln I|− ln I|kT|

oc (shaded)

oc: ) *oc*(*shaded*)

# ()( )sc( full) sc(shaded)

shunt

sc (shaded) and

sc measurements s

<u>v − ln(v + 0.72) qVoc( full)</u> *FF₀* 8

|oc = NOWN P verifying that the I tester and remeasure the cell I probes are removed, R and SunsVoc pseudoFF|oc v + 1 oc ROBLEMS sc(shaded) this is not the case it implies that the one sun I XPERIMENTAL RESULTS s|, where Since they both describe FF in the absence of R should agree with the pseudoFF[7] from SunsVoc measurements. The pseudoFF will be more accurate since it is not affected by temperature fluctuations during the measurement and the shading level does not need to be The shading method relies on several assumptions for accurate results. The first requirement is that the cell I proportional to the light intensity. This is easy to test for by. Secondly the temperature of the cell must be stable. is strongly affected by temperature and shading may reduce the cell temperature. The measurement should be done as quickly as possible and a good contact between the block and the cell. At Georgia Tech we use an automated and V sc A screen-printed cell of 100 cm² was measured. The cell has two straight parallel busbars running right across the cell and 5 cm in from the edges. The fingers run at right angles and are also 5 cm long. The cells were first tested by placing a set of probes at the ends of the busbars giving four sets of top contact probes. As each set of contact increases but R factor stay the same. There is also good agreement between|v oc is a constant fraction of I. oc|= nkT sc shunt|, FF₀ s is sc. If sc(full) is affected and ideality|
|---|---|---|---|---|---|
|||SunsVoc 4 probes 3 probes 2 probes 1 probe||||

1 probe 7 2 probes 3 probes 6 4 probes

5 chosen. 4

6. K**Rs (ohmcm²)**3
2

by Rs0 Voc0123 **current (A)**

Figure 7: Not only does the cell Rs increase as each probe

is removed but the variation on Rs also increases, as evidenced by the increasing slope. Rs is calculated from the difference between the SunsVoc and the illuminated IV curve.

7. E
8. CONCLUSION Distributed effects in Rs can cause the IV curve to look like one with a high ideality factor or one with a low shunt resistance. Guessing if a cell is limited by Rs, Rshunt or high J₀₂ by looking at the illuminated IV curve has no sound basis. The variation in Rs typically precludes the use of the use of fitting algorithms. Shading the cell to around
FF₀ 0.1 suns and measuring the cell Voc, Isc and current at –0.5 volts reveals a wealth of information about the cell. Even

3.5 without calibration it provides: the effective Rs at
maximum power point, shunt resistance, average diode 3 ideality factor between Vmpand Voc, and shows the presence of non-ohmic contacts such as rear surface

2.5
diodes. Using a calibrated shading also indicates if Isc at one sun is affected by Rs. The technique can be used on 2 existing or automated apparatus with only minor modifications.

1.5
Current (A)

19. REFERENCES
st

0.5 [1] J. Zhao, A. Wang and M.A. Green, 21 IEEE PVSC, p.
333 (1990) 0 [2] E. Van Kerschaver, R. Einhaus, J. Szlufcik, J. Nijs and 0 0.1 0.2 0.3 0.4 0.5 0.6 R. Mertens, EC 14 (1997) Voltage (V) [3]A. R. Burgers, J. A. Eikelboom, A. Schonecker, W. C. th Sinke, 25 IEEE PVSC, p569 (1996)

Figure 6: As top contact testing probes are removed the th

[4] R.T. Otterbein and D. L. Evans, 14 IEEE PVSC p574- cell Rs increases. The SunsVoc measurement gives the cell 8 (1980) IV curve without the effects of Rs. rd [5] A.G. Aberle, S.R.Wenham and M. A. Green, 23 IEEE Prob FF Rsn RshuntFF₀ Pseudo PVSC, p. 133, (1993) es Ωcm² Ωcm² FF [6]M. Wolf and H. Rauschenbach, Advanced Energy 4 0.75 1.3 1.09 1341 0.816 0.812 Conversion, V 3. pp 455-479 Apr.1963 3 0.73 1.7 1.09 1344 0.816 0.812 [7]R. A. Sinton and A. Cuevas, 16th European PVSEC p 2 0.67 3.2 1.09 1353 0.816 0.812 1152 (2000). 1 0.53 6.6 1.10 1344 0.815 0.812 [8] P.P. Altermatt, G Heiser, A.G. Aberle, A. Wang, J. Zhao, S.J. Robinson, S. Bowden and M.A. Green, Progress in Photovoltaics, Vol 4 pp 299-414 (1996)

[9] M.A. Green, “Solar Cells-Operating Principles, Technology and System Application”, UNSW, Australia.
