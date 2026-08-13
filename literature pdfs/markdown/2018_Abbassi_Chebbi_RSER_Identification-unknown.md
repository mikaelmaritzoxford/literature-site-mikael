Renewable and Sustainable Energy Reviews 90 (2018) 453–474

Contents lists available at ScienceDirect

Renewable and Sustainable Energy Reviews

journal homepage: www.elsevier.com/locate/rser

Identification of unknown parameters of solar cell models: A comprehensive overview of available approaches a,b,⁎ c c a Rabeh Abbassi, Abdelkader Abbassi, Mohamed Jemli, Souad Chebbi a University of Tunis, Higher National Engineering School of Tunis (ENSIT), LaTICE Laboratory, 5 Avenue Taha Hussein, PO Box 56, 1008 Tunis, Tunisia b University of Hail, College of Engineering, Saudi Arabia c University of Tunis, Higher National Engineering School of Tunis (ENSIT), Engineering Laboratory of Industrial Systems and Renewable Energies (LISIER), 5 Avenue Taha Hussein, PO Box 56, 1008 Tunis, Tunisia

ARTICLE INFO ABSTRACT Keywords: Solar energy is increasingly attracting the attention of industry and academia. This heightened focus is mainly Photovoltaic cells motivated by the challenge to contribute to fossil fuels' alternative and to limit the pollution of environment Parameter extraction caused by their emissions. The number of researches focusing on solar photovoltaics is continually increasing. I–V and P-V characteristics The behavior of a photovoltaic (PV) cell/module may be deduced via its current–voltage (I–V) characteristic Single-diode model which depends on its circuit model parameters. Whilst, the extraction of appropriate circuit model DC para- Double-diode model meters is crucial to carry out precise performance investigations and control studies on solar PV systems, it Three-diode model remains highly constrained nonlinear non-convex optimization problem. The main objective of this paper is to Analytical approaches review the existing research works on PV cell model parameter estimation problem and to assess the perfor- Numerical approaches mance of the newest approaches. Based on the conducted review of more than 100 methods published over the past 7 years, the recommendations provided for future research are an important goal that will improve the methods of research in this area. In addition, this article implements two real models (single-diode and double- diode) and examines their accuracy to draw the current–voltage (I– V) and power–voltage (P–V) characteristics.

1. Introduction The share of renewable energies in the world's electricity mix had an exponential growth over the last years (23% in 2015) [1]. This increase, higher than that of conventional energies, will continue over the next four years to reach 28% by 2021. Renewable energies benefit from the dynamic of the Kyoto Protocol, which favors this solution in the fight against greenhouse gases [2,3]. Several technologies, namely wind and solar, have reached a real technical maturity and are now competitive compared to a cost of energy integrating the value of CO₂ [4–8]. Currently, solar energy is more and more becoming as a key element of the future energy mix. It is developing particularly in industrialized countries where the sunshine is favorable and where it is supported by public aid. Regional strategies set important targets for the construction of more than 20 GW of additional CO₂-free [9], in particular solar, electricity production capacity in Mediterranean countries by 2020 [10]. Thus, among the different solar technologies, solar photovoltaic (SPV) represents an important part of the development of renewable energies in the world with rising annual growth rate [11]. The performance of a PV module depends mainly on various factors which include the availability of solar radiation and the efficiency of
conversion. Although the average value of conversion efficiency is up to now about 20%, its valuation draws a particular attention from re- searchers as it can generate optimistic economic predictions that can seduce investor expectations [12]. Indeed, to operate SPV plant at its maximum possible capacity, it is essential to learn about the exact parameters of a solar cell/module [13–15]. However, the conversion efficiency and overall performance of solar cell/module is directly af- fected by its various physical parameters [16]. Therefore, an accurate estimation of such parameters is always required not only to carry out the evaluation of cell performance but also to improve the design, the optimization of fabricate process and the quality control of the cell [17,18]. According to the majority of the published works [13–19], the I-V and P-V characteristic curves, which derive from the diode model parameters, are very decisive for solar cells/modules being a direct indicator of performance. However, the reverse process of the diode model parameters derivation from the I-V and P-V characteristics re- mains a key challenge particularly because of the strong nonlinear re- lationship that governs the PV cell behavior. Various researches [19–21] have been focused on the foremost issues related to the methodologies of the identification of DC solar cell parameters. In [22],

[https://doi.org/10.1016/j.rser.2018.03.011](https://doi.org/10.1016/j.rser.2018.03.011) Available online 24 April 2018 1364-0321/ © 2018 Elsevier Ltd. All rights reserved.

⁎ Corresponding author at: University of Tunis, Higher National Engineering School of Tunis (ENSIT), LaTICE Laboratory, 5 Avenue Taha Hussein, PO Box 56, 1008 Tunis, Tunisia. E-mail addresses: r_abbassi@yahoo.fr (R. Abbassi), abd_abbassi@yahoo.com (A. Abbassi), mohamed.jemli@isetr.rnu.tn (M. Jemli), chebbi.souad@gmail.com (S. Chebbi).

Received 14 December 2017; Received in revised form 21 February 2018; Accepted 13 March 2018

|R. Abbassi et al.||||Renewable and Sustainable Energy Reviews 90 (2018) 453–474|
|---|---|---|---|---|
|Nomenclature||SIV GOTLBO|Suitability Index Variable Generalized|Oppositional|
|DE|Differential Evolution||Optimization||
|RADE|Repaired Adaptive Differential Evolution.|STLBO|Simplified Teaching Learning Based Optimization||
|PDE|Penalty based DE|TVIWAC-PSO|Particle Swarm Optimization with Time Varying||
|IADE|Improved Adaptive DE||Inertia Weight and Acceleration Coefficients||
|AE|Absolute Error|ABSO|Artificial Bee Swarm Optimization||
|APE|Absolute Power Error|AIS|Artificial Immune System||
|APVE|Absolute Power and Voltage Error|ANN|Artificial Neural Network||
|SSE|Sum of Squared Errors|BBO|Bio-Geography Based Optimization||
|ABCO|Artificial Bee Colony Optimization|BFA|Bacterial Foraging Algorithm||
|AGA|Adaptive Genetic Algorithm|BPFPA|Bee Pollinated Flower Pollination Algorithm||
|APSO|Particle Swarm Optimization with Adaptive Inertia Weight|GA|Genetic Algorithm||
||Control|IAE|Individual Absolute Error||
|BBO-M|Bio-Geography|IGHS|Innovative Global Harmony Search||
||Strategies|IPSO|Improved Particle Swarm Optimization||
|BMO|Bird Mating Optimization|LM|Levenberg-Marquardt||
|CPSO|Chaos Particle Swarm Optimization|MPCOA|Mutative-Scale Parallel Chaos Optimization||
|DDM|Double Diode Model|MSE|Mean Squared Error||
|MDDM|Modified Double Diode Model|N.E|Not Extracting||
|DEIM|Differential Evolution with Integral Mutation|NOCT|Nominal Operating Cell Temperature||
|HS|Harmony Search|PS|Pattern Search||
|IGHS|Improved Global Harmony Search|R-JADE|Repaired Adaptive Differential Evolution||
|GGHS|Grouping Based Global Harmony Search|SA|Simulated Annealing||
|IBCPSO|PSO with Inverse Barrier Constraints|SDM|Single Diode Model||
|IP|Interior Point|ISDM|Improved Single Diode Model||
|JADE|Adaptive Differential Evolution|TDM|Three Diode Model-STC: Standard Test Conditions||
|LS|Least Square|TLBO|Teaching Learning Based Optimization||
|NR|Newton-Raphson|VC-PSO|Particle Swarm Optimization with Velocity Clamping||
|PSA|Parallel Swarm algorithm|CPU|Central Processing Unit||
|RMSE|Root Mean Squared Error|NMS|Nelder-Mead Algorithm||
|SBMO|Simplified Bird Mating Optimization||||

Teaching Based Learning

Based Optimization with Mutation

it has been proved that it is impossible to solve this nonlinear problem accurately relying solely on linear identification methods. Many sug- gestions [23,24] have been proposed regarding the use of nonlinear electrical models to extract the effective parameters of solar cells ac- curately and to make sure its operating conditions. Based on the I-V curves of a P-N junction diode, many models are established to describe the behavior of solar cells. Recently, the litera- ture is richer than previously concerning the estimation of the I-V curves [15,25–33]. The most cited models are the single-diode model (SDM), the double-diode model (DDM), the modified double-diode model (MDDM) and the three-diode model (TDM). Referring to the infinity of published studies, the DDM is judged the almost used for representing the equivalent electrical circuit of solar panel [33–36]. Nonetheless, it has been proven that it is the more complex considering its longer execution time and the nonlinearity relationship of its dif- ferent parameters [37,38]. On the other side, many researchers have demonstrated that the SDM is the most prevalent taking into account its simplicity [39]. Thus, this model is divided into two different types, which are the Ideal SDM (ISDM) [40] that neglects the series and shunt resistors and the improved SDM that characterizes the relation of its parameters by maintaining the effect of all resistors of the equivalent electrical circuit [41,42]. To extract the parameters of the electrical circuit of solar panel, a multitude of methodologies have been pro- posed. In this work, these methodologies have been classified into three different families. The first consists in resolving the problem of the nonlinearity of the relation between the different parameters by using mathematical manipulations which are based on the analytical ap- proaches [43–45]. The second family includes essentially the techni- ques based on the exploitation of several numerical approaches for calculating the parameters of photovoltaic cells [46–49]. These are iterative based algorithms [42].

In addition, metaheuristic approaches are sorted within the third family. These approaches contributed very strongly in the identification of the key parameters of equivalent electrical circuit of PV panels [13,50–52]. In this case, an improved version of modeling based on multitude of algorithms has been used. These techniques are considered as stochastic optimization approaches and has the advantage of being the most effective in term of computational time and accuracy of ex- tracted parameters [38,53–55]. To overcome the drawbacks mentioned in the literature, several methods have been proposed. In this context, this paper aims to exploit this variety of proposed solutions in order to classify and review the existing equivalent electrical circuit, the different parameters extraction techniques and the results found in many previous studies. The ad- vantages and disadvantages of the discussed approaches are summar- ized and compared according to three different categories. Besides, the most cited types of equivalent electrical circuit has been investigated and implemented carefully. This paper is organized as follows; Section 2 provides an insight into the available electrical circuit models of PV cells. Section 3 reviews, discusses, summarizes and explains the most used techniques of extraction of PV model parameters. In Section 4, the implementation of SDM and DDM models is achieved and the para- meters of each of them are extracted. Finally, some conclusions judged very useful for researchers in the field are also drawn by Section 5.

2. Available electrical circuit models of PV cells
2.1. Fundamental In general, the modeling of a photovoltaic module involves the use of the I-V characteristic of a specific model under well-defined en- vironmental conditions. The design of models that can estimate

parameters in a truly representative way remain a complex task [6]. Indeed, the modeling depends on various factors namely the multitude of PV cell types including the number of diodes, shunt resistance (in- finite or finite), ideality factor as well as the most appropriate numer- ical methods [6–49]. According to the literature [13–34], the algorithms for extracting the parameters of the PV cells hinge essentially on the different tech- nologies of the photovoltaic systems, their operating conditions of temperature and illumination and their size. That is why it is extremely important to identify the different parameters that influence the pre- cision of the main equations used for modeling each model [6,55].

Fig. 1 presents five different models of solar cell used in literature.

The first one ISDM [18,51,52] is easily understandable but less used (Fig. 1a). The three parameters, which are the short circuit current Isc, the open circuit voltage Vocand the ideality factor A have to be ex- tracted. The second model includes five parameters, which are the short circuit current Isc, the open circuit voltage Voc, the ideality factor A, the series resistance Rsand the shunt resistance Rsh. This model has the advantage to be the very accurate model according to the variation of the solar radiation and temperature (Fig. 1b) [15,18,20,22–24,28,30,34–36,38–47,49–53,56]. Fig. 1c shows the DDM model. This model is more complex than that of a single diode, it is characterized by seven key parameters and takes a longer calculation time [13–16,18–20,23,27,28,31–37,48,52,54,55]. The MDDM char- acterized by eight parameters has also been proposed (Fig. 1d) [25,57]. Besides, a new lumped-parameter equivalent circuit model using three diodes and known as TDM model has been developed (Fig. 1e) [26,58,60]. The current-voltage relation of photovoltaic cell of the ISDM is given by: ⎛⎜⎛ <u>VRI +</u> Vt <u>s</u> ⎞ II =−=−phIdIphIe0 ⎝ ⎠−1 ⎟⎞ ⎝ ⎠ (1) In the Eq. (1), the junction thermal voltage at reference conditions is given by: <u>AkT</u> *V* *t* = *q* (2) The current-voltage relation of photovoltaic cell of the improved SDM is given by: I

⎛⎛ <u>VRI +</u> V <u>s</u> ⎞⎞ <u>VRI +s</u> II =−−=−phIdIshIphIe ⎝⎜⎟ ⎝ t ⎠−1 ⎠ − Rsh (3) The current-voltage relation of photovoltaic cell of the DDM is given by: ⎛ VRI + s ⎞ II =−−−=−phId1Id2IshIphIexp01⎜⎛ ⎝ aV 1t1⎠ −1 ⎟⎞ ⎝ ⎠ − Iexp ⎛ ⎛⎝ VRI aV + 2t2 s ⎞⎠ −1 ⎞ − <u>VRI +s</u> 02⎜⎟ ⎝ ⎠ Rsh (4) The current-voltage relation of photovoltaic cell of the modified double-diode MDDM model is ⎛ VRI + s ⎞ given by:IIIIIIIexp =−−−=−ph d1 d2 sh ph 01⎜⎛⎝ aV 1t1⎠ −1 ⎞ ⎟ ⎝ ⎠ − Iexp02⎜⎟ ⎛⎛⎝ <u>VRII R +−</u> aV <u>s</u> 2t2 <u>d2 s2</u>⎞⎠ −1 ⎞ − <u>VRI +s</u> ⎝ ⎠ Rsh (5) The current-voltage relation of photovoltaic cell of the TDM model is given by: ⎛⎛ VRI + s ⎞ ⎞ I =−−−−=− IphId1Id2Id3IshIphI₀₁⎜exp⎝ aV 1t1⎠ −1⎟ VRI + VRI + ⎝ ⎠ − Iexp02⎜⎟ ⎛ ⎛⎝ aV 2t2 s ⎞⎠ −1Iexp ⎞−03⎜⎟ ⎛⎛⎝ aV 3t3 s ⎞⎠ −1 ⎞ − <u>VRI +s</u> ⎝ ⎠ ⎝ ⎠ Rsh (6) Where I is the photocurrent generated at Standard Test Conditions STC (25 °C, 1000 W/m ph 2 ) (A) I₀ is the dark saturation current (A) −19 q is the electron charge (1.6.10 C) T is the cell temperature (K) Rsis the series resistance (Ω) Rshis the shunt resistance (Ω). A is the diode ideality factor k is the Boltzmann constant (1.38.10 −23 J/K) Eqs. (1), (3), (4), (5) and (6) show that the current-voltage re- lationship of the photovoltaic cell involves various parameters those vary depending on the solar irradiance and cell temperature (n, Rs, Rp, Rs I Rs I

Id1 Id2 Rsh V Iph D1 D2 Rsh V Id Id Iph D V Iph D

|(a)|||(b)||||(c)|
|---|---|---|---|---|---|---|---|
|||Rs|I|||Rs|I|
||Id1 Id2|Ish||Id1 Id2|Id3|Ish||
|Iph|D1 D2|Rsh|V Iph|D1 D2|D3|Rsh|V|
|Fig. 1. Equivalent electrical circuit of a solar cell; (a) SDM, (b) ISDM, (c) DDM, (d) MMDM, (e) TDM.|R|(d)|||(e)|||
||||455|||||

S2

I o, and Iph). According to literature [10–60], four distinguished models of the photovoltaic cell are commonly used: the ISDM, the SDM, the DDM and the TDM. The expressions (1), (3), (4), (5) and (6) of the characteristic I-V are transcendental equations and can only be solved numerically. However, in order to exploit this characteristic, it is first necessary to determine such parameters. Whatever the model used, the short circuit current and the open circuit voltage are the most important key parameters and without them we cannot do anything. The short circuit current Iscindicates the maximum current that can be delivered by the cell when it is short-circuited, i.e. when the voltage at its terminals is zero. The open-circuit voltage denoted Voc: is that at the terminals of the cell when the cell is in open circuit, that is to say when the current passing through it is then zero. In what follows, we focus on the methods for extracting the parameters of such models of the PV cells.

2.2. Single-diode PV cell model
2.2.1. ISDM parameters extraction Based on the Eq. (1), the short circuit current (Isc), the open circuit voltage (Voc), the current (Im) and the voltage (Vm) at maximum power point (MPP) are given as follows [6,51,52]: II sc=ph V=0 (7) V 0c= <u>sB</u> ln ⎛⎜1+
<u>sc</u> ⎟⎞ <u>nN k T I</u> q ⎝ *I₀* ⎠ (8)

exp ⎜⎟⎜ ⎛ 0c⎞ = ⎛1+m ⎟⎜ ⎞exp ⎛m⎟⎞ qV qV qV ⎝ nN ksBT ⎠ ⎝ nN ksBT ⎠ ⎝ nN ksBT ⎠ (9) ⎛⎜ ⎛⎜⎟ qVm⎞−1⎟⎞ II Iexp mph0=− ⎝ ⎝ nN ksBT ⎠ ⎠ (10) At MPP operating point, the derivative of the current with respect to the voltage yields: *dI* qI₀ qV =− exp ⎜⎛ ⎟⎞ *dV* nN ksBT ⎝ nN ksBT ⎠ (11) At the best operating point of the system (MPP), the corresponding voltage is: <u>nN k TsBnN k TsB</u> ⎛ *dI* ⎞ V m= ln ⎛⎜− ⎟⎞ q ⎝ qI₀ ⎝*dV* ⎠Vm ⎠ (12) Considering the asymptotic behavior describing how the current- voltage curve behaves near the limits of short and open circuit

conditions, the derivative appearing in (12) can be evaluated by: *dI* ≅− 0− *I* *sc* =− *I* *sc* *dVVmV₀₀c*−0 *Vc* (13) The current and the voltage at the maximum power point are then determined by substituting the derivative (13) in (11) and (12). <u>nN ksBT</u> ⎛<u>nN ksBT Isc</u>⎞ V m= ln ⎜ ⎟ q ⎝ qI₀₀ *Vc*⎠ (14) <u>nN ksBT</u> ⎜⎛ I sc II Imph0=+− ⎟⎞ q ⎝ V0c ⎠ (15) Finally, the maximum output power is: <u>nN k T</u> I <u>nN k T nN k T I</u> P mph0= ⎜⎟ ⎛II +− <u>sB</u> ⎜⎟ ⎛sc⎞⎞<u>sB</u>ln ⎜⎛<u>sB sc</u>⎟⎞ ⎝ q ⎝ V0c ⎠⎠ q ⎝ qI₀₀ *Vc*⎠ (16) Real conditions: taken account the temperature and the solar radiation variation The majority of PV manufacturers provide the data sheet illustrating only the I-V and P-V curves under standard test conditions (STC). For different temperature or radiation levels it is absolutely necessary to recalculate the critical parameters. The photocurrent is given by the following expression: I(E/E)(I ph=+−ref phrefμ(TT))i ref (17) where T ref, Erefare respectively the temperature and irradiance at STC conditions, Iphrefis the reference photocurrent at STC and μiis the temperature coefficient of the short circuit current (A/°C). The satura- tion current is expressed as: I = <u>Iμ(TT)</u> <u>scref+−i STC</u> 0 exp q <u>Vμ(TT)</u> <u>0cref +− v ref</u> −1 ()nN ksBT (18) Where V0crefis the reference open circuit voltage and μvis the temperature coefficient of open circuit voltage (V/°C). Using the maximum power point current (Eq. (10)) and the sa- turation current at the reference temperature given by Eq. (18), the diode quality coefficient is determined as: <u>q(Vmref− V0cref) 1</u> N = <u>Imref</u> Nk TsBref ln (1− I ) (19) scref

Fig. 2. I-V and P-V characteristics.

Herein, Vmref,Imref,V0crefand I0crefare provided by manufacturers.

2.2.2. SDM parameters extraction Under Standard Test Conditions In STC conditions, the current-voltage relationship that is subject to the Eq. (1) can be rewritten in the following form [28–30]:
⎛e⎛ <u>VR +</u> Vtref <u>sref</u>I⎞ ⎞ − <u>VR +sref</u>I II =−phrefI0ref ⎜⎟ ⎝ ⎠−1 ⎝ ⎠ Rshref (20) where I phref, I0ref, Vtref, Rsrefand Rshrefare evaluated in a particular point of current-voltage characteristics curve represented in Fig. 2. The eva- luation of the currents of the three critical operating points (short cir- cuit, open circuit and maximum power) makes it possible to establish the relations (21), (22) and (23), respectively. <u>RI</u> <u>sref scref</u> ⎛⎛ Vtref ⎞⎞ − <u>Iscref</u> II Ie scref=−phref 0ref ⎜⎟ ⎝ ⎠−1Rsref ⎝ ⎠ Rshref (21)

⎛⎛ V0ref ⎞⎞ −= <u>V0ref</u> IIe1 phref−0ref ⎜⎟ ⎝ Vtref ⎠− 0 ⎝ ⎠ Rshref (22) <u>VRI</u> <u>mref + sref mref</u> ⎛⎛ Vtref ⎞⎞ − VRImref+sref mref II Ie mref=−phref 0ref ⎜⎟ ⎝ ⎠−1 ⎝ ⎠ Rshref (23) Under standard test conditions, the derivative of the current (3) with respect to the voltage at the open circuit condition and with re- spect to the short circuit current at the short circuit condition leads to the series resistance Rsrefand shunt resistance Rshref, respectively: dI 1 =− dVI0/VV == 0cref Rsref (24) dI 1 =− dVII == scref /V0 Rshref (25) The junction thermal voltage at reference conditions is given by: <u>AkTref</u> *V* *tref*= *q* (26) Where I screfis the short circuit current at STC V0refis the open circuit voltage at STC Vmrefis the voltage at the maximum power point MPP at STC I mrefis the voltage at the maximum power point MPP at STC The above parameters are normally provided by the manufacturer’s datasheet. At MPP, the derivative of the power with respect to the voltage is equal to zero (27): dP = 0 dVII == mref /VV mref(27) From Eqs. (21) and (22), the generated photocurrent Iphrefand the dark saturation current I₀ can be related by (28): ⎛⎛ V0ref ⎞⎞ − <u>V0ref</u> IIe1 phref=0ref ⎜⎟ ⎝ Vtref ⎠− ⎝ ⎠ Rshref (28) The substitution of the previous expression into the Eq. (21) gives the relation (29) which can be simplified as (30): <u>RI</u> <u>sref scref</u> ⎛⎛ V0ref ⎞ ⎛ Vtref ⎞⎞ + <u>VIR0ref−scref sref</u> IIe scref=0ref ⎜⎟ ⎝ Vtref ⎠ − e ⎝ ⎠ ⎝ ⎠ Rshref (29)

⎛⎛ VV0ref ⎞⎞ <u>VIR0ref−scref sref</u> IIe scref=0ref ⎜⎟ ⎝ tref ⎠ + ⎝ ⎠ Rshref (30) For I0ref, we will find: <u>VIR −</u> ⎛ V0ref ⎞ I(I 0ref=−scref <u>0ref scref sref</u> )e⎝− Vtref ⎠ Rshref(31) The substitution of relations (31) and (28) into (23) gives: II mref=−0ref VRI RI mref+−sref mref sref scref −(I0ref Rshref <u>VRI</u> <u>mref + sref mref</u> <u>VRI</u> <u>0ref−sref scref</u> ⎛ Vtref ⎞ − Rshref )e⎝ ⎠ (32) Eq. (27) becomes: dP d(IV) dI dV ==+ dV I dV V II == mref /VV mref(33) From Eq. (32), the term *dV* *dI* can be given by: <u>∂f(I,V)</u> dI = <u>∂V</u> dV 1−<u>∂f(I,V)</u> (34) ∂I From (34), the Eq. (33) is rewritten as: <u>∂f(I,V)</u> dP d(IV)∂V ==+ Imref <u>∂f(I,V)</u> V mref dVII == mref /VV mref dV 1− ∂I(35) Finally, we obtain the following equation: <u>V +R I</u> <u>V0ref − Rsref Iscref</u> <u>mref sref mref</u> ⎞⎠ −− (I0ref)e⎛⎝ Vtref dP Rshref Vtref Rshref − Rshref 1 dV II =+ IV mref mref <u>V</u> <u>mref+Rsref mref I</u> == mref /V Vmref (I0ref − V 0ref Rshref − Rsref scref )e⎝ I ⎛ Vtref ⎞ ⎠ Rs 1+− Vtref Rshref Rshref (36) Taking into account the Eqs. (25), (35) and (36), the three un- knowns Rs, Rshand Arefcan be easily found. <u>Vmref +Rsref Imref</u> −− (I0ref <u>V0ref − Rsref Iscref</u> )e⎝ ⎛ V tref ⎞ ⎠ R shref <u>1</u> <u>1</u> VR tref shref − Rshref − = <u>V +R I</u> Rshref <u>V0ref − Rsref Iscref</u> ⎛ <u>mref</u> V tref <u>sref mref</u> ⎞ 1+− (I0ref − Rshref )e⎝ ⎠ <u>Rs</u> VR tref shref Rshref (37) Based on the relations (32), (36), (37), (28) and (31), the five un- known parameters of SDM model (Iphref, I0ref, Rsref, Rshrefand Aref) are easily determined. Under real conditions: variation of temperature and irradiation The parameters of the PV module are sensitive to the weather conditions changes as follows. The ideality factor, the saturation cur- rent of the diode, the photo-current are given by (38), (39) and (40), respectively: A = A(T/T)ref ref (38) ⎛ ⎞ ⎜⎜ EgNs <u>Tref</u> ⎟⎟ II(T/T)e 00ref ref= 3 ⎜ V1 ⎝ tref()− T ⎟⎠ (39) I(G/G)(I ph=+−ref phrefα(TT)Isc ref) (40) Herein, T, Tref, G and Grefare the cell junction ambient and reference temperatures, instantaneous solar irradiances and instantaneous solar irradiance and standard test conditions irradiance, respectively. E is theg band gap energy of semi-conductor. αIscis the temperature coefficient of short circuit current (A/°C). The open circuit voltage V0cis:

V 0c=−−+ Vβ(TT)Vln(G/G)0cref ref t ref (41) The series resistance, the shunt resistance, the short circuit current, the maximum power point current and the maximum power point voltage are expressed by (42), (43), (44), (45) and (46), respectively:

Rssref=− R ⎡ ⎢⎜⎟ ⎛<u>t</u>⎞e(V/V) − 0c t⎤ ⎥ <u>V</u> ⎣⎝ I⁰⎠ ⎦ (42) Rsh= R(G/Gshref ref) (43) II(G/G)αI(TT sc=+−scref ref sc ref) (44) II(G/G mmref=ref) (45) V mmref=−− Vβ(TT)ref (46)

2.3. DDM parameters extraction According to the Fig. 1(c), the output current related to the voltage to describe the I-V characteristics of a DDM of solar cells is defined by [13–16]:
+ s ⎛ VRI aV 1t1⎠ ⎞ II =−−−=−phID1ID2IshIphIexp01⎜⎛ ⎝ −1 ⎟⎞ ⎝ ⎠ ⎛⎛ VRI aV + 2t2⎠ s ⎞⎞ − VRI +s − Iexp02⎜⎟ ⎝ −1 ⎝ ⎠ Rsh (47) where I phis the photo current generated by the incident light I₀₁ is the saturation current due to diffusion mechanism I₀₂ is the saturation current because of carrier recombination in space charge region a₁ is the diode ideality factor for diffusion current a₂ is the diode ideality factor for generation recombination current Vt1and Vt2are the thermal voltages expressed by: <u>NkTs</u> V t1=== VVt2 t q (48) Where Nsis the number of series connected PV cells in the PV panel −23 K is the Boltzmann’s constant (1.38 ×10 J/k) Eq. (47) is composed by seven unknown parameters to be de- termined, which are Iph, I₀₁, I₀₂, a₁, a2,Rsand Rsh. These parameters are based on the datasheets of the PV module. Manufacturer gives the different parameters at Standard Test Conditions (STC) (1000 W/m², 25 °C). However, these data are not available provided that there is variations of solar irradiance and temperature. For this reason, we try to find these parameters in all possible conditions. Three characteristics points are given by the manufacturer: the open circuit voltage (V0c, 0), the short circuit current (0, Isc) and the current and voltage at maximum power point MPP (Vmp, Imp). Eq. (47) is evaluated at the three characteristics conditions as follows [33–37]: At the short circuit point: ⎛⎛ RI 1t1⎠ ssc⎞ ⎞ − ⎛⎛ RI 2t2⎠ ssc⎞ ⎞ − <u>RIssc</u> II Iexp sc=−ph 01⎜⎟⎜⎟ ⎝ aV −1Iexp02 ⎝ aV −1 ⎝ ⎠ ⎝ ⎠ Rsh (49) At the open circuit point: V0c ⎛⎜⎟⎜⎟⎛ V0c ⎞ 1t1⎠⎞ − ⎛⎛ 2t2⎠⎞⎞ − <u>V0c</u> 0 =− IIexpph ⎝ aV −1Iexp ⎝ aV −1 ⎝ ⎠ ⎝ ⎠ Rsh (50) At the maximum power point:

⎛ ⎜⎟ ⎛ <u>VRI</u> <u>mp+ s mp</u>⎞ ⎞ ⎛⎛⎜⎟ <u>VRI</u> <u>mp+ s mp</u>⎞ ⎞ IIIexp mp=−ph 01 ⎝ aV 1t1 ⎠ −1Iexp − 02 ⎝ aV 2t2 ⎠ −1 ⎝⎜ ⎠⎟ ⎝⎜ ⎠⎟ <u>VRI</u> <u>mp+s mp</u> − R (51) sh The power supplied by the PV module is obtained by: *P* =× *I V* (52) Eq. (52) is differentiated with respect to Vas follows: *dP dI* ⎞ ×+ = ⎛ *V I* *dV* ⎝*dV* ⎠ (53) The derivative of the power with respect to the voltage at the maximum power point is zero, thus: *dI Im* =− *dV Vm*(54) So, the derivative of (47) with respect to the voltage is given by: *dI IdI*01 ⎛⎝ VRI + s ⎞⎠ *IdI* 02 ⎛⎝ VRI + s ⎞⎠ =− ⎛1R +s⎞expaV 1t1 − ⎛1R +s⎞expaV 2t1 *dV* aV1t1⎝ *dV* ⎠ aV1t1⎝ *dV* ⎠ 1 ⎛ *dI* ⎞ − 1R +s Rsh ⎝ *dV* ⎠ (55) By substituting (55) in (54), we have: *I* *m* = aV ⎛1R *IdI* 01 + ⎞exp ⎛ VRI ⎝ aV + 1t1⎠ s ⎞ + aV ⎛1R *IdI* 02 + ⎞exp ⎛ VRI ⎝ aV + 2t1⎠ s ⎞ *V* s *dV* s *dV* *m* 1t1⎝ ⎠ 1t1⎝ ⎠ 1 ⎛⎝1R *dI* ⎞⎠ + R sh +s *dV* (56) Using (50), we obtain: ⎛ V0c ⎞ ⎛ V0c ⎞ <u>V</u> IIexp = ⎛⎜⎟⎜⎟ ⎝ aV 1t1⎠ −1Iexp ⎞ + ⎛ ⎝ aV 2t2⎠ −1 ⎞ + R<u>0c</u> ph 01 02 ⎝ ⎠ ⎝ ⎠sh (57) Substituting (57) into (49), RI V0c ⎞ ssc⎞ ⎛ V0c ⎛⎝ aV ssc ⎞ ⎛⎛ aV ⎛ RI aV⎞⎛ aV ⎞ 2t2⎞⎠ I sc= I₀₁⎜⎟ exp⎝ 1t1⎠ − exp⎝ 1t1⎠ + I₀₂⎜exp⎝ 2t2⎠ −exp ⎟ ⎝ ⎠ ⎜ ⎝ ⎟ ⎠ <u>VRI</u> <u>0c−s sc</u> + Rsh(58) Substituting (57) into (51), ⎜⎟ ⎛⎝ <u>VRI</u> <u>mp+ s mp</u> ⎞⎠ ⎜⎟ ⎛⎝ <u>VRI</u> <u>mp+ s mp</u> ⎞⎠ ⎛ ⎛ V0c ⎞ aV 1t1 ⎞ ⎛ ⎛ V0c ⎞ aV 2t2 ⎞ I mp= I₀₁⎜exp⎝ aV 1t1⎠ −exp ⎟+I₀₂⎜exp⎝ aV 1t1⎠ −exp ⎟ ⎝⎜ ⎠⎟ ⎝⎜ ⎠⎟ <u>VV</u> <u>0c−mpRIsmp</u> + Rsh − Rsh(59) ⎛ V0c ⎜⎟ ⎛ <u>VRI</u> <u>mp+ s mp</u>⎞ ⎞ I(1 mp+= <u>Rs</u> )Iexp01⎜ ⎛⎝ aV 1t1⎞⎠ −exp ⎝ aV 1t1 ⎠ ⎟ Rsh ⎜ ⎟ ⎝ <u>VRI +</u> ⎠ ⎛ ⎜⎟ ⎛⎝ <u>mp s mp</u> ⎞⎠ ⎞ ⎛ V0c ⎞ aV 2t2 <u>VV0c−mp</u> + Iexp02⎜ ⎝ aV 1t1⎠ −exp ⎟ + Rsh ⎜ ⎟ ⎝ ⎠ (60) Eqs. (56), (58) and (60) are three independent equations with four unknown variables I₀₁, I₀₂, Rsand Rsh. The derivative of the current with respect to the voltage at the short circuit current is equal to: *dI* =− *dV* *IIsc* *V* = =0 *Rsh* (61) The derivative of the current with respect to the voltage at the open circuit voltage is equal to:

*dI* =− *dV V*=0 *Rs* *IIsc* = (62) Rshand Rscan be calculated simultaneously by iteratively increasing the value of Rswhile simultaneously calculating the Rshvalue. From Eq. (29) at maximum power point condition, the expression for Rshcan be rearranged and rewritten as [33,52]: <u>VIR +mp s</u> *R* *p*=<u>Vmp</u>++ <u>RsImpmp Vmp RsImp</u> IIexp − ⎛⎛ ⎝ a1Vt1 ⎞ ⎠ ++ exp ⎛ ⎝ a2Vt2 ⎞ ⎠ 2 ⎞ − <u>Pmp,E</u> ph 0 Vmp ⎝ ⎠ (63) Where P mp,Eis the maximum power provided by the manufacturer’s data- sheet. The initial conditions for both resistances are given by: *V* *mp*<u>VV0_ cSTC−mp</u> *R* *sp* 00== 0, *R* − *IV* *scSTC*−*mpImp* (64) Now, after defining all the equations governing the current-voltage characteristics of a solar cell, the Eq. (47) is defined in a non-linear manner and it is needed to solve it to check the current-voltage and power-voltage dependence. Under real conditions: taking into account the variation of the temperature and the solar radiation The photo-current is given by: <u>G</u> I(I ph=+−ph−STCK(TT))i STC GSTC(65) Where <u>RR</u>ps<u>+</u> II ph−− STC=sc STC Rp (66)

Kiis temperature coefficient of short circuit current (A/°C) I sc_STCis the short circuit current at Standard Test Conditions (A) Taking account the dependency on temperature variation of open circuit voltage and of short circuit current. The reverse saturation current of the diodes D₁ and D₂ can be expressed by the following Eqs. [18,31]: IK(TT) sc−STC+−i STC II I 00102=== <u>VK(TT) +−</u> exp() <u>0c−STC</u> aV <u>v</u> t <u>STC</u> −1 (67) Where V0c_STCis the open circuit voltage at Standard Test Conditions (V) Kvis temperature coefficient of open circuit voltage (V/°C) The integration of the solar variation on the open circuit voltage into Eq. (51), has allowed us to describe this equation in the form [18,48]: IK(TT) sc−STC+−i STC II I 00102===G ⎛ (V0c−STC +− + Kv (T TSTC)) aV ln ( t GSTC)⎞ exp ⎜ aVt ⎟−1 (68) ⎝ ⎠ <u>G</u> I(G,T) sc=+− Isc_STCK(TiSTCT) GSTC(69) <u>G G</u> V 0c(G, T) =−− V0c_STCKv(T TSTC) + aVln (t) GSTCGSTC(70)

I(G,T) I mp=mp_STC G G (71) STC <u>G</u> V mp(G, T) =−− Vmp_STC G K(T TvSTC) (72) STC

2.4. MDDM model parameters extraction In the MDDM, the influence of grain boundary region is taken into consideration. Therefore, an additional resistance RS2is added in series with the second diode D₂ as shown in Fig. 1d. This fact is well justified as the resistivity in the vicinity of grain boundaries is higher than that within the crystallites [25,57]. By applying KCL, the relationship be- tween the supplied current and the voltage is expressed by Eq. (73).
⎛⎝ VRI + s ⎞⎠ II =−−−=−phId1Id2IshIphIexp01⎜⎛aV 1t1 −1 ⎟⎞ ⎝ ⎠ ⎛⎛ <u>VRII R +− s d2 s2</u>⎞ ⎞ <u>VRI +s</u> − Iexp02⎜⎟ ⎝ aV 2t2 ⎠ −1− ⎝ ⎠ Rsh (73)

2.5. TDM model parameters extraction Although the ideal values of n₁ and n₂ of TDM were evaluated by 1 and 2 respectively, these values are not valid for industrialized panels of larger size. In addition, the announced values show that the model has two diodes represents deficiencies to correctly represent the different parameters of the solar cells [58]. In [59], it has been proved by simulations and experimental tests made on crystalline Si solar cells that the diode ideality factor, n, in- creases with increasing defect density. Given the fact that solar cells are vulnerable to increased localized defects during their fabrication, an increase in Donor-Acceptor Pairs (DAPs) that are effective for in- creasing the recombination rate leads to higher values of the ideality factor n which can reach a value of 5. For this reason, new works have proposed a circuit model equivalent to three diodes that takes into account the leakage current in the periphery [58]. II =− I{ *exp*
<u>qIR (V++so(1 KI))</u> } ph 01 *nkT* 1 <u>IK(TT)</u> <u>sc−STC+−i STC</u> = (V0c−STC +− + Kv (T TSTC)) aV ln ( t G ) ⎛ <u>GSTC</u> ⎞ exp ⎜ aVt ⎟−1 ⎝ ⎠ (74) In this case study, the series resistance Rsis not assumed to be constant. Therefore, it is evolved as a variable parameter which strictly depends on the load current variation. This variable résistance is indeed replaced with Rs0(1 + KI), where I is the load current and k is another parameter [58]. The current through the PV cell for TDM considering the series resistance can be defined by: ⎧ <u>qIR (V++s0(1 KI))</u> ⎫ ⎧ <u>qIR (V++s0(1 KI))</u> ⎫ II =−phI01*exp* −1I −02*exp* −1 ⎨ ⎩ *nkT*1⎬⎭ ⎨⎩ *nkT*2⎬⎭ ⎧ <u>qIR (V++s0(1 KI)) (V++ IRs0(1 KI))</u> − I₀₃ *exp* − 1⎫ − ⎨ ⎩ *nkT*3⎬⎭ *Rsh* = I(V, I, parameters) (75) Where parameters = (I, I, *nnnRKR*, I,, I,,,,) ph 01 1 02 2 03 3 s0 *sh* (76)

3. Extraction of parameters for PV model
3.1. Problem statement With the potential interest of photovoltaic electricity in scientific
⎜⎟

and economic terms, photovoltaic cells are being at the heart of the electricity production chain. Competition over optimizing and in- creasing the efficiency of photovoltaic cells, leads researchers and in- dustrialists to find efficient and reliable methods to determine the in- trinsic parameters of these cells [39,61–64]. In the literature several methods have been proposed for the extraction of the parameters of the solar cell models. Two types of approaches have been used: analytical or traditional approaches [18,20,43,45] and numerical or evolutionary approaches [19,28,29,42,51,65]. Each of these methods has drawbacks, either at the level of the complexity of the use and the precision, or at the level of the convergence and the speed. To deal with this challenge in this area, this paper reviews the methods of estimating electrical parameters for SDM, DDM, MDDM and TDM models.

3.2. Overall review on methods of PV cells parameter estimation In the literature, the SDM is the most used compared with different other models [15,36,38,39,42,47,50–53,61,63,64,66–93]. In all these cases, the evolutionary algorithms are more investigated in comparison with the analytical and the numerical approaches. Among these algo- rithms, we can cite, in particular, the Genetic Algorithm (GA) [13,61], the Particle Swarm Optimization (PSO) [13,14,61,65,75,77] and the Differential Evolution (DE) [13,33,51,56,61,68,74,78]. In the previous works, the parameters to be extracted varied from 3 to 7 for the SDM and from 4 to 8 for the DDM. Furthermore, 10 parameters have to be extracted for the TDM. This means that the problem reformulation depends entirely on the number of used diodes to describe the equivalent electrical circuit of the solar cell model. For that purpose, a multitude of photovoltaic cell technologies has been investigated like Poly-crystalline, Mono-crystalline, and Thin-film/Amorphous. While, each of them is characterized by its typical performance, influence of temperature, advantages and disadvantages. The most dominant and undisputed factor in the various studies that have addressed the issue of estimating the parameters of a model de- scribing the equivalent electrical circuit of a solar cell/module/panel is the criterion of performance evaluation of the used model. According to this factor, all references have almost agreed that Relative Error (RE) is essential to evaluate the achieved results [13,16,27,37,54,55,68,69,71,73,80,84,89,90]. RE basically describes the difference between the extracted and the measured parameters in percent [94]. In order to quantify the accuracy and the goodness of the proposed models over current-voltage characteristics, a Root Mean Square Error (RMSE) analysis was also applied [16,31,33,36,37,39,42,52,53,56, 60,61,66,69–71,73,77,78,84,88,95,96]. Besides, some other metrics of the magnitude of the error are possible to be used but they are not very widespread in the literature, such as the Mean Square Error (MSE) [66,91,96,97], Mean Bias Error (MBE) [16,33,39,52,56,78], Absolute Error (AE) [33,47,51,67,84,89], Individual Absolute Error (IAE) [55,71,73] and Sum of Squared Error (SSE) [13,16]. Thanks to the used performance criteria, each of these works has shown the accuracy of the problem to be solved in an efficient way. But, the difference between these different works is in the use of the experimental data to describe the real behavior of the I-V and P-V characteristic or not. The following Tables discuss, summarize, and classify the foremost techniques for DC parameter extraction on the basis of the year of publication, the used model, the used approaches, the number of ex- tracted DC parameters, the used data, the type of PV cells and the performance criteria. For each of the models discussed, a critical ana- lysis of found results is carried out to highlight its advantages and disadvantages. The Tables 1–3 depict the analytical, the numerical and the metaheuristic based methodologies, respectively. Following the critical study of published techniques related to the extraction of parameters of PV cells, Table 4 highlights the different types and models of the PV cells studied by the reviewed works. At this stage, it is important to focus on another type of
classification. Indeed, it is important to note that the use of the math- ematical / analytical model is more often effective for PV cell parameter extraction if the manufacturer datasheet information’s are used, whereas numerical techniques are more effective when using experi- mental data. The Tables 5, 6 classify the approaches methods that use datasheet information’s and those that use experimental data. As mentioned previously, the result of the issue of extraction of the parameters of a solar cell is obvious when it is followed by a serious evaluation. For this, the following section describes in detail the dif- ferent evaluation criteria used in the majority of the works mentioned in the above tables (Table 1, Table 2 and Table 3) as follows: The RMSE evaluation criterion, which compares the error between experimentally and calculated data, is defined by [16,31,33,36,39, 42,52,53,60,61,66,70,78,88,93,95,96]: *N* 12 *RMSE* =− ∑ () *IIactual calc* *N* *i*=1 (77) The RMSE which evaluates the objective function and used in the case of optimization problem, is given by [69,71,73,77,83,84]: *N* *RMSE* = 1 ∑ ((,, )) *fVIxi ii* 2 *N* *i*=1 (78) The equation that describes the Normalized Root Mean Square Error (NRMSE) is as follow [92]: 1 ∑ *N* () *IIexp*−*sim* 2 *N i*=1 *NRMSE* = 1 *N* *N* ∑*i*=1*Iexp*2 (79) The Root-Mean-Square Deviation (RMSD) [93]: *Ncurve* 2 <u>∑j=1() II</u>*jj*<u>−</u> *RMSD* = *Ncurve* (80) The Normalized Root-Mean-Square Deviation (NRMSD) [87,93]: *NRMSD*(%) = <u>RMSD</u>

.100
*I* *sc*(81) The Mean Absolute Error (MAE) [16,64,65,69,79,84,88,96]: 1 *N* *MAE* (%) =− *N* ∑ |*IIVaii*(,)|.100 (82) *i*=1 The Mean Absolute Error in Power (MAEP) [16,93]: <u>∑</u>|| <u>PP −</u> *MAEP* (%) = <u>curve model</u>

.100
*Ncurve*(83) The Mean Bias Error (MBE) [16,33,39,52,56,78]: *N* *MBE* (%) =− 1 ∑ [*IIVaii*(,)] 2

.100
*N* *i*=1(84) The Mean Square Error (MSE) [66,91,96,97]: <u>∑</u> *N* <u>() Ii −</u>2 <u>i=1 ii</u> *MSE* = *N* (85) The Sum Square Error (SSE) [16,56]: *N* *SSE* (%) =− ∑ [*IiiI* (*V*, *a*)]2.100| *i*=1(86) The value of the Residual Error of the Fitness Function (REFF) [86]:

*REFF* = ∑ *fk*(*x*) (87) *k*=1 The Absolute Error (AE) [33,47,51,67,73,78,83,84,89,97]:

R. Abbassi et al.
Analytical and unnamed used approaches for determining the parameters of PV cell/panel/module.

Table 1

References Year of publication [15]

[43]

[62]

[63]

[64]

[67]

[85]

[86]

[87]

[93]

[104]

[105]

[110]

Used approaches Number of Used data parameters Mathematical techniques Five parameters Manufacturer I-V and P-V data

Analytical and Quasi-Five parameters-Real data measurements Explicit (AQE)-Theoretical data

Analytical approach Five parameters Measurement I-V data, Rsh Analytical approach Five parameters

Unnamed Five parameters Standard datasets

Analytical approach Five parameters Experimental I-V data from manufacturers

Unnamed Five parameters Numerical informations of manufacturer data sheet Unnamed Six parameters Manufacturers’datasheet

Lambert W based analytical Five parameters Datasheet information method Unnamed Five parameters Manufacturers’datasheets

Theoretical analysis Five parameters approach I-V curves Unnamed Five parameters Single I-V curve

Analytical approach Five parameters Datasheet values

Performance criteria

MAPE ( Eq. 93) R²(Eq. 91) Normalized Area Error

MAE ( Eq. 82)

-AMD -RMSd MAE( Eq. 82) ACE( eq. 100 )

AE (Eq. 88)

AE( Eq. 88)

REFF( Eq. 87)

NRMSD( Eq. 81) -CPU Execution time MAEP( Eq. 83) RMSD( Eq. 80) NRMSD( Eq. 81)

-AM -SD RMSE ( Eq. 77)

Not mentioned

Results

The presented discussion and classi fication of DC parameter extraction techniques provides a reference for researchers to select the appropriate model based on the structure of the experiment and the selected implements. AQE method uses just the coordinates of four arbitrary points of the I-V characteristic and their slopes. Compared with OAM method [72] and analyticalfive-point method [98], experimental results show that AQE exhibits fast convergence speed and high accuracy because no simplifications are used. Simulation results manifest the superiority of the proposed model including the inverse dependence of the shunt resistance on the irradiance on the SDM model in terms of accuracy with the measured data and average error reduction. Results shows that the model de fined by the new electrical characteristics exhibits a high degree of accuracy of the operating current evaluation, even during rapid changes of solar irradiance. Based only on good measurement of the panel temperature and the OSMP (T; VOC; ISC; VM and IM), the proposed technique gives more accurate results, compared to other existing techniques (LMSA, CPSO, SA, PS, BMO ABSO, GA, NR). It needs simple calculation and few measurements but it is not suitable for multi-junction solar cells/ panels. The observed superior accuracy of the proposed model to describe PV modules behaviors, at any irradiance and temperature point, con firms that it allows an even better phenomenological description of the nonlinear e prevalent in PV modules. This might be a valuable design tool during the production as ffects of electrical mechanisms well as during the use of PV systems. The method simply implemented considers the error and error propagation. It provides high selective capability for users of PV module according to their requirements with more accuracy and reliability in prediction of performance of PV modules. This paper suggests a fast, flexible and accurate algorithm based on a reduced-form of the nonlinear system of equations for the computation of the six parameters required by the CEC6PPVMM model. The proposed method is a computational improvement of the model of De Soto, in terms of accuracy, efficiency, robustness and ease of implementation. It is very useful for various operating conditions of PV modules. *Renewa* •The proposed method defines a new error metric MAEP. •It extracts the parameters using the P –V curves instead of I –V curves. The values ranges of estimated parameters respect their physical meaning. *ble and Sustainable Energy Reviews 90 (2018) 453–474* • •It is more accurate than well-known methods (Xiao ’s Method [99], Villalva ’s Method [100], Nonlinear Least Square (NLS) Method[101], Mahmoud ’s Method [102], Accarino’s Method (Explicit Equations) ( [103]). As part of the presented theoretical and practical analysis, the developed fully mathematical approach makes it possible to simplify the procedures of the simulations of PV systems and to improve their accuracy considerably. The proposed algorithm does not require the particular parameters Isc,Vocand Pmmp.It is also very important as it: •is simple and without any approximation •works even for incomplete I-V curves •does not involve the slopes (dI/dV) at any point. Result shows that the proposed model allows a more accurate modeling of the PV modules based solely on reference data. The model is based primarily on an analytical relationship devoid of any simpli fication that can affect the reliability of the results.

Experimental I-V characteristic

Datasheet values and experimental-SA

R. Abbassi et al.
Table 2

Numerical used approaches for determining the parameters of PV cell/panel/module. References Year of Used approaches Number of Used data Performance criteria Results

|References|Year of|Used approaches|Number of|Used data|Performance criteria|Results|
|---|---|---|---|---|---|---|
||publication||parameters||||
|[31]|2016|Lambert W-function based exact representat-ion (LBER)|Seven parameters|Experimental I–V, P-V data Manufacturer’s I-V, P-V data|ACE ( eq. 100 ) RMSE ( Eq. 77)|A significant result of the proposed LBER is the fact that in spite of the more time consuming, the proposed model is more accurate and robust.|
|[37]|2014|Analytical and numerical (Newton-Raphson) approaches|Five parameters|Experimental I-V data|RE (Eq. 89) NRMSE (Eq. 79)|The results show the superiority and validity of the application of the analytical-numerical proposed technique to merge the obtained simulated I curves with the experimental data.|
|[38]|2014|The nonlinear equation solver Five parameters ‘fsolve’||Experimental I-V and P-V curves|Derating factors|The modi fied simulation model was found to be valuable for accurately predicting the I-V curve characteristics of PV modules.|
|[39]|2015|Numerical algorithm|Five parameters|Manufacturers’I-V data|DC:r²(Eq. 91) RMSE(Eq. 77) MBE( Eq. 84)|Accurate model with measured data of six crystalline silicon PV panels and acceptable suitable for practical applications|
|[42]|2016|Villalva[99] T. Esram [106] Vika [107]|Five parameters|Manufacturer’s data sheet|RMSE(Eq. 77) MABE(Eq. 92) MAPE(Eq. 93)|The comparative study of Villalva performances in terms of accuracy, speed of computation, required memory space, ease of implementation and robustness, is a decision key for selecting the best extraction algorithm|
|[47]|2014|Lambert W function based method|Five parameters|Manufacturer datasheet|AE( Eq. 88)|Compared to the popularR the current-voltages points at the maximum point and even in case of ideality factors variations.|
|462 [54]|2011|Newton-Raphson algorithm|Four parameters|Manufacturers’I-V and P-V data|RE (Eq. 89)|In accordance with theoretical prediction, the accurateness of the proposed TDM based MATLAB Simulink PV system simulator reduces computational time and input parameters available on standard PV module datasheet. This has been verified for di when interfaced with actual power electronic converters driven by MPPT algorithms.|
|[27]|2011|Newton- Raphson Algorithm|Four Parameters|I-V data from Manufacturers|RE (Eq. 89)|Thanks to its simplicity, its convergence speed and its precise correspondence with the keys points of the I-V curve, this method proves to be very e circuit simulators developers and photovoltaic power converters designers.|
|[56]|2017|Explicit Model|Eight Parameters|Experimental I-V data|SSE (eq. 86)|The found results reveal that the parameter values extracted does not contradict the conventional parameters and their physical concepts.|
|[66]|2015|Numerical approach|Five parameters|Datasheet values provided by manufacturer-s|MSE ( Eq. 85) RMSE ( Eq. 77)|The presented model is able to compute accurately all the model parameters. Renewa An improvement was also reported in the Newton-Raphson’s solving to accelerate the convergence.|
|[76]|2014|New compound method|Five parameters|Basic manufacture template data|RE( Eq. 89) -Prediction of the output power of real PV power stations|The proposed algorithm provides an easy, feasible and accurate mean for: Simulating the I Predicting the real-time generation output of a PV power station.|
|[108]|2016|Runge-Kutta-Merson iterative method|Seven parameters|Datasheet I-V,P-V|Not mentioned|The computed results have been compared with di U-EA110, MPV95-S, and MST-43LV modules. The outcomes of the proposed model show achieves a good improvement of the design and operation under different weather conditions.|
|[111]|2014|Numerical approach based on reduced forms|Five parameters|Experimental I-V curve|-Squared Error SE-RMSE (Eq. 77) -AE (Eq. 88) -MAE (Eq. 82) -Weighted RMSE|The presented approach allows characterizing a PV module from its measured I- V curve with an accuracy and execution time never obtained before. A comparison study with other recent and e different cases is established.|

–V

[99], Esram[106] and Vika [107] algorithms

pmodel, an excellent agreement was found between

fferent types and large array simulation of PV modules even

ffective for

*ble and Sustainable Energy Reviews 90 (2018) 453–474* •–V and P–V characteristics of a PV array • fferent manufacturers data of

ffective techniques in the forms of two

R. Abbassi et al.
Table 3

<u>Metaheuristic used approaches for determining the parameters of PV cell/panel/module.</u> References Year of Used approaches Performance criteria

RE( Eq. 89) Evolutionary Algorithms (EA):Genetic Algorithm Seven parameters [13]

- Fitness value
(GA), Particle Swarm Optimization (PSO) and -CPUtime Differential Evolution (DE).

[14] PSO MRE ( Eq. 90)

[16] Shu ffled Complex Evolution (SCE) technique

[33] (DEIM)

[36] Evolutionary Algorithms (EA): PSO CS CS-NMS GA [50] Artificial neural Network (ANN)

[51] Differential Evolution (DE)

[52] Evolutionary Algorithms (EA)

[53] Simplified Bird Mating Optimizer (SBMO) approach [55] Fireworks Algorithm (FWA)

Number of parameters Used data

Datasheet I-V data

Seven parameters Experimental I-V curves

Seven parameters Experiment al data

(PDE model [19], Rcr-IJADE [27,29,106] and IADE [109]).

Five parameters Experimental I-V points Seven parameters

Five parameters

Three parameters Experimental I-V data from manufacturers

Five and seven Experimental I-V points parameters Five parameters Experimental I-V data

Seven parameters I-V datasheet

RE( Eq. 89) SSE(eq. 86) RMSE( Eq. 77) MBE( Eq. 84) MAE( Eq. 82) MAEP( Eq. 83) MBE( Eq. 84) AEmppt(Eq. 88) -CPU-execution time (s) -NE -RMSE ( Eq. 77)

Results

According to various evaluation criteria namely accuracy, consistency, speed of convergence, calculation e fficiency and the number of control parameters required, it has been proved that the EA methods make it possible to construct an efficient PV system simulator and speci fic. The PSO based parameter extraction routine can rapidly reach a goodfitting of the extracted parameters of solar cells and PV modules from the I –V curves. It also seems to be a useful tool to determine the parameters that a ffect the performance of these devices. Compared with AM, LM, GA, DE, and PSO methods, the SCE presents: •a more accuracy. •a low convergence computational time. •a significant ability to solve all global optimization problems. The proposed DEIM performs high accuracy and fast convergence speed. Results depict that, The average root mean square error, mean bias error, and absolute error of the proposed model at maximum power point are 1.713%,

0.149%, and 4.515%, respectively. Referring to the goodfitting of the fundamental behavior of the I–V curves, the presented approach may yield optimized solutions not as physically correct as it was expected. Thus, a correctly interpretation of the optimization results must be taken. The ANN model can be useful to determine a higher accuracy than the conventional SDM under various operating conditions. The proposed model shows promising performance for any temperature and irradiance variations. It is highly effective to obtain an accurate PV module model useful for PV simulator developers. The electrical model using the parameters estimated by
*Renewa* the proposed methodology showed better results than several models from literature. *ble and Sustainable Energy Reviews 90 (2018) 453–474* The approach (SBMO) presented is very promising in the presence of problems of optimization of photovoltaic modules. The proposed Fireworks algorithm has been comprehensively tested with SM55 & SP70 and Kyocera200GT PV technologies. It have been also benchmarked with GA and PSO methods. The FWA algorithm allows to: ▪ Reduce the probability of premature convergence. ▪ Reduce computational complexity ▪ Produce I-V characteristics near accurate with those of panel data sheet ▪ Reduce the convergence time by 0.95s and 2.85s relative to GA and PSO, respectively. ▪ Get more precision. (continued on next page)

AE (Eq. 88)

RMSE ( Eq. 77) MBE ( Eq. 84) RMSE ( Eq. 77)

IAE (Eq. 94) RE (Eq. 55)

Differential Evolution with Integrated MutationSeven parameters Experimental data and other models -ARMSE

Datasheet and experimental I-V dataNot mentioned

Table 3 (continued)

References Year of Used approaches Number of parameters

Differential Evolution and Electromagnetism-likeFive parameters [56] algorithms

[60] Moth-Flame optimizer (MFO) algorithm Ten parameters

Five and seven parameters

Seven parameters

[68] Differential Evolution Technique (DET) Five parameters Seven parameters [69] Harmony Five and seven Search (Hs)-based algorithms parameters [70] bio-inspiredalgorithms Five parameters

[61] LMA GA DE PSO ABC [65] Particle Swarm Optimization method

-Five parameters for SDM -Seven parameters for DDM Five parameters

Used data

Experimental I-V data points

Experimental I-V characteristics

Experimental I-V and P-V curves, current Vs time variation

Measured illuminated I-V characteristic of 82 solar cell samples

Experimental I-v data I-V measurement

Datasheet I-V curves

Real I-V, P-V data

Real data of voltage and current measured from a PV module

R. Abbassi et al.
Performance criteria Results

RMSE( Eq. 77) The found results manifest the superiority of the proposed MBE ( Eq. 84) evolutionary algorithm with integrated mutation per CD r²(Eq. 91) iteration and evolutionary algorithm with adaptive -CPU execution time mutation per iteration, compared to electromagnetism- like algorithm. The main advantages are related to the execution time, the accuracy and the convergence. -RMSE ( Eq. 77) The main advantage of the MFO algorithm compared to -MFO the DEIM and FPA techniques is that it converges rapidly -DEIM to optimal solutions. -FPA -R² (Eq. 91) RMSE ( Eq. 77) The ABC algorithm shows that it is very accurate, in terms NMAE of the estimated values of unknown parameters, compared to the LMA, GA, DE and PSO algorithms.

MAE( Eq. 82) The suggested engineeringfit model between the reverse saturation current and ideality factor of the first diode seams an easy method to predict the PV module output by reducing the number of silicon solar cell parameters needed for its modeling. IAE (Eq. 94) Compared with ABSO, CPSO, HSA, SA, PS, OIS, and DAB RE (Eq. 89) parameter extraction techniques, the DET method o ffers RMSE ( Eq. 77) more accuracy with faster convergence. RMSE ( Eq. 78) Simulation results obtained using HS variants show that RE (Eq. 89) HS-based algorithms is a consistent tool for modeling PV MAE ( Eq. 82) cell systems. RMSE( Eq. 77) The critical discussion of the di fferent bio-inspired algorithms (GA, DE, ABC, BFA and CS) to extract the parameters of the SDM made it possible to evaluate the advantage of each algorithm in terms of the RMSE, the speed of convergence and the accuracy. RMSE( Eq. 78) The proposed MPCOA outperforms other meta-heuristic IAE(Eq. 94) algorithms, such as GA, CPSO, ABSO, SA, PS, HSA. The RE( Eq. 89) proposed new technique is preferable method to *Renewa* determine the parameters of PV cell models. -Error between Simplified It has been proven that OAM method is advantageous than parameters A, B, C, D and analyticalfive point method. OAM approach outperforms *ble and Sustainable Energy Reviews 90 (2018) 453–474*

E. other methods that need to know the slope of the real I-V (Eqs. 95 –99) curve near the open circuit point. Besides OAM involves a -Area between real and simple calculus in its resolution. OAM seems to be a useful Estimated I-V curves. tool to characterize PV modules and to analyze their
behavior. Nevertheless, further investigations should be focused on analyzing the parameter sensitivity of this method under variation of climatic conditions. Eq. 78) The proposed BPFPA method, combining ABC and FPA, AE( Eq. 88) was compared with Flower FPA, PS, GA, HS and ABSO RE( Eq. 89) algorithms. The potential in BPFPA is esteemed as it is IAE(Eq. 94) easy to comprehend and it converges to global optimum -Curve fit accuracy location with fast execution speed. -Convergence to global optimum (continued on next page)

[71] Mutative-Scale Parallel Chaos OptimizationAlgorithm (MPCOA) [72] Oblique Asymptote Method (OAM)

[73] (BPFPA) -Five parameters for SDM -Seven parameters for DDM

Bee pollinator Flower Pollination Algorithm Experimental data and other models RMSE(

R. Abbassi et al.
Table 3 (continued)

References Year of Used approaches Number of parameters Used data Performance criteria Results

[74] Improved Free Search Differential Evolution Five parameters Real data acquired in di fferent-Minimum, The validity of the IFSDE is approved compared with other (IFSDE) temperature conditions-Maximum well-known metaheuristics, namely GA, HS and PSO. Its -Median superiority is found particularly as it is better in escaping -Mean local optima. -Standard deviation of the objective function [75] Particle Swarm Optimization (PSO) technique Three parameters: Manufacture ’s data-APE The accuracy of the model using PSO with binary with binary constraint-Ideality factor ( a), (for KD210GH-2PU) constraints is assured regardless the insolation and the -Series-APVE at MPP temperature change. The proposed technique is also able Resistance(Rs) (for SP70 and SQ85) to determine ideality factor, series and shunt resistance -Parallel resistance ( Rp) simultaneously without the need of estimating ideality factor andfield data measurements. [77] Modi fied Simplified Swarm Optimization (MSSO) Five parameters for SDM Experimental data of RMSE( Eq. 77) Compared to many other famous optimization algorithms -Seven parameters for 57-mm diameter commercial (R.T.C. (SSO, ABC, SBMO), the MSSO method enables better DDM France) silicon solar cell performances in terms of robustness, e fficiency, accuracy and coincidence of the I-V characteristics with those of experimental data. [78] Differential Evolution with Adaptive Mutation perFive parameters Experimental data and results of AE( Eq. 88) The improved DEAM is advantageous compared with PDE iteration algorithm (DEAM) other previous methods (PDE and RMSE( Eq. 77) and IADE methods, in terms of accuracy, convergence, and IADE) optimal adjusted control parameters. MBE( Eq. 84)•Its RMSE is lower than PDE and IADE methods by CD-r (Eq. 91) about 14.3%. •Its MBE value is less than PDE and IADE by 23.3%. The CPU-execution time is less than both PDE and IADE by

8.5% and 9% respectively.
[79] Imperialist Competitive Algorithm (ICA)-Five parameters for-Experimental data extracted from MAE( Eq. 82) The proposed ICA algorithm is superior, e fficient and SDM datasheets reliable in estimating the PV cell/module optimal -Seven parameters for-Other reported meta-heuristic parameters for both SDM and DDM as it ensures the best DDM optimization algorithms fitness function with acceptable time. [80] Teaching Learning Based Optimization (TLBO) Five parameters Experimentally measured I–V RE( Eq. 89) The proposed TLBO algorithm overcomes the limitation of algorithm characteristics various numerical methods and conventional optimization algorithms to identify the solar cell parameters. The found results exhibit that the values of extracted parameters match exactly with the reported data. [81] Five versions of the bacterial foraging (BF) Five parameters for SDM Nameplate data of the PV module Matching between The findings show that all various BF algorithm versions *Renewa* optimization algorithm And Seven parameters experimental and allow to reach PV module parameters. A good matching for DDM analytical has been exhibited between experimental and analytical results with high accuracy and fast convergence speed. *ble and Sustainable Energy Reviews 90 (2018) 453–474* [82] Based Powell’s optimization method PSIM Five parameters Manufacturer’s datasheet values IEC EN50530 standard The proposed PSIM simulation model improves the simulation model measured under STC accuracy by tuning thefive model parameters by Powell’s optimization method according to the time-varying irradiance and temperature conditions. It can be applied to various simulation programs and as the PV simulation engine in PV hardware simulators. It allows the automation of the process of extraction of the parameters which facilitates its use and guarantees uniform and very accurate results. [83] Generalized Oppositional Teaching Learning-Five parameters for Experimental data AE( Eq. 88) The GOTLBO method uses the concept of GOBL to Based Optimization (GOTLBO) SDM RMSE( Eq. 78) diminish the convergence time of original TLBO according to the initialization step and generation jumping. -Seven parameters for-ANFES When compared with GA, CPSO, PS, SA, IGHS, ABSO, Rcr- DDM-SR IJADE and STLBO, for SDM, and with PS, SA, IGHS, ABSO, -Convergence graphs Rcr-IJADE and STLBO, for DDM, GOTLBO behaves better in terms of computational overhead and solution accuracy. (continued on next page)

Table 3 (continued)

References Year of Used approaches

[84] (ER-WCA)

[88] Reduced-Space Search based method

[89] Genetic Algorithms (GA)

[90]-LMA -TRRN -SDO

[91] PSO-guided BF

[92] Adaptive Estimation Approach

[95] approach

[96] Artificial Neural Network (ANN)

[97] Hybrid optimiser approach

[112] Mean Blast Algorithm (MBA)

Number of parameters Used data

Five parameters Experimental data

Five parameters Experimental I–V curves

Five parameters Manufacturers’datasheet

Five parameters Measured Data

Four parameters Measured data

Five parameters Standard test conditions informations

Real operating P-V data

Four and five parameter models

Seven, Eight and Nine parameters Five and seven Measured Values parameters

Performance criteria

RMSE ( Eq. 78) AE (Eq. 88) MAE ( Eq. 82) RE (Eq. 89) MRE ( Eq. 90) -NFE -Number of steps -Number of Function Evaluations (FES) RMSE( Eq. 77) MAE( Eq. 82) -Solution times AE( Eq. 88) RE( Eq. 89)

R. Abbassi et al.
Results

In terms of RMSE, MAE and MRE, the ER-WCA is advantageous to NMMPSO, GOTLBO, MABC, CSO, BBO-M methods even under changing irradiation and temperature conditions.

This method exhibits two signi ficant advantages: •The ability tofind high-quality solutions at a reduced computational complexity •The possibility to be fully automated without the recourse to preliminary data selection. •Applicability to I-V curves independently of the weather conditions. •It does not require solving the transcendental equation describing I-V characteristic •Satisfactory accuracy and simple calculation •Feasible in absence of datasheet or in case of old and degraded PV panels •It complies with the datasheet-based method for clear sky conditions and more advantageous than it for cloudy sky conditions •Accurate in MPP prediction. •PSO-guided BF could find simply the best value of the objective function and requires no mathematical derivations. •Under different operating conditions, PSO-guided BF always exhibits least MSE. All the results prove that the proposed method: •Is easy to implement •Is robust and faster than the others methods •Is able to generate a unique and accurate solution even for impracticable initial guesses Compared to the reverse propagation network (BP) model, the presented TWIESN model is more satisfactory in terms *Renewa* of simplicity, accuracy, robustness and e fficiency regardless of the operating conditions. The ANN model predicts the power and current of the PV *ble and Sustainable Energy Reviews 90 (2018) 453–474* module accurately more than the analytical models. A comparative study exhibits that the 3 –7–4–1 ANN model is better than the four andfive parameter models.

Results obtained using the proposed single-equation model allows fast and accurate convergence to extract the solar cells parameters even in cases of their degradation. The mean blast algorithm shows more efficiency and reliability compared with other competitive heuristic methods. Results highlight the matching between the measured and calculated I-V, P-V characteristics with negligible absolute errors. (continued on next page)

RE( Eq. 89) -Empirical convergence speed and model-fit accuracy

MSE( Eq. 85)

NRMSE( Eq. 79)

RMSE( Eq. 77) -TIME -ERROR CD-R (Eq. 91) MSE( Eq. 85) MAPE( Eq. 93) MAE( Eq. 82) -MaxabsE -MinabsE MSE( Eq. 85) AE( Eq. 88) MAE ( Eq. 82)

Evaporation Rate based Water Cycle Algorithm

time warp invariant echo state network (TWIESN)Three parameters

-Manufacturer datasheet values -Experimental testing results

Current-voltage Experimental data

R. Abbassi et al.
Table 3 (continued)

References Year of Used approaches Number of parameters Used data Performance criteria Results

[113] Multi-verse optimization (MVO) approach Five parameters Experimental data and speci fications-RMSE ( Eq. 77) It is found that the proposed MVO approach is very useful by vendor’s datasheets-MAE ( Eq. 82) for PV power designers. It is superior to approximate mathematical method and recent heuristic-based approaches. In particular the MVO approach matches very accurately for I –V curves points with a good computational efficiency. [114] Pattern search optimization algorithm Five parameters Manufacturer datasheet values- Current error and power Compared to some conventional and heuristic-based error in the MPP region optimization approaches, the developed approach shows

- Extraction time an absolute consistency between experimental and
theoretical data. The more promising thing is that these results make MVO algorithm scalable to be very useful in case of multi-diode models. [115] Improved JAYA (IJAYA) optimization algorithm Five and seven Experimental data- RMSE( Eq. 78) Experimental results indicate that the proposed IJAYA parameters method is highly competitive in terms of computational overhead and solution reliability and accuracy. [116] Adaptive Nelder-Mead simplex Five and seven Experimental curve- RMSE( Eq. 78) Experimental results compared with those of three (NMS) hybridized with the arti ficial bee colony parameters- IAE(Eq. 94) benchmark problems of a RTC France solar cell and (ABC) metaheuristic algorithms, EHA-NMS photowatt-PWP201 prove that the EHA-NMS outperforms other methods particularly in terms of convergence and reliability. [117] Improved Chaotic Whale Optimization Algorithm Five and seven Measured data-RE (Eq. 89) proposed CWOA algorithm improves capabilities to (CWOA) parameters-Normalized extract PV cell parameter and shows high robustness and relative error accuracy. A comparative study, supported by -MAE ( Eq. 82) experimental results, with other optimization methods -Normalized mean over different datasets is illustrated. absolute error -NRMSE ( Eq. 79) -MBE ( Eq. 84) -Normalized mean bias error

*Renewa* *ble and Sustainable Energy Reviews 90 (2018) 453–474*

R. Abbassi et al. *Renewable and Sustainable Energy Reviews 90 (2018) 453–474*
Table 4
 <u>Different types and models of the PV cells studied by the reviewed approaches.</u>

|Different types and models of the PV cells studied by the reviewed approaches.|||
|---|---|---|
|References|SDM DDM|TDM Type of PV cells|
|Analytical used approaches|||
|[15]|✓✓|Not mentioned|
|[43]|✓|Aerospace High Efficiency Silicon Cell|
|[62]|✓|Multi-crystalline, Mono-crystalline, CIGS, Tandem, Amorpho-us and cdte|
|[63]|✓|Mono-crystalline silicon|
|[64]|✓|35 polycrystalline panels, 32commercial mono-crystalline, 30 thin film panels.|
|[67]|✓|Mono-Crystalline, Multi-Crystalline and Thin-film|
|[85]|✓|Commercial RTC siliconsolarcells|
|[86]|✓|CEC6PPVMMSanyo HIT-N225A01 PV module|
|[87]|✓|ConergyPowerPlus 190PC, Day4 Energy 60MC-I, Perllight PLM-250P-60, Solea SM 190 and Yingli YL-165|
|[93]|✓|Polycrystalline PV Panel Kyocera KC200GT, Polycrystalline PV Panel Kyocera KS20T|
|[104]|✓|Mono-crystalline, Multi-crystalline silicon|
|[105]|✓|Poly-Crystalline silicon PV: PTL Solar|
|[110]|✓|Kyocera KC175GHT-2 and Sanyo HIT240HDE-4|
|Numerical used approaches|||
|[31]|✓|Not mentioned|
|[37]|✓|Not mentioned|
|[38]|✓|Crystalline silicon|
|[39]|✓|Crystalline silicon|
|[42]|✓|Nexpower technology (1-a-Si), NH-100UT_5A polar PV TFSMT-3x(2-a-Si), Xunlight XR12 (3-a-Si), First solar Fs-280 (CdTe), Sunperfect Solar CRM1753K5M-72 (mono-Si), Kyocera Solar KD210GX-LPU(Multi-Si)|
|[47]|✓|57 mm diameter Commercial mono-crystalline silicon cell, QCELLS mod. Q6LM cell|
|[54]|✓|Multi-crystalline, mono-crystalline and thin-film|
|[55]|✓|Multi-crystalline, Mono-crystalline and Thin-film|
|[56]|✓|Poly-crystalline silicon,Mono-crystalline silicon|
|[66]|✓|Mono-Crystalline, Poly-Crystalline, Thin-film and Amorphous|
|[76]|✓|Multi-crystallinePV modules (TSM-230PC05), Mono-crystalline (TSM-180DC01)|
|[106]|✓|Amorphous silicon and thin film|
|[111]|✓|Polycrystalline silicon cells Photowatt-PWP 201Silicon solar cell RTC France|
|Metaheuristic used approaches|||
|[13]|✓|Multi-crystalline, mono-crystalline and thin-film|
|[14]|✓|Mono-Crystalline and Multi-Crystalline silicon|
|[16]|✓|KC120-1 Kyocera PV module|
|[33]|✓|Kyocera KC120-1 multi-crystalline photovoltaic module|
|[36]|✓✓|Not mentioned|
|[50]|✓|Multi- crystalline|
|[51]|✓|Multi-crystalline, mono-crystalline and thin-film|
|[52]|✓|Crystalline silicon and Thin film|
|[53]|✓|Not mentioned|
|[55]|✓|Mono-Crystalline and Multi-Crystalline|
|[56]|✓|Not mentioned|
|[60]||✓ Multi-crystalline silicon|
|[61]|✓|Crystalline silicon Amorphous silicon Micro-morph silicon|
|[65]|✓|Single crystalline silicon solar cells|
|[68]|✓✓|Mono-Crystalline and Multi-Crystalline|
|[69]|✓✓|Silicon solar cell|
|[70]|✓|Not mentioned|
|[71]|✓✓|Multi-crystalline KC 200GTcc silicon, Mono-crystalline SQ 150-PC|
|[72]|✓|Polycrystalline and mono-crystalline photovoltaic modules of EURENER manufacturer|
|[73]|✓✓|Kyocera KC200GT, SM55:mono-crystalline, S36: multi-crystalline, ST40: Thin Film|
|[74]|✓|KC200GT poly-crystalline|
|[75]|✓|Poly-crystalline, KD210GH-2PU, Mono-crystalline, SP70 and SQ85|
|[77]|✓✓|Passivated emitter and rear cell (PERC)|
|[78]|✓|Multi-crystalline PV module|
|[79]|✓✓|Mono-crystalline (SQ150-PC), Poly-crystalline (R.T.C France KC200GT), Amorphous(ST400)|
|[80]|✓|Silicon, Plastic, Dye-sensitized solar cells, Mono-crystalline si solarcell, Poly-crystalline si solar module|
|[81]|✓✓|Eclipsall NRG72 PV module|
|[82]|✓|Crystalline Kc65gt, Kc200gt, Sq160pc|
|[83]|✓✓|57 mm diameter Commercial (R.T.C. France) siliconsolarcell|
|[84]|✓✓|M/s R.T.C. France pv cell, M/s photowatt (pwp-201) pv module|
|[88]|✓|Photowatt-PWP201 module, 57 mm diameter RTC France siliconsolarcell, aSiMicro03036-Cocoa, aSiMicro03036-Eugene, aSiMicro03038- Golden, aSiTandem72-46-Cocoa, aSiTandem72-46-Eugene, aSiTandem90-31 Golden, aSiTriple28324-Cocoa, aSiTriple28324-Eugene, aSiTriple28325-Golden, CdTe75638-Cocoa, CdTe75638-Eugene, CdTe75669-Golden, CIGS8-001-Cocoa, CIGS8-001-Eugene, CIGS1-001- Golden, CIGS39017-Cocoa, CIGS39017-Eugene, CIGS39013-Golden, HIT05667-Cocoa, HIT05667-Eugene, HIT05662-Golden, mSi0166- Cocoa, mSi0166-Eugene, mSi0247-Golden, mSi0188-Cocoa, mSi0188-Eugene, mSi0251-Golden, mSi460A8-Cocoa, mSi460A8-Eugene, mSi460BB-Golden, xSi12922-Cocoa, xSi12922-Eugene, xSi11246-Golden|
|[89]|✓|Polycrystalline silicon PV Panel Kyocera KC200GT|
|[90]|✓|300-W newly installed polycrystalline silicon panel, 210-W 20-year-old polycrystalline silicon panels|
|[91]|✓|LDK C1D2-140P Multi-crystalline silicon PV modules|
|[92]|✓|PV module KC200GT, Multi-crystalline KD201GH-2PU, Mono-crystalline Shell SQ85, Thin film Shell ST40|
|[95]|✓|Not mentioned|
|[96]|✓|Not mentioned|
|[97]||✓ Not mentioned|

(continued on next page)

R. Abbassi et al.

|Table 4 (continued)|||
|---|---|---|
|References|SDM DDM|TDM Type of PV cells|
|[112]|✓✓|Poly-crystalline Si solar cell RTC France Poly-crystalline KC200GT Kyocera Multi-crystalline PW20500 Photo Watt|
|[113]|✓|Kyocera KC200GT RTC France Si Photowatt-PWP 201 solar module|
|[114]|✓|THERM Solar technik AT50, BP Solar MSX60, Kyocera KC65GT, BP Solar MSX120 Shell Solar SQ160PC, Kyocera KC200GT, Samsung LPC241SM, Trina Solar TSM245PC, and Hanwha Solar SF260|
|[115]|✓✓|RTC France silicon solar cell Polycrystalline silicon cells Photowatt-PWP201|
|[116]|✓✓|R.T.C France solar cell Photowatt-PWP201 PV module|
|[117]|✓✓|Polycrystalline solar panel Monocrystalline solar panel|

Table 5
 Datasheet information based approaches. Numerical Analytical Comments approaches approaches [31] [15] When we ignore the deviation and abrupt [39] [64] variations of measurements, mathematical/ [42] [67] analytical model can be considered as the [47] [85] more effective compared to the numerical [54] [86] solutions. For this reason, the analytical [55] [87] approaches are more used based on datasheet [66] [93] information’s, which confirms that this model [76] [104] is only used to adjust it with the data provided [108] [110] by manufacturers and then to find the
parameters to be determined.

Table 6

Measurement based approaches. Numerical Analytical Comments approaches approaches [31] [43] Based on experimental data, it has been [37] [62] proven that numerical methods are more [38] [63] effective for determining and identifying the [56] [104] parameters of solar panel. This is due [111] essentially to the research and minimization of the error between measured and extracted parameters, and that motivates those techniques compared to the analytical one.

*AE* =− || *ImeasuredIcalculated*(88) The Relative Error (RE) [13,16,37,54,55,68,69,71,73,76,80,84, 89,90]: <u>II</u> <u>measured− calculated</u> *RE* = *I* *measured* (89) The Mean Relative Error (MRE) [14,84]: 1 *N* *MRE* = ∑*REi* *N* *i*=1(90) The Coefficient of Determination (R²) [15,39,56,60,78,96]: *N* <u>∑i=1() IIpe−</u> *R* =− *N N* ∑*i*==(() *IIp*− *N* ∑*i e*) (91) The Mean Absolute Bias Error (MABE) [42]:

<u>∑i</u> *N* <u>=1</u>() <u>IIestiamed−target</u> 2 *MABE* = ∑ *N* () *II* −2 *i*=1 *estiamed mean* (92) The Mean Absolute Percentage Error (MAPE) [15,42,96]: *N* 1 <u>IIestiamed−target</u> *N* ∑ *i*=1 *I* *target* (93) *MAPE* =

The Individual Absolute Error (IAE) [55,68,71,73]: *eIAE* =− *It*()( ) *measuredIt calculated* (94) The Error between Simplified Parameters (ESP) A, B, C, D and E, which are given by [72]: *NI R* *A* = *pph sh* *RR* *ssh* + (95) *NIRps sh* *B* = *RR* *ssh* + (96) 1 *Cexp* = () *NnVst*(97) *R* *s* *D* = exp () *NnVpt* (98) <u>Np 1</u> *E* = *NR*+ *R* (99) *ss sh* The Absolute Current Error (ACE) [31,64]: *ACEcal*__ *LBER*=− *Ical LBERI* (100)

3.3. Some directions for future researches After reviewing, assessing and critically discussing more than 100 methods published over the past 7 years concerning the extraction of the main electric parameters of a solar cell, various issues need to be improved. The main points in concern are: ◆ Avoid the inaccuracy of the estimated parameters of the model by using more powerful tools in experimental measurements. In addi- tion, a large margin of variation of the meteorological data (irra- diance and temperature) must be taken into account during the measurement of the I-V characteristics. This helps particularly to better define the estimated parameters. ◆ Search for other effective strategies to handle the optimization problem of parameters extraction of PV cells while taking into ac- count a more reliable comparison procedure. ◆ A variety of Meta heuristic optimization algorithms have already been proposed to solve the problem of identifying solar cell

parameters, such as the genetic algorithm (GA), Particle swarm PSO optimization, differential evolution (DE), Evolutionary Algorithm (EA), Artificial Neural Network (ANN), Simplified Bird Mating Optimizer (SBMO), Fireworks Algorithm (FWA), Artificial Bee Colony (ABC), Moth-Flame Optimizer (MFO) algorithm, Harmony Search (Hs) based algorithms, Mutative-Scale Parallel Chaos Optimization Algorithm (MPCOA), Differential Evolution with Integrated Mutation (DEIM), Bee Pollinator Flower Pollination Algorithm (BPFPA), Free Search Differential Evolution (FSDE), Teaching Based Learning Optimization (TLBO) algorithm, Generalized Oppositional Teaching Based Learning Optimization (GOTLBO), Evaporation Rate Based Water Cycle Algorithm (ER- WCA). In high hopes of obtaining better results than those exhibited by existing parameter identification algorithms, it is strongly re- commended that the use of new algorithms or the combination of two or more algorithms together should be taken into account in future works. ◆ In the previous works treating Meta heuristic algorithms, each of them deals only with a single objective function by minimizing the error between the optimized parameters and those given experi- mentally. However, in none of the existing research, a multitude of objective functions have been compared to better choose the most appropriate parameters that describe the static characteristics of PV cells. ◆ In most existing works, the comparison of the error of fit has been made effectively. On the other hand, only a minority of the works were integrated the notion of execution time in their studies. For this, the CPU execution time and the convergence speed must be integrated with the other performance evaluation criteria. ◆ In cases where experimental data are used to extract solar cell parameters, many researchers have focused their works on a single axis in order to solve this type of problem. The comparison of a multitude of approaches that assemble analytical, numerical, and evolutionary-based algorithms in the same work seems to be un- avoidable given that this contributes significantly to increase the performance of the proposed method.

4. Implementation of SDM and DDM models
4.1. I-V and P-V characteristics From the solar cell manufacturer data sheet, we usually find five key values that are all given in the standard test condition. The parameters in question are the short circuit current Isc, the open circuit voltage V0c, the maximum power Pm, the temperature coefficient of the short circuit current α and the open circuit voltage β. In order to simulate a PV cell, it is crucial to first choose a suitable model that describes the equivalent electrical circuit of the latter. By selecting this model, the parameters describing the electrical circuit must be determined. Based on the manufacturer's data sheet or experimental data, the problem of finding the different solar cell model parameters is carried out as part of searching, identifying or optimizing the parameters de- scribing the electric circuit model. The objective is to calculate these different parameters with a minimum error and a high accuracy. This is why this type of problem has strongly attracted the researcher’s at- tention last years. To overcome this problem, a multitude of approaches have been proposed in the literature. These approaches can be classified into three main pillars. The first pillar is based on solving the problem by analy- tical methods, all of which are based on mathematical manipulations. The second one translates methodologies based on numerical ap- proaches in the form of random algorithms. In this case, the analysis of the parameters obtained is made by a predefined tolerance, of which it describes the difference between the simulated parameters and those given by the manufacturers or experimentally. In addition, the third

|pillar|is metaheuristic|of the|talline).|
|---|---|---|---|
|||470||
 pillar is metaheuristic methodologies whose reformulation of the
Table 7

key Specifications of different technologies of the used PV modules. Characteristics Multi-crystalline Mono-crystalline Thin-Film BP SX 150S STP270S CHSM 5011T I sc(A) 4.75 9.28 1.020 V 0c(V) 43.5 38.3 164 P m(W) 150 270 100 I m(A) 4.35 8.77 0.88 V m(V) 34.5 30.8 113.6 Α (0.065 +−0.015)%/°C 0.060%/°C 0.05%/C Β Γ (−−0.5 + 160 +−−0.05%/°C 20)mV/°C − −0.34%/°C 0.41%/°C − −0.31%/C 0.27%/C

problem is declared in the form of an optimization algorithm which is based on the minimization of an objective function based on an error. In this review article, the most important simulations to show the difference between the extracted parameters for the SDM and the DDM models have been performed. The three different types of technologies including multi-crystalline, mono-crystalline and the thin-film have been investigated. The Table 7 depicts the key specifications of the different technologies of PV modules namely the Multi-crystalline BP SX 150S, Mono-crystalline STP270S and Thin-Film CHSM 5011T. The current-voltage, power-voltage characteristics of the multi- crystalline BP SX 150S, mono-crystalline STP270S and thin-film CHSM 5011T models for different solar irradiance levels are respectively shown in Fig. 3, Fig. 4 and Fig. 5. The comparison of the I-V and P-V curves derived from calculated parameters with those originate from the manufacturer for three in- dustrial samples was performed for the SDM and DDM models using MATLAB environment. The parameters of the different models were estimated by fitting the calculated curve of the I-V and P-V character- istics to the measured I-V and P-V characteristics with an acceptable error. The calculated I-V and P-V curves of both two models for the Multi-crystalline technology are depicted by Fig. 3 illustrating the good match obtained between the two characteristics. For this technology, the variation of the solar irradiation has no influence on the char- acteristics obtained, except for irradiances less than 600 W/m² and exactly when the operating point is close to the maximum power point (MPP). In this case, the curves describing the P-V characteristics of the SDM and DDM models are not really confounded and this implies a variation around 7%. The calculated and measured I-V and P-V curves for Mono-crystal- line and Thin-film technologies for different levels of irradiance are shown in Fig. 4 and Fig. 5, respectively. For Mono-crystalline tech- nology, the variation in solar irradiation has no influence. The I-V characteristics obtained and the three fundamentals points (Isc,V0cand P

m) are still within a reasonable margin for irradiance ranging from
180 5 150 4 120 3 90 2 60 1 30

Fig. 3. I-V and P-V characteristics for different irradiation levels (Multi-crys-

talline).

R. Abbassi et al.
250 8 200 6 150 4 100 2 50

00 55 10 10 15 15 20 20 25 25 30 30 35 35 40 40

Fig. 4. I-V and P-V characteristics for different irradiation levels (Mono-crys-

talline).

|1.2||
|---|---|
||120|
|1||
||100|
|0.8||
||80|
|0.6||
||60|
|0.4||
||40|
|0.2||
||20|
||0|
|0 20 40 60 80 100 120 140 160||

Fig. 5. I-V and P-V characteristics for different irradiation levels (Thin-film).

200 W/m² to 1000 W/m². In this case, the curves describing the P-V characteristics of the SDM and DDM models are not according and the error does not exceed 3%. Regarding Thin-film technology, the I-V and P-V curves for the two studied models can seriously describe the static characteristics of the solar panel, for irradiations of 600 W/m², 800 W/m² and 1000 W/m². On the other hand, the difference between these two models is found in the case of irradiation levels of 200 W/m² and 400 W/m², where the current and the voltage of the maximum power point of the SDM are 5% greater than those obtained by the DDM. Besides, the same margin is almost recorded at the open circuit voltage level.

4.2. Parameters identification of PV panel The first interesting result discussed in the Section 4.1 regards the characteristics of SDM and DDM solar cells for the three famous tech- nologies. The Figs. 3, 4 and 5 show that it seems to be a critical for determining the five parameters of the equivalent electrical circuit of a SDM and the seven parameters of the DDM model. The various domi- nant extracted parameters are presented in Tables 8, 9. For the Multi-crystalline technology, for irradiance from 1000 W/ m² to 200 W/m², the shunt resistance varies from 121 Ω to 606 Ω for the SDM model and 253 Ω to 606 Ω for the DDM model. Even if the series resistance remains at a value close to 0.12 Ω for the SDM model, it varies between 0.8 Ω and 1.06 Ω for the DDM model. For both studied models, the photo-current varies from 4.75 A for an irradiation of 1000 W/m² up to 0.95 A for an irradiation of 200 W/m². Thin-Film technology is characterized by a fairly large value of shunt resistance compared to the other two technologies. In this case, the shunt
Table 8

Parameters identification of the SDM for different technologies of PV modules. Parameters Multi-crystalline BP SX 150S Mono-crystalline STP270S CHSM 5011T Thin-Film 2 1000 W/m ,25°C R sh121.29 121.3 849.037 Rs 0.12 0.121 0.606 A 2.33 1.81 1.223 I0 3.44e-8 5.84e-9 8.93e-8 Isc 4.750 9.28 1.02 V0c 43.5 38.3 164 Im 4.35 8.77 0.88 Vm 36.5 33.50 128.3 Iph 4.754 9.289 1.0207 800 W/m²,25°C R sh151.61 151.613 1061.296 Rs 0.121 0.121 0.606 A 2.33 1.811 1.223 I0 3.445e-8 5.84e-9 8.93e-8 Isc 3.80 7.424 0.816 V0c 42.98 37.895 161.72 Im 3.48 7.016 0.704 Vm 36.5 33.50 128.3 Iph 3.80 7.431 0.816 600 W/m²,25°C R sh202.15 202.152 1415.061 Rs 0.121 0.121 0.6064 A 2.33 1.811 1.223 I0 3.445e-8 5.84e-9 8.93e-8 Isc 2.85 5.568 0.612 V0c 42.31 37.375 158.77 Im 2.61 5.262 0.528 Vm 36.5 33.50 128.3 Iph 2.853 5.573 0.612 400W/m²,25°C R sh303.23 303.227 2122.59 Rs 0.121 0.121 0.6064 A 2.33 1.811 1.223 I0 3.445e-8 5.84e-9 8.93e-8 Isc V0c

1.9
41.36
3.712
36.641
0.408
154.63
Im 1.74 3.51 0.352 Vm 36.5 33.50 128.3 Iph 200 W/m²,25°C

1.90 3.72 0.408
R sh606.45 606.46 4245.18 Rs 0.121 0.122 0.6064 A 2.33 1.811 1.223 I0 3.44e-8 5.84e-9 8.93e-8 Isc V0c

0.95
39.75
1.856
35.385
0.204
147.546
Im 0.87 1.754 0.176 Vm 36.5 33.50 128.3 Iph 0.951 1.857 0.204

resistance can reach a value of 4000 Ω for an irradiance of 200 W/m² against 600 Ω for the SDM model and 1150 Ω for the DDM model of Mono-crystalline technology. The Tables 8, 9 allow highlighting that the error of the values of the five and seven parameters of the SDM and DDM models, respectively, was relatively small around the points of the short circuit current and the open circuit voltage in all cases. The recapitulation of this work proves that whatever used model is nearly appropriate to describe the behavior of the PV modules. The current-voltage and power-voltage curves of the SDM and DDM models are approximately the same for the different levels of solar irradiance. Each model has its strong and weak points. That’s why, by playing on the accuracy, the fastness (simulation time) and farther away than that on the model complexity to choose the most suitable model. After comparison between the two different models, the obtained results indicate the durability, the accuracy and the satisfactory per- formance of these models to describe the real characteristics of solar panel.

R. Abbassi et al.
Table 9
 <u>Parameters identification of the DDM for different technologies of PV modules.</u> Parameters Multi-crystalline Mono-crystalline STP270S Thin-Film

|Parameters|Multi-crystalline|Mono-crystalline STP270S|Thin-Film|
|---|---|---|---|
|1000 W/m ,25°C|BP SX 150S||CHSM 5011T|
|R|253.58|925.45|1227.88|
|Rs|0.81|0.331|0.853|
|a1|1|1|1|
|a2|1.25|1.25|1.25|
|I01, I02|2.912e-10|1.504e-10|9.192e-10|
|Isc|4.734|9.276|0.977|
|V0c|43.4|38.2|163.8|
|Im|4.35|8.77|0.87|
|Vm|36.5|33.50|128.01|
|Iph 800 W/m²,25°C|4.75|9.28|1.02|
|R|260|970.32|1361.296|
|Rs|0.89|0.36|0.85|
|a1|1|11||
|a2|1.25|1.25|1.25|
|I01, I02|2.912e-10|1.504e-10|9.192e-10|
|Isc|3.878|7.583|0.836|
|V0c|42.95|38|161.3|
|Im|3.48|7.2|0.704|
|Vm|36.5|33.50|128.013|
|Iph 600 W/m²,25°C|3.80|7.424|0.816|
|R|202.15|990.010|1415.061|
|Rs|0.951|0.39|0.87|
|a1|1|11||
|a2|1.25|1.25|1.25|
|I01, I02|2.912e-10|1.504e-10|9.192e-10|
|Isc|2.99|5.836|0.604|
|V0c|42.31|37.15|158.77|
|Im|2.61|5.29|0.528|
|Vm|36.5|33.50|128.01|
|Iph 400 W/m²,25°C|2.85|5.568|0.612|
|R|303.23|1013|2122.59|
|Rs|1.01|0.41|0.8|
|a1|1|11||
|a2|1.25|1.25|1.25|
|I01, I02|2.912e-10|1.504e-10|9.192e-10|
|Isc|2.059|4,01|0.405|
|V0c|41.36|36.8|154.63|
|Im|1.74|3.59|0.352|
|Vm|36.5|33.50|128.01|
|Iph 200 W/m²,25°C|1.9|3.712|0.408|
|R|606.45|1150.41|4245.18|
|Rs|1.06|0.43|0.81|
|a1|1|11||
|a2|1.25|1.25|1.25|
|I01,I02|2.912e-10|1.504e-10|9.192e-10|
|Isc|1.071|2.078|0.2|
|V0c|39.78|35.20|148.9|
|Im|0.92|1.69|0.176|
|Vm|36.5|33.50|128.01|
|Iph|0.95|1.856|0.204|
 2 sh sh sh sh sh
5. Conclusions Nowadays, solar cell model parameters extraction is considered among the most attractive research topics, which largely discusses the successful exploitation of solar potential and probably renewable en- ergy. This review article critically outlines, discusses and classifies, according to three different pillars, the main issues of the variety of published research methods on the identification of cell/panel/PV module parameters. Based on this in-depth analysis, some directions for future works have been provided to better benefit from the huge growth expected in PV systems. Indeed, although a great deal of work and ef- fort has been done by the researchers, there is still a chance to improve some trials. Thus, the parameters that make up the equivalent electric circuit of the solar cell of which they describe the current-voltage
characteristic have been restored. In this review, five and nine para- meters describing respectively the SDM and the TDM were identified. The tests of these two models were made based on three different technologies that included Mono-crystalline, Multi-crystalline and Thin-Film. The authors strongly believe that this paper provides re- searchers, engineers and investors in the related field with an overview of the different solar cell parameters extraction methods; which would be very useful for the future. References [1] Geng Y, Chen W, Liu Z, Chiu ASF, Han W, Liu Z, Zhong S, Qian Y, You W, Cui X. A bibliometric review: energy consumption and greenhouse gas emissions in the residential sector. J Clean Prod 2017;159:301–16. [2] Streimikiene D, Girdzijauskas S. Assessment of post-Kyoto climate change miti- gation regimes impact on sustainable development. Renew Sustain Energy Rev 2009;77:129–41. [3] Lau LC, Lee KT, Mohamed AR. Global warming mitigation and renewable energy policy development from the Kyoto Protocol to the Copenhagen Accord—A com- ment. Renew Sustain Energy Rev 2012;16:5280–4. [4] Jha SK, Bilalovic J, Jha A, Patel N, Zhang H. Renewable energy: present research and future scope of Artificial Intelligence. Renew Sustain Energy Rev 2017;77:297–317. [5] Abbassi R, Chebbi S. energy management strategy for a grid–connected wind-solar hybrid system with battery storage: policy for optimizing conventional energy generation. Int Rev Electr Eng 2012;7:3979–90. [6] Abbassi A, Dami MA, Jemli M. A statistical approach for hybrid energy storage system sizing based on capacity distributions in an autonomous PV/Wind power generation system. Renew Energy 2017;103:81–93. [7] Xu J, Li L, Zheng B. Wind energy generation technological paradigm diffusion. Renew Sustain Energy Rev 2016;59:436–49. [8] Baghdadi F, Mohammedi K, Diaf S, Behar O. Feasibility study and energy con- version analysis of stand-alone hybrid renewable energy system. Energy Convers Manag 2015;105:471–9. [9] Mcelroy MB, Chen X. Wind and Solar Power in the United States: status and Prospects. CSEE J Power Energy Syst 2017;3:1–6. [10] Tsikalakis A, Tomtsi T, Hatziargyriou ND, Poullikkas A, Yasin A. Review of best practices of solar electricity resources applications in selected Middle East and North Africa (MENA) countries. Renew Sustain Energy Rev 2016;15:2838–49. [11] Jordehi AR. Maximum power point tracking in photovoltaic (PV) systems: a review of different approaches. Renew Sustain Energy Rev 2016;65:1127–38. [12] photovoltaic systems: going beyond the performance ratio. Sol Energy Herteleer B, Huyck B, Catthoor F, Driesen J, Cappelle J. Normalized efficiency of 2017;157:408–18. [13] Ishaque K, Salam Z, Taheri H, Shamsudin A. A critical evaluation of EA compu- tational methods for Photovoltaic cell parameter extraction based on two diode model. Sol Energy 2011;85:1768–79. [14] Macabebe EQB, Sheppard CJ, Ernest, van Dyk E. Parameter extraction from I–V characteristics of PV devices. Sol Energy 2011;85:12–8. [15] Humada AM, Hojabri M, Mekhilef S, Hamada HM. Solar cell parameters extraction based on single and double-diode models: a review. Renew Sustain Energy Rev 2016;56:494–509. [16] Gomes RCM, Vitorino MA, Corrêa MBR, Fernandes DA, Wang R. Shuffled complex evolution on photovoltaic parameter extraction: a comparative analysis. IEEE Trans Sustain Energy 2017;8(2):805–15. [17] Tamrakar1 R, Gupta A. A review: extraction of solar cell modeling parameter. Int J [18] Innov Res Electr Electron Inst Control Eng 2015;3:1. Jordehi AR. Parameter estimation of solar photovoltaic (PV) cells: a review. Renew Sustain Energy Rev 2016;61:354–71. [19] Ishaque K, Salam Z, Mekhilef S, Shamsudin A. Parameter extraction of solar photovoltaic modules using penalty-based differential evolution. Appl Energy 2012;99:297–308. [20] Chin VJ, Salam Z, Ishaque K. Cell modelling and model parameters estimation techniques for photovoltaic simulator application: a review. Appl Energy 2015;154:500–19. [21] Liu CC, Chen CY, Weng CY, Wang CC, Jenq FL, Cheng PJ, Wang YH, Houng MP. Physical parameters extraction from current–voltage characteristic for diodes [22] using multiple nonlinear regression analysis. Solid-State Elect 2008;52:839 Lim LHI, Ye Z, Ye J, Yang D, Du H. A linear method to extract diode model –43. parameters of solar panels from a single I-V curve. Renew Energy 2015;76:135–42. [23] Derick M, Rani C, Rajesh M, Farrag ME, Wang Y, Busawon K. An improved opti- mization technique for estimation of solar photovoltaic parameters. Sol Energy 2017;157:116–24. [24] Zhou W, Yang H, Fang Z. A novel model for photovoltaic array performance prediction. Appl Energy 2007;84(12):1187–98. [25] Kassis A, Saad M. Analysis of multi-crystalline silicon solar cells at low illumina- 2010;94(12):2108 tion levels using a modi –12. fied two-diode model. Sol Energy Mat Sol Cells [26] Khanna V, Das BK, Bisht D, Vandana, Singh PK. A three diode model for industrial solar cells and estimation of solar cell parameters using PSO algorithm. Renew [27] Ishaque K, Salam Z, Taheri H. Simple, fast and accurate two-diode model for Energy 2015;78:105–13.

R. Abbassi et al. photovoltaic modules. Sol Energy Mat Sol Cells 2011;95(2):586–94. [28] Qun N, Letian Z, Kang L. A biogeography-based optimization algorithm with mutation strategies for model parameter estimation of solar and fuel cells. Energy Convers Manag 2014;86:1173–85. [29] Gong W, Cai Z. Parameter extraction of solar cell models using repaired adaptive differential evolution. Sol Energy 2013;94:209–20. [30] Nassar-eddine I, Obbadi A, Errami Y, El fajri A, Agunaou M. Parameter estimation of photovoltaic modules using iterative method and the Lambert W function: a comparative study. Energy Convers Manag 2016;119:37–48. [31] Gao X, Cui Y, Hu J, Xu G, Yu Y. Lambert W-function based exact representation for double diode model of solar cells: comparison on fitness and parameter extraction. Energy Convers Manag 2016;127:443–60. [32] Sandrolini L, Artioli M, Reggiani U. Numerical method for the extraction of pho- tovoltaic module double-diode model parameters through cluster analysis. Appl Energy 2010;87:442–51. [33] Muhsen DH, Ghazali AB, Khatib T, Abed IA. Parameters extraction of double diode photovoltaic module’s model based on hybrid evolutionary algorithm. Energy Convers Manag 2015;105:552–61. [34] Et-torabi K, Nassar-eddine I, Obbadi A, Errami Y, Rmaily R, Sahnoun S, El fajri A, Agunaou M. Parameters estimation of the single and double diode photovoltaic models using a Gauss–Seidel algorithm and analytical method: a comparative study. Energy Convers Manag 2017;148:1041–54. [35] Bana S, Saini RP. A mathematical modeling framework to evaluate the perfor- mance of single and double diode based SPV systems. Energy Rep 2016;2:171–87. [36] Barth N, Jovanovic R, Ahzi S, Khaleel MA. PV panel single and double diode model: optimization of the parameters and temperature dependence. Sol Energy Mater Sol Cells 2016;148:87–98. [37] Hejri M, Mokhtari H, Azizian MR, Ghandhari M, Soder L. On the Parameter ex- traction of a five-parameter double-diode model of photovoltaic cells and modules. IEEE J Photovolt 2014;4(3):915–23. [38] Ma T, Yang H, Lu L. Development of a model to simulate the performance char- acteristics of crystalline silicon photovoltaic modules/strings/arrays. Sol Energy 2014;100:31–41. [39] Mares O, Paulescu M, Badescu V. A simple but accurate procedure for solving the five-parameter model. Energy Convers Manag 2015;105:139–48. [40] Mahmoud Y, Xiao W, Zeineldin HH. A simple approach to modeling and simula- tion of photovoltaic modules. IEEE Trans Sustain Energy 2012;3(1):185–6. [41] Zhang Y, Gao S, Gu T. Prediction of I-V characteristics for a PV panel by combining single diode model and explicit analytical model. Sol Energy 2017;144:349–55. [42] Ayodele TR, Ogunjuyigbe ASO, Ekoh EE. Evaluation of numerical algorithms used in extracting the parameters of a single-diode photovoltaic model. Sustain Energy Technol Assess 2016;13:51–9. [43] Toledo FJ, Blanes JM. Analytical and quasi-explicit four arbitrary point method for extraction of solar cell single-diode model parameters. Renew Energy 2016;92:346–56. [44] Pindado S, Cubas J. Simple mathematical approach to solar cell/panel behavior based on datasheet information. Renew Energy 2017;103:729–38. [45] Cubas J, Pindado S, Victoria M. On the analytical approach for modeling photo- voltaic systems behavior. J Power Sources 2014;247:467–74. [46] Lineykin S, Averbukh M, Kuperman A. An improved approach to extract the single- diode equivalent circuit parameters of a photovoltaic cell/panel. Renew Sustain Energy Rev 2014;30:282–9. [47] Peng L, Sun Y, Meng Z. An improved model and parameters extraction for pho- tovoltaic cells using only three state points at standard test condition. J Power Sources 2014;248:621–31. [48] Lun S, Wang S, Yang G, Guo T. A new explicit double-diode modeling method based on Lambert W-function for photovoltaic arrays. Sol Energy 2015;116:69–82. [49] Wang G, Zhao K, Shi J, Chen W, Zhang H, Yang X, Zhao Y. An iterative approach for modeling photovoltaic modules without implicit equations. Appl Energy 2017;202:189–98. [50] Singh KJ, Kho KLR, Singh SJ. Artificial neural network approach for more accurate solar cell electrical circuit model. Int J Comp Sci Appl (IJCSA) 2014;4:3. [51] Ishaque K, Salam Z. An improved modeling method to determine the model parameters of photovoltaic (PV) modules using differential evolution (DE). Sol Energy 2011;85:2349–59. [52] Siddiqui MU, Abido M. Parameter estimation for five- and seven-parameter pho- tovoltaic electrical models using evolutionary algorithms. Appl Soft Comp 2013;13:4608–21. [53] Askarzadeh A, Coelho LS. Determination of photovoltaic modules parameters at different operating conditions using a novel bird mating optimizer approach. Energy Convers Manag 2015;89:608–14. [54] Ishaque K, Salam Z. Syafaruddin. A comprehensive MATLAB Simulink PV system simulator with partial shading capability based on two-diode model. Sol Energy 2011;85:2217–27. [55] Babu TS, Ram JP, Sangeetha K, Laudani A, Rajasekar N. Parameter extraction of two diode solar PV model using Fireworks algorithm. Sol Energy 2016;140:265–76. [56] Muhsen DH, Ghazali AB, Khatib T, Abed IA. A comparative study of evolutionary algorithms and adapting control parameters for estimating the parameters of a single-diode photovoltaic module's model. Renew Energy 2016;96:377–89. [57] Bühler AJ, Krenzinger A. Method for photovoltaic parameter extraction according to a modified double-diode model. Prog Photovolt: Res Appl 2013;21:884–93. [58] Khanna V, Das BK, Bisht D, Vandana, Singh PK. A three diode model for industrial solar cells and estimation of solar cell parameters using PSO algorithm. Renew Energy 2015;78:105–13. [59] Steingrube S, Breitenstein O, Ramspeck K, Glunz S, Schenk A, Altermatt PP.
Explanation of commonly observed shunt currents in c-Si solar cells by means of recombination statistics beyond the Shockley-Read-Hall approximation. J Appl Phys 2011;110:1. [60] Allam D, Yousri DA, Eteiba MB. Parameters extraction of the three diode model for the multi-crystalline solar cell/module using Moth-Flame Optimization Algorithm. Energy Convers Manag 2016;123:535–48. [61] Kichou S, Silvestre S, Guglielminotti L, Mora-Lopez L, Munoz-Ceron E. Comparison of two PV array models for the simulation of PV systems using five different al- gorithms for the parameters identification. Renew Energy 2016;99:270–9. [62] Ruschel CS, Gasparin FP, Costa ER, Krenzinger A. Assessment of PV modules shunt resistance dependence on solar irradiance. Sol Energy 2016;133:35–43. [63] Brano VL, Orioli A, Ciulla G. On the experimental validation of an improved five- parameter model for silicon photovoltaic modules. Sol Energy Mater Sol Cells 2012;105:27–39. [64] Tong NT, Pora W. A parameter extraction technique exploiting intrinsic properties of solar cells. Appl Energy 2016;176:104–15. [65] Khanna V, Das BK, Vandana, Singh PK, Sharma P, Jain SK. Statistical analysis and engineering fit models for two-diode model parameters of large area silicon solar cells. Sol Energy 2016;136:401–11. [66] Bonkoungou D, Koalaga Z, Njomo D, Zougmore F. An improved Numerical ap- proach for photovoltaic module parameters acquisition based on single-diode model. Int J Curr Eng Technol 2015;5(6):3735–42. [67] Dongue SB, Njomo D, Ebengai L. An improved nonlinear five-point model for photovoltaic Modules. Hindawi Publishing Corporation. Int J Photoenergy 2013:680213. [68] Chellaswamy C, Ramesh R. Parameter extraction of solar cell models based on adaptive differential evolution algorithm. Renew Energy 2016;97:823–37. [69] Askarzadeh A, Rezazadeh A. Parameter identification for solar cell models using harmony search-based algorithms. Sol Energy 2012;86:3241–9. [70] Ma J, Bi Z, Ting TO, Hao S, Hao W. Comparative performance on photovoltaic model parameter identification via bio-inspired algorithms. Sol Energy 2016;132:606–16. [71] Yuan X, Xiang Y, He Y. Parameter extraction of solar cell models using mutative- scale parallel chaos optimization algorithm. Sol Energy 2014;108:238–51. [72] Toledo FJ, Blanes JM. Geometric properties of the single-diode photovoltaic model and a new very simple method for parameters extraction. Renew Energy 2014;72:125–33. [73] Ram JP, Babu TS, Dragicevic T, Rajasekar N. A new hybrid bee pollinator flower pollination algorithm for solar PV parameter estimation. Energy Convers Manag 2017;135:463–76. [74] Ayala HVH, Coelho LS, Mariani VC, Askarzadeh A. An improved free search dif- ferential evolution algorithm: a case study on parameters identification of one diode equivalent circuit of a solar cell module. Energy 2015;93:1515–22. [75] Bana S, Saini RP. Identification of unknown parameters of a single diode photo- voltaic model using particle swarm optimization with binary constraints. Renew Energy 2017;101:1299–310. [76] Bai J, Liu S, Hao Y, Zhang Z, Jiang M, Zhang Y. Development of a new compound method to extract the five parameters of PV modules. Energy Convers Manag 2014;79:294–303. [77] Lin P, Cheng S, Yeh W, Chen Z, Wu L. Parameters extraction of solar cell models using a modified simplified swarm optimization algorithm. Sol Energy 2017;144:594–603. [78] Muhsen DH, Ghazali AB, Khatib T, Abed IA. Extraction of photovoltaic module model’s parameters using an improved hybrid differential evolution/electro- magnetism-like algorithm. Sol Energy 2015;119:286–97. [79] Fathy A, Rezk H. Parameter estimation of photovoltaic system using imperialist competitive algorithm. Renew Energy 2017;111:307–20. [80] Patel SJ, Panchal AK, Kheraj V. Extraction of solar cell parameters from a single current–voltage characteristic using teaching learning based optimization algo- rithm. Appl Energy 2014;119:384–93. [81] Awadallah MA. Variations of the bacterial foraging algorithm for the extraction of PV module parameters from nameplate data. Energy Convers Manag 2016;113:312–20. [82] Park JY, Choi SJ. A novel simulation model for PV panels based on datasheet parameter tuning. Sol Energy 2017;145:90–8. [83] Chen X, Yu K, Du W, Zhao W, Liu G. Parameters identification of solar cell models using generalized oppositional teaching learning based optimization. Energy 2016;99:170–80. [84] Kler D, Sharma P, Banerjee A, Rana KPS, Kumar V. PV cell and module efficient parameters estimation using Evaporation Rate based Water Cycle Algorithm. Swarm Evol Comput 2017;35:93–110. [85] Deihimi MH, Naghizadeh RA, Meyabadi AF. Systematic derivation of parameters of one exponential model for photovoltaic modules using numerical information of data sheet. Renew Energy 2016;87:676–85. [86] Laudani A, Lozito GM, Mancilla-David F, Riganti-Fulginei F, Salvini A. An im- proved method for SRC parameter estimation for the CEC PV module model. Sol Energy 2015;120:525–35. [87] Batzelis EI, Papathanassiou SA. A method for the analytical extraction of the single-diode PV model parameters. IEEE Trans Sustain Energy 2016;7(2):504–12. [88] Cardenas AA, Carrasco M, Mancilla-David F, Street A, Cardenas R. Experimental parameter extraction in the single-diode photovoltaic model via a reduced-space search. IEEE Trans Ind Electron 2017;64(2):1468–76. [89] Cervellini MP, Echeverría NI, Antoszczuk PD, Retegui RAG, Funes MA, González SA. Optimized parameter extraction method for photovoltaic devices model. IEEE Lat Am Trans 2016;14(4):1959–65. [90] Bharadwaj P, Chaudhury KN, John V. Sequential optimization for PV panel

R. Abbassi et al. parameter estimation. IEEE J Photovolt 2016;6(5):1261–8. [91] Awadallah MA, Venkatesh B. Bacterial foraging algorithm guided by particle swarm optimization for parameter identification of photovoltaic modules. Can J Electr Comp Eng 2016;39(2):150–7. [92] Moshksar E, Ghanbari T. Adaptive estimation approach for parameter identifica- tion of photovoltaic modules. IEEE J Photovolt 2017;7(2):614–23. [93] Silva EA, Bradaschia F, Cavalcanti MC, Nascimento AJ. Parameter estimation method to improve the accuracy of photovoltaic electrical model. IEEE J Photovolt 2016;6(1):278–85. [94] Abbassi A, Gammoudi R, Dami MA, Hasnaoui O, Jemli M. An improved single- diode model parameters extraction at different operating conditions with a view to modeling a photovoltaic generator: a comparative study. Sol Energy 2017;155:478–89. [95] Lun S, Wang S, Guo T, Du C. An I–V model based on time warp invariant echo state network for photovoltaic array with shaded solar cells. Sol Energy 2014;105:529–41. [96] Karamirad M, Omid M, Alimardani R, Mousazadeh H, Heidari SN. ANN based simulation and experimental verification of analytical four- and five-parameters models of PV modules. Simul Model Pract Theory 2013;34:86–98. [97] Castro FD, Laudani A, Fulginei FR, Salvini A. An in-depth analysis of the modelling of organic solar cells using multiple-diode circuits. Sol Energy 2016;135:590–7. [98] De Blas MA, Torres JL, Prieto E, Garcia A. Selecting a suitable model for char- acterizing photovoltaic devices. Renew Energy 2002;25:371–80. [99] Villalva MG, Gazoli JR, Ruppert EF. Comprehensive approach to modeling and simulation of photovoltaic arrays. IEEE Trans Power Electron 2009;24(5):1198–208. [100] Xiao W, Dunford WG, Capel A. A novel modeling method for photovoltaic cells. In Proceedings IEEE Power Electron Spec Conference; 2004. p. 1950–1956. [101] Nayak BK, Mohapatra A, Mohanty KB. Parameters estimation of photovoltaic module using nonlinear least square algorithm: A comparative study. In Proceedings Annu IEEE India Conference; 2013. p. 1–6. [102] Mahmoud YK, Xiao W, Zeineldin HH. A parameterization approach for enhancing PV model accuracy. IEEE Trans Ind Electron 2013;60(12):5708–16. [103] Accarino J, Petrone G, Ramos-Paja CA, Spagnuolo G. Symbolic algebra for the calculation of the series and parallel resistances in PV module model. In Proceedings International Conference Clean Electr Power; 2013. p. 62–66. [104] Laudani A, Fulginei FR, Salvini A. Identification of the one-diode model for
photovoltaic modules from datasheet values. Sol Energy 2014;108:432–46. [105] Rhouma MBH, Gastli A, Ben Brahim L, Touati F, Ben Ammar M. A simple method for extracting the parameters of the PV cell single-diode model. Renew Energy 2017;113:885–94. [106] Esram T. Modelling and control of an alternating-current photovoltaic module. in: Illinois; 2010. [107] Vika HB. Modelling of photovoltaic modules with battery energy storage in Simulink/Matlab. Trodehim: Norwegian University of Science and Technology;

2014.
[108] Elbaset AA, Ali H, Abdelsattar M. New seven parameters model for amorphous silicon and thin film PV modules based on solar irradiance. Sol Energy 2016;138:26–35. [109] Jiang LL, Maskell DL, Patra JC. Parameter estimation of solar cells and mod- ulesusing an improved adaptive differential evolution algorithm. Appl Energy 2013;112:185–93. [110] Brano VL, Ciulla G. An efficient analytical approach for obtaining a five para- meters model of photovoltaic modules using only reference data. Appl Energy 2013;111:894–903. [111] Laudani A, Fulginei FR, Salvini A. High performing extraction procedure for the one-diode model of a photovoltaic panel from experimental I–V curves by using reduced forms. Sol Energy 2014;103:316–26. [112] El-Fergany A. Efficient tool to characterize photovoltaic generating systems using mine blast algorithm. Electr Power Compon Syst 2015;43:890–901. [113] Ali EE, El-Hameed MA, El-Fergany AA, El-Arini MM. Parameter extraction of photovoltaic generating units using multi-verse optimizer. Sustain Energy Technol Assess 2016;17:68–76. [114] Park J-Y, Choi S-J. A novel datasheet-based parameter extraction method for a single-diode photovoltaic array model. Sol Energy 2015;122:1235–44. [115] Yu K, Liang JJ, Qu BY, Chen X, Wang H. Parameters identification of photovoltaic models using an improved JAYA optimization algorithm. Energy Convers Manag 2017;150:742–53. [116] Chen Z, Wu L, Lin P, Wu Y, Cheng S. Parameters identification of photovoltaic models using hybrid adaptive Nelder-Mead simplex algorithm based on eagle strategy. Appl Energy 2016;182:47–57. [117] Oliva D, Mohamed AEA, Hassanien AE. Parameter estimation of photovoltaic cells using an improved chaotic whale optimization algorithm. Appl Energy 2017;200:141–54.
