Accepted: 7 January 2024

# Unveiling the mechanism of attaining high fill factor in silicon

### 1,2,3 1 2,3

## | Can Han | Chaowei Xue |

## | Pingqi Gao

University, No. 66, Gongchang Road, A world record conversion efficiency of 26.81% has been achieved recently by LONGi team on a solar cell with industry-grade silicon wafer (274 cm², M6 size). An 2 LONGi Green Energy Technology Co., Ltd., Xi'an, 710016, China unparalleled high fill factor (FF) of up to 86.59% has also been certified in a separated device. The theoretical FF limit has been predicted to be 89.26%, while the practical FF is far below this limit for a prolonged interval due to the constraints of recombina- Correspondence tion (i.e., SRH recombination) and series resistance. The ideality factor (m) in the equivalent circuit of silicon solar cells is consistently ranging from 1 to 2 and rarely Solar Energy Systems, Shenzhen Campus of Sun Yat-sen University, No. 66, Gongchang falls below 1, resulting in a relatively lower FF than 85%. Here, this work comple- ments a systematic simulation study to demonstrate how to approach the FF limit in Email: gaopq3@mail.sysu.edu.cn design of silicon solar cells. Firstly, a diode component with an ideality factor equal to Guangdong Basic and Applied Basic Research2/3 corresponding to Auger recombination is incorporated in the equivalent circuit Foundation, Grant/Award Number: for LONGi ultra-high FF solar cell; Secondly, an advanced equivalent circuit is put for- Development Program of China, Grant/Awardward for comprehensive analysis of bulk recombination and surface recombination Number: 2022YFB4200203; National Natural on the performance, in which specific ideality factors are directly correlated with vari- ous recombination mechanisms exhibiting explicit reverse saturation current density Numbers: 62104268, 62034009; Shenzhen Fundamental Research Program, Grant/Award (J₀). Finally, we evaluate precisely the route for approaching theoretical FF in practical solar cell fabrication based on electrical design parameters using the developed

diode model, fill factor, recombination, silicon solar cell

Received: 21 August 2023 Revised: 6 December 2023 DOI: 10.1002/pip.3775

### <u>RESEARCH ARTICLE</u>

solar cells

### 1 1,2,3

## Hao Lin | Genshun Wang | Qiao Su

### 2,3 2,3 2,3

## Shi Yin | Liang Fang | Xixiang Xu

1 School of Materials, Institute for Solar Energy Systems, Shenzhen Campus of Sun Yat-sen Abstract

Shenzhen, Guangdong, 518107, China

3 LONGi Central R&D Institute, Xi'an, 712000, China

Pingqi Gao, School of Materials, Institute for

Road, Shenzhen, Guangdong 518107, China.

Funding information

2019B151502053; National Key Research and

Science Foundation of China, Grant/Award

Number: JCYJ20200109142425294

model.

KEYWORDS

### 1 | INTRODUCTION

The current density–voltage (J–V) curve of conventional p–n junction usually satisfies the diode equation, Jm= J0m{exp[V/(m Vth)] 1}, where J0m, Vth, and m represent the reverse saturation current den- sity, thermal voltage, and ideality factor, respectively. In most devices, the m value is ranging from 1 to 2, therefore equivalent circuit with

Prog Photovolt Res Appl. 2024;32:359–371.

double diodes (with m = 1 and m = 2) is widely used for more precise description of the J–V characteristics. This double-diode model serves as core methodology in analytical models or softwares in silicon pho- tovoltaic (PV), such as minority charge carrier analysis of surface recombination (reverse saturation current density, J₀) by Sinton, 1 car- rier selectivity model by Brendel et al, 2,3 equivalent circuit, 4 and Grid- dler software. 5

wileyonlinelibrary.com/journal/pip

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made. © 2024 The Authors. Progress in Photovoltaics: Research and Applications published by John Wiley & Sons Ltd.

1099159x, 2024, 6, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.3775](https://onlinelibrary.wiley.com/doi/10.1002/pip.3775) by Oxford University, Wiley Online Library on [03/03/2026]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License LIN ET AL.

The intrinsic recombination in crystalline silicon (c-Si) bulk is resistance (RS< 0.2 Ω cm²) leads to a world record FF of 86.59%. In intrinsically dominated by Auger rather than radiative process by its this context, it is critical to revisit the existing c-Si solar cell models, indirect bandgap nature. In the development of c-Si solar cell, the including the FF improvement strategy, the characterization of the extrinsic recombination, that is, defective bulk and surface recombina-m for recombination at different injection level, and the equivalent cir- tion, normally limits cell performance and covers up the Auger recom-cuit model for recombination modeling. bination effect. As such in an equivalent circuit for c-Si solar cell, the In this study, we first demonstrate the measured J-V characteris- Auger recombination containing information of J0 2/3(reverse satura-tics of the solar cell with record FF. The upward trend of FF along with tion current density with m = 2/3) 6 only reveals itself when the surface recombination suppression is explained by double-diode defect-related recombination indicated by J₀₁ and J₀₂ (reverse satura-model with J₀₁ and J0 2/3(representing the surface recombination and tion current density with m = 1 and 2, respectively) are suppressed to Auger recombination, respectively). Subsequently, the correlation a substantially low level. Assuming defect-free fabrication processes between the modified double-diode model and various recombination (Auger recombination dominant), Richter et al estimated that a theo-mechanisms are elucidated. A detailed description of the influence of retical power conversion efficiency (PCE) and upper limit of FF for c-Si bulk recombination and surface recombination, as well as the corre- solar cells are 29.4% and 89.26%, respectively. 7 In practical c-Si solar sponding simplified J₀, on cell performance is presented. Finally, two cell fabrication, the following electrical performances are demanded methods, that is, conventional equivalent circuit model and simplified to approach the theoretical FF limit⁸: high-quality wafer (lifetime of recombination model, are established for accurate analysis and fit of SRH, τSRH> 10 ms), low surface recombination (J₀surf< 2 fA/cm²), the solar cell J–V parameters. The guideline for approaching theoreti- and low series resistance (RS< 0.2 Ω cm²). While wafer quality is cal FF limit is discussed. improved continuously, surface passivation and series resistance become the major challenge to enhance c-Si solar cell performance to break the predicted limit of FF merely on J₀₁ diode equation, that is, 2 | REALIZATION OF ULTRA-HIGH FF IN FF = ~85% of Green limit⁹ with m = 1. For examples, passivated C-SI SOLAR CELL emitter and rear cells (PERCs) and tunnel oxide passivated contact (TOPCon) solar cells with a diffused junction are inaccessible from Figure 1a shows the PCE of notable high-performance solar cells in perfect surface passivation, while silicon heterojunction (SHJ) solar relation to open circuit voltage (VOC) and FF. The Green limit⁹ lines of cell is struggling in minimize the contact resistance. 10 Recently, LONGi m = 2/3 and m = 1 (gray dotted lines), as well as the two “intrinsic team broke the Green limit for FF of m = 1 by developing a p-type recombination + surface recombination” curves (blue and red solid nanocrystalline silicon contact possessing ultra-low activation lines) are given. The intrinsic recombination was calculated by using energy. 11 The simultaneous optimization of passivating contact (J₀ the Auger recombination model proposed by Black and Macdonald¹² surf< 1.5 fA/cm², contact resistance of ρc<20 mΩ cm²) and series and considering radiative recombination with a photon recycling

FIGURE 1 Realization of ultra-high FF in c-Si solar cell. (a) PCE of notable high-performance silicon solar cells in relation to VOCand FF.

11 The blue and red solid lines are the FF–VOCcurves calculated by only considering the bulk intrinsic recombination and the surface J₀₁ recombination, and assuming a negligible series resistance (RS), where blue and red solid lines represent the 130-μm-thick n-type (1.5 Ω cm) wafer and 110-μm- thick undoped wafer, respectively. The areas colored by semitransparent blue/red represent the restricted region due to the bulk recombination limit. Blue dashed lines represent the FF–VOCcurves (corresponding to the blue solid line) taking different RSinto account. (b–e) The structure diagram (b), J–V curves with liner ordinate (c), J–V curves with logarithmic ordinate (d), and m–V curves (e) for the silicon solar cell with record FF labeled by yellow star in (a). The light J–V curve is shifted by JSCto obtain the “JSC-shifted light J–V” curve in (d), while the Suns-VOCcurve is shifted by +JSCto obtain the “JSC-shifted Suns–VOC” curve in (c). The inset in (d) is the equivalent circuit of the three diodes, while the three diagonal dashed lines at the bottom right represent the J–V curves' slope of those three diodes. The m–V curves were extracted from (d).

probability of 0.6 (n-type c-Si wafer, 130 μm, 1.5 Ω cm, and 110 μm, undoped c-Si), while the surface recombination is modeled by varying J₀₁. It shows clearly that the VOCvalue is strongly pro- moted by advanced surface passivation from PERC (green square) to TOPCon (blue square) and then to SHJ (red square) cells. A rapid pro- motion of FF is observed at a transition point where VOCexceeds 740 mV. For the LONGi's SHJ cells with VOCof around 750 mV, the FF rapidly changes from ~85% to 86.6% at a relatively small increase- ment of VOC. The data points of different high-performance silicon solar cell are located between the two blue dashed lines marked by R S= 0.2 Ω cm² and RS= 0.4 Ω cm², indicating they obeys the trend of “intrinsic recombination + surface recombination” curve but with R Sof 0.2–0.4 Ω cm².

Figure 1b–e displays the information of the cell with record FF

(yellow star in Figure 1a). As shown in Figure 1b, this n-type silicon solar cell featuring electron-selective contact of TCO/n-nc-SiOx:H/i- a-Si:H and hole-selective contact of TCO/(p-nc-Si:H)/i-a-Si:H, where TCO, n-nc-SiOx:H, p-nc-Si:H, and i-a-Si:H are transparent conducting oxide, n-type hydrogenated nanocrystalline silicon oxide, p-type hydrogenated nanocrystalline silicon, and intrinsic hydrogenated amorphous silicon, respectively. Three types of J–V curves¹⁴ are shown in Figure 1c–e, namely, J–V curves with linear y-axis (Figure 1c, usually describes the light J–V curve), J–V curves with loga- rithmic y-axis (Figure 1d, usually describes the dark J–V curve) and m- V curves (Figure 1e, derivative of the J–V curves in Figure 1d). In

Figure 1c, the blue solid line represents the light J–V curve acquired

from ISFH CalTech, in comparison to the Suns–VOCcurve (red solid line) obtained in our Lab. Inset table in Figure 1c summarizes the J–V

parameters derived from the above two curves. Series resistance effect is eliminated in Suns–VOCmeasurement and explains the high FF. As shown in Figure 1d, the J–V curves of tree diodes with m = 1, m = 2 and m = 2/3 (colored dotted lines marked by J₀₁, J₀₂, and J₀ 2/3) present different slopes, corresponding to the equivalent circuit in the inset. The actual J–V curve contains abovementioned information of tree diodes, which can be extracted by the slope of J–V curve.

Figure 1e shows the m–V curves, where m is calculated by the equa-

tion of m = 1/Vth(dV/dlnJ), representing the slope of J–V curves (Figure 1d) at difference voltage points. The curves of Suns–VOCand J SC-shifted light J–V basically follows the same trend for the voltage range below 740 mV. While the JSC-shifted light J–V curve has a slight upward warping once the voltage exceeds 740 mV. This discrepancy is believed to be related to the series resistance. In addition, near the V OCpoint, the m value is close to 2/3, indicating that the Auger recombination becomes dominant factor.

FIGURE 2

J₀₁ and J0 2/3. The J₀₁ ranges from 10 16

|J₀₁ and J|. The J₀₁ ranges from 10|A/cm², while the J||is fixed at 2.5|10 A/cm². The inset is the equivalent circuit of the|||
|---|---|---|---|---|---|---|---|
|double diodes. The intersections of the colored lines with the gray dashed line of 1 sun indicate the V||||||under different J₀₁. (b-e) The PV||
|parameters of single diode with J₀₁ (labeled by diode J₀₁) and double diodes with J₀₁ and J|||||(labeled by diodes J₀₁ + J||): (b) V or V|
|a function of J₀₁; (c) FF as a function of J₀₁; (d) at V of J₀₁; (e) FF as a function of V (short dotted lines) represent the actual situation given by the simplified recombination model (Section 6). The pie charts in d are the detail||or V|point, recombination percentage of diode J|||in diodes J₀₁ + J|as a function or diode J₀|
|recombination percentage of the record FF solar cell at V|||and V|points.||||

to 10 13 A/cm², while the J0 2/3

OC MPP OC Auger MPP OC

3 | EXPLANATION VIA A DOUBLE-DIODE MODEL WITH J₀₁ AND J02/3

A modified double-diode model is introduced to explain the “intrinsic recombination + surface recombination” curve in Figure 1a, where the diode J₀₁ and diode J₀2/3represent the surface recombination and intrinsic recombination, respectively. Similar to Figure 1d,

Figure 2a shows the J–V curves with logarithmic y-axis. According to

the evaluation of intrinsic recombination of the wafer (130 μm, n-type c-Si, 1.5 Ω cm), J0 2/3is set to 2.5 10 21 A/cm², and its J-V curve is

is fixed at 2.5 10 21 A/cm². The inset is the equivalent circuit of the OC 0 2/3 0 2/3 OC MPPas 0 2/3 0 2/3 0 bulk

Exploration of the underlying mechanism for ultra-high FF using a double-diode model. (a) The J–V curves of double-diodes with

. The yellow stars represent the solar cell with record FF, while the curves marked by diode J

given by the black dot-dashed line, while the J–V curves of diode J₀₁ (colored solid and extended dotted lines) are shifted from the bottom 16 right to the upper left (red arrow) with the increase of J₀₁ from 10 13 2 to 10 A/cm.The double diodes are set in parallel (inset) so that the total recombination current density equals to the sum of the intrinsic and surface components. Because the slope of J–V curve of diode J₀₁ is smaller than that of diode J0 2/3, the J₀₁ diode information only manifests within a certain range of voltages below a transition point, while this transition voltage (the dividing point dominated by diode J₀₁ and diode J0 2/3) is moving up from ~0.6 to >0.9 V with the growth of J₀₁ from 10 16 to 10 13 A/cm². As a consequence of increasing J₀₁, the information of J0 2/3diode within the voltage range of VMPP–VOC(VMPPis voltage at maximum power point) will gradually submerge under that of J₀₁ diode. FF basically obeys the curve rule of diode with J₀₁ (i.e., Green limit m = 1 in Figure 1a) when J₀₁ above 10 14 A/cm² and gradually transits to comply with Green limit m = 2/3 as J₀₁ is suppressed, especially when down to 10 16 A/cm². From the point of view of VOCand VMPP, above phenomenon of rapid increase in FF with the decline of J₀₁ can be better described in

Figure 2b–e. In terms of FF, the electrical component VMPP/VOCplays

a more important role than the optical component JMPP/JSC,and thus, the VMPPand VOCas a function of J₀₁ is presented in Figure 2b. For single diode J₀₁, the VMPP(or VOC) will increase linearly (dashed lines) with the decrease of J₀₁, leading to a similar trend of linear increase in FF (dashed line in Figure 2c). For diodes J₀₁ + J0 2/3, with the decrease of J₀₁, one can see the VMPP(or VOC) enters into a saturation voltage of ~695 mV (or ~760 mV) (limited by fixed J₀2/3). Because the changing point of VOCentering into the saturation range is prior to that of VMPP, that is, J₀₁ ~ 8 fA/cm² versus J₀₁ ~ 1 fA/cm² (solid lines in Figure 2d), leading to a rapid increase of FF during the decrease of J₀₁ of 10 14 –10 15 A/cm² (solid line in Figure 2c). Finally, according to Figure 2b and Figure 2c, the curves of FF as a function of VOCcan be plotted with canceling out the intermediate variable of J₀₁,as shown in Figure 2e. Therefore, with the continuous increase of VOC, embodying that the proportion of surface recombination significantly decreases and more intrinsic recombination information related to J₀ 2/3is revealed, FF therefor changes from original dashed line (diode J₀₁) to the dot-dashed line (diode J0 2/3). The solar cell with record FF is also marked by yellow stars in

Figure 2b–e, and the corresponding parameters have a little deviation

from the curves of diodes J₀₁ + J0 2/3. Obviously, using diode J0 2/3is too simple to describe the actual situation. In fact, the diode J₀2/3 should be replaced by recombination of silicon bulk (marked by diode J₀bulk) including Auger, radiative, and Shockley–Read–Hall (SRH) recombination, which will be discussed in the next section. While from the curves considering real recombination (dotted lines) marked by diodes J₀₁ + J₀bulk, those show similar trends as above situation of only considering diodes J₀₁ + J₀2/3. As show in Figure 2d, the per- centage of Auger recombination (marked as diode J₀Auger) in total recombination reached at 43% and 79% for VMPPand VOCpoints, indi- cating the FF surpass over 86% dominated by Auger recombination has appeared. It should mention that J0 2/3only correlates the infor- mation of J₀ with m = 2/3, a unique character of Auger recombination

TABLE 1 The formula of recombination rate (U) corresponding to

radiative, Auger, and Shockley–Read–Hall (SRH) recombination, where B, C, and Cn pare the coefficients of radiative recombination, electron Auger recombination, and hole Auger recombination, respectively. The n, n, and p are the concentration of intrinsic carrier,i electron, and hole, respectively. The τp0and τn0are the wafer-quality dependent hole and electron capture time constant, respectively. The n₁ (p₁) is the Shockley–Read factor for electrons (holes), which depends on the location of trap level and can be ignored when it closes to the E (i.e., defects of deep level). Δn and Ni Dare the excess carrier concentration and doping concentration of silicon bulk, respectively. The analysis of USRHat low (or high) injection is simplified under assumption of τn0¼ τp0¼ τSRHand deep level located trap.

UradUAugerUSRH 2 2 <u>np n</u>2 Formula Bnp C n p þ C npn p<u>ðÞi</u> τ p0 ðÞþ nþn1 τn0ðÞ pþp1 Low injection BNDΔn CnND2Δn τSRH <u>1</u>Δn (Δn ND) High injection B (Δn) 2 (C þ C) (Δn) 3 <u>1</u> Δn n p 2τSRH <u>(Δn ND)</u>

at high injection. However, in fact, the m and J₀ of real Auger recombi- nation will change along with the voltage, so using J0 Augerto repre- sent the calculated Auger recombination is more accuracy than J0 2/3. In general, J0 Augerincludes J01 Augerand J0 2/3 Auger, which will be dis- cussed in next part.

4 | CORRELATIONS BETWEEN RECOMBINATION AND DIODE MODEL

The diode model is strongly correlated with the recombination model. For the ideal silicon solar cell, the quasi-Fermi level across all regions in bulk is assumed as same, and thus, the implied VOC(iVOC, i.e., the difference between the two quasi-Fermi level for electrons and holes) equals to the applied voltage (more details are showed in Figure S1). According to the equation of Jrec.= UqWbulk, the characteristics of J–V curve in device is similar as that of U-iVOCcurve, where Jrec., U, q, and Wbulkare the recombination current density, recombination rate, electron charge, and the thickness of bulk, respectively. 15 Therefore, comprehension of the characteristics of U-iVOCcurves with variable recombination in bulk, and the contribution of U to the diode model of J₀₁, J₀₂, and J0 2/3contributes to interpretation of the characteris- tics of J–V curves in real devices. Formulas for recombination rate (i.e., Urad, UAuger, and USRH, respectively) of radiative recombination, Auger recombination, and Shockley–Read–Hall (SRH) recombination are listed in Table 1. In the formulas, n and p represent the carrier concentration of electron and hole, respectively. The difference in their product indicates different number of particles involved in a recombination process. For exam- ples, radiative recombination with U proportional to np associates a two-particle process, while Auger recombination with U proportional to n²p associates a three-particle process. The SRH recombination is

~ an intermediate-defect-state assisted two-particle process resulting in Δn ¼ n exp <u>iVOC</u> ð2Þ i 2V a formula more complex than the other two. To reveal subtle amongth the differences, the expressions of U are analyzed in separate situa- tions of low injection and high injection. Under low injection condi-Therefore, under high injection, the ideality factors corresponding tion, the excess carrier concentration (Δn) is much lower than the to radiative recombination, Auger recombination and SRH recombina- doping concentration (ND) of silicon bulk, that is, Δn ND. The high tion are 1, 2/3, and 2, respectively. In fact, from Equations (1) and (2), injection condition is vice versa. The corresponding variables and con-the Δn increases exponentially with the growth of iVOC, for ideality stants are expressed in red and black fonts, respectively. Under low factor m = 1 at low injection, and ideality factor m = 2 at high injec- injection, the recombination rate U follows the change of Δn linearly tion. The physical meaning is related to the relationship between the for all recombination processes (the second row in Table 1). The Δn movement of the quasi-Fermi level and iVOC(Figure S2). The change and iVOCdependence satisfies the following equation at low injection. of iVOCalmost completely acts on the movement of minority carrier quasi-Fermi levels at low injection, while the movement values of the 2~ <u>n</u> <u>iiVOC</u> two quasi-Fermi levels are same and occupy half of the change of Δn ¼ exp ð1Þ ND1Vth iVOCat high injection.

Figure 3a–c shows the U-iVOCcurves of three types of recombi-

which means the ideality factor for all recombination rates is 1 (i.-nation at different bulk doping concentrations (ND). By extracting the

e., m = 1) at low injection, where ni,iVOC, and Vthare intrinsic carrier slope of the U-iVOCcurves in logarithmic y-axis, one can get the m- concentration (silicon bulk), implied VOC, and thermal voltage, iVOCcurves (Figure 3d–f) as well as the color diagrams of the m as a respectively. function of NDand iVOC(Figure 3g–i). As shown in Figure 3a,b, the Under high injection, the recombination rate U follows the change low/high injection region can be well distinguished from the slope of Δn to the second, third, and first power depending on the recombi-change of U-iVOCcurves. For SRH or Auger recombination, at low nation process. Considering high injection, Δn is the exponential injection, the curve slope is m = 1 (marked as J₀₁SRHor J₀₁Auger), increase function of iVOCwith an ideality factor of 2, that is,
while at high injection, the slope is m = 2(J02 SRH)orm = 2/3 (J0 2/3

FIGURE 3 Recombination analysis. Recombination rate (U)(a–c) and ideality factor (m)(d–f) as a function of iVOCwith different ND. (g-i) The

color diagrams of m as a function of NDand iVOC, corresponding to SRH recombination, Auger recombination, and SRH + Auger recombination, from left to right. The lifetime of SRH recombination (τSRH) and the thickness of wafer (Wbulk) are separately set as 7 ms and 130 μm. The one-sun line (black dotted line) is calculated by JSC/qWbulk, where the JSCis set as 43.36 mA/cm². The formulas indicated in (g) and (h) are that for calculating the recombination of J₀ in a and b. The radiative recombination (Figure S3) shows negligible influence on the final trend of recombination.

Auger). And the transition region in iVOCof low/high injection increase changes from J01 SRHto J01 Augerwhen the NDincreases. This explains from ~0.3 to ~0.8 V with the growth of NDfrom 10 13 to 10 17 cm 3, why the combined U decreases first with higher NDbut turns around consistent with the definition of low/high injection in Table 1. This up when NDincreases further (black arrow). The figure of m-iVOCmay transition region can also be well observed in m-iVOCcurves help us distinguish the dominant recombination at different injection (in Figure 3d,e), that is, the region where m changed from 1 to 2 (from levels. As shown in Figure 3f, with low ND, such as 10 13 cm 3, the 1 to 2/3) for SRH (Auger) recombination. As J₀₁SRH/ 1/NDand dominated recombination current density is shifted from J₀₁SRH J₀₁Auger/ ND(the formula showed in Figure 3g,h), the J₀₁SRHand (m = 1) to J₀₂SRH(m = 2) and finally to J₀2/3 Auger(m = 2/3). At J 01 Augershowed opposite changes with the increase of ND(direction higher NDup to 10 17 cm 3, the corresponding m-iVOCcurve is basi- of black arrows). On the other hand, Figure 3g,h shows that J₀₂SRHcally consistent with that of Auger recombination. and J0 2/3 Augeris independent of ND(labeled as the SRH limited line The color diagrams of the m are shown in Figure 3g,h. For exam- and Auger limited line), representing an upper limit of SRH recombina-ple, in SRH (or Auger) recombination, the green region represents the tion and a lower limit of Auger recombination, respectively. According J₀₁ region of SRH (or Auger) recombination, that is, the low injection to the formula of J02 SRHand J0 2/3 Augerinserted in Figure 3g,h, the region, while the red (or blue) region represents the J₀₂ (or J₀2/3) upper limit of SRH is determined by τSRHand the thickness of bulk region of SRH (or Auger) recombination, that is, the high injection (Wbulk), while the lower limit of Auger is only determined by Wbulk.As region. In Figure 3i, the regions dominated by SRH recombination and shown in Figure 3c, when SRH and Auger are combined together, the Auger recombination can be quickly distinguished (the boundary is U-iVOCcurves become more complex. The dominant recombination labeled by white dashed line). Due to the negligible effect of radiation

FIGURE 4 Bulk recombination. (a) The J–V curves with four different lifetimes τSRHof the silicon wafers, where the different color lines are

with different doping concentration (same as Figure 3c). The intersection point of J-V curve and 1 sun line (black dotted line) is the corresponding V OC. The red star represents its maximum power point (MPP), which is calculated by assuming a JSCof 43.36 mA/cm². The red and blue dashed lines represent the SRH and auger limited lines (similar as that in Figure 3a,b), respectively. (b) The color diagrams of ideality factor (m)asa function of doping concentration (ND) and voltage at τSRHof 1, 5 10, and 20 ms. the black dotted line and black solid line represent the VMPPand V OC, respectively. (c) The PCE and FF as a function of NDfor the four different τSRH.

recombination, the models of “Auger + radiative recombination” and “SRH + Auger + radiative recombination” are only presented in Figure S3 as supplements. Meanwhile, three-dimensional diagrams of above recombination containing more details are presented in Figure S4.

5 | QUANTIFICATION OF BULK AND SURFACE RECOMBINATION

Four kinds of wafers with different τSRHacross a wide range from 1 to 20 ms were set to investigate the influence of wafer quality on solar cell performance. Figure 4a,b shows the J–V curves (assuming a JSCof

43.36 mA/cm²) and the color diagrams of m as a function of V and ND, respectively. The maximum power point (MPP) and VOCare marked. One can readily perceive the impact of SRH recombination on MPP and VOCpoint. For example, when τSRH= 1 ms, the SRH lim- ited line (red dotted line) is above the MPP in Figure 4a, and VMPPline is basically covered by red color representing SRH recombination with m = ~2 in Figure 4b. As such, the VMPPpoint is more affected by the SRH recombination. With the increase of τSRH, the influence of SRH recombination on cell performance will be less pronounced, which is reflected by the downward moving of SRH limited line in Figure 4a, and the shrinking of SRH dominated region (red region) in Figure 4b. When τSRHsurpasses 20 ms, the VMPPline is basically covered by blue color. The J–V curve ranging from VMPP-VOCis dominated by intrinsic recombination and FF approaches the theoretical limit. The increase of FF can also be reflected by the decreased span between VMPPline and VOCline in Figure 4b, from 97.8 to 68 mV, similar as that in
Figure 2b.

Figure 4c shows the PCE and FF as a function of NDunder the
 four different τSRH(and the gray lines represent the situation with only considering intrinsic recombination, i.e., τSRH= ∞). A perfect sur- face passivation and a fixed JSCof 43.36 mA/cm² is assumed here. The PCE trending complies with that of FF, indicating that FF is the primary factor for PCE improvement when perfect surface passivation can be obtained. For a good quality wafer (τSRH⩾ 5 ms), with the increase of ND, the PCE and FF are independent of NDat first and then deteriorate rapidly at a NDhigher than 10
15 cm 3 where Auger recombination takes over. For a poor quality wafer (τSRH= 1 ms), with the growth of ND, the PCE and FF also maintain a stable value at first, but followed by a rapid ramp up and down. The MPP point is primarily affected by J₀₂SRH(independent of ND) at low ND, and then by J₀₁SRH(/ 1/ND) with at higher ND, especially ND⩾ 5 10 15 cm 3, and finally by J₀₁Auger(/ ND). This leads to a practical guideline for solar cell fabrication on unsatisfactorily controlled wafer quality, in which scenario appropriately increasing the doping concentration of silicon wafers can help to obtain a higher PCE in more steady production. The surface recombination velocity (S) describes the recombina- tion severity of electron and hole at surface. The surface recombination rate (Us) is defined as

Us¼ S Δnsð3Þ

where Δnsdenotes excess carrier concentration at surface. We reveal here that surface field passivation plays a critical role in surface recombination due to its impact on surface excess carrier concentra- tion. In the absence of a field, known as flat band state, the excess carrier concentration in the bulk is equal to that at the surface (i.e., Δn = Δns). In the presence of a field, a band bending forms in sur- face region making Δn≠Δns.

Figure 5 shows the analysis of surface recombination under field

passivation. The classic p + n junction is taken as an example here, while the field caused by the surface charge or the heterojunction with doped layer should have similar properties.

Figure 5a,b shows the schematic diagram of the band structure

with two types of surface field (strong and weak) under the equilib- rium state and nonequilibrium state, respectively. The φs0represents the barrier height of the surface, which is dependent on the doping concentration of the doped layer (NA+) and silicon bulk (ND). It can be expressed as

~ ! p s0<u>NAþ</u> φ s0¼ βln ¼ βln2ð4Þ p₀ n i =ND

where β = kT/q, with the Boltzmann constant k, the absolute temper- ature T, and the electron charge q. A linear dependence of φs0on ln (NA+) is thus revealed here. With the increase of iVOC, as shown in

Figure 5a,b (right panels), the surface field φswill decrease. It satisfies

φs= φs0-iVOCat low injection (Δn ND) and φs= (φs0-iVOC)/2 at high injection ( Δn ND) (Figure S5). Because of high φs0(high NA+;

Figure 5a), it can keep low injection (Δns< NA+) at surface, making the

surface recombination dominated by J₀₁ (marked as J₀₁surf)at the range below VOC. For low NA+at surface, weak bend banding of φs0(Figure 5b) is formed and makes the surface to quickly enter the high injection (Δns> NA), mainly leading to the surface recombination J₀₂ (J₀₂surf). At the edge of the p–n junction, low NA+can be easily formed, which endows the edge a main source of J₀₂surf (Figure S6).

Figure 5c shows the surface recombination rate (Us/Wbulk)asa

function of iVOC. The formula for calculating the surface recombina- tion rate (Us)is

ð E C U ¼ n p n² <u>ν</u> <u>thDitðÞ E dE</u> ð5Þ s s s i σ1ðÞ E ½þ n þ n ðÞ E σ1ðÞ E ½ p þ p ðÞ E E V p s 1 n s 1

It assumes that the defects are mainly concentrated in deep level. The n₁ and p₁ are small values, the surface defect density of states Dit= Nit(E Et), where Nitis the surface density at local energy level. The nsand psare the electron and hole concentrations at the surface. The σp, σn, and νthare the hole capture cross section, electron capture cross section, and thermal velocity. E is the energy relative to the intrinsic energy. The corresponding formula (5) can be simplified as

FIGURE 5 Surface recombination. (a,b) The schematic band structure diagrams of forming the surface recombination J₀₁ (J01 surf) and surface

recombination J₀₂ (J02 surf) in the cases of strong field passivation (a, high NA+) and weak field passivation (b, low NA+), respectively. The band structure diagrams include the situation under the equilibrium state (left) and nonequilibrium state (right). Here, NA+represents an effective p-type doping concentration at bulk surface, which can be formed by p+-doped layer, surface negative charge, and the heterojunction with p +-doped layer, while NDis the doping concentration of bulk. Sitrepresents the surface recombination caused by defects. The φs0and φsare the surface barrier heights under equilibrium and nonequilibrium states, respectively. Δnsand Δn are excess carrier concentrations at the surface and in the bulk, respectively. EC, EV, EFn, and EFpdenote conduction band energy, valance band energy, electron quasi-Fermi level, and hole quasi- Fermi level, respectively. (c) The recombination rate from surface (US/Wbulk) as a function of iVOCunder different NA+(representing the field passivation). The situations of low NA+and high NA+present J₀₂ and J₀₁ dominated information, respectively, at VMPP-VOCrange. (d) The effective surface recombination velocity (Seff) as a function of Δn under different NA+. Here, the surface recombination is introduced on the surface of the p+ layer, while Seffrepresents the recombination rate caused by the surface defects with different field passivation. We set S it= 1 cm/s as the case of chemical passivation (under flat band). The bulk silicon is n-type with an NDof 3 10 15 cm 3.

<u>s s i</u>

|||U ≈ n p|n²||ð6Þ|and the|curves dominated|by J₀₁|at V –V|range when|N|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||S n|þ S p|||>3 10 W –iV|cm (yellow line). In addition, under high injection, U / curves will also fall into a line with m = 2, and the curves|||||
|The S|and S are the hole and electron surface recombination|||||will be|dominated|by J₀₂ at|V –V|range when|N|
|velocities, where S|¼ υ|σ N, S ¼ υ|σ N.|||<3 10|cm (bright blue line).|||||
|It should be noted that the unit of U|||is cm|s ,soifU|is com-|To compare with the recombination in bulk, it is preferred to||||||
|pared with the previous recombination rate from bulk (like U|||||or|convert Δn|in Equation|(3)toΔn.|From|the definition|of|
|U), it needs to be divided by the wafer thickness of W|||||, that is,|S Δn = S|Δn, and|the assumption of|n p = np|(i.e., the quasi-||
|U /W. Same as the SRH recombination in bulk (Figure 3a), at low||||||Femi level keeps same at||the surface and in bulk,||and the|n and|
|injection|(Δn N),|the ideality|factor|of m|= 1 and|p are the carrier concentration of electron and hole in bulk, while||||||
|J ¼ n²|=N qS, while at high injection (Δn|||N), m = 2, and||n and p|are those|at surface),|the following|equation|can be|
|J₀₂ = n|qS. The U /W|will decrease with the growth of N|||,|deduced.||||||

MPP OC A s 1 1 p0 s n0 s 17 3 + s bulk OC p0 n0 MPP OC A p01 th p it n01 th n it + 14 3

s 2 1 s Auger s SRH bulk s eff s s s bulk Aþ 01 surf i Aþ Aþ s s surf i s bulk A+

TABLE 2 Summary of the source of J₀₁, J₀₂, and J0 2/3. The situation of the parameters under low (or high) injection was labeled as_li.(or_hi.)

at the subscript, such as J0 Auger_hi.(instead of the J0 2/3 Augerabove). R and J₀ represent the amount of recombination and the reverse saturation current density, respectively. W and N are the thickness and doping concentration of different layers, respectively.

Ideality R factor (m) Rec. type Rec. formula Rec. area J0m <u>pn</u> 3=22/3 Auger Rec. in high injection R ≈ C þ C W Δn³ Bulk J0 Auger_hi:¼ qn³iWbulkðÞ Cnþ Cp ≈ R02=3 n 2Auger_hi: n p bulk i

|2=2 1 pn ≈ R₀₁ 2 n i|Radiative Rec. (band to band)|R ≈ BW pn Bulk rad bulk J|
|---|---|---|
||Auger Rec. in low injection|p+ ≈ C N W pn R J Aþ pþ Auger_li:pþ p n+ R ≈ C N W pn J Dþ nþ Auger_li:nþ n Bulk (p) R ≈ C N W pn J A Auger_li:p bulk p Bulk (n) R ≈ C N W pn J D Auger_li:n bulk n|
||SRH Rec. in low injection Surface Rec. (surface SRH rec., complex)|W Bulk(p) R ≈ pn SRH_li:p J τ N nbulk A W bulk Bulk (n) R ≈ pn SRH_li:n J τ N p D pn Surface J R ≈ S Δn;or ≈ J surf 0 surf 2 qn i J|

0 rad¼ qBn²Wbulk i

0 Auger_li:pþ¼ qCpNAþn²i eff ðÞWpþ 0 Auger_li:nþ¼ qCnNDþn²i eff ðÞWnþ 0 Auger_li:p¼ qCpNAn²iWbulk 0 Auger_li:n¼ qCnNDn²iWbulk

0 SRH_li:p¼ qn2iWbulk τ n N A 0 SRH_li:n¼ qnτ2iW N bulk p D <u>n²</u> i 0 surf_li:pþ¼ qSn N 2 A; 0 surf_li:nþ¼ qSp N <u>n</u> <u>i</u> D ;orJ0E <u>pn</u> 1=22 SRH Rec. in high injection R SRH_hi:¼ Wbulk Δn Bulk J0 SRH_hi:¼ <u>qni Wbulk</u> ≈ R₀₂ n 2τnþτp τnþτp i 2 SRH Rec. at depletion region R ≈ Ð ðÞ <u>nx ðÞpx ðÞni</u> dx Depletion ≈ J01:85 DR DR τp0nx ðÞþτn0px ðÞ region SRH Rec. at edge region Rsurf≈ S Δn;or Edge of p-n J0 surf_hi:¼ qSni 1=2junction ≈ J0 surf qpn 2 n 2 <u>i</u>

<u>np ðÞ NDþ Δn</u> surface recombination returns to the field-absent-case, that is, Δns≈ ≈ Δn ð7Þ p sðÞ NAþþ Δns

0.5 cm/s here. In general, the relationship between the Seffand Δn is complex as
and shown in Figure 5d. However, because the surface recombination can also be classified as SRH recombination, the Us/Wbulkas a function of <u>ðÞ NDþ Δn</u> iV OCis similar as Figure 3a. When the field is sufficiently strong, such S eff≈ S ð8Þ ðÞ NAþþ Δns as N >3 10 18 cm 3, for S = 1 cm/s, the corresponding J–V rela- A+ tionship in the range of VMPP–VOCcan be described as the diode <u>n²</u> <u>i</u> þ where NA+and NDare the effective doping concentration at surface equation of J₀₁, that is, J01 surf¼N Aþ qS (for p n junction). When the and doping concentration in bulk, respectively. Here, S represents the field is weak, such as NA+<3 10 14 cm 3, for S = 1 cm/s, the corre- S itin Figure 5. sponding J–V relationship in the range of VMPP–VOCcan be described

Figure 5d shows the Seffas a function of Δn (defined by Equa-as the diode equation of J₀₂, that is, J02 surf¼ niqS (for pþn junction).

tion 8), where NA+changes from 10 13 to 10 19 cm 3, while NDand Table 2 summarizes the formulas for the abovementioned recom- S are set as 3 10 15 cm 3 and 1 cm/s, respectively. When NA+= NDbination processes in separate high and low injections. The spatial dis- (green line), similar as the situation without surface field (i.e., flat tribution of J₀₁, J₀₂, and J₀2/3in silicon solar cell is displayed in band), there are Seff= 1 cm/s at low injection and Seff= 0.5 cm/s at Figure 6. The expressions of the recombination saturation current high injection. This is consistent with the general law of SRH recombi-density (J0m, m is the ideality factor) are also defined. For example, nation. When NA+< ND, the Seffappears even above the original S at when m = 2/3, the recombination current density is only related to low injection (Δn ND). For the case of sufficiently high surface dop-the high injection of Auger recombination, the relationship with Δn is ing, that is, NA+> ND, it is divided into three stages. In the first stage, the third power, and the reverse saturation current J0 Auger_hi(i.e., J₀ at Δn ND, the Seff= (ND/NA+)S relationship is established, where2/3 Auger) is proportional to the thickness of silicon wafer (Wbulk). In S effbasically maintains a fixed value with the change of Δn and other words, a thinner silicon wafer can effectively reduce the influ- decreases with the increase of NA+, indicating that a larger field leads ence of Auger recombination from bulk on cell PCE. For m = 1, almost to a smaller surface recombination rate. In the second stage of all the recombination is linked to low injection. While J₀₂ recombina- NDΔn NAþ, the Seff= [(ND+ Δn)/NA+]S relationship is estab-tion current density mainly comes from the SRH recombination of lished, indicating that the Seffincreases with Δn. In the third stage, at bulk silicon at high injection (especially in the wafer with low ND), Δn NAþ, the surface field of φsis almost equal to 0, and thus, the depletion regions and edge regions (more details are showed in

FIGURE 6 The distribution of J₀₁, J₀₂, and J0 2/3in silicon solar cell.

FIGURE 7 Fitting of J–V curves by the triple-diode equivalent model and our simplified recombination model. (a) Triple-diode model. It

utilizes J₀₁, J₀₂, and J0 2/3diodes to fit the experimental J–V curves extracted by Suns–VOC(green circle). The red color lines are the fitting curves.

(b) Simplified recombination model. It utilizes the equations of intrinsic, SRH, and surface recombination to fit the J–V curves extracted by Suns– V OC(green circle) and the RSequation to fit the light J–V curves (blue triangle), where the J–V curves include three forms of expression, that is, light J–V curve (with liner y-axis), illumination–voltage curve (as dark J–V curves with logarithmic y-axis), and m–V curve. The “intrinsic,”“+SRH,” “+J0 surf,” and “+RS” mean that the J–V curves adding intrinsic recombination (including Auger recombination and radiative recombination with photon recycling), SRH recombination, surface recombination (J0 surf, including J01 surfand J02 surf), and series resistance (RS) equations one by one.

||Recombination|J₀₁ (A/cm²)|J₀₂ (A/cm²)|J (A/cm²)|TABLE 3|The calculated parameters|
|---|---|---|---|---|---|---|
||||||of J₀₁, J₀₂, and J|according to the|
|Bulk|Radiative Auger|3.02 10 7.11 10||2.7 10|fitting parameters in Figure 7b and the formulas in Table 2.||
||SRH|3.78 10|6.98 10||||
|J|SRH|1.15 10|||||

0 2/3 0 2/3

01 surf

Figure S6). Based on above partitioning and simplified formula, one can quickly calculate the general current equation through the recom- bination current equation with J₀₁, J₀₂, and J0 2/3.

6 | APPLICATIONS OF THE TRIPLE-DIODE EQUIVALENT MODEL AND SIMPLIFIED RECOMBINATION MODEL IN J-V CURVE ANALYSIS

The experimental J–V curve can be fitted through a triple-diodes equivalent circuit with J₀₁, J₀₂, and J0 2/3(Figure 7a), as well as by the simplified recombination model (Figure 7b). The upper panels in

Figure 7a,b show the corresponding equivalent circuits. The triple-

diode model uses only three parameters of J₀₁, J₀₂, and J₀2/3to describe the recombination and corresponding performance of solar cell. The simplified recombination model can not only distinguish the sources and types of recombination but also distinguish the recombi- nation from intrinsic recombination, bulk SRH recombination, and sur- face recombination (J₀₁surfand J₀₂surf, here, J₀₂surfis negligible) equations in sequence. Similar as the Figure 1c–e, three typical J–V curves, that is, light J–V curve (similar as the J–V curves with liner ordinate in Figure 1c), illumination–voltage curve (i.e., Suns–VOC curve, similar as the J–V curves with logarithmic ordinate in Figure 1d, where J=JSCSuns), and ideality factor–voltage (m–V) curve, are taken for evaluation on the effectiveness of these two modes. The blue triangle and green circle represent the experimental data of light J–V curve and Suns–VOCcurve, respectively, while the red solid line is the fitted line of recombination current density (Jrec:) calculated by the equation of

X ≥ ~ <u>V</u> J rec:¼ J0mexp 1 ð9Þ m¼1, 2, 2=3 m VT

for triple-diode model, and

X ~ <u>V</u> J rec:¼ ðÞ UAugerþ Uradþ USRHqWbulkþ J0m surf:exp 1 m¼1, 2 m VT ð10Þ

for simplified recombination model. To fulfill our simplified recombination model, the fitting process must follow the subsequent steps. Firstly, upon the already known silicon wafer characteristics, such as doping concentration, thick- ness, and quality (i.e., τSRH), the corresponding recombination for- mula (or Table 2) is employed to calculate the respective J–V curve related to bulk recombination. Then, the experimental lines of illumination-voltage and ideality factor-voltage data are fitted through adjusting J₀₁ and J₀₂ (see bottom right panels in Figure 7a,b). At last, the experimental light J–V curves are fitted through adjusting Rs.It should be noted that, in simplified recombination model, the set of sil- icon wafer quality will directly impact the J₀₁ (or J₀₂) ratio between the surface recombination and bulk recombination, so the silicon

wafer quality should be assessed by separate passivation test if necessary. The fitting J–V curve (gray solid line) in Figure 7b contains the Auger recombination (by Black and Macdonald¹²) and the radiative recombination with a photon recycling of ~0.6, while USRHis accord- ing to equation in Table 1. From the comparison between the three J– V curves, one can see that both methods are quite effective in fitting the experimental curve. In fact, according to the description in Table 2, though the m of bulk recombination will change with injec- tion, the J₀ at low/high injection can still be calculated (Table 3). From the triple-diode model, J₀₁, J₀₂, and J₀2/3are 2.3 fA cm 2,

5.5 10 10 A cm
2, and 2.73 10 21 A cm 2, respectively, which are nearly equal to the results of that in Table 3 (simplified recombination model), that is, J₀₁rad+ J₀₁Auger+ J₀₁surf= 2.27 fA/cm², J 02 SRH= 7.0 10 10 A cm 2, and J0 2/3 Auger= 2.73 10 21 A cm 2, indicating the equivalence of the two methods. Uniquely, the latter can better quantify various type of recombination, especially when the information of silicon bulk are measurable, which is very suitable for process development and loss analysis for solar cells.

7 | FORECASTING THE IMPLIED FF (IFF) OF SILICON SOLAR CELLS VIA SIMPLIFIED RECOMBINATION MODEL

At a condition of low edge recombination and depletion region recombination (Figure S6), the main sources of J₀₂ can be basically ignored here, and the FF and VOCwill be mainly affected by J₀₁surf and τSRH. Figure 8 shows the iVOCor iFF as the function of τSRHand J₀₁surf. The corresponding fitting conditions are shown in the upper left corner in Figure 8a. It can be clearly seen that, after setting the parameters of silicon wafers and the photocurrent (J) along with L, the decrease of J01 surfand the increase of τSRH, the iVOCincrease will slow down, especially when 746 mV is reached. This indicates that the intrinsic recombination is gradually playing a dominant role. At this time, the promotion of iFF will become as a main driving force for effi- ciency growth. In the range of τ < 10 ms and J < 1 fA/cm, 2 SRH 01 surf iFF ramps up significantly with the increase of τSRH, but not J₀₁surf. The bulk SRH recombination become the main source of recombina- tion at this time. As the τSRH> 20 ms and J01 surf> 1 fA/cm², the sur- face recombination will become the main source of recombination. For our SHJ solar cells, 11 the corresponding total J₀₁surfcan be suppressed down to 2 fA/cm², and even to below 1 fA/cm² in excel- lent cases. In this case, wafer quality will undoubtedly have a great effect on the cell efficiency. In addition, it can be seen from the figure that if the corresponding iVOCand iFF can be tested, the wafer quality and surface passivation quality corresponding to the cells can be roughly estimated (any additional J₀₂ information ignored here can be contained in τSRH). The parameters of the 26.3%-PCE SHJ solar cell showed in Figure 1 are marked in Figure 8 by yellow star, where the corresponding J₀₁ and τSRHare attained by fitting the corresponding J–V curves. Obviously, if J01 surf< 0.8 fA/cm², and τSRHcan be raised to >30 ms, its iFF will exceed 88%.

≥

|FIGURE 8|Forecasts on the iV|and iFF of silicon solar cells. (a) The iV|and J||
|---|---|---|---|---|
|and J R is Ω cm²) according to the ref., and shunt influence, while iFF is implied FF, which only consider the recombination effect.|. The red star represents the 86.59%-FF solar cell in Figure 1b–e. The real FF = pFF|and pFF ≈ iFF when shunt resistance is high enough. The pFF is pseudo FF, which consider the recombination|ΔFF, where ΔFF ≈ R|cm) (unit of|

OC OCas a function of τSRH 01 surf. (b) The iFF as a function of τSRH 1 2 01 surf S5(%Ω 16 S

It is noted that the abovementioned iFF only consider the recom- bination effect. In fact, the practical FF should also need to consider the influence of series resistance (RS) and shunt resistance (RSh)of solar cells. If RShis high enough, pFF ≈ iFF, where pFF is pseudo FF in which the influence from both recombination and RShare considered. According to the relationship of ΔFF ≈ RS5% (unit of RSis Ω cm²), 15 the practical FF can be deduced from pFF. For example, the

26.30% efficient cell demonstrates a series resistance of ~0.2 Ω cm², where accordingly its FF can be calculated as pFF-ΔFF ≈ 87.41%
0.2 5% = 86.41%. The calculated value is consistent with the mea- sured value in decent accuracy. Further reduction on SRH recombination to increase τSRHturns to be an effective means to further improve iFF. If keeping the same R S, through improving τSRHto 30 ms and reducing J₀₁surfto
0.8 fA/cm², FF can approach 87.4% (88.4% 0.2 5%). Further improving τSRHto 90 ms and reducing J₀₁surfto 0.7 fA/cm², FF can approach 88.0% (89.0% 0.2 5%).
can be completely reproduced. Furthermore, the relationship between ideality factor and specific recombination process is established. For surface recombination with a strong field, the J–V curves show the characteristics of J₀₁ diode. It is also revealed that J₀₂ mainly comes from the depletion region and the edge region of p–n junction. Then we discriminated the recombination current density of J₀ in specific regions and established the relation between triple-diode model and our simplified recombination mode. Both models were compared to fit measured J–V curves, and their equivalence was demonstrated. Finally, we show that continuous improving bulk quality (τSRH) and surface recombination (J₀₁) will lead to further promotion of FF. The estimated FF can approach 88.0% when τSRH≥90 ms, J 01 surf≤ 0.7 fA/cm², and RS≤ 0.2 Ω cm².

ACKNOWLEDGMENTS This work was financially supported by the National Key Research and Development Program of China (2022YFB4200203) and the National Natural Science Foundation of China (62034009, 62104268), Shenzhen Fundamental Research Program (JCYJ20200109142425294), and Guangdong Basic and Applied Basic Research Foundation (2019B151502053).

CONFLICT OF INTEREST STATEMENT The authors declare no competing interests.

DATA AVAILABILITY STATEMENT The data that support the findings of this study are available from the corresponding author upon reasonable request.

### 8 | CONCLUSION

Thanks to the advances in silicon PV technologies in passivation and resistance reduction, record filling factor of silicon solar cells has reached 86.6%. The corresponding light J–V curve showed an average ideality factor less than 1 between MPP and open-circuit conditions. By using a double-diode model with J0 2/3and J₀₁, representing intrin- sic recombination and surface recombination, the process occurring in the rapid increments of FF with J₀₁ reduction experimentally observed

REFERENCES

1. Cuevas A, Macdonald D. Measuring and interpreting the lifetime of silicon wafers. Solar Energy. 2004;76(1-3):255-262. doi:10.1016/j. solener.2003.07.033
2. Brendel R, Peibst R. Contact selectivity and efficiency in crystalline silicon photovoltaics. IEEE J Photovolt. 2016;6(6):1413-1420. doi:10. 1109/JPHOTOV.2016.2598267
3. Brendel R., Riencker M., Peibst R. A quantitative measure for the car- rier selectivity of contacts to solar cells.32nd European Photovoltaic Solar Energy Conference & Exhibition. 2016.
4. Chan DSH, Phang JCH. Analytical methods for the extraction of solar-cell single- and double-diode model parameters from I-V charac- teristics. IEEE Trans Electron Devices. 1987;34(2):286-293. doi:10. 1109/T-ED.1987.22920
5. [http://www.griddlersolar.com](http://www.griddlersolar.com)
6. Macdonald DH. Recombination and Trapping in Multicrystalline Silicon Solar Cells. Australian National University; 2001.
7. Richter A, Hermle M, Glunz SW. Reassessment of the limiting effi- ciency for crystalline silicon solar cells. IEEE J Photovolt. 2013;3(4): 1184-1191. doi:10.1109/JPHOTOV.2013.2270351
8. Razzap A, Allen T, Wolf A. Design criteria for silicon solar cells with fill factors approaching the Auger limit. ACS Energy Lett. 2023;8(10): 4438-4440. doi:10.1021/acsenergylett.3c01519
9. Green MA. Solar cell fill factors: general graph and empirical expres- sions. Solid-State Electron. 1981;24(8):788-789. doi:10.1016/0038- 1101(81)90062-9
10. Allen TG, Bullock J, Yang X, Javey A, Wolf SD. Passivating contacts for crystalline silicon solar cells. Nat Energy. 2019;4(11):914-
928. doi:10.1038/s41560-019-0463-6
11. Lin H, Yang M, Ru X, et al. Silicon heterojunction solar cells with up to
26.81% efficiency achieved by electrically optimized nanocrystalline-
silicon hole contact layers. Nat Energy. 2023;8(8):789-799. doi:10. 1038/s41560-023-01255-2

12. Black LE, Macdonald DH. On the quantification of Auger recombina- tion in crystalline silicon. Solar Energy Mater Solar Cells. 2022;234: 111428. doi:10.1016/j.solmat.2021.111428
13. Richter A, Werner F, Cuevas A, Schmidt J, Glunz SW. Improved quan- titative description of Auger recombination in crystalline silicon. Phys Rev B. 2012;86(16):165202. doi:10.1103/PhysRevB.86.165202
14. McIntosh, K.R. Lumps, humps and bumps: three detrimental effects in the current-voltage curve of silicon solar cells. University of New South Wales (2001).
15. Cuevas A. The recombination parameter J0. Energy Procedia. 2014; 55:53-62. doi:10.1016/j.egypro.2014.08.073
16. Pysch D, Mette A, Glunz SW. A review and comparison of different methods to determine the series resistance of solar cells. Solar Energy Mater Solar Cells. 2007;91(18):1698-1706. doi:10.1016/j.solmat.
2007.05.026
SUPPORTING INFORMATION Additional supporting information can be found online in the Support- ing Information section at the end of this article.

How to cite this article: Lin H, Wang G, Su Q, et al. Unveiling the mechanism of attaining high fill factor in silicon solar cells. Prog Photovolt Res Appl. 2024;32(6):359‐371. doi:10.1002/pip. 3775
