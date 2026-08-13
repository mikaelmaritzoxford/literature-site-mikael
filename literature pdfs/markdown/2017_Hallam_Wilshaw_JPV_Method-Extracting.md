IEEE JOURNAL OF PHOTOVOLTAICS, VOL. 7, NO. 5, SEPTEMBER 2017

## Method of Extracting Solar Cell Parameters From Derivatives of Dark I–V Curves

Brett J. Hallam, Phill G. Hamer, Ruy S. Bonilla, Stuart R. Wenham, and Peter R. Wilshaw

***Abstract*—A method is presented to extract solar cell parameters from the derivatives of dark current–voltage curves with a three-**

**diode model, using the monotonic properties of the current–voltage characteristic associated with each diode or resistive current. The**

**method yields an improved accuracy of the solar cell parame- ters when compared with that used on the actual current–voltage**

**curves. Despite the complexity of the three-diode model with seven** **fit parameters, a good accuracy can be reached using the proposed method with a relatively small computational effort. A hypothetical**

**case is presented using various approaches to obtain the solar cell** **parameters, with a root-mean-square error for the logarithm of the current–voltage curve (RMSlog10*I*)of4*×*10** ***−*3** **. An example fitting is then demonstrated on a multicrystalline passivated emitter rear**

**contact solar cell, yielding RMSlog10*I*= 1*.*45 *×*10** ***−*1** **.**

***Index Terms*—Characterization of photovoltaic (PV), curve fit- ting, PV cells.**

I. INTRODUCTION
ECOMBINATION in silicon solar cells significantly af-

# Rfects performance. As solar cell manufacturers push to

develop more efficient devices, significant efforts are placed around understanding recombination mechanisms in devices and, importantly, how they can be eliminated. For example, in re- cent years, several key developments have been used to improve the efficiencies of solar cells. For p-type solar cells, the devel- opment of new and improved silver pastes has allowed a shift to more lightly doped emitters. This has resulted in a decrease in Auger-related emitter recombination components and an im- provement in the blue response, while enabling a low-resistance ohmic contact and effective shielding of minority carriers from the metal/silicon interface [1]. Another key development is the transition to the passivated emitter and rear locally contacted

Manuscript received May 19, 2017; revised June 30, 2017; accepted July 18, 2017. Date of publication August 2, 2017; date of current version August 18, 2017. This work was supported in part by the Australian Government through the Australian Renewable Energy Agency and the Australian Cen- tre for Advanced Photovoltaics, and in part by the U.K. Government through the International and Industrial Engagement Fund and the Supersilicon project (EP/M024911/1), supported by the Engineering and Physical Sciences Research Council. *(Corresponding author: Brett J. Hallam.)*

B. J. Hallam and S. R. Wenham are with the School of Photovoltaic and
Renewable Energy Engineering, University of New South Wales, Kensing- ton, NSW 2052, Australia (e-mail: brett.hallam@unsw.edu.au; s.wenham@ unsw.edu.au).

P. G. Hamer, R. S. Bonilla, and P. R. Wilshaw are with the De-
partment of Materials, University of Oxford, Oxford OX1 2JD, U.K. (e-mail: phillip.hamer@materials.ox.ac.uk; sebastian.bonilla@materials.ox.ac. uk; peter.wilshaw@materials.ox.ac.uk). Color versions of one or more of the figures in this paper are available online at [http://ieeexplore.ieee.org](http://ieeexplore.ieee.org). Digital Object Identifier 10.1109/JPHOTOV.2017.2731778

(PERC) solar cell [2], [3], by passivating the rear surface of the solar cell and using localized rear contacts rather than a full-area aluminum back-surface field. This reduced contact fraction has the benefit of improving rear surface passivation and, therefore, decreasing dark saturation current densities. However, the use of localized rear contacts increases series resistance losses in the device, and the improved rear surface enhances the impact of bulk defects. As a result, methods to eliminate the negative im- pact of bulk defects have become increasingly important, which has seen a rapid development of engineering methods such as advanced illuminated hydrogen passivation processes to reduce the impact of defects. For example, rapid treatments performed on finished screen-printed solar cells have been used for the passivation of boron–oxygen defects in Czochralski silicon or defect clusters in multicrystalline silicon [4]. For n-type silicon solar cells, which typically use high-bulk-lifetime wafers, ef- forts have focused on the implementation of passivated contact structures to improve surface passivation [5], [6]. A number of characterization techniques are commonly used throughout solar cell fabrication including photoluminescence imaging [7] and photoconductance lifetime measurements [8]. On finished devices, recombination losses are often quanti- fied using techniques such as photoluminescence imaging and current–voltage (*I–V*) measurements. For *I–V* measurements, several methods can be utilized such as illuminated *I–V* mea- surements, as well as that performed under open-circuit condi- tions (Suns–*V*OC) to remove series resistance effects [9], or dark *I–V* measurements to remove light-generated current effects. In this work, we focus on the use of dark *I–V* measurements. Dark *I–V* curves provide significant detail about the various recombi- nation losses in solar cells. For example, providing information about series and shunt resistance mechanisms, as well as dark saturation current densities and resistance-limited recombina- tion mechanisms in the device. A thorough study of dark *I–V* curves with the associated recombination losses and understand- ing of such losses was presented by McIntosh [10]. By knowing the performance-limiting recombination mechanisms in a de- vice, processes can be modulated to reduce or eliminate such recombination mechanisms. A variety of methods have been used to fit *I–V* curves, such as the Newton–Raphson technique, although particular atten- tion must be paid to the initial conditions to ensure convergence of the iteration and a high level of accuracy of the determined values [11]. Other methods have included the use of algorithms to find the root of a function of voltage and current (*f* (*V, I*)) that is equal to zero for only the correct value of *I* [12], genetic

2156-3381 © 2017 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [http://www.ieee.org/publications](http://www.ieee.org/publications) standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on September 02,2024 at 06:30:47 UTC from IEEE Xplore. Restrictions apply.

: METHOD OF EXTRACTING SOLAR CELL PARAMETERS FROM DERIVATIVES OF DARK *I–V* CURVES

Fig. 1. Circuit diagram for the three-diode model of a solar cell.

HALLAM *et al.*

algorithms, and particle swarm optimizations [13], [14], as well as various iteration and estimation methods [15]–[19]. This pa- per will discuss a method to extract information on the solar cell parameters in the three-diode model from the derivatives of dark *I–V* curves. It will compare various approaches with different assumptions for the extraction of the parameters and discuss the limitations of each approach. It will demonstrate that de- spite the complexity of the three-diode model, a good accuracy can be achieved with a relatively simple procedure and small computational effort.

### II. ONE-DIODE,TWO-DIODE, AND THREE-DIODE MODELS

To fit illuminated *I–V* or dark *I–V* curves, various equivalent circuit models may be used, with different numbers of diodes. In a one-diode model, the dark saturation current components that represent the various recombination mechanisms in the device are lumped together into a single diode *D₁*, with current *I₁* and associated dark saturation current density of *I₀*1. This diode has a floating ideality factor, *n₁*. Series resistance *RS*effects are also lumped together, acting on the total current *I* of the device. Similarly, shunting effects are lumped together into a single parallel resistance *RSH*with associated current *ISH*.Inmany instances, this fitting fails to accurately describe the dark *I–V* curves of a solar cell, and as a result, a poorly modeled fit is obtained. In the two-diode model, in addition to *RS*and *RSH*,two separate diodes are used to represent recombination in the de- vice. For the first diode, *D₁*, an ideality factor of unity is as- sumed (*n₁* = 1). The dark saturation current density associated with this diode (*I₀*1) represents the current crossing the p-n junction from recombination in the bulk, emitter, and surfaces of the device. This includes both Shockley–Read–Hall (SRH) [20], [21] and Auger recombination effects, giving a current flowing through diode *D₁* of *I₁*. The second diode *D₂* has a floating ideality factor, *n₂*. The dark saturation current den- sity associated with this diode (*I₀*2) can be caused by SRH recombination in the depletion region [22], SRH recombina- tion at the edge [23], where the edge intersects the p-n junc- tion, and SRH recombination in high-injection conditions [24]. This gives a current *I₂* flowing through *D₂*. Similarly, in many instances, the two-diode model is not able to provide an ac- curate representation of the dark *I–V* characteristics of a solar

||||D|H|
|---|---|---|---|---|
|||T|||
|H|H|H SH|||
|H|H||||

cell. In the three-diode model, an additional diode is present. The current *I* flowing through this third diode *D* is used to rep- resent resistance-limited enhanced recombination in the device, with resistance *RH*, due to localized recombination [10], [25]. Here, *D* has a floating ideality factor, *n*. In the three-diode model, *D₁* and *D₂* have fixed ideality factors of *n₁* = 1 and *n₂* = 2, respectively. The electrical circuit used to describe so- lar cells for the three-diode model is shown in Fig. 1, including

||= I₀ I|e|
|---|---|---|
||H||
|H||S|
|H|SH|SH|

the light-generated current *IL*(shown in gray) that is zero for dark *I–V* curves. The equivalent circuit for the one-diode model can be obtained by ignoring current paths *I₂* and *I*, and simi- larly for the two-diode model by ignoring the current path *I*.

III. CHALLENGES OF PLOTTING *I–V* CURVES AND FITTING DARK *I–V* DATA

There are significant challenges in extracting appropriate so- lar cell parameters from dark *I–V* data: first, the low signal-to- noise ratios, particularly for values in the vicinity of *V* = 0V that are required for extracting some parameters; second, the diode models used are only theoretical constructions to approx- imate the recombination behavior of solar cells. However, they do not fully describe the complicated behavior of silicon solar cells. A third major challenge is the complicated nature of the mathematics used in these diode models. There is even a chal- lenge in being able to plot modeled *I–V* curves to enable curve fitting. For isolated components, *I–V* curves can be plotted easily from an explicit function of the current through each component in terms of the voltage across it, and the associated parameters, to give *I* = *f* (*V*). However, for the given circuit in Fig. 1, the current flowing through each component cannot be expressed by a function only including the cell voltage *V* and the component parameters. That is, a simple relationship of *I* = *f* (*V*) cannot be found. The currents *I₁*, *I₂*, and *ISH*are directly dependent on the voltage across the component *VD*rather than on *V*.To express the currents as a function of *V*, knowledge of the total current flowing through the cell (*I*) and the series resistance (*RS*) values is required. Similarly, for *IH*, the current directly depends on *VH*rather than *V* or *VD*, and hence, knowledge of all current components is required. The equations for the total current through the cell in the dark (neglecting *IL*), the current through each component, and the simplifications that can be made for the voltage across the component of either *V* or *V* are shown in (1)–(7), where *V* is the thermal voltage

*I* = *I₁* + *I₂* + *I* + *I* (1) ( <u>V −I ·R S</u> ) *I₁* = *I₀*1*eV T−* 1 (2)

() <u>V −</u> 2*V* <u>I ·R S</u> *I₂* = *I₀*2*eT−* 1 (3)

( <u>V −I ·R −I ·R</u> ) *n H V T* <u>S H H</u> *H−* (4)

<u>V −I·R</u> *I* = *R*

(5)

|, and of V|for I||||
|---|---|---|---|---|
|SH|H||||
|H||Fig. 2.|Simulated dark I–V curve (absolute value) and associated|curve|
|H|D|for a sample with the following parameters: I₀₁ = 800 fA, I₀₂ = 5 × 10 R = 0.3 Ω, R||A, =|
|||2.5.|||

|D|S||
|---|---|---|
|H|S H|S|

<u>dI</u> *dV* *−*7 *−*5 A, *RH*= 30 Ω,and*nH* *S SH*= 10 000 Ω, *I₀H*= 1*×*10

*V* = *V −I·R* (6)

*V* = *V −I·R − I · R.* (7)

While an explicit function, *I* = *f* (*V*), cannot be used, the values of *I* at each given *V* can be obtained using iterative methods, which can then enable plotting. Given that dark *I–V* curves are monotonically increasing, only one value exists for when the function*I* equals the input guess for the current (*I*guess) at a given voltage. Hence,*I*guesscan be varied until it is consistent with the output current determined from the expression of *I*. Alternatively, explicit expressions of current can be obtained as a function of *VD*for *I₁*, *I₂*, and *IH*.The corresponding values of *IH*at each *V* can then be interpolated to obtain the corresponding value of *I* at *V*. Subsequently, the currents of all components can be added to determine *I* and then the function interpolated to find the corresponding *I* values for each cell voltage *V*. Other methods have used the Lambert W function [26]–[29], although this approach is not straightforward. There are also significant challenges in fitting dark *I–V* curves due to the number of variables. In the three-diode model, there are seven variables. Fitting such curves with potentially hun- dreds of points by sweeping each variable and establishing a least-squares fit can be quite computationally expensive. Even, with approximate values of *RSH*and *RS*, five variables remain to fit in the three-diode model. Similarly, expressions of the derivatives of each current com- ponent cannot be expressed in terms of only *V*, but also require <u>dI</u> values for *I* and the total derivative ( *dV* ). The equations for the derivatives of each current component using the chain rule and are shown in (8)–(12). Again, iterative methods can be used to <u>dI</u> plot curves of *dV*. Alternatively, the derivative can be obtained numerically from the function of *I* by determining the local gradient at each point. This appears to be a simpler solution and is the approach used in this work

*dI dI₁ dI₂ dIHdISH* = + + + (8) *dV dV dV dV dV* <u>V</u> () *dI₁ I₀*1 *V* <u>D</u> *dI* = *eT·* 1 *− RS*(9) *dV VTdV* <u>V</u> () *dI₂ I₀*2 2*V* <u>D</u> *dI* = *eT·* 1 *− RS*(10) *dV* 2*VTdV* <u>V H</u>() *dIHI₀Hen H V TdI* =<u>V H</u>*·* 1 *− RS*(11) *dV* *n V* + *I en H V T* *dV* *H T* 0*H* () *dISH*1 *dI* = *·* 1 *− RS.* (12) *dV RSHdV*

IV. FITTING DARK *I–V* CURVES USING DERIVATIVES

A significant amount of information about component param- eters is given in the curve of *dV* <u>dI</u>. An example theoretical curve of the magnitude of *I* (*|I|*) is shown in Fig. 2 along with the derivative of *I*, *dV* <u>dI</u>. It is noted that for *V<*0V,*I<*0 A, and therefore, plotting *|I|* when using a logarithmic scale is helpful for establishing the fit to *I* at negative voltages. In this example,

<u>dI</u> the *dV* curve is dominated by *RSH*effects for *V<−*0*.*2V.At high voltages (*V>*0*.*8 V), the curve is dominated by*RS*effects. In the intermediate regions transitioning from the *RSH*domi- nated region to the *RS*dominated region (0*.*2V*<V <*0*.*8V), the curve is dominated by the three diodes. Depending on the parameters of an individual sample, these ranges will vary. For example, in heavily shunted samples (with sufficiently low val- ues of *RSH*in relation to the diode components,) *RSH*will dominate to higher *V* and possibly still dominate for voltages in the vicinity of *V* = 0 V or slightly above. <u>dI</u> Curves of *dV* provide valuable information about the solar cell parameters and can be used to place limits of the range of values a given solar cell parameter can take. With the mono- tonic increase of all current contributions, the benefit of using derivatives is that tighter tolerances can be placed on the values rather than directly using *I–V* curves. To demonstrate this method, we will first fit hypothetical *I–V* data, followed by experimental data later in the paper. For the theoretical example in the following sections, we use hy- pothetical *I–V* and <u>dI</u> curves of a cell with the following pa- *dV* rameters: *I* = 800 fA,*I* = 5*×*10 *−*7 A,*R* = 0*.*3 Ω,*R* = 0 1 *−* 05 2*S SH* 10 000 Ω, *I₀H*= 1*×*10 A,*RH*= 30 Ω, and*nH*= 2*.*5. In the following simulations, these curves of *I–V* and <u>dI</u> will be re- *dV* ferred to as the actual *I–V* and <u>dI</u> curves. Simulated curves used *dV* to predict parameters for the cell will be referred to as modeled curves. For this, voltages are in the range of *−*0*.*8V*<V <*1V with 100 data points. A summary of the fitting procedure used in this work is shown diagrammatically in Fig. 3. It highlights the range of voltages, *V*, used to determine each given parameter. This diagram is range here to guide the reader through the following sections. Unless otherwise specified, once an initial value for a given parame- ter has been estimated, the parameter remains enabled for the determination of other parameters. It should be noted that although the three-diode model is used in this paper to demonstrate the method, the method is also applicable for the one-diode and two-diode models. However, appropriate changes must be made in the determination of *I₀*

HALLAM *et al.*: METHOD OF EXTRACTING SOLAR CELL PARAMETERS FROM DERIVATIVES OF DARK *I–V* CURVES

*dI*

|Fig. 4.|Simulated|curve for a sample with the values specified in Fig. 2 (I|
|---|---|---|
|and I|) or a one order of magnitude reduction to the values of I||
|and I conductance G|= 1 × 10|A(0.1I are shown for the range of −0.6V<V <−0.2 V (for|
|I and I|)andatV|= 0 V for both cases.|

*dV* 2 *−*8 *H* 02= 5*×*10 A *−*6 0*H*2and 0*.*1*IH*). Values for the estimated shunt *SH,*est 2 *H*

currents flowing through diodes *D₁*, *D₂*, and *DH*are zero, and hence, there is a constant reverse current component flowing through the three diodes of *I*reverse= *I₀*1+ *I₀*2+ *I₀H*. Subse- <u>dI</u> quently, there is no contribution of the diode currents to.In *dV* <u>dI</u> this regime, is dominated by *RSH*, with only a minor influ- *dV* ence of *RS*. It should be noted, however, that care must be taken not to use excessively high reverse biases for *RSH*extraction, where the potential reverse breakdown effects could affect the accuracy of the value obtained. The shunt conductance (*GSH*) <u>dI</u> can then be taken as an average values of over a given range, *dV* for example, between *−*0*.*6V*<V <−*0*.*2 V. As a first ap- proximation, *RSH*can be approximated as the inverse of *GSH*. *−*4 In Fig. 4, *GSH*is estimated as 1*.*012*×*10 S, corresponding 3 to an estimate for *RSH*of 9*.*89*×*10 Ω, with *<* 1*.*2% error. However, once knowledge about *RS*is available, it should be corrected for *RS*, particularly when *RS*is high. The equation for determining *RSH*is given as

<u>(1 − GSH· RS)</u> *RSH*=*.* (13) *GSH* If taking an estimate of *RSH*at *V* = 0 V, the influence of *D₂* and *DH*will result in an overestimation of the value for *GSH*, 4 with a value of 2*.*67*×*10 S. This would result in an estimate 3 of *RSH*of 3*.*75*×*10 Ω, which is a 167% underestimation of the actual value. However, with a reduced influence of *D₂* and *DH*(such as a reduction of one order of magnitude for *I₀*2and *I₀H*), this would be reduced to an underestimation in *RSH*of 14.3%. For a two order of magnitude reduction in

Fig. 3. Summary of the iterative fitting procedure for dark *I–V* data. All

*I₀*2and *I₀H*, the underestimation in *RSH*would be reduced to parameters are enabled unless otherwise specified.

1.6%. Similarly, reduced values of *I₀*2and *I₀H*would result in improved estimations of the*RSH*when taking an approximation
<u>dI</u> from the average value of in the range between *−*0*.*6V*<* *dV* and/or *I₀*2to allow for floating ideality factors, such as for the *V<−*0*.*2V. determination of *I₀H*in the three-diode model.

*B. Fitting the Series Resistance (RS)*
*A. Fitting the Shunt Resistance (RSH)*
Similarly, a first approximation for *RS*can be obtained from <u>dI</u> Extracting the shunt resistance is relatively straightforward. the inverse of at high voltages. However, doing so overesti- *dV* At sufficient reverse biases, the exponential terms for the mates *RS*and should be treated as an upper limit of the possible

|dI d log (()) dV (a) Curve of|and the voltage (|V = 0. 52 V) correspond-|Fig. 6.|(a) Test dark I–V curve and (b) associated||dI curve for a cell with the||
|---|---|---|---|---|---|---|---|
|dV ing to the onset of visible resistive effects. (b) Test tangent (on a logarithmic scale) from, and D in increasing the H|V. ref values, as it does not take into account any influence of dI|ref I–V curve and corresponding D₁. In this example, a value of|10 000 Ω, values), I,|following parameters: I = 800 fA, I 01 02 − 5 = 1 × 10 A, R I 0 H H both (a) and (b) show corresponding curves with and I disabled (set to 0), and various 02 0 H − 15 − factor of 10 from 1 × 10 to 1 × 10|= 5 × = 30 Ω,and 9 A.|dV − 7 10 A, R = 0. 3 Ω, R S SH n = 2. 5. Modeled curves in H R and R enabled (same SH S I values increasing by a 01||
|= 0. 32 Ω was obtained, an overestimation of|dV imately 6.6%. A lower bound value may be obtained by identi- fying the voltage at which resistive effects are clearly noticeable|R by approx- S||||||
|dI I and dV from a domination of D₂ will increase the slope of the curve log dI decrease in the slope of log( dV|. In this instance, the monotonically increasing properties are utilized. In the absence of toward D₁|R, any change S with increasing voltage dI) (d (log()) dI dV, ().Any dV dV) at high voltages is characteris- dI d log (())||||||
|||dV||||||

Fig. 5.

=

*RS* *D₂* *RS*

*dI* in *dV* of both

|Fig. 7.||R|R using test|
|---|---|---|---|
|values forUpper and lower bounds on enabled. R|I for iterations to calculate = 10 000 Ω.|Rvalues and error in with only R|, R and I|

*S S* 0 1*S SH S* 01 *SH*

tic of a resistive effect. Therefore, the point at which *dV* begins to decrease indicates a point at which *RS*effects can be observed in the *I–V* curve [see Fig. 5(a)], in this instance cor- responding to a reference voltage of *V*ref= 0*.*52 V. A tangent (on a logarithmic scale) is then drawn on the *I–V* curve from this point up to a predetermined current value [see Fig. 5(b)]. From this, the difference in voltage (Δ*V*) between the actual *I–V* measurement and the tangent can be used to estimate *RS*. Using this approach, a lower bound value for *RS*of 0*.*25 Ω is obtained (a 17.3% underestimation). An improved approximation for the *RS*can be obtained by <u>dI</u>

|for a curve with only R||and a large value|||||||
|---|---|---|---|---|---|---|---|---|
|dV||SH||||0||−9|
|−9|S||dI dV|||S 0|0|S|
||S||||||||

simulating the *dV SH* of *I₀*1active that grossly overestimates a reasonable value of *I₀*1such as 1*×*10 A. Then, an iteration can be performed for curves with various *R* values until a fit to the at high voltages (e.g., at *V* = 1 V) is obtained. This can also be con- sidered as an upper limit for *R*. The advantage of using the derivative to form the fit, rather than using the actual *I–V* curve, is highlighted in Fig. 6. When simulating an *I–V* curve using the correct values for*RSH*and*RS*, varying the *I₀* value can lead to substantial changes in the value of *I* at *V* = 1 V. In contrast, the same changes do not significantly affect *dV* <u>dI</u>. Similarly, a lower limit on the *RS*value can be obtained by applying the same test with a sufficiently small *I₀* value such as 1*×* *−*

A.
Performing such an iteration will, therefore, lead to reduced errors in the obtained upper limit value of *RS*, provided that the *I* value used is sufficiently high. Fig. 7 shows the errors from 0 1 this *R* extraction by choosing different *I* values from the test *S* 01 curve shown in Fig. 6. Using a test *I* value of 1*×*10 *−*9 A 0 1 results in an overestimation of *R* by 5.5%, to give a value of

0*.*3165 Ω. Further improvements in the accuracy of *R* can be obtained once approximate values of *I* and *I* are known.
1 2

*C. Fitting I₀*1*and I₀*2 First approximations for the values of *I₀*1and *I₀*2can be obtained in a similar manner, which can also be considered as upper limits for the respective values, provided that the*RS*is not too high. If the *RS*is too high, resistive effects will dominate at large positive biases and result in a slight underestimation of *I₀*. To estimate *I₀*, only *RS*, *RSH*, and *I₀* are enabled,

||||Fig. 9.|dI dI I–V and curves along with modeled I–V and curves using the dV dV|
|---|---|---|---|---|
|dI I–V and dV enabled for determining upper bounds for (a)|curves, along with modeled curves with|R, R ,and S SH I₀₁ and (b) I₀₂.|nated by the dI then dV|progressive estimates for R, R, I ,and I. 01 02 S SH dI can be ignored. Here, in the vicinity of V = 0V, is domi- dV, provided that R is sufficiently high. If so, D H SH I₀ H is approximately proportional to. Furthermore, n V H T I₀ H|
|using the current estimates of performed to give the highest possible value of dI dV bias range from 0. 4V <V < used to determine an upper limit of I₀ 2 values of the modeled and actual underestimation of the I–V same iteration against the I–V will result in a larger error in I₀ 1 dI curve result in an estimation for dV − 7. 83 × 10|R and S curve does not exceed the value of the actual curve at any point within a specific range (e.g., a high positive. Example fittings for the upper limits of are shown in Fig. 8. The images also show the corresponding I–V and I₀|R. An iteration is SH such that the I₀ 1 dI dV 1 V). The same method is then by disabling I₀ and I₀ 2 1 I₀ and I₀ 1 curves, highlighting the curve. Therefore, if performing the dI curve, it curve rather than the dV. Here, extracting values 2 I₀ of 8. 81 fA and 1 A, overestimating the respective values by|the value of 2 V Subsequently, assuming that|the second derivative is approximately proportional to 2 (n V) H T Therefore, taking the ratio of the first and second derivatives in the vicinity of V = 0 V (such as 0 V <V < 0. 2 V) can give n V. In this example, this range of voltages re- H T values from 2.79 to 4.00 (with a minimum sults in a range of n H value occurring at V = 0. 147 V). This minimum value of 2.79 is an overestimation by 11.6%, while the values obtained near = 0 V show larger errors to the presence of shunt resistance. can be estimated using (14) at this voltage, I₀ H and D are the only active components. In R SH H − 5 A is obtained, an overesti- this instance, a value of 1. 37 × 10 mation by 37% V I − R SH I₀ =. (14), estimate V H|

Fig. 8.

*I₀₁* or *I₀₂*

.

modeled

enabling

from the *I₀*2of 5

10.1% and 16.5%. In comparison, extracting the values from the *I–V* curve results in estimations of *I₀*1= 243 fA (203%
*−*7 overestimation) and 6*.*45*×*10 A (29% overestimation). Once approximate values of *I₀*1and *I₀*2are known, an accurate value of *RS*can be obtained. This value is obtained using the same method as used previously to determine *RS*, with both *I₀*1and *I₀*2enabled using the current estimates of *I₀*1and *I₀*2. Here, despite the errors in the estimations of *I₀*1and *I₀*2,an error in *RS*of less than 0.1% is obtained. It should be noted, however, that for excessively high values of *RS*, knowledge of approximate values for *DH*may be required for an accurate estimation of *RS*. Using the estimations of the values obtained so far, an excellent fit can be obtained for large positive biases dominated by *D₁*, *D₂*, and *RS*effects. The dominant errors in the fit arose from the presence of *DH*associated recombination (shown in Fig. 9). The corresponding root-mean-squared error of *I*, i.e., RMSlog 10*I*, is 0.269.

*D. Fitting I₀H, nH, and RH* Fitting values for the three parameters related to*DH*are more involved. However, the values of *I₀H*and *nH*can be estimated in the vicinity of *V* = 0 V, where the resistive effects from *RH*
### en H V T− 1

To improve the accuracy of the *nH*estimate, the effects of <u>dI</u> both *RS*and *RSH*can be removed from *I–V* and *dV* curves. Here, *V* is first corrected for the drop in voltage across *RS*to give the corresponding values of *VD*[according to (6)]. Subse- quently, the current is corrected for *RSH*using (15). Example <u>dI</u> *I–V* and *dV* curves corrected for *RS*, and both *RS*and *RSH*, are shown in Fig. 10. Using the ratio of the first and second derivatives of the *RS*- and *RSH*-corrected *I–V* curves, using the same uncorrected voltage range (0 V *<V <*0*.*2V),*nH*values in the range of 2.47 to 2.79. Here, the most accurate values are obtained in the range of 0 V *<V <*0*.*1 V. Assuming *V* = 0V, a value of 2.47 is obtained (1.3% error) with a corresponding *−*5 *I₀H*of 1*.*07*×*10 A (7% error). Alternatively, the *RS*- and *RSH*-corrected *I–V* curve at sufficiently large negative voltages provides the negative summed value of *I₀*1, *I₀*2, and *I₀H*.In *−*5

Fig. 10, this value is 1*.*05*×*10 A, which provides an estima-

tion of the upper limit of *I₀H*(a 5.5% overestimation). A lower limit for *IH*is obtained with the knowledge of the upper lim- its of both *I₀* and *I₀*. In the situation that *I₀H>> I₀* + *I₀*, this provides a very accurate value for *I₀H*. Here, a value of *I₀H*= 9*. ×* *−* A is obtained, a 5.3% underestimation.

|high values of R|, where D|has a significant influence in the||
|---|---|---|---|
||S|H||
|S||dV dI||
||S|||
||||S|
|S|||SH|

Fig. 10. (a) *I–V* and (b)*dV*

<u>dI</u> curves along with the corresponding curves corrected for *RS*, and both *RS*and *RSH*.

Using these upper and lower limits for *I₀H*and the known value of *I* at this voltage, assuming that *DH*is the only active compo- nent, this gives respective values of 2.46 and 2.40 for *nH*, with corresponding errors of 1.6% and 3.8%

<u>VD</u> *I* *RS,RSH−*corrected= *I*cell*−.* (15) *RSH*

*I₀H*and *nH*can also be estimated using an iterative approach at low voltages. Here, a voltage range is chosen (such as

0*.*05 V *<V <*0*.*1 V) that is sufficiently low to ignore effects of *RH*. *I₀H*is estimated using the *I–V* curve. A test curve is generated with current estimates for *RS*, *RSH*, *I₀*1, and *I₀*2. For all iterations, the *RH*is disabled. In the first iteration, *nH*is assumed to be 1. The iteration is performed to find the maximum value of *I₀H*that results in the modeled curve being less than the actual *I–V* curve for all values in the voltage range. With this value of *I₀H*, an iteration is performed using <u>dI</u> to find the minimum value of *n*, where the test
<u>dI</u> curve *dV H dV* is lower than the actual *dV* <u>dI</u> curve for all values in the voltage range. This process is performed multiple times to converge on an approximate value of *I₀H*and *nH*. In this instance, a value of *I₀H*= 1*.*071*×*10 *−*5 A is obtained, an 7.1% overestimation. The corresponding value of *nH*= 2*.*67 is obtained, a 6.9% overes- timation. Using the same method of iteration with the estimate of the lower limit of *I₀H*from the *RS*- and *RSH*-corrected *I–V* curve, *nH*is estimated at 2.50, with *<* 0.1% overestimation. Subsequently, *RH*is estimated using an iterative method to find the minimum *RH*value to keep the test *dV* <u>dI</u> curve below

the actual *dV* <u>dI</u> curve over a specified voltage range. Here, *I₀H* is taken as the lower bound from the *RS*- and *RSH*-corrected *I–V* curve (9*.*47*×*10 *−*6

A), and *nH*is taken from the ratio
of the first and second derivatives of the corrected *I–V* curve (2.47). From this iteration, a value of *RH*= 37*.*0 Ω is obtained, a 23.4% overestimation of *RH*. Despite what may appear as significant errors for some parameters (such as for *RH*), the fitted curve provides an excellent approximation of the actual *I–V* curve when presented on a logarithmic scale (not shown), with RMSlog 10*I* = 0*.*012. The dominant discrepancy of the curves comes from the overestimation of *I₀*2and *RH*.

*E. Refinement of Values* Once approximations are known for all values, the estimations for several parameters can be refined. For*RS*, while in the given example an improved estimate is not required, for excessively *R* affected region of the curve, improved accuracy of the approximation of *R* can be obtained. For this, an iteration is performed to find the maximum value of*R* given the estimation of all other parameters. In this example, no significant change in *R* (0*.*2999 Ω) or subsequent change in *R* (9*.*89*×*10
3 Ω) is observed. In the previous approximation of *I₀*2, the absence of the con- tributions of diodes *D₁* and *DH*to the modeled *dV* <u>dI</u> resulted in an overestimation of *I₀*2. To correct for this, *RS*- and *RSH*- corrected <u>dI</u> curves are generated for the actual <u>dI</u> curve and *dV dV* test curves with only the *D₁*, *D₂*,or*DH*diodes active [see

Fig. 11(a)]. Subsequently, at the voltage whereby the ratio of the

*D₂*-related *dV* <u>dI</u> curve to the actual *dV* <u>dI</u> curve is maximized (the point whereby *I₀*2is estimated), the values of all diode-related *dV* <u>dI</u> values are estimated. An improved estimated for *I₀*2is given by (16). Here, the revised estimate for *I₀*2is 5*.*10*×*10 *−*7 A, a

2.0% overestimation. In the given example, the voltage range is not sufficiently high to allow for an improved approximation of *I*,asthe*R*- and *R*-corrected
<u>dI</u> curves of the actual <u>dI</u> 0 1*S SH dV dV* curve and *D₁*-related curve did not converge <u>dI02</u> *I₀,*revised= *I₀* <u>dV</u>

*.* (16)
2 2*dI₀₁ dI₀₂ dI₀* *H* *dV* + *dV* + *dV* Subsequently, *I₀H*can be revised using the updated value of *−*6 *I₀*2to give *I₀H*= 9*.*55*×*10 A, a 4.5% underestimation. Then, <u>dI</u> the value of *nH*can be obtained from an iteration of *dV* as used previously to give a value of *nH*= 2*.*46 (an error of 1.5%), and similarly, *RH*can be obtained to give a value of *RH*= 33*.*7 Ω (a 12.3% error). These values provide an excellent fit to the <u>dI</u> *dV* curve as shown in Fig. 11(b), with RMSlog 10*I* = 0*.*004.

V. E XAMPLE APPLYING THE METHOD TO REAL DATA
An industrial 156 mm *×* 156 mm PERC solar cell was cleaved into small cells (3 cm *×* cm). The dark *I–V* characteristics were measured on a custom-built *I–V* tester using a Keithley 2401 Source Measuring Unit and four-wire sensing to minimize contributions from resistance in the test leads. An example dark *I–V* curve is shown in Fig. 12(a) along with the

|Fig. 11.|(a) Actual R|-andR|-corrected|curve and modeled D|, D,|
|---|---|---|---|---|---|
|and D|curves. (b) Actual I–V and||curves along with the corresponding|||
|test curves using the estimated parameters: I|||= 881 fA, I|= 5.11 × 10|A,|
|R = 0.2999 Ω, R and n|= 2.52.|= 10 000 Ω, I|= 9.99 × 10|A, R|= 34.45 Ω,|

*S SH dV* *dI* 1 2 *H dV* *dI* *dV* *dI* 01 02 *−*7 *S SH* 0*H* *−*6 *H* *H*

fitted curve using the methods described in the previous section. As shown, an excellent fit is obtained using the parameters listed in the caption, with an error of RMSlog 10*I* = 0*.*145. The asso- ciated *RS*- and *RSH*-corrected *I–V* and *dV* *dI* curves are shown in Fig. 12(b) and (c), respectively. It should be noted that no smoothing was applied to the data. Although accurate data ac- quisition is essential to ensure that the background noise in the instrument in the low-current range does not produce signifi- cant noise, the application of smoothing will likely improve the quality of the data for fitting purposes. At voltages below *−*0*.*6 V, the actual *dV* <u>dI</u> data deviate from the modeled curve due to noise [see Fig. 12(a)]. The associated noise in the *RS*- and *RSH*-corrected *I–V* curve [see Fig. 12(b)] would cause an error in the determination of *I₀H*. However, the flat nature of the *RS*- and *RSH*-corrected curve in range of *−*0*.*6V*<V <−*0*.*2 V indicates a high accuracy of the determined *RSH*(2460 Ω), and therefore the estimation of *I₀H*. This provides an estimation of the summed value of *I₀*1, *I₀*2and *I₀H*of 1*.*29 *−* 1*.*41 *×*10 *−*5

A. With the known estimations of
*I₀*1(1120 fA) and *I₀*2(5*.*26*×*10 *−*7

A) being substantially lower
than this, it accurately estimates *I₀H*. One weakness of using *dV* <u>dI</u> data for the extraction of solar cell parameters in that small errors in *I–V* data can lead to significant errors in *dV* <u>dI</u>. This is particularly the case for extremely small currents at negative voltages or in the vicinity of *V* = 0V.The *RS*- and *RSH*-corrected *dV* <u>dI</u> curve in Fig. 12(c) shows noise

Fig. 12. *I–V* and

<u>dI</u> data and the corresponding test curves with the estimated *dV* parameters: *I₀₁* = 1120 fA, *I₀₂* = 5*.*26*×*10 *−*7 A, *RS*= 0*.*370 Ω, *RSH*= 2460 Ω, *I₀H*= 1*.*29*×*10 *−*5 A, *RH*= 34*.*8 Ω,and*nH*= 2*.*85. Actual (b) *I–V* and (c)*dV* <u>dI</u> curves along with the corresponding curves corrected for *RS*, and both *RS*and *RSH*.

for *V<−*0*.*1 V, deviating away from the modeled curve. This suggests that the sensitivity in <u>dI</u> is limited to approximately *dV* 1 *×*10 *−*5 A*/*V with this dataset and experimental setup. Hence, for the determination of *nH*, the voltage range should be above *−*0*.*1 V, but still sufficiently low to avoid significant effects from *RH*(or the other diodes). In this example, all data points in the vicinity of *V* = 0 V with currents as low as 1*×*10 *−*6 A resulted in meaningful *dV* <u>dI</u> values. The approximation of *nH* from the ratio of the *RS*- and *RSH*-corrected curves for *I–V* and *dV* <u>dI</u> in the range of *−.*1V*<V <.*1 V gives a range of *nH*= 2.35–2.98, compared with a value of 2.85 using an iterative approach. For the fitted curve in this example, the dominant discrep- ancy between the actual and modeled *I–V* data is related to

resistance limited recombination effects (*DH*). Estimations for the ranges of *DH*-related parameters from the iterative pro- *−*5 cesses were *I₀H*= 1*.*28*−*1*.*34 *×*10 A, *nH*= 2*.*83*−*2*.*86, and *RH*= 33*.*7*−*36*.*5 Ω. This entire range of parameters pro- vides an excellent fit to the data with corresponding values for RMSlog 10*I* in the range of 0.14–0.15. In our future work, we will apply the technique to a range of *I–V* curves from solar cells with greatly different *I–V* properties. This will serve as further validation for the technique as well as highlighting the associated limitations.

### VI. CONCLUSION

In this paper, a technique to extract recombination and resis- tance parameters from the derivatives of dark *I*-*V* curves has been presented. This method takes advantage of the monotonic properties of each current component and the associated deriva- tive components. To determine *RSH*, small negative voltages should be used to avoid potential influences of resistance-limited recombination effects from *I₀H*in the vicinity of *V* = 0V.For *RS*, test curves of *dV* <u>dI</u> with a range of *I₀*1values can be used to ( <u>dI</u> ) *−*1 give a much closer approximation rather than using *dV* at high voltages. For first approximations of *I₀*1and *I₀*2, iterative processes can be applied to find the maximum value at which <u>dI dI</u> the simulated *dV* values are below the actual *dV* values within in a given voltage range with only the *RSH*, *RS*, and the *I₀* component of interest enabled. Subsequently, a more accurate value of *RS*can be obtained. Fitting values for the parameters related to *DH*are more involved. The values of *I₀H*and *nH*can be estimated in the vicinity of *V* = 0 V, where the resistive effects from *RH*can be ignored. The ratio of the first and second derivatives of the *RS*- and *RSH*-corrected *I–V* curves can be used to obtain the value of *nH*and subsequently *I₀H*. Alternatively, the *RS*- and *RSH*-corrected *I–V* curve can give an upper limit for *I₀H*as well as a lower limit (based on the upper limit estimations for *I₀*1and *I₀*2). Knowledge of *I₀H*can then be used to refine the estimation of *nH*. Another approach is to perform an iteration to determine values of *I₀H*and *nH*in the vicinity of *V* = 0 V. Subsequently, an iterative method is used to determine *RH*. Once estimations of all values have been obtained, the same methods can be used to refine the estimations further. On a hypothetical case, a value of with RMSlog 10*I* = 0*.*004 was obtained demonstrating an excellent fit. The methods were then applied to real *I–V* data from a cleaved industrial PERC solar cell, yielding RMSlog 10*I* =

0*.*145.
REFERENCES

[1] V. Shanmugam *et al.*, “Impact of the phosphorus emitter doping profile on metal contact recombination of silicon wafer solar cells,” *Sol. Energy* *Mater. Sol. Cells*, vol. 147, pp. 171–176, 2016. [2] A. W. Blakers, A. Wang, A. M. Milne, J. Zhao, and M. A. Green, “22.8% efficient silicon solar cell,” *Appl. Phys. Lett.*, vol. 55, no. 13, pp. 1363–1365, 1989. [3] ITRPV Working Group and others, “International technology roadmap for photovoltaics (itrpv.net): Results 2015,” *ITRPV: Germany*, 7th ed., 2016. [4] B. J. Hallam *et al.*, “Advanced hydrogenation of dislocation clusters and boron-oxygen defects in silicon solar cells,” *Energy Procedia*, vol. 77, pp. 799–809, 2015.

[5] D. Smith *et al.*, “Generation III high efficiency lower cost technology: Transition to full scale manufacturing,” in *Proc. 38th IEEE Photovoltaic* *Spec. Conf.*, 2012, pp. 594–597. [6] S. Glunz *et al.*, “The irresistible charm of a simple current flow pattern- 25% with a solar cell featuring a full-area back contact,” in *Proc. 31st Eur.* *Photovoltaic Sol. Energy Conf.*, 2015, pp. 259–263. [7] T. Trupke, R. A. Bardos, M. C. Schubert, and W. Warta, “Photolumi- nescence imaging of silicon wafers,” *Appl. Phys. Lett.*, vol. 89, 2006, Art. no. 044107. [8] R. A. Sinton, A. Cuevas, and M. Stuckings, “Quasi-steady-state photo- conductance, a new method for solar cell material and device characteri- zation,” in *Proc. 25th IEEE Photovoltaic Spec. Conf.*, 1996, pp. 457–460. [9] R. Sinton and A. Cuevas, “A quasi-steady-state open-circuit voltage method for solar cell characterization,” in *Proc. 16th Eur. Photovoltaic* *Sol. Energy Conf.*, 2000, pp. 1–5. [10] K. R. McIntosh, *Lumps, Humps and Bumps: Three Detrimental Effects in* *the Current-Voltage Curve of Silicon Solar Cells* Univ. New South Wales, 2001.. Kensington, Australia:

[11] N. Enebish, D. Agchbayar, S. Dorjkhand, D. Baatar, and I. Ylemj, “Nu- merical analysis of solar cell current-voltage characteristics,” *Sol. Energy*

[12] S. Suckow, T. M. Pletzer, and H. Kurz, “Fast and reliable calculation of *Mater. Sol. Cells*, vol. 29, no. 3, pp. 201–208, 1993.

the two-diode model without simplifications,” *Prog. Photovoltaics, Res.* *Appl.*, vol. 22, no. 4, pp. 494–501, 2014. [13] J. A. Jervase, H. Bourdoucen, and A. Al-Lawati, “Solar cell parameter extraction using genetic algorithms,” *Meas. Sci. Technol.*, vol. 12, no. 11, 2001, Art. no. 1922. [14] M. Ye, X. Wang, and Y. Xu, “Parameter extraction of solar cells us- ing particle swarm optimization,” *J. Appl. Phys.*, vol. 105, no. 9, 2009, Art. no. 094502. [15] K. Ishaque, Z. Salam, and H. Taheri, “Simple, fast and accurate two-diode model for photovoltaic modules,” *Sol. Energy Mater. Sol. Cells*, vol. 95, no. 2, pp. 586–594, 2011. [16] M. G. Villalva, J. R. Gazoli, and E. Ruppert Filho, “Comprehensive ap- proach to modeling and simulation of photovoltaic arrays,” *IEEE Trans.* *Power Electron.*, vol. 24, no. 5, pp. 1198–1208, May 2009. [17] M. Chegaar, G. Azzouzi, and P. Mialhe, “Simple parameter extraction method for illuminated solar cells,” *Solid-State Electron.*, vol. 50, no. 7, pp. 1234–1237, 2006. [18] A. Ortiz-Conde, F. J. G. Sanchez, and J. Muci, “New method to extract ´ the model parameters of solar cells from the explicit analytic solutions of their illuminated I–V characteristics,” *Sol. Energy Mater. Sol. Cells*, vol. 90, no. 3, pp. 352–361, 2006. [19] M. AlRashidi, M. AlHajri, K. El-Naggar, and A. Al-Othman, “A new estimation approach for determining the I–V characteristics of solar cells,” *Sol. Energy*, vol. 85, no. 7, pp. 1543–1550, 2011. [20] W. Shockley and W. Read, Jr,, “Statistics of the recombinations of holes and electrons,” *Phys. Rev.*, vol. 87, no. 5, pp. 835–842, 1952. [21] R. N. Hall, “Electron-hole recombination in germanium,” *Phys. Rev.*, vol. 87, no. 2, p. 387, 1952. [22] C.-T. Sah, R. N. Noyce, and W. Shockley, “Carrier generation and re- combination in pn junctions and pn junction characteristics,” *Proc. IRE*, vol. 45, no. 9, pp. 1228–1243, 1957. [23] C. Henry, R. Logan, and F. Merritt, “The effect of surface recombina- tion on current in Al*x*Ga₁*−x*As heterojunctions,” *J. Appl. Phys.*, vol. 49, no. 6, pp. 3530–3542, 1978. [24] W. Shockley, “The theory of p-n junctions in semiconductors and p-n junction transistors,” *Bell Syst. Tech. J.*, vol. 28, no. 3, pp. 435–489, 1949. [25] F. Hernando, R. Gutierrez, G. Bueno, F. Recart, and V. Rodriguez, “Humps, a surface damage explanation,” in *Proc. 2nd World Conf. Pho-* *tovoltaic Sol. Energy Convers.*, 1998, pp. 1321–1323. [26] J. H. Lambert, “Observationes variae in mathesin puram,” *Acta Helvetica*, vol. 3, no. 1, pp. 128–168, 1758. [27] L. Euler, “De serie lambertina plurimisque eius insignibus proprietatibus,” *Acta Acad. Scient. Petropol*, vol. 2, pp. 29–51, 1783. [28] T. Banwell and A. Jayakumar, “Exact analytical solution for current flow through diode with series resistance,” *Electron. Lett.*, vol. 36, no. 4, pp. 291–292, 2000. [29] A. Jain and A. Kapoor, “Exact analytical solutions of the parameters of real solar cells using lambert w-function,” *Sol. Energy Mater. Sol. Cells*, vol. 81, no. 2, pp. 269–277, 2004.

Authors’ photographs and biographies not available at the time of publication.
