Available online at www.sciencedirect.com

# ScienceDirect

Solar Energy 122 (2015) 1235–1244 www.elsevier.com/locate/solener

# A novel datasheet-based parameter extraction method for a single-diode photovoltaic array model

⇑

## Jun-Young Park, Sung-Jin Choi

School of Electrical Engineering, University of Ulsan, 93 Daehak-ro, Nam-gu, Ulsan 680-749, Republic of Korea

Received 12 June 2015; received in revised form 4 October 2015; accepted 2 November 2015 Available online 19 November 2015

Communicated by: Associate Editor Frank Nuesch

Abstract

This paper presents an effective parameter extraction algorithm for photovoltaic (PV) panels based only on datasheet values, which is very useful in the development phase of a power conditioning system (PCS). In order to increase the accuracy of a PV circuit model, especially in the vicinity of the maximum power point (MPP), the objective function incorporating the MPP error is formulated in the single-diode model, and a pattern search algorithm is utilized to optimize the parameters. In addition, the parameter search region and initial value are also discussed and criteria for the model accuracy in the MPP region are established. Comparison study using mea- surement data from the crystalline PV panel shows that the proposed method is a more accurate, uniform, and faster method of param- eter extraction that is less dependent on the panel type and user skill. Furthermore, with a simple modification, this method successfully describes the PV characteristics even for various temperatures and irradiation levels in addition to the standard test condition (STC). 2015 Elsevier Ltd. All rights reserved.

Keywords: Photovoltaic panel; Single-diode model; Parameter extraction; Pattern search optimization

1. Introduction Among the various methods used to determine the PV
equivalent circuit, modeling techniques based on only data- The output characteristic of a real photovoltaic (PV) sheet values are practically valuable because they can be panel is highly non-linear and depends on ambient temper-used to extract circuit parameters for a real PV panel with- ature and irradiation level. Therefore, instead of real pan-out additional measurements, and they provide rapid per- els, a PV equivalent circuit model is a very powerful tool formance estimation with high accuracy (Wagner, 1999; in the development phase of a power conditioning system Kezzar et al., 2014; Xiao et al., 2004; Crispim et al., (PCS). Among the performance measures of a PV model, 2007; Villalva et al., 2009; Siddique et al., 2013; Sera the accuracy near the maximum power point (MPP) is et al., 2007; Chan and Phang, 1987; Park and Kim, the most important because a PCS usually adopts MPP 2014). By investigating the limitations of conventional tracking (MPPT) to maximize the utilization of the PV works, this paper presents a more effective method for panels during the daytime, which increases the overall effi-parameter extraction in datasheet-based modeling. ciency of the photovoltaic system (Cubas et al., 2014).

2. Problem definition
⇑ Corresponding author. Tel.: +82 52 259 2716; fax: +82 52 259 1686. A PV panel can generally be described using a single- E-mail address: sjchoi@ulsan.ac.kr (S.-J. Choi). diode model that has a current source with a diode in

[http://dx.doi.org/10.1016/j.solener.2015.11.001](http://dx.doi.org/10.1016/j.solener.2015.11.001) 0038-092X/ 2015 Elsevier Ltd. All rights reserved.

J.-Y. Park, S.-J. Choi / Solar Energy 122 (2015) 1235–1244
parallel, as shown in Fig. 1(a). This model accounts for the non-linear I–V characteristic of a PV panel (Ouennoughi and Chegaar, 1999; Chegaar et al., 2001). The equation to determine the I–V characteristic is <u>vþiRs</u> i ¼ IphIoeN s AV T1 ðv þ iRsÞGshð1Þ

where VTis the thermal voltage of the diode. In order to represent a PV panel using the single-diode model, the five circuit parameters of photovoltaic current (Iph), dark satu- ration current (Io), series resistance (Rs), shunt conductance (Gsh), and diode ideality factor (A) must be determined only from the panel datasheet, which specifies the number of cells (Ns), the voltage at maximum power (Vmpp), the current at maximum power (Impp), the open circuit voltage (Voc), and the short circuit current (Isc). Some papers also describe the shunt conductance (Gsh) as the inverse of shunt resistance (Rsh). Using these values, a PV circuit model that provides almost the same I–V characteristic as that of the real PV panel can be obtained. Many researchers have presented parameter extraction methods that make use of four conditions provided in datasheets:

(1) The I–V curve passes through the MPP.
(2) The slope of the P–V curve is null at the MPP.
(3) The I–V curve starts at (Voc, 0).
(4) The I–V curve ends at (0, Isc). These conditions are graphically demonstrated in
Fig. 1(b). The extraction of Ioand Iphaccording to condi-

tions (3) and (4) is straightforward. However, obtaining the other three parameters, Rs, Gsh, and A, is rather compli- cated because there are only two conditions available for

i + Rs

|A, I|1||R|
|---|---|---|---|
|ph o|sh|ph o|s|
||||sh|

I v G

-

**(a)**
i**dP/dV**p **(Isc, 0)** I mpp **MPP**

determining three unknowns. Furthermore, a numerical method is necessary for solving the simultaneous equations because of their implicit form.

3. Conventional algorithm Many researchers investigated effective algorithms in order to solve the under-determined situation of the PV modeling and they can be were classified under three differ- ent groups. In the first group, they reduced the number of parame- ters such that the number of unknown equals to the num- ber of constraints, and extract model parameters by solving simultaneous equations (Wagner, 1999; Kezzar et al., 2014; Xiao et al., 2004; Crispim et al., 2007). For example, Wagner (1999) assumed Gshto be very low and thus excluded it from the equivalent circuit as shown in
Fig. 2(a). Although such technique simplifies calculation
 steps and thus is computationally very fast, it inevitably shows poor accuracy for some PV panels due to the reduced number of model parameters. Therefore, it does not always guarantee the model accuracy. Instead of omitting model parameter, the other group fixed the unknown parameter to a reasonable value in advance (Villalva et al., May 2009; Siddique et al., 2013). For example, the diode ideality factor (A) can be set before
i + Rs 1 I phA, Io Removed v Gsh

-

**(a)**
i + s Fixed value I A, I 1 v G

-

**(b)**
i1 **(Isc, 0)** Rsh I mpp **Additional assumption** 1 Rs

### (0, Voc)

Vmpp v

**(c)**
Fig. 2. Key concepts in conventional algorithms. (a) group I, (b) group II,

(c) group III.
### (0, Voc)

Vmpp v

**(b)**
Fig. 1. Characteristic of a PV panel. (a) Single-diode model, (b) critical

points in the I–V curve.

beginning the extraction process as shown in Fig. 2(b). Among them, Villalva (Villalva et al., 2009) shows good accuracy with reduced complexity. However, the choice of diode ideality factor heavily relies on user’s skill and experience, so an inappropriate selection can lead to incor- rect model parameters. In order to clarify this limitation, different P–V curves for a PV panel (KC200GT) are obtained by Villalva method in case of different assumption of A’s and plotted in Fig. 3(a). Although the maximum value is constant, P–V curve is slightly changed according to the A value. The third group introduced an extra slope condition of the I–V curve at the short circuit point (Sera et al., 2007; Chan and Phang, 1987) or the open circuit point (Park and Kim, 2014) as shown in Fig. 2(c), which makes the number of unknown parameters equal to the number of conditions For example, Pedro (Sera et al., 2007) used the assumption that the shunt resistance of the model can be obtained by an inverse of the tangential slope evaluated at short circuit point in an I–V curve. However, an approx- imation made at the far ends of the I–V curve does not guarantee model accuracy in the MPP region. Fig. 3(b) illustrates possible error caused by adopting this approxi- mation. It shows an I–V curve for a PV panel (KC65GT) predicted by Pedro method. Consequently, conventional approaches result in performance degradation in terms of model accuracy especially near MPP. In order to enhance

the accuracy, a new method is introduced in the following section.

4. Proposed algorithm
Fig. 4 shows the overview of the proposed algorithm. At
 first, datasheet values are divided into two groups: MPP- related constraints and endpoint constraints. The MPP constraints are (1) the I–V curve passes through the MPP, and (2) the slope of the P–V curve is null at the MPP. The endpoint constraints are (3) the I–V curve starts at (Voc, 0), and (4) the I–V curve ends at (0, Isc). The former poses an under-determined problem set solved by optimiza- tion techniques that extract circuit parameters without reducing the number of parameters, fixing one of the parameters, or introducing an extra approximate condi- tion. The latter are reduced into simple simultaneous equa- tions with trivial solutions. Consequently, 5 unknown circuit parameters are obtained from only 4 datasheet conditions.
4.1. Objective function definition In this subsection, the objective function is derived from the MPP constraints. Applying condition (1) to Eq. (1), the following equation holds:
<u>V mppþI mpp Rs</u> I mpp¼ IphIoe N s AV TðV mppþ ImppRsÞGshð2Þ

The above equation can be reformulated in a new impli-

||220||||MPP±10%||
|---|---|---|---|---|---|---|
||200 180 160 140 120 100 80 Power (W) 60 40 20 0 0 4.5 4.0|5|MPP(A=1.0) MPP(A=1.5) Villalva(A=1.0) Villalva(A=1.5) 205 200 195 190 24 10 15 (a)|25 26 20 Voltage (V)|27 28 29 25 30 MPP±10%|35|
||3.5 3.0 2.5 2.0 1.5 Current (A) 1.0 0.5|4.0 3.5 3.0 15.25 Pedro measured|18.30||||
|Fig. 3. group III.|0.0 0|5|10 (b)|15 Voltage (V) Possible error caused by conventional algorithms. (a) group II, (b)|20|25|

cit form:

### f ðRs; Gsh; AÞImpp¼ 0 ð3Þ

On the other hand, the output power of a solar array can be described as a function of output voltage:

pðvÞ¼iv: ð4Þ

From the above equation, the first derivative of the P–V relation results in

Datasheet values : Vmpp, Impp, Voc, Isc (4 datasheet informations)

MPP conditions End-point conditions Optimization method Simultaneous equation

R, Gs sh, A Iph, Io

PV equivalent circuit model (5 unknown parameters)

Fig. 4. Overview of the proposed algorithm.

dp dðivÞ di ¼ ¼ i þ v: ð5Þ dv dv dv

Therefore, condition (2) can be represented as Eq. (6), and its implicit form is obtained as Eq. (7).

G <u>ðI</u> <u>sc</u> <u>=GshV ocþIscRs Þ</u> e <u>V mpp þ</u> N <u>I mpp</u> s AV T <u>Rs V oc</u> þ 1 <u>dp</u>sh <u>N sAV T</u> ¼ ImppVmpp <u>V mpp þImppRs V oc</u>¼ 0 dv@mpp 1 þ R G <u>ðI</u> <u>sc</u> <u>=GshV ocþIscRs Þ</u> eNsAV Tþ 1 s sh N sAV T

ð6Þ

### gR ðÞ¼s; Gsh; A 0 ð7Þ

Combining Eqs. (3) and (7), an objection function is defined as Eq. (8), and the optimal values of Rs, Gsh, and A that minimize this function are determined so that those three parameters simultaneously best match conditions (1) and (2). In other words, determining the Rs, Gsh, and A using only the MPP constraints is now possible.

|||2|2|
|---|---|---|---|
|s sh|s sh|mpp|s sh|
||||o|

EðR; G; AÞ f ðR; G; AÞI þ g ðR; G; AÞð 8Þ

Meanwhile, the remaining two parameters, I and Iph, can be directly obtained from the endpoint constraints. From Eq. (1) and conditions (3) and (4), the following two equations are obtained: <u>I sc Rs</u>

|I ¼ I|e I|R G||
|---|---|---|---|
|sc ph||sc s sh||
|ph o|oc sh|||
||ph sc|s|i i i i|
|o|||s|
|o sc|oc sc s|sh||

I o N s AV Tð9Þ

<u>V oc</u> I ¼ I eN s AV Tþ V G : ð10Þ

By eliminating I in Eqs. (9) and (10) with the assump- tion that Voc>> I R, which is widely accepted in many papers, I can be obtained as <u>V oc</u> I ¼½I ðV I R ÞG eN s AV T: ð11Þ

4.2. Parameter search region and initial value Any numerical method to solve non-linear problems needs to specify a search region for the parameter vari- ables. To implement the proposed algorithm, the search regions for Rs, Gsh, and A should be properly defined. The search range should not only be easily determined from the datasheet, but also physically meaningful. First, the series resistance, Rs, is ideally zero when there is no ser- ies loss. Its maximum value can be graphically obtained using the slope of a straight line connecting the short circuit point and MPP. Accordingly, the search range for Rsis given as <u>VocVmpp</u> 06Rs6 : ð12Þ
I mpp

Likewise, the shunt conductance, Gsh, has zero value when there is no leakage loss in the PV panel, and its max- imum possible value can found in a similar fashion. There- fore, the search range for Gshwill be given as

<u>I</u> <u>scImpp</u> 06Gsh: ð13Þ Vmpp

The diode ideality factor, A, is inherent from the mate- rial characteristic. For a silicon PV panel, it is better to define the search range for A as:

### 0 < A 6 2: ð14Þ

The objective function defined in Eq. (8) is highly non- linear and can cause a convergence issue in optimization algorithms, so the initial value of the solution should be carefully selected in order to prevent such issues. In this algorithm, it is reasonable to choose an initial search vector having ideal values for each parameter as follows:

### X₁ ¼½Rs;1Gsh;1A₁¼½0; 0; 1 : ð15Þ

4.3. Pattern search optimization algorithm Among the various methods (Peng et al., 2014; Ismail et al., 2013; Ishaque and Salam, 2011; Yuan et al., 2014; Soon and Low, 2012) to minimize the 3-dimensional objec- tive function given by Eq. (8), pattern search optimization was chosen. Because this method does not employ differen- tiation process of the objective function and any multi-dimensional problem is solved by sequences of 1-dimensional sub-problems, it is quite robust and simple, and thus can be easily implemented. Additionally, it shows good performance in short computation time (Venkataraman, 2009). In the pattern search algorithm, the solution vector, X, successively reaches the next solution Xi+1= X + a S using the search vector, Si, in the direction of the unit vec- tor of each parameter variable, i.e., S₁ = [1,0,0] for R, S₂ = [0,1,0] for Gsh, and S₃ = [0,0,1] for A. The search direction is cycled through the number of variables in an orderly manner, executing one additional search direction as the sum of the scalar product of the previous search directions. During this process, the scalar multiplier, ai,is determined in order to minimize the 1-dimensional objec- tive function, E(Xi+1). In this step to solve the single- variable minimization problem, aiis determined using the golden section algorithm. A flow chart of the proposed parameter extraction algorithm incorporating pattern search optimization is summarized in Fig. 5. If the termination conditions of the algorithm
### jDEj 6 e₁ ð16Þ

DX T DX 6 e ð17Þ 2

are met with e₁ = e₂ =1 10 8, the algorithm concludes with the optimal parameters. The termination conditions are based on the function decrease in each cycle and the change in the parameter variable.

5. Performance result To evaluate the performance of the proposed algorithm, nine crystalline PV samples – THERM Solartechnik AT50, BP Solar MSX60, Kyocera KC65GT, BP Solar MSX120,

**Start**

**Initialize X₁** **Set search vector Si=ei(i=1, 2, 3)**

**For Xi+1=Xi+ƄiSi(i=1, 2, 3)** **Calculate Ƅito minimize E(Xi+1)**

|Set up additional search step|||
|---|---|---|
||S₄=X₄-X₁|Update X₁ȠX₅|
||X₅=X₄+Ƅ₄S₄|Reset weighting factor Ƅ|
|Calculate Ƅ to minimize E(X )|||

**K** **4 5**

**^ůE^ƈ₁** <u>No</u> **QTůXTůXƈ₂**

**Yes** **Extract Rs, Gsh, A** **Calculate Iph, Io**

**End**

Fig. 5. Flow chart of the proposed algorithm.

Shell Solar SQ160PC, Kyocera KC200GT, Samsung LPC241SM, Trina Solar TSM245PC, and Hanwha Solar SF260 – are selected to extract PV circuit models. The datasheet values of each panel are shown in Table 1. Using only the datasheet values, the three conventional methods in Wagner, Villalva, and Pedro and the proposed method are tested using the following steps. First, from the Isc, Voc, Impp, Vmpp, and Nsvalues pro- vided in datasheets, the parameters of the PV model for each panel are extracted using individual algorithms imple- mented with MATLAB m-script. Secondly, those extracted values are used to obtain the simulated I–V and P–V curves through the PSIM circuit blocks from Villalva et al. (2009), PSIM User’s Guide (2010), as shown in Fig. 6. Finally, the

Table 1

Datasheet values of PV panels. I sc(A) Voc(V) Impp(A) Vmpp

|AT50|3.3|21.5|2.86|17.5|50|39|–|–|
|---|---|---|---|---|---|---|---|---|
|MSX60|3.8|21.1|3.5|17.1|60|36|2.47 10|80|
|KC65GT|3.99|21.7|3.75|17.4|65|36|1.59 10|82.1|
|MSX120|3.87|42.1|3.52|33.7|120|72|2.47 10|80|
|SQ160PC|4.9|43.5|4.58|35|160|72|1.4 10|161|
|KC200GT|8.21|32.9|7.66|26.7|200|54|3.18 10|123|
|LPC241|8.54|37.4|8.01|30.1|241|60|2.135 10|127.5|
|TSM245|8.68|37.5|8.13|30.2|245|60|4.0796 10|120|
|SF260|8.4|44.3|7.76|36.1|280|72|3.104 10|115.52|

AT50 3.3 21.5 2.86 17.5

characteristic curves of the PV model are plotted in Figs. 7 and 8 together with the measured data from a real PV panel. Because the model accuracy of Villalva method heavily depends on the selection of the diode ideality fac- tor, different values for A are used, and the one that shows the best performance is chosen in each plot. To obtain measured data, most of literature (Wagner, 1999; Kezzar et al., 2014; Xiao et al., 2004; Crispim et al., 2007; Villalva et al., 2009; Siddique et al., 2013; Sera et al., 2007; Chan and Phang, 1987; Park and Kim,

2014) which studies datasheet-based parameter extraction usually utilizes the only datasheet values. This is because datasheet values are already measured in compliant to standard test condition (STC) – cell temperature of 25 C, sunlight of 1000 W/m², and air mass of 1.5 – which is suggested by EN standard and repeating the experiments just for extracting the PV characteristic is redundant work and also prone to additional error. In this paper, all mea- surement data are directly obtained from the curve shown in PV panel datasheets except for AT50 panel whose data are reconstructed from literature (Park and Kim, 2014). Figs. 7 and 8 show that, even if each algorithm shows slightly different trends in the I–V and P–V curves, it is dif- ficult to determine the best algorithm without using prede- termined criteria. Therefore, it is necessary to establish a measure of model accuracy, especially for the region in the vicinity of the MPP, and EN50530 can be used as the basis (IEC EN50530). This standard states that the actual I–V characteristic of the PV simulator must not deviate by more than 1% from the rated output power within the voltage range from 0.9Vmppto 1.1Vmpp(Vmpp± 10%) related to the predetermined characteristic. To assess the accuracy of each algorithm according to this standard, the current error and power error in the MPP region are introduced in Eqs. (18) and (19): <u>1</u>
Z <u>i ðvÞi ðvÞ</u> <u>s m</u> e I ð%Þ¼ dv 100 ð18Þ 0:2Vmpp V mpp 10% i mðvÞ

Z e P ð%Þ¼ 1 <u>psðvÞpmðvÞ</u> dv 100: ð19Þ 0:2Vmpp V mpp 10% p mðvÞ

where the subscripts ‘m’ and ‘s’ denote the measured and simulated values, respectively. To implement the numerical

(V) Pmpp(W) Nski(A/ C) kv(mV/ C) 50 39 – –
3 3 3

|1.4 1.2 1.0 0.8 0.6 Current (A) 0.4 0.2 0.0|measured Wagner Perdro Villalva(A=1.1) proposed||
|---|---|---|
|3.5|0.0 4.5 9.0 13.5 18.0 Voltage (V) (a)|22.5|
|3.0 2.5 2.0 1.5 Current (A) 1.0 0.5 0.0|measured Wagner Pedro Villalva(A=1.4) proposed||
|0.0|4.5 9.0 13.5 18.0 Voltage (V) (b)|22.5|
|4 3 2 Current (A) 1|measured Wagner Pedro Villalava(A=1.6) proposed||
|0|0 4 8 121620242832364044 Voltage (V) (c)||
|9.0 7.5 6.0 4.5 3.0 Current (A) 1.5|measured Wagner Pedro Villalva(A=1.3) proposed||
|0.0 Fig. 7. KC200GT.|0 5 10 15 20 25 30 Voltage (V) (d) I–V characteristic curve. (a) SLP020, (b) AT50, (c) MSX120, (d)|35|

|Fig. 6. PSIM|implementation|to simulate|the characteristic|curve. (a)|
|---|---|---|---|---|
|equivalent circuit, (b) parameter calculation.|||||

integration in Eqs. (18) and (19), the trapezoidal rule is used. Performance comparisons regarding model accuracy are shown in Fig. 9(a) and (b). While Wagner method shows large error in AT50, KC65GT, KC200GT, and TSM245PC, Pedro method has large error in AT50, MSX120, KC65GT, and TSM245PC and needs long calculation time. Villalva method shows improved results in both accuracy and calculation time, but it still shows large current error in KC65GT and KC200GT and incorrect results especially in power error. Therefore, it is clear from the results that even if one algorithm shows good accuracy for certain PV samples, it may show poor accuracy for other samples. Because users usually have no idea of which algorithm should be adopted in advance, crucial and demanding fea- ture for the algorithm is the uniform model accuracy. The proposed algorithm shows high accuracy, and what’s more, its performance is relatively independent of individual solar-panels. To prove the superiority, we introduced sta- tistical indices such as average error (E), standard deviation of error (r). Because larger standard deviation not always means poor uniformity, the third index called ‘‘coefficient of variation”, defined by the ratio of the standard deviation to average value, is introduced to measure the uniformity of the results. The results are summarized in Table 2. The average data shows that the proposed method shows better accuracy than other methods. Moreover, its lower coeffi- cient of variance shows that it provides more uniform model accuracy. As predicted in Section 3, conventional methods show relatively poor performance due to the way how they solved the underdetermined parameter extraction problem.

Fig. 9(c) compares the parameter extraction time for

simulations performed using an Intel i5 2.80 GHz processor, where Wagner method is excluded in the plot

|25 20 15 10 Power (W) 5 0||measured Wagner Pedro Villalva(A=1.1) proposed|
|---|---|---|
|52.0 45.5 39.0 32.5 26.0 19.5 Power (W) 13.0 6.5||0246810121416182022 Voltage (V) (a) measured Wagner Pedro Villalva(A=1.4) proposed|
|0.0 126 105 84 63 Power (W) 42 21||0246810121416182022 Voltage (V) (b) measured Wagner Pedro Villalva(A=1.6) proposed|
|0 0 220 200 180 160 140 120 100 80 Power (W) 60 40 20||5 10 15 20 25 30 35 40 45 Voltage (V) (c) measured Wagner Pedro Villalva(A=1.3) proposed|

|3.5|||AT50|
|---|---|---|---|
|3.0|||MSX60 KC65GT|
|2.5|||MSX120 SQ160PC KC200GT|
|2.0|||LPC241SM TSM245PC|
|1.5|||SF260|
|1.0 10% current error (%) 0.5 0.0 2.5|Wagner|Pedro Villalva (a)|proposed|
|2.0 1.5 1.0 10% power error (%) 0.5 0.0|||AT50 MSX60 KC65GT MSX120 SQ160PC KC200GT LPC241SM TSM245PC SF260|
|14|Wagner|Pedro Villalva (b)|proposed AT50|
|12|||MSX60|
|10|||KC65GT|
|8|||MSX120|
|6|||SQ160PC KC200GT|
|4|||LPC241SM|
|2 0.20 0.15 Calculation Time (sec) 0.10 0.05|||TSM245PC SF260|
|0.00|Pedro 10% power error, (c) extraction time.|Villalva (c) Fig. 9. Comparisons of algorithm performance. (a) 10% current error, (b)|proposed|

because it is a non-iterative algorithm. The proposed algo- rithm shows the best performance among all of them. Vari- ations in the extracted parameters for KC200GT and the corresponding value of the objective function with respect to the iteration steps of the proposed method are shown 0in Fig. 10. Through the iteration process, the unknown

|0 5|10 15|20 25|30 35|
|---|---|---|---|
||Voltage (V)|||

0 5 10 15 20 25 30 35 parameter converges, and the parameters for the PV single-diode model are extracted within 41 steps. Conse-

**(d)**
quently, the proposed algorithm provides an accurate, uni-

Fig. 8. P–V characteristic curve. (a) SLP020 (b) AT50, (c) MSX120 (d)form, and rapid parameter extraction solution for the

KC200GT. single-diode model of PV panels.

|1242|||J.-Y. Park, S.-J. Choi / Solar Energy 122 (2015) 1235–1244||
|---|---|---|---|---|
|Table 2|||||
|Statistical verification for each algorithm.|||||
||Current error (%) E|rr|/EE|Power error (%)|
|Wagner|1.652|0.637|0.385|1.196|
|Pedro|1.459|0.563|0.386|1.03|
|Villalva|1.121|0.447|0.399|1.033|
|Proposed|0.954|0.315|0.33|0.87|

Calculation time (s) rr /EE rr /E

0.555 0.464 – – –

|0.012 0.01|||
|---|---|---|
||A*0.01||
|0.008 0.006|||
|0.004 Parameters value|Gsh Rs*0.01||
|0.002|||
|0 0|5 10 15 20 25 30 35 40 45 Number of iteration (a)||
|0 -1 -2 -3 -4 -5 lgo10(E) -6 -7 -8|||

|9.0|2 S=200 W/m|
|---|---|
|7.5|simulated 2 S=400 W/m|
|6.0|simulated S=600 W/m² simulated|
|4.5|S=800 W/m² simulated S=1000 W/m²|
|3.0 Current (A) 1.5|simulated|
|0.0 0 9.0|5 10 15 20 25 30 35 Voltage (V)|
|7.5 6.0 4.5 3.0 Current (A) 1.5|o T=25 C simulated o T=50 C simulated o T=75 C simulated|

|0.555|0.464|–|–|–|
|---|---|---|---|---|
|0.513|0.498|3.3|5.571|0.592|
|0.4|0.387|0.046|0.173|0.268|
|0.321|0.37|0.028|0.073|0.386|

0.0 0 5 10 15 20 25 30 35
Voltage (V)

Fig. 11. I–V and P–V characteristic curves of KC200GT panel at varying

irradiation values.

does not provide the temperature dependencies of MPP, -9

|5 10|15 20|25 30|35 40|45|
|---|---|---|---|---|
||Number of iteration||||

0 but the following approximations have been reported to be valid (Soon and Low, 2012; King et al., 1997).

|k ffi k|; k|ffi k|
|---|---|---|
|i;mpp|i v;mpp i,mpp|v v,mpp|
|mpp|mpp||
||sc||

**(b)** ð20Þ
Fig. 10. Optimization process of the proposed method in KC200GT. (a) where k and k are the temperature coefficients of

Parameter convergence, (b) objective function evaluation.I and V, respectively. For the compensation of irradiation level, it is also known that I from the PV panel is directly proportional

6. Temperature and irradiation dependence
to the irradiation level as

S Usually, datasheet values are measured in STC – cell Isc¼ Isc;STCð21Þ 2SSTC temperature of 25 C, sunlight of 1000 W/m, and air mass of 1.5 – and the characteristics of a PV panel deviate where S is the irradiation level and the subscript ‘STC’ according to the ambient temperature and irradiation level. stands for its value in STC. The dependency of Vocon For the temperature compensation, datasheet specifies tem-the irradiation condition is known to have a logarithmic perature coefficients only for the endpoints of the PV curve proportionality (De Soto et al., 2007; Celik and Acikgoz, such as kifor Iscand kvfor Voc. The manufacturer usually 2007; Gonzalez-Moran et al., 2009) and is approximated as

|¼ V where A Therefore, lowing manner:|~ S þ N A V ln oc;STC s STC T S STC is the diode ideality factor that has STC extracted from the datasheet. datasheet values should be updated include the temperature and irradiation effects in the fol-|ð22Þ been to|4.5 4.0 3.5 3.0 2.5 2.0|2 S=200 W/m simulated S=400 W/m² simulated 2 S=600 W/m simulated S=800 W/m² simulated 2 S=1000 W/m simulated|
|---|---|---|---|---|
|¼ I sc;STC|S ½1 þ k ðT T Þ i STC S STC ~|ð23Þ|Current (A) 1.5 1.0 0.5||
|¼ V ¼ I|S þ N A V ln ðT T Þð þ k oc;STC s STC T v STC S STC S ½1 þ k ðT T Þ mpp;STC i;mpp STC S STC|24Þ ð25Þ|0.0 0 4.5 4.0|5 10 15 20 25 Voltage (V)|
|¼ V mpp According|~ S þ N A V ln ðT T Þ þ k mpp;STC s STC T v;mpp STC S STC where T is the operating temperature and the subscript ‘STC’ stands for its value in STC. to the updated equations, the proposed method extracts new parameter values depending on tem-|ð26Þ|3.5 3.0 2.5 2.0 1.5 Current (A) 1.0 0.5|o T=25 C simulated o T=50 C simulated o T=75 C simulated|
|perature mental|and irradiation conditions. To verify approach, the PV characteristic curves in various environ- conditions are simulated and compared|this with|0.0 0 irradiation values.|5 10 15 20 25 Voltage (V) Fig. 13. I–V and P–V characteristic curves of KC65GT panel at varying|
|5.5 5.0|S=200 W/m² simulated 2||measure|data in Figs. 11–13 for KC65GT, KC200GT,|
|4.5 4.0|S=400 W/m simulated 2 S=600 W/m|and||SQ160PC, respectively. The measured points obtained from the manufacturer’s datasheets. It is clear|
|3.5 3.0|simulated 2 S=800 W/m simulated|that|the|proposed algorithm successfully describes characteristic of a real PV panel even in conditions other|
|2.5 2.0|2 S=1000 W/m simulated||than the STC.||
|Current (A) 1.5 1.0|||7. Conclusion||
|0.5|||This|paper presents an effective parameter extraction|
|0.0 0 5.5 5.0 4.5 4.0 3.5 3.0 2.5 2.0 Current (A) 1.5 1.0 0.5|5 10 15 20 25 30 35 40 45 Voltage (V) o T=20 C simulated o T=40 C simulated o T=60 C simulated|form|straints. optimization|method for a single-diode PV model using only the data- sheet values of real PV panels. In order to enhance the model accuracy, especially for the MPP region, the data- sheet information is divided into MPP and endpoint con- The former are solved using pattern search with an objective function specifying the MPP conditions, and the latter are solved using multi- ple simultaneous equations. The performance comparison of the current error and the power error near the MPP according to EN50530 verifies that this algorithm provides good accuracy irrespective of the individual PV panel char- acteristics. Therefore, the presented method provides uni- method for parameter extraction that is|

Voc

I sc

Voc

I mpp

V

are

the

only

0.0less

||0 5|10 15 20|25 30|35 40|45|
|---|---|---|---|---|---|
|||Voltage (V)||||
|Fig. 12. irradiation values.|I–V and P–V characteristic curves of SQ160PC panel at varying|||||

dependent on the panel type and skill of users. Further- more, the implementation is simple, and the extraction time is very short. Additionally, with simple updated equations for the datasheet values, the proposed method shows great

accuracy even under temperature and irradiation condi- tions different from STC.

Acknowledgement

This work was supported by the 2013 Research Fund of University of Ulsan, Republic of Korea.

References

Celik, A.N., Acikgoz, N., 2007. Modeling and experimental verification of the operating current of mono-crystalline photovoltaic modules using four- and five-parameter models. Appl. Energy 84 (1), 1–5. Chan, D., Phang, J., 1987. Analytical methods for the extraction of solar cell single- and double-diode model parameters. IEEE Trans. Electron. Dev. 34 (2), 286–293. Chegaar, M., Ouennoughi, Z., Hoffmann, A., 2001. A new method for evaluating illuminated solar cel parameters. Solid-State Electron. 45, 293–296. Crispim, J., Carreira, M., Castro, R., 2007. Validation of Photovoltaic Electrical Models against Manufacturer’s Data and Experimental Results. In: International Conference on Power Engineering, Energy and Electrical Drives. Cubas, J., Pindado, S., Victoria, M., 2014. On the analytical approach for modeling photovoltaic systems behavior. J. Power Sources 247, 467–

474.
De Soto, W., Klein, S.A., Beckman, W.A., Jan. 2007. Improved and validation of a model for photovoltaic array performance. Sol. Energy 81 (1), 78–88. Gonzalez-Moran, C., Arboleya, P., Reigosa, D., Diaz, G., Gomez- Alexandre, J., 2009. Improved Model of Photovoltaic Sources consid- ering ambient Temperature and Solar Irradiation. In: IEEE PES/IAS Conference on Sustainable Alternative Energy. IEC EN50530, Standard for Overall Efficiency of Photovoltaic Inverters, CENELEC, Stassart 35, B-1050 Brussels. Ishaque, K., Salam, Z., 2011. An improved modeling method to determine the model parameters of photovoltaic (PV) modules using differential evolution (DE). Sol. Energy 85, 2349–2359. Ismail, M.S., Moghavvemi, M., Mahlia, T.M.I., 2013. Characterization of PV panel and glabal optimization of its model parameters using genetic algorithm. Energy Convers. Manage. 73, 10–25.

Kezzar, R., Zereg, M., Khezzar, A., 2014. Modeling improvement of the four parameter model for photovoltaic modules. Sol. Energy 110, 452–

462.
King, D.L., Kratochvil, J.A., Boyson, W.E., 1997. Temperature Coeffi- cients for PV Modules and Arrays: Measurement Method, Difficulties, and Results. In: IEEE 26th Photovoltaic Specialists Conference. Ouennoughi, Z., Chegaar, M., 1999. A simpler method for extracting solar cell parameters using the conductance method. Solid-State Electron. 43, 1985–1988. Park, H.A., Kim, H.S., 2014. Mathematical consideration on PV cell modeling. Trans. Korean Inst. Power Electron. 19 (1). Peng, L., Sun, Y., Meng, Z., 2014. An improved model and parameters extraction for photovoltaic cells using only three state points at standard test condition. J. Power Sources 248, 621–631. PSIM User’s Guide, Ver. 9, May 2010, POWERSIM. Sera, D., Teodorescu, R., Rodriguez, P., 2007. PV Panel Model Based on Datasheet Values. In: IEEE International Symposium on Industrial Electronics, pp. 2392–2396. Siddique, H.A.B., Xu, P., De Doncker, R.W., 2013. Parameter Extraction Algorithm for One-Diode Model of PV Panels based on Datasheet Values. In: International Conference on Clean Electrical Power (ICCEP). Soon, J.J., Low, K.S., 2012. Photovoltaic model identification using particle swarm optimization with inverse barrier constraint. IEEE Trans Power Electron 27 (9). Venkataraman, P., 2009. Applied Optimization with MATLAB Program- ming, second ed. WILEY. Villalva, M.G., Gazoli, J.R., Filho, E.R., 2009. Modeling and circuit- based simulation of photovoltaic arrays. IEEE Trans. Power Electron., 1244–1254 Villalva, M.G., Gazoli, J.R., Filho, E.R., May 2009. Comprehensive approach to modeling and simulation of photovoltaic arrays. IEEE Trans. Power Electron. 24 (5), 1198–1208. Wagner, A., 1999. Photovoltaik Engineering, Die Methode der Effektiven Solarzellen-Kennlinie. Springer-Verlag, Berlin, Heidelberg, New York. Xiao, W., Dunford, W.G., Capel, A., 2004. A Novel modeling method for photovoltaic cells. In: IEEE 35th Annual Power Electronics Specialists Conference (PESC), vol. 3, pp. 1950–1956. Yuan, X., Xiang, Y., He, Y., 2014. Parameter extraction of solar cell models using mutative-scale parallel chaos optimization algorithm. Sol. Energy 108, 238–251.
