Solar Energy Vol. 44, No. 5. pp. 271-289, 1990
Printed in the U.S.A.
MODELING DAYLIGHT AVAILABILITY AND IRRADIANCE
COMPONENTS FROM DIRECT AND GLOBAL IRRADIANCE
RICHARD PEREZ, PIERRE INEICHEN, ROBERT SEALS,
JOSEPH MICHALSKY, and RONALD STEWART
Atmospheric Sciences Research Center, State University of New York at Albany,
Albany, NY 12205, U.S.A.
Abstract--This paper presents the latest versions of several models developed by the authors to predict short
time-step solar energy and daylight availability quantities needed by energy system modelers or building
_ designers. The modeled quantities are global, direct and diffuse daylight illuminance, diffuse irradiance and
illuminance impinging on tilted surfaces of arbitrary orientation, sky zenith luminance and sky luminance
angular distribution. All models are original except for the last one which is extrapolated from current
standards. All models share a common operating structure and a common set of input data: Hourly (or
higher frequency) direct (or diffuse) and global irradiance plus surface dew point temperature. Key exper-
imental observations leading to model development are briefly reviewed. Comprehensive validation results
are presented. Model accuracy, assessed in terms of root-mean-square and mean bias errors, is analyzed
0038-092X/90 $3.00 + .00
Copyright © 1990 Pergamon Press pic
both as a function of insolation conditions and site climatic environment.
1. INTRODUCTION
Specific solar, HVAC, or daylighting applications re-
quire specific solar radiation components for simula-
tion or monitoring purposes. For instance, the simu-
lation of daylight distribution in complex interior
spaces, which is now possible thanks to new software
development (e.g., {1]), requires an accurate knowledge
of the distribution of light in the sky. Because these
specific components are many and are often too ex-
pensive to measure on a routine basis, one has to rely
on conversion models that use more routinely acces-
sible data.
We present in this paper a series of extensively val-
of such components and contribute to bridging
are (i) the preparation of local climatological data bases
for direct use by interested engineering parties—this
is currently being done for several locations in the State
of New York[2]—and (ii) the modification of the ra-
diation processing algorithms of specific system sim-
ulation programs (e.g., [3]). The models are the result
of a three year development/validation study per-
formed on experimental data recorded at 10 American
and three European sites. Climates and environments
range from high altitude desert to temperate maritime,
including humid continental, subtropical and highly
polluted environments.
Although the models’ end-use fields may be very
different, their common input and structure calls for
this single unifying paper. This may contribute to pre-
senting solar resource assessment as a global question
rather than a combination of research fields which have
all too often evolved on parallel tracks in the past.
idated models that can generate a comprehensive set
271
2, METHODS
2.1 Model overview
The models presented in this paper are of three
types;
!. Luminous efÏcacy models that relate, in terms of
number of lumens per watt, the three basic radiation
components—direct, global and diffuse irradi-
ance—to their photopic equivalent—direct, global,
and diffuse illuminance. [Huminance may be de-
fined as the yield of a given light source—in the
present case, the sun/sky—when its spectrum is
weighted by the transfer function of the human eye
[4]. The International Hlumination Commission
(CIE) standard human eye response curve and solar
spectrum are compared in Fig. |.
. Models that predict diffuse irradiance or illumi-
nance received by tilted surfaces.
. Models that are concerned with the angular distri-
bution of light in the sky dome rather than with the
integrated diffuse values as in (2). A model that
predicts the luminance at the sky’s zenith is pro-
posed and evaluated along with a model, extrapo-
lated from CIE standards[5]-[7], that estimates
luminance at any point in the sky dome.
All models are “all-weather” short-time-step con-
version algorithms with a common operating structure.
They are validated here with both hourly and 15-min-
ute data.
The interrelationship between models, input data
and main application fields may be seen in Fig. 2.
2.2 Modeling approach
2.2.1 Model input and insolation condition pa-
rameterization. The input to the models consist of
short-time-step (hourly or less) direct and global ir-


272 R. PEREZ et al.
3 nre) -
$f >
$ ” Spectrum Curve a7 es
d
2 . =
=
©] Oo rf 4
2 ® | ieg
o
= 8
z 76
Bo!
ar
Fy 73a 8 °
CIE Photopic Curve
o° —_ | 1 °
0.0 0.5 1.0 15 2.0
Wavelenth (micrometers)
Fig. 1. The CIE Human Eye Photopic curve plotted with respect to the solar spectrum.
radiance data, as well as, for those where spectral effects maintenance rotating shadowband radiometer suggest
are of concern, three-hourly surface dew point tem- that these will be more widely available in the future
perature. Global and direct irradiance constitute today networks[8.9]. Modeled input may be used, in the
the most widely available type of solar radiation data. absence of either the direct or both quantities, with a
Moreover, the recent development of the low cost/ corresponding loss in accuracy[10]. The other input
SOLAR GEOMETRY |
DEW POINT TEMPERATURE ANGULAR DISTRIBUTION
SKY LUMINANCE
4
4
y
MODEL |---- DIFFUSE ILLUMINANCE
.
MODELS ++»
ON ATILTED SURFACE
{ LOBAL IRRADIANCE |
IRRADIANCE ON A TILT
MEASUREMENT NETWORKS
ROTATING SHADOWBAND
RADIOMETER [8,9]
v
<<" S
DIRECT, GLOBAL , DIFFUSE
DAYLIGHT ILLUMINANCE
Fig. 2. Interrelationship between model inputs and outputs. The models’ input data may be readily supplied
by the Rotating Shadowband Radiometer, a new instrument well suited for precise network operation [9].


Modeling daylight availability and irradiance components from direct and global irradiance
to some of the models presented here, 3-hourly surface
dew point temperature is a widely available standard
met orological parameter.
The above inputs are processed to derive four basic
components that parameterize all insolation conditions
from overcast to clear. These components are
(1) The solar zenith angle, noted as Z;
(2) The sky’s clearness, noted as ¢ and given by
e=[(Dht+1)/Dht «Z?]/{L+«Z°?], (1)
where Dh is the horizontal diffuse irradiance, / the
normal incidence direct irradiance and «x a constant
equal to 1.041 for Z in radians; the Z? formulation
was added to the original, simpler ¢ expression to elim-
inate dependence between this component and the so-
lar zenith angle.
(3) The sky’s brightness, noted as A and given by
A= Dham/I,, (2)
where 7 is the relative optical airmass[11] and /, the
extraterrestrial irradiance.
(4) The atmospheric precipitable water content,
denoted }’ (cm), and given by
W’ = exp(0.07* Td — 0.075) (3)
where Td (°C) is the three-hourly surface dew point
temperature.
The formulation in eqn (3) is similar to that pro-
posed by Reitan[!2] which is applicable to monthly
averages and validated for 15 locations in the United
States. Its validity for short-time-step data was exper-
imentally validated in the context of this project by
Wright er a/.[13].
It will be noted that the A-e parameterization used
here carries a quantity of information equivalent to
the K-kt or kd-kt representations often reported in the
literature(14,15]. However, it is thought that the pres-
ent approach better separates two distinct character-
istics of the atmosphere: (i) « variations express the
transition from a totally overcast sky to a low turbidity
clear sky; (ii) A variations reflect the opacity /thickness
of the clouds.
2.2.2 Models structure. All the models presented
here have a common structure represented by the fol-
lowing equation:
Y = X«F (insolation condition,
receptor/sun geometry) (4)
where Y is the modeled quantity (e.g., zenith lumi-
nance), X is a quantity depending only on the three
basic inputs specified above, (e.g., diffuse irradiance),
and F is a transfer function depending on the insolation
condition components and solar geometry. The func-
tion F combines an analytical formulation for the
variables A, Z and W and a discrete (bin) formulation
for the variable «. This semianalytical formulation al-
273
lows for maximum computer calculation eficiency—
discrete data table access is much less time consuming
than computations—while allowing manageable hand
calculations if necessary (see discussion in [16]). In
most instances, the dependence of F on insolation
conditions will be expressed as
+ cfe)e(Z) + dile)h(A) (5)
where /, g, and / are analytical functions and a,, ;, c;
and d, are discrete functions represented by eight-term
vectors corresponding to eight ¢ bins. These bins have
been optimized to account for the observed variability
of sky radiance distribution at several site[17] are
specified in Table 1.
2.2.3 Model derivation. All models presented and
tested here, with the exception of the luminance an-
gular distribution model, were experimentally derived.
The terms of the function F specified above were ob-
tained in each case through least-square fitting of large
data sets representative of a variety of climatic envi-
ronments. Note that the structure of the function F is
not entirely statistical but reflects in many cases the
physical properties of radiation transfer.
2.3 Experimental data
Experimental data from a total of 13 sites are used
in this study for model derivation and/or model val-
idation purposes[42-46]. These are listed in Table 2
along with their dominant climatic/environment
characteristics, the length of the available data set and
the frequency of experimental measurements.
A typical instrumentation set-up used for 10 out of
13 sites[17,20] is shown in Fig. 3. Table 3 identifies
measurements available at each site and indicates if
data from the site were used in this study for model
derivation purposes or strictly for independent vali-
dation purposes. Note that both |5-minute and hourly
data where used indiscriminately in this paper for
model derivation and validation purposes, hence the
“short-time-step” term used to qualify the models.
Data are known in each case to be of high quality
and to have undergone strict calibration monitoring
and stringent quality control. Class I pyrano/pyrhe-
liometers were used in all cases except for the vertical
irradiance measurements in the New York locations.
The cosine responses of each pyranometer and pho-
tometer used for the derivation of luminous efÏcacy
Table 1. Discrete sky clearness categories
ey
ee ee ee ee ee)
1. Overcast 1 1.065
2. 1.065 1.230
3. 1.230 1.500
4, 1.500 1.950
5. 1.950 2.800
6. 2.800 4.500
7. 4.500 6.200
8. Clear 6.200 --
ee ee


274 R. PEREZ ef al.
Table 2. Origin, size and climatic environment of experimental data sets
eee
ee a ee?
Geneva,
Switzerland [42]
Trappes, France
[43]
Carpentras,
France (43]
Albany, NY, USA
[44,45]
New York, NY,
USA [45]
Farmingdale, NY,
USA [45]
Oswego, NY, USA
[45]
Glens Falls, NY,
USA [45]
Phoenix, AZ,
USA [46]
Albuquerque, NM,
USA [46]
Los Angeles, CA,
USA [46]
Osage, KS, USA
[46}
C. Canaveral, FL,
USA [46]
ee
ee
Climate/Environment
Main Features
Data Set Span
and Frequency
ee
Temperate maritime, with central
Europe continental influence.
Persistent nebulosity enhanced
by “blocking position at foot-
hill of the Alps.
l yr. hourly data
Temperate maritime with high 3 yr. hourly data
incidence of intermediate skies
Mediterranean 3 yr. hourly data
Humid continental with bimodal 3yr. hourly data
2 yr. 15 min. data
Humid continental with maritime data
influence plus Large City’s
anthropogenic environment
lyr. 15 min.
Same as above but without city’s 1 yr. 15 min. data
environment
Humid continental, Great Lakes 6 mo. 15 min. data
basin
Humid continental 6 mo. 15 min. data
Arid, low elevation 6 mo. hourly data
Arid, High elevation (1800 m) 1 yr. hourly data
Arid and maritime influence 6 mo.
plus high frequency of
anthropogenic smog events
hourly data
Continental, U.S. Great Plains 6 mo. hourly data
Subtropical, low latitude, 6 mo. hourly data
maritime
a a ee ee ee)
models were experimentally determined. Data were
corrected to account for this source of error, which
may become critical at low elevations, particularly if
the illuminance and irradiance sensors have opposite
responses, as was Often the case. This process is reported
and thoroughly discussed in [18,19].
3. RESULTS
Result presentation is structured as follows: for each
model, a brief review of experimental observations is
first presented, followed by the formulation of the
model and validation results.
3.1 Luminous efÏcacy models
Much observational work and modeling has oc-
curred over the last 50 years to estimate luminous ef-
ficacy for specific insolation conditions and locations
(e.g., see the comprehensive review by [21] and recent
work by [22,23]). However, until very recently, no
model development effort was undertaken to system-
atically predict the three photopic component from
their irradiance equivalent for all insolation conditions.
The following luminous efÏcacy models were derived
from over 25,000 data points in five northeast U.S.
locations{20]. They are validated against data from
each of these sites plus, independently, against data
from one European site using similar instrumenta-
tion[24].
3.1.1 Global irradiance to illuminance conversion.
Key Observations. Experimental values of global
luminous efÏcacy, Gq, aS a function of several sky
condition parameters have been plotted in Fig. 4. These
include (i) variations of G.q with sky clearness ¢ for
Z ~ constant: (ii) variations with sky brightness A for
overcast conditions and ~ constant Z; (iii) variations
with zenith angle for very clear (« > 6) and, (iv) “av-
erage” (0.1 < A < 0.3) overcast conditions (¢ < 1.2).
A polynomial fit to data, illustrating the combined
variations of Geff with A and e, may be found in Fig.
5. The two previous figures include all data available
from Geneva, and the five New York State sites.
Features previously noted by the authors[25] are
quite apparent through these plots. Of particular in-
terest is the exponential variation of G.q with brightness,
observed for overcast conditions. This has also been
noted since by Littlefair{[26]. This is attributable to
the increase of water vapor absorption, hence the in-
crease in luminous efÏcacy, with cloud thickness. One


Modeling daylight availability and irradiance components from direct and global irradiance
Global irradiance Global, Hluminance
275
Veritco! Muminonce
Veritcal lrradionce
a
exe)
WA ound Shields
Luminonce Sensors
Beam ftlurninance
Beorm Irradiance© ~) “
24 in.
14 in Doto
Acquisition va
& Storage
4 Modem
LO L.
Cy Cai Link to A SRC.)
30 in.
<=
Le _ La
jo LJ
a i |f 48 in. 1
Fig. 3. Typical data acquisition set-up.
will also note from Fig. 4 that the clear sky zenith angle
effect is minimal but that a noticeable zenith angle
trend is observed for overcast conditions. A more de-
tailed presentation and discussion of these results may
be found in [20].
Of importance is the fact that observations inde-
pendently performed in five distinctive northeastern
U.S. and one Swiss location are in good agreement,
suggesting that model site dependency may not be a
major obstacle. This statement is supported by Fig. 6
where G.g variations with A for the 50°~70° zenith
angle range are compared for each of the six sites.
Model formulation. Equation (6) below is used to
calculate global illuminance from irradiance and the
sky condition parameters. This was derived from
25,000 data points from the five New York State sites:
The coefÏcients a;, b;, c;, and d; are given in Table 4
for each e€ bin.
Model validation. Performance evaluation results
are summarized in Table 5. This includes model RMSE
and MBE for three ranges of insolation conditions (re-
spectively, overcast, intermediate, and clear) and six
locations. The Geneva test is independent, the five
other tests are technically dependent, since the test data
were used to derive the model. However note that, for
this and the other models tested here, a set of environ-
mentally distinct sites are considered over a wide sea-
sonal range. The testing process considers each site/
season /insolation conditions distinctly; a satisfactory
behavior of the model for each element in this com-
prehensive range of environments may be considered
as a valid testing ground, especially if one realizes that
quality independent data sets of this type are partic-
ularly scarce today. Of course, subsequent independent
testing is strongly recommended; the CIE’s Interna-
tional Daylighting Measurement Year Program[41]
should provide the data needed for these verifications.
Resultant RMSE for all six sites is 3% while MBE
is kept near or below 1% for all conditions and sites.


276 R. PEREZ et al.
Table 3. Measurements available at each site—Role of data in model derivation validation
ee
Available
Measurements
Luminous Slope
EfÏcacy Diffuse
Irradiance Illuminance
ee
Trappes # -- BV
Carpentras # “* D,V
Albany 1 & - DV
Farmingdale *
Albany 2 *
Queens *
Oswego *
Glens Falls *
Geneva * v
Phoenix # --
Los Angeles # o*
Albuquerque # --
Cape Canaveral # +
Osage # “- B,
ee a a ay
Slope zenith Skylight
Diffuse Luminance Angular
Distribution
is
D: Site data were used for model derivation
V: Site data were used for model validation
i a i)
Available Measurements:
a
I, i, G, g, BD, d, Ge 90° N-E-S-W, ge 90° N-E-S-W, Lvz, Lve 456 N-E-S-W*
# 1, G, Ge 45° S, Ge 90° N-E-S-W
& I, G, Ge 33-43-53° S, Ge 90° N-E-S- W
I, £, G, g, D, d, Ge 30-45-60° S$, Gc 90° N-E-S-W
Note: Ground-reflected component was
ea ee?
This is remarkable since these values are of the order
of instrumentation precision levels. The independent
test in Geneva is consistent with the others, although
minor degradation is noted, which may be downplayed
for two reasons: (i) A dependent test in Geneva does
not yield substantial improvement for that site; and
(it) photopic instrument characterization, a crucial
components of luminous efÏcacy measurements [27 ],
200
~ r (ums/w) 5
B <1.2
o 180 }
3! 0.1<A<0.3
160 |}
an
3
© 140
&
3 120 |
Z oo |2 100
oO
BO re i 4. rn
0 20 40 60 80 (degs.)
Zenith Angle
¢ 200 ¢ (Lm/W)
mman
a E>6
5 180 +
3 160 |
n
=
= 140 +
E
3 120 }
3 L2 100
uo
80 4 i 1 k
0 20 40 60 80 (dags.)
Zenith Angle
removed from all Ge and ge points
a re
was not emphasized in Geneva to the extent that they
were in the New York sites.
In summary, the model reduces overall RMSE by
a factor of 1.4 over a constant luminous ethicacy model
set at the mean of all points. For such specific condi-
tions as dark overcast skies, error reduction approaches
a factor 3. Summer and winter bias are found to be
less than 0.5%; this indicates that the model accounts
200 ¢
b (Lm/w)
180 | 50° <Z<7C°
140 -
100 fT
BO in r de n a 4.
0 2 4 6 8 {0 12
Sky Clearness
i4
ae
bes)
200 ¢
d 200 (Lm/W)
50° <2<70°
E<1.2
160 -
140
120
100
80 2 £. i r
0.0 0.2 0.4 0.6 0.8
Sky Brightness
3.0
Fig. 4. Variations of global luminous efÏcacy with (a) Solar zenith angle for overcast conditions. (b) Sky
Clearness, ¢, for a limited zenith angle range. (c) Solar zenith angle for very clear conditions. (d} Sky
Brightness, A, for overcast conditions. (Data from five New York sites and Geneva).


Modeling daylight availability and irradiance components from direct and global irradiance
140
CE el coed
Oo me NM
-& D @
92
(«/un)
— Aavouya jeqoip -
“
gotpx
a
oO
gvers ast
Ky ¢
Fig. 5. Best-fit polynomial surface showing combined varia-
tions of global luminous efÏcacy with « and A at Z and Td =
constant. (Note that the surface is plotted only for the e-A
plane region where the quasi-totality of events were recorded—
the remaining of the plane corresponds to either extremely
unlikely (low A, middle «) or to physically impossible situations
(high A, high ¢).
277
satisfactorily for seasonal differences that have been
previously reported [28].
3.1.2 Diffuse irradiance to illuminance conversion.
Key Observations. Variations of diffuse luminous
efÏcacy. Dey, with « have been plotted in Fig. 7 for each
of the six sites. A similar trend is apparent at each site
showing a marked increase from overcast to clear con-
ditions caused by an increased contribution of molec-
ular (Rayleigh) scattering. (Note that the values of ¢
(sky clearness) achieved in Geneva ware far below
those achieved at the New York sites; this is a result
of climatic differences reported in Table 2). A poly-
nomial surface has been fitted to the ensemble of data
(Fig. 8) to illustrate the combined variations of Deg
with clearness and brightness at Z ~ cst. This varies
from less than 110 lumen/watt for bright overcast
conditions to above 150 for clear skies. Clear sky lu-
minous efÏcacy further increases with solar zenith an-
gle, likely because of increased contribution. on the
horizontal, of multiple Rayleigh scattering at the ex-
pense of circumsolar Mie scattering; this may be seen
in Fig. 9. As before, a more detailed analysis of results
will be found in [20].
200 F 200 F
(Lm/w) Albany (Lm/w) Farmingdale
180 f 180 f
160 } 160 r
140 —s
i2o Ff
100 f | 100 fF
ao ri 4 4 nN 80 4 i i. i.
0.0 0.2 0.4 06 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
200 F 200 Ff
3 (Lm/W) Geneva {Lm/W) Oswego
& 180 } 180 }
i
“160 } 160°}
Q .
2140 oy. 140
S Ar 
ed .
3 120 | 120 | "Betas ee
@ 100 ft 100 }
g
oo ao i r i i isi) i. A, 4, 4
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
200 F 200 ¢
(Lm/W) Queens (im/W) All sites
180 } 180 }
160 } 160 -
140 Fo 140
120 | Wipes... 120
100 100
a0 ‘ i i 1 80 i re i he
0.0 0.2 0.4 0.6 0.8 1.0 6.0 0.2 0.4 0.6 0.8 1.0
SKY BRIGHTNESS
Fig. 6. Variations of global luminous efÏcacy with sky brightness. .\, for five locations.


278 R, PEREZ et al.
Table 4. Luminous efÏcacy and zenith luminance model coefÏcients
(eee i i
ee ee rs i
el ee ee 2 i ey
Ce
¢ bin ay by cy dy
1 96.63 ~O.47 11.50 -9.16
2 107.54 0.79 1.79 “1.19
3 98.73 0.70 4.40 -6.95
4 92.72 0.56 8.36 -8,31
5 86.73 0.98 7.10 -10.94
6 88.34 1.39 6.06 -7.60
7 78.63 1.47 4.93 -11.37
8 99.65 1.86 4.46 “3.15
Diffuse Luminous EfÏcacy (Eq.7)
e bin ay by Cy dy
1 97.24 -0.46 12.00 -8.91
2 107.22 1.15 0.59 -3.95
3 104,97 2.96 -5.53 -8.77
4 102.39 5.59 +-13.95 ~-13.90
5 100.71 §.94 -22.75 -23.74
6 106.42 3.83 -36.15 -28.83
7 141.88 1.90 -53.24 -14.03
8 152.23 0.35 -45.27 -7.98
ay by Ci dy
57.20 4,55 -2.98 117.12
98.99 3.46 “1.21 12.38
109.83 ~4,90 “1.71 +8.81
110.34 -5.84 -1.99 ~4.56
106.36 -3.97 “1.75 -6.16
107.193 -1.25 “L.51 -26.73
105.75 0.77 “1.26 -34.44
101.18 1.58 -1.10 8.29
Zenith Luminance Prediction (Eq.10)
ay cy ce,’ dy
40,86 26.77 -29.59 -45.75
26.58 14.73 58.46 -21.25
19.34 2.28 100.00 0.25
13.25 “1.39 124,79 15.66
14,47 ~5.09 160.09 9.13
19.76 -3.88 154.61 -19.21
28.39 -9.67 151.58 -69.39
42.91 -19.62 130.80 -164.08
Model formulation. Diffuse illuminance may be
derived from diffuse irradiance and the sky condition
parameters through eqn (7). This is given below:
The coefÏcients of eqn (7), which were derived by teast-
square fitting of over 20,000 points are given in Table
4. CoefÏcients for the two highest ¢ bins were derived
from fixed shadowband diffuse irradiance and illu-
minance measurements available in Albany only: al-
though diffuse measurements with standard shadow-
bands are inherently less accurate than those obtained
by global and direct difference, this is not the case for
clear day diffuse luminous efÏcacy measurement: in
this case, the diffuse component is small compared to
Table 5. Luminous efÏcacy and zenith luminance model RMS and mean bias error as a function of
insolation conditions and location
ee ee ee eee
ee ee ee ee ee ee
Overcast Intermededite Clear All events
SITE —«—-_—_ we nme nme meter e ene eee
MBE RMSE MBE RMSE MBE RMSE MBE RMSE
Global Illuminance Prediction Model
Albany 0.3% 5.0% 0.5% 3.3% 0.3% 2.4% 0.4% 3.4%
Farmingdale 1.28 3.4% 1.4% 3.0% 1,28 2.7% 1.28 3.2%
Queens “1.3% 3.5% “1.3% 2.7% “1.2% 2.4% -1.2% 2.9%
Glens Falls “0.3% 4.9% -0.6% 4,0% -0.6% 3.3% -0,6% 4.1%
Oswego -0.5% 2.5% 0.9% 2.5% 1.28 1.9% 0.5% 2.5%
Geneva O.1% 5.7% “1.5% 3.7% 1.63 3.2% 0.7% 4.3%
Diffuse Illuminance Prediction Model * *
Albany 0.2% 5.1% 0.8% 7.2% 0.9% 13.7% (7%) 0.6% 8.4% (6%)
Farmingdale 1.1% 3.5% 1.5% 6.1% 1.9% 11.13% 1.4% 6.7%
Queens “1.1% 3.5% “1.18 6,0% *1,3% 12.1% -1.13 7.4%
Glens Falls -0.3% 5.2% -0.8% 8.7% -0.5% 17.3% -0.5% 10.6%
Oswego -0.6% 2.7% 0.8% 5.0% -1.4% 11.4% -0.8% 5.9%
Geneva 0.4% 6.1% 3.8% 9.1% 3.5% 10.2% 2.3% 8.7%
* Value derived from fixed shadowband measurements
Direct Illuminance Prediction Model
Albany s+ * ++ wees 1.6% 10.7% 0.7% 5.7% 0.7% 7.18%
Farmingdale ----- vere 1.2% 10.7% 1.0% 4.3% 1.0% 5.8%
Queens = --<-- wees -1.4% 10.0% -0.9% 4.2% -1.0% 5.6%
Glens Falls ----- ooee -1.6% 12.8% *1.3% 5.3% ~1.4% 7.4%
Oswego we eee woes 1.9% 9.8% 1.3% 4.0% 1.5% 5.9%
Geneva sterner ween “4.3% 14.0% 0.8% 4.5% -1.6% 9.5%
Zenith Luminance Prediction Model
Albany 3.2% 19.0% -1.13 24.0% 1.0% 24.1% 0.4% 21.5%
Farmingdale 3.0% 19.1% -2.3% 24.0% 2.0% 30.2% 0.8% 22.9%
Queens ~2.5% 17.6% 1.3% 21.9% 0.3% 28.2% -1.2% 21.8%
Glens Falls -3.1% 25.1% 4.9% 29.4% 3.6% 26.3% -0.9% 30.6%
Oswego -9,0% 23.9% L.1e 24.9% 1.6% 23.8% 0.3% 24.6%
ee ee ee ee ee ed


Modeling daylight availability and irradiance components from direct and global irradiance 279
250 F 250 fF
(L/w) Albany (Lm/w) Farmingdale
200 F 200 Ff
150 f ‘ 150 fy [Nee
100 fF ¢ 100 F
50 | 3 a a A. i. 4 4 50 i rf 4. L. A. , i
Oo 2 4 6 8 10 12 14 16 Gc 2 4 6 8 10 12 14 #16
> 250 F 250 ¢
u (Lm/W) Geneva (Lm/W) Oswego
=
f: 200 } 200 +
od :
A ‘
pe Sw vt
2 150 + 10 Fs
— geno’.
#100 F | 100
Po
te
a 50 4 4 —i_., A. a i. 1. 50 4, 1 i i © i. é.
0 2 4 6 8 {0 12 t4 16 0 2 4 6 @ 10 12 14 #I€
250 F 250 F :(Lm/W} Queens {Lm/W) All sites
200 + 200
150 fF TAQ
100 F 100
§0 i 4 a. i. i A be, 50 i. de. L | a Y t. iw
0 2 4 6 8 {0 12 i4 #16 0 2 4 6 &@ 10 12 4 #16
SKY CLEARNESS
Fig. 7. Variations of diffuse luminous efÏcacy with sky clearness, ¢, for five locations.
the direct and global components. If diffuse is obtained
by difference of the latter, a small relative error in any
one of those will result in a potentially large relative
error in the diffuse value; moreover, since diffuse lu-
150
140
(asa)
~ AdBOYJA asnjyig —yes
Fig. 8. Best-fit polynomial surface showing combined varia-
tions of diffuse luminous efÏcacy with « and 4 at Z and Td
= constant. (see note in Fig. 5.).
minous efÏcacy is the ratio of two such differences, the
measurement error may reach unacceptable levels. On
the other hand, when deriving luminous efÏcacy from
shadowband measurements, the initial source of error
has a tendency to “self-correct” since the shadowband
blocks an identical portion of the sky for both irradi-
ance and illuminance; aside from circumsolar spectral
differences, the shadowband error is canceled out by
ratioing the two quantities.
200
| (L/w) Albany
E>6
—_
Oo ©
©
140 +
Measured
diffuse luminous efÏcacy
120 +
100 fF
arent
20 40 60
Zenith angle
eo
2
80 = (degs.)
©
Fig. 9. Variations of diffuse luminous efÏcacy with solar zenith
angle for very clear conditions. Data from Albany, NY (fixed
shadowband measurements).


280
400
.
(Lm/w) 50° <Z<70°
300 }
200 + :
100 7
Beam luminous efÏcacy
ai. ad
0 2 4 6 8 10 12 14 16
Sky clearness
Fig. 10. Variations of direct beam luminous efÏcacy with sky
clearness, ¢, from overcast to clear conditions. Data from Ge-
neva and 5 New York sites.
Model validation. Prediction errors sorted by site
and insolation conditions are reported in Table 5. Re-
sults for Geneva are consistent with the other sites’,
except for a slightly higher bias, possibly traceable to
small calibration differences between the European and
American sets of instruments. Note that the relatively
high RMSE (10-15%) for clear conditions is believed
to be a result of measurement imprecision described
in the previous paragraph. Tests performed in Albany
on more reliable fixed shadowband data yield a RMSE
of about 7% for these conditions.
Use of the luminous efÏcacy model improves overall
prediction error by a factor of 1.8 with respect to a
constant luminous efÏcacy model optimized to the data
set. When based on more reliable fixed shadow band
data, the improvement factor reaches 2.9. As before,
no seasonal bias is detected. Existing winter-summer
differences are well accounted for by the surface dew
point input (coefÏcient 5; in eqn (7)).
3.1.3 Direct irradiance to illuminance conversion.
Key observations. Observed variations of direct lu-
minous efÏcacy, /.¢, with sky clearness at Z ~ cst are
; 120 +
3 110
S +
e = 100 +
+= 90
pod +
& so +
; ;
70
4
+
ae ss$ % s
Oo 4 an4 one
Lo termediate e) -
\ qvercast in ngs (108 scal )
ky clearm
Fig. 11. Best fit Polynomial surface showing combined vari-
ations of direct luminous efÏcacy with sky clearness, «, and
surface dew point temperature, Td. (Note that the surface
was not plotted for low « values where direct luminous efÏcacy
becomes a meaningless quantity).
R. PEREZ et al.
reported in Fig. 10. Except for an understandable in-
crease in scatter toward overcast conditions, the ob-
served dispersion for the six sites is remarkably low.
Some of the dispersion for intermediate conditions may
be accounted for by varying conditions of the other
parameters, notably by the dew point temperature. The
polynomial surface fitted to all data and plotted in Fig.
11 illustrates the markedly different effect of atmo-
spheric moisture on /,¢ for clear and intermediate con-
ditions. /.¢ decreases with increasing Td for interme-
diate conditions, likely because of enhanced aerosol
scattering, while it increases for clear conditions, be-
cause of increased absorption in the infrared. This ef-
fect, which was recently reported and discussed in [13]
is not accounted for in physically based approaches
such as [29]. The combined influence of sky clearness
and zenith angle may be assessed in Fig. 12, where
modeled /.g values (eqn (8)) have been plotted: The
effect of «, while small for low zenith angles becomes
crucial for zenith angles in excess of 70°.
Model formulation. Direct illuminance, /, is ob-
tained from direct irradiance, /, and the sky condition
parameters through eqn (8).
i= max{0, /[a; + bw
The coefÏcients of eqn (8), which were derived at least-
square fitting of 14,000 points are given in Table 4.
The exponential formulation for Z had been previously
optimized[13].
Model validation. Prediction errors are reported in
Table 5. Performance is consistent at all sites, with
slightly more dispersion observed in Geneva for inter-
mediate conditions: Possible causes are instrumenta-
tion differences, and a possibly different HW’-Td rela-
tionship at the European location.
Overall, the present model results in an improve-
ment by a factor of 3 over a constant luminous efÏcacy
model optimized to the present data set and by a factor
of 1.4 over a model! that would account for solar ele-
vation only. Seasonal bias variations are found not to
exceed 0.3% [20].
Modeled direct luminous efÏcacy
Vv Eps. « &
: © Eps. = 540
[ x Eps. = 3
20 5 + Eps. »2
4 Eps. = 1.5
8) [a on r
0 20 40 60 80 = (dags.)
Solar zenith angle
Fig. 12. Variations of modeled direct beam luminous efÏcacy
with solar zenith angle for different values of sky clearness, e.
Data from five New York sites.


Modeling daylight availability and irradiance components from direct and global irradiance
3.2 Diffuse irradiance and illuminance on tilted
surfaces modeling
These models estimate the total (integrated) sky
diffuse irradiance/illuminance received by a surface
tilted from the horizontal (e.g., a window). The
ground-reflected diffuse component may be added to
obtain the total hemispheric diffuse radiation on a
slope. This is not treated here but in a separate paper
by the authors[30]. Output data are suitable for most
energy gain calculations (e.g., solar{31], HVAC[3])
and for simple daylighting calculations (e.g., [32]).
More complex daylighting applications that require an
actual knowledge of the light source angular distribu-
tion should instead rely on the models presented in
Section 3.3.
Both models are based on the anisotropic diffuse
model developed by Perez et a/.[33] and commonly
referred to as the Perez model. This has been consid-
erably simplified since the original version{!6] while
conserving its original representation of the sky dome
as an isotropic background upon which are superim-
posed a circumsolar and horizon/zenith effects; these
effects are, respectively, simulated by a point source at
the sun’s position and a linear source at the horizon;
the latter can be either a positive or negative source
signifying respectively horizon and zenith brightening.
Model formulation. The model governing equation
for both illuminance and irradiance is
Xe = Xh[(1 — F,)( 1 + cos S)/2
+ Fia/b + Fyin S} (9)
where Xc and XA are, respectively, the tilted and hor-
izontal diffuse value of either illuminance or irradiance,
S is the considered surface’s slope, F; and F> are coef-
ficients expressing the degree of circumsolar and ho-
rizon/zenith anisotropy respectively; they are functions
of the sky condition. The terms a and bare given below:
a= max(0,cos@) and 6 = max(0.087, cos Z)
where @ is the incidence angle of the sun on the con-
sidered slope.
3.2.1 Irradiance model. The irradiance version of
the model has been extensively validated. In its original
version, it was reviewed and selected by the Interna-
tional Energy Agency[34]. Recent research and co-
operation programs[35] allowed for optimizing and
testing the model against data from 13 sites.
Model coefÏcients. The variations of horizon and
circumsolar brightening coefÏcients F; and F2 with in-
solation conditions have been observed to be consistent
from site to site[17,20]. Some of the key features are
presented in Fig. 13 where variations with ¢ for a given
zenith angle range have been reported. These features
include gradual increase of the circumsolar coefÏcient
from a value of 0 for overcast conditions to about 0.6
for intermediate-to-clear conditions (¢ = 2-3) followed
by a marked decrease toward very clear conditions.
For the horizon coefÏcient, an increase from a negative
281
1.OF
0.8
0.2} ’ . ee fe
~0.2
0.01 0.05 0.1 05 tf 5 10
Sky clearness €~-1)
1.0
0.8
0.6
- ia * .
0.2 , e . Rae ;
0.05 a gale DAR PRES |
a i? Oma : chan
-0.2
0.01
Horizon brightening (F2) Circumsolar Brightening (F1)
0.05 0.1 05 1 5 10
Sky clearness (g~-1)
Fig. 13. Variations of circumsolar and horizon brightening
coefÏcients with sky clearness, ¢« at Z ~ constant (45°-55°).
Data from Albuquerque. Pheonix, Los Angeles. Cape
Canaveral, and Osage.
value for overcast conditions to a positive value for
clear conditions is noted. These observations are con-
sistent with the physical processes affecting solar ra-
diation atmospheric transfer: the circumsolar peak for
intermediate conditions corresponds to a maximum
in forward scattering by thin/scattered cloud and/or
high aerosol content, the subsequent decrease toward
clear conditions is indicative of a decrease in atmo-
spheric aerosol content. The negative value for F; is
traceable to a relative brightening of the zenithal region
for overcast conditions the physical nature of which is
well understood|[ 36], the positive value for clear skies
is to be expected from Rayleigh scattering in an ho-
mogeneous nonabsorbing atmosphere. However. per-
haps more remarkable than basic agreement with un-
derstood physical processes, is the fact that the observed
variation patterns are continuous and exhibit low dis-
persion over the complete range of insolation condi-
tions and that indeed, the so-called intermediate skies
exhibit very predictable site-independent anisotropic
features, when parameterized as proposed, despite the
possible combinations of cloud type/height and tur-
bidity for these conditions.
The recommended set of coefÏcients is based on
data from Albany, Geneva, Los Angeles, Albuquerque,
Phoenix, Cape Canaveral, Osage, Trappes. and Car-
pentras. These are given in Table 6. This set differs
slightly from that presented at an earlier stage in Perez
et al.{t7]. The continuous evolution of coefÏcients
may be related to their sensitivity to the range of the
data from which they are derived. However. the vali-
dation results reported in Table 7 demonstrate that the
coefÏcients have now achieved an asymptotic level of
optimization and that the choice between the current
and previous sets is far from critical.


282 R. PEREZ et al.
Table 6. Perez model coefÏcients for irradiance and illuminance
a a a ee ee ee lad
OH OER ORR OO ERT THERESE SEH HH MH mm mw
eBin Fit Fi? Fu3
IRRADIANCE COEFFICIENTS
1 ~0.008 0.588 0,062
2 0.130 0.683 -0.151
3 0.330 0.487 “0.221
4 0.568 0.187 0.295
5 0.873 -0.392 -0.362
6 1.132 -1.237 -0,412
7 1.060 ~1,600 -0.359
8 0.678 -0.327 -0.250
ILLUMINANCE COEFFICIENTS
1 0.011 0.570 «0.081
2 0.429 0.363 ~0,307
3 0.809 -0,054 0.442
4 1.014 ~0,252 -0.$31
5 1.282 ~0.420 -0.689
6 1.426 -0.653 -0.779
7 1.485 -1.214 -0.784
8 1.170 -0,300 ~0.615
eooocoeoo
-0
462
823
.127
377
.158
.008
-O.
350
-0.
“0.
-0.
-L.
169
559
785
629
892
-0.
-Q.
-0.
-O.
«0.
-0.
-0.
“0.
018
065
092
096
114
097
082
055
i a es
Horizon Brightening CoefÏcient
ee es
Model validation. Model resultant RMS and mean
bias error for all sites studied are reported in Table 8.
These are sorted as a function of surface orientation
and compared to that of two reference models: the
isotropic and the Hay models[{ 37]. Overall RMS error
is kept at ~15 W/m, as opposed to 39 and 25 W/
m7? for the two reference models.
Site dependency may be assessed by looking at Ta-
ble 7 where overall RMS errors have been reported,
sorted by site and origin of coefÏcient set. It can be
seen (i) that performance is consistent at all sites, and
that (ii) for all but one case, (Osage, KS). coefÏcients
derived from any one site yield a better performance
than the reference models-—-the Osage exception may
be traced to the lack of experimental data for certain
insolation conditions and the resulting distortion from
the coefÏcients fitted to those data.
3.2.2 Illuminance model. The model formulation
is identical to that of the irradiance model (eqn (9)),
with the exception that horizontal diffuse illuminance
is the first term on the right-hand side of eqn (9). This
is obtained from diffuse irradiance using eqn (7).
Model coefÏcients. Concerning the coefÏcients, a
i
Circumsolar Brightening CoefÏcient Fy = Fiz + Fyota + Fy3*Z
Fo = Fo, + Fa2* + F23*2
re a
distinct illuminance set is recommended to account
for the difference between daylight and radiant power
anisotropy. The recommended illuminance set is pro-
vided in Table 6. This was derived from five northeast
U.S. sites. The use of a distinct set is clearly justified
by the validation results presented below. Some qual-
itative differences between irradiance and illuminance
coefÏcients are shown in Fig. 14: Observed variations
with «at Z = cst are compared for two time-coincident
sets. Differences are small but two distinctions merit
a comment: (i) the decrease of circumsolar brightening
toward very clear skies is less pronounced for the illlu-
minance component; and (ii) horizon darkening (i.e.,
zenith brightening) for overcast conditions is more
pronounced for the irradiance component—~a conse-
quence of water vapor absorption (see [20]).
Model validation. Model performance is reported
in Table 8, in terms of orientation-dependent RMSE
and MBE. Four versions of the mode! are presented
and compared to the two reference models. Versions
1, 2, and 3 use measured horizontal diffuse illuminance
as input for eqn (9) but use three different sets of coef-
ficients, respectively: (i) the recommended illuminance
Table 7. Tilted diffuse irradiance model composite RMSE as a function
of location and origin of coefÏcients
a ee ee ee ee ee ee oe ee oe)
MODEL PEREZ HAY IS0
CoefÏcients Phoen. Osage C.Can. Alby Fra Geneva - -
El Mte Albugq. SNLA USA US+Fr. ALL
LOCATION Five-Orientation Composite RMSE (W/m }
Phoenix, AZ 13.615 64 15 20 13 18 15 22 17 16 16 20 34
El Monte, CA 15 13 48 17 #17 #146 18 «15 19 «#16 «17 17 230 «45
Osage, KS 17° 16 #13 20 18 «15 20 18 «+20 «#18 «iF («217 «628 «(46
Albuquerque, NM 13 14 50 12 15 13 16 13 17 «#14 15 14 20 33
C.Canaveral, FL 14 17 36 14 12 14 16 14 #19 #17 «217 «217 ~«23°«134
ALL ABOVE SITES 14 15 51 16 17 14 17 #15 #19 16 #16 #16 22 38
Albany (SEMTS) 17. 16 «442 «#16 «17 :«216=«130«14:«118 «130 «14 130 26 36
ALL ABOVE SITES 16 16 45 16 17 15 14 14 16 14 15 14 23 36
Trappes & Carp. 20 20 21 20 19 19 16 47 #15 16 #17 #16 28 43
ALL ABOVE SITES 17 17 #43 17 #+41?7 «+17 «+18 15 16 215 16 15 25 38
Geneva, Switz. 19 #17 #23 #18 #18 #18 #«417 #16 «17 «216=~«215«~«15¢~«C2G O39
ALL SITES 19 #218 #41 #18 #«18 #«17 «16 «#16 «47 «1506160~6«2506«6250«(39
ee Ow


Modeling daylight availability and irradiance components from direct and global irradiance 283
Table 8. Overall RMSE and mean bias error for tilted diffuse irradiance and illuminance models
ee ee ee ee ee ee ee ee Oe es
IRRADIANCE MODEL ERROR (W/m?)
ISOTROPIC HAY
RMSE MBE RMSE MBE
32 18 24 1
43 -7 29 “9
38 0-1? 25-10
43 ~6 28 +7
36 0-22 2200-11
39 17 25 9
ILLUMINANCE MODEL ERROR (100 * LUX)
Surface Mean Global
Orlentation Irradiance PEREZ 1
(W/m*) RMSE MBE
90° North 64 11 3
90° East 174 17 -2
90° South 230 16 0
90° West 173 17 1
45° South 396 14 “1
Composite error 15 2
Surface Mean Global
Orlentation Illumin. PEREZ 1 PEREZ 2 PEREZ 3 PEREZ 4 ISOTROPIC HAY
(100*lux) RMSE MBE RMSE MBE RMSE MBE RMSE MBE RMSE MBE RMSE MBE
ee ee er es
90° North 71 12, 2 #12 «2
90° East 160 17, -1 «190
90° South 269 16 -L #18 = «+2
90° West 173 17.32 «20
Composite error 16 2 18 2
ee ee i a a a id
Ce ed
re a a oe ii wed
PEREZ 1: Illuminance coef. PEREZ 2: Dependent Irradiance Coef.
PEREZ 3: Independent Irradiance Coef.
ISOTROPIC, HAY, PEREZ 1, 2 and 3: Diffuse Illuminance Input
PEREZ 4: Operational Model -- Illum. coef. plus diffuse irradiance input --
i
set in Table 6; (ii) a set of irradiance coefÏcients derived
from the same data; and (iii) the independent irradi-
ance set recommended tn Table 6. The fourth version
is the operational version of the model which combines
eqn (7) to derive horizontal diffuse illuminance and
the illuminance coefÏcients.
Results show that performance degradation from
an illuminance coefÏcient set to an irradiance set de-
rived from the same data exceeds that from the latter
to an independently derived irradiance set. This ob-
servation tends to justify the recommendation for a
ev
& 2 irradiance
ag 2
& .
S
2+
i 2
asé L
§ =
zo +
0.01 0.05 0.1 0.5 1 5 10
om,
= 2 Nluminance
ae OP Ff
&
4 ~Se
zo
ue
a ee
a — a eR i
S S|] tinting eer"
A F
g <
= ° *
0.01 0.05 0.1 0.5 1 5 610
Sky clearness (€-1)
ee ed
distinct set of coefÏcients for the illuminance model.
Results also show that the operational version of the
model, which uses only the irradiance data as input,
does not yield significant performance deterioration.
In summary, the prediction of diffuse illuminance on
a tilt is as accurate overall as that of diffuse irradiance.
3.3 Sky luminance modeling
3.3.1 Zenith luminance prediction model. Zenith
luminance is treated distinctly because (i) it is a design
quantity of interest by itself, and because (ii) this is
Irradiance
Circumsolar Brightening (F1)
0.4
o i
9
~~
S rl heen
0.01 0.05 0.1 05 1 5 10
&
mw Hluminance
&os t
Cc
&
at -
faa)
bane
5 2 ~
o ©
“A
E
a6
Es —_
Q 0.01 0.05 0.1 05 1 5 10
Sky clearness (€-1)
Fig. 14. Compared variations of circumsolar and horizon brightening coefÏcients with ¢ for irradiance and
illuminance (45° < Z < 55°). Data from five New York sites.


284 R. PEREZ et al.
the main input quantity of CIE standard angular lu-
minance distribution models [5-7].
Key observations. A “pseudo luminous efÏcacy,”
Le, is defined as the ratio of zenith luminance to diffuse
irradiance. Observed variations of Lz with selected sky
conditions parameters are presented in Fig. 15. This
includes (i) variations with ¢ at Z =~ cst, (ii) variations
with A for overcast conditions at Z =~ cst, (iii) varia-
tions with Z for average overcast conditions (0.1 < A
< 0.3), and (iv) variations with Z for clear sky con-
ditions. Plots are based on all data available from the
five New York sites.
Variations are well defined and are in general
agreement with radiative transfer expectations. As
noted before, the continuous pattern across all inso-
lation conditions is remarkable. The strong decrease
with increasing sky brightness for overcast conditions
is most interesting: It indicates that standard CIE
overcast description[5] with it bright zenithal region
is valid only for dark overcast skies.
Model formulation. Zenith luminance, Luz, is ob-
tained from diffuse irradiance, Di, and the sky con-
dition parameters through eqn (10).
Loz = Dh[a; + ¢; cos Z
+c¢,;)exp(-3Z)+d,A] (10)
The coefÏcients of eqn (10), which were derived
by least-square fitting of 22,000 points may be found
in Table 4. Given the zenith angle validation domain
(17° < Z < 85°) care should be used outside those
bounds. Notably, the authors recommend use of Z’
= max(Z, 0.6) instead of Z for the lowest « bin in eqn
(10) and to view results for Z < 17° with caution until
further validation.
Model validation. Mean bias and RMS prediction
errors are reported in Table 5, in percentage of mean
value terms. Differences between sites studied are neg-
ligible as can be seen from the overall bias errors which
are kept below [% (this is also found to be season in-
dependent[20]). Relative RMS errors are larger than
that obtained for the other type of models described
above: this is to be expected because of the high vari-
ability that may occur in a confined region of the sky
dome for all but extremely clear and dark overcast
conditions. In absolute terms, RMS errors range from
0.7 kcd/m? for clear conditions to 1.5 ked/m? for
bright intermediate skies. Comparison for clear sky
conditions against existing models proposed by Dog-
niaux[38} and Karayel et a/.[39] indicates 2: 1 per-
formance gain[{18]—note that these models. opera-
tional for clear sky conditions only are turbidity de-
pendent, hence, require the same input information
as the present model.
3.3.2 Sky luminance angular distribution model.
Sky luminance distribution ts the “ultimate” daylight
availability quantity for daylighting calculations.
Modern design software[1] is now able to effectively
use sky maps and beam illuminance to precisely model
z
= 80 ¢ 80 ¢
© £<1.2 50° <Z<70°
=
> 40 =F 40 fF
o
F
& 5 .E 20 20
2 -
s i .
= Q 4. 1 A. 1 0 a i. i. i. dew i i i
3 0 20 40 60 BO (degs.) 0 2 4 6 8 10 12 14 #16
o Zenith Angle Sky Clearness
E 80 F 8G F
c E>6 . 50 <Z<70°
» 60 | 60 | Re. &<12
> 40 Ff 40 7%.
2 .
S
re
E 20 oT 20 fF
a
| fa) 4 i a oe iL re) Fy di. ry i
i} 0 20 40 60 80 (degs.) 0.0 0.2 0.4 0.6 0.8 1.0
zenith Angle Sky Brightness
Fig. 15. Variations of zenith luminance-to-diffuse irradiance ratio with (a) Solar zenith angle for overcast
conditions. (b) Sky clearness, ¢, for a limited zenith angle range. (c) Solar zenith angle for very clear conditions.
(d) Sky Brightness, A, for overcast conditions. (Data from five New York sites).


Modeling daylight availability and irradiance components from direct and global irradiance
light distribution in complex interior spaces with com-
plex apertures and outdoor obstructions. Because of
the limited coverage of sky luminance distribution
available for this study (five points in the sky dome)
and the possibility for resulting model distortion, new
model development was not undertaken at this time.
Rather, the study focused on evaluating and developing
operational versions of existing standard models. More
complete model development and validation of other
nonstandard approaches [e.g.. 15,40] will occur in the
foreseeable future using the large worldwide sky lu-
minance distribution data base the CIE’s International
Daylighting Measurement Year[41] is expected to
produce,
Model formulation. A combination of CIE skies is
proposed as an interim operational model. These are
(i) the standard CIE overcast sky[{5], (ii) the standard
CIE clear sky[6], (iii) a high turbidity formulation of
the latter[7], and (iv) a realistic formulation for in-
termediate skies proposed by a CIE working commit-
tee[7].
The model is formulated as follows:
Luc = Lezay (11)
where y is a geometrical factor depending on the solar
position, and the considered luminance direction. It is
obtained by interpolation of four CIE formulations [eqs
(12), (13), (14), and (15)] given below.
Clear sky formulation
Ves = P(Y)S)/[P( 4/2) f(Z)] (12)
where
#(X) = 1 — exp(—0.32/sin X)
S(X) = 0.91 + 10 exp(—3X) + 0.45(cos X)?
y: considered point elevation in radians
¢: direct beam vs. considered direction angle in
radians
Z: solar zenith angle in radians
Clear turbid (polluted) sky
Vs = BY) S'UO)/[S(r/2)f'(Z)] (13)
where {’(X) = 0.856 + 16 exp(—3X) + 0.3(cos X)?
Intermediate sky
Vis = a(ys, yexp[S(ys, ¥)]/
{a(y,, m/2)exp[Zb(y,, 7/2)]} (14)
where
a(X, Y) = [1.35 {sin(3.59Y — 0.009) + 2.31}
xX sin(2.6X + 0.316) + Y + 4.799] /2.326,
285
b(X, Y)
= —0.563[(Y + 1.059)(X — 0.008) + 0.812].
Overcast sky
Yos = (1 + 2 sin y)/3 (15)
The linear interpolation of the four terms is a function
of the sky condition components A and e. Limits are
determined by correspondence between each CIE
standard’s distribution profiles and experimentally de-
rived coefÏcients of the Perez diffuse illuminance model
(Section 3.2.2). For instance, the intermediate CIE sky,
which features a strong circumsolar effect, but no ho-
rizon brightening, is set at ¢ = 1.2 and A = 0.5—this
corresponds to a large value of F, at F, = 0 in the
illuminance model (see Fig. 14).
Specifically y is obtained from
Ife S 1.2 then
where
a= min{1, max[0, (e — 1)/0.2, (A — 0.05)/0.4]},
If 1.2 <¢ S 3 then
where
b = (e€— 1.2)/1.8,
Ife > 3 then
¥=(1-o)Y. + Ws,
where
c = min[1, (« —3)/3].
Model evaluation. Two versions are evaluated here,
one that uses measured Lvz as input in eqn (11) and
an “operational version” that combines eqns (11) and
(10) and uses only an irradiance input. Performance
is compared to that of two simpler models: (i) an iso-
tropic sky model that assumes constant luminance
throughout the sky dome; and (ii) an anisotropic
equivalent sky luminance model; the latter assumes
that luminance at any given point in the sky dome is
equal to the mean luminance viewed by a tilted plane
facing that point—mean luminance is obtained by di-
viding the diffuse illuminance value from eqn (9) by
the sky Lambertian solid angle viewed by the plane.
Validation data consist of measured luminance
values at 45° elevation in four azimuths. Note that in
this case, validation is totally independent since there
is no relationship between test experimental data and
model derivation. Observed relative (%) differences
between modeled and all available measured values in
Albany are plotted as a function of sky clearness in


286 R, PEREZ et al.
Fig. 16. It is apparent that the CIE combination models
do a better job than the two simpler models to predict
luminance at 45° elevation in the sky vault. The ten-
dency of the equivalent luminance anisotropic sky
model to overestimate for clear conditions is simply
caused by the fact that this incorporates horizon
brightening (seen by the tilted plane) whereas the test
positions are above the luminance enhancement re-
gion. Use of modeled rather than measured input for
the CIE formulation does not result in apparent per-
formance deterioration.
Quantitative validation summaries (RMSEs and
MBEs) are given in Table 9 for each site, model and
luminance direction. It is noteworthy to remark that
the model that uses modeled zenith luminance from
irradiance is slightly more accurate than the one that
relies on measured zenith luminance. This is under-
standable because the diffuse irradiance input contains
information from the entire sky whereas zenith lu-
minance is a point measurement. Overall, use of this
model results in a 1.6: 1 performance improvement
over the uniform sky and a 1.25: | improvement over
the anistropic equivalent luminance sky for the region
of the dome presently under investigation.
Recommendation. Closer scrutiny of results indi-
cates that it is likely that luminance distribution model
300 F
Model 1
200 [
100
~100 [
~200
5
-
~300 b
0
300 fF
200 [7
100 Ff
b
~ 100
~200
*
be L h. 1 n mn
MODEL ERROR (%)
fae]
co
for)
i)
=)
<)
-300 &
0 2 4 6 9 10 12 14
performance may be improved in the future. Table 10
reports model MBEs and RMSEs for Farmingdale,
sorted by sky condition, solar zenith angle and lumi-
nance direction for the selected model. The distinct
bias pattern would indicate that a better fit to the data
is possible. This task cannot be undertaken with the
present luminance data since a fit to that data (only
five directions in the sky vault) could result large dis-
tortions for other positions in the sky.
For the present, the level of precision achieved in
this independent test would warrant recommendation
of the proposed CIE interpolation method for appli-
cations as an “all-weather” operational skylight distri-
bution model. Note that, in practice, when a map of
the sky is generated the resultant overall bias can be
totally eliminated by simple normalization as shown
in eqn (17).
L’vce = Lee at |( { Lve sin rae) (17)
all-sky
The normalized luminance, L'vc, at any given point
is equal to the luminance obtained from eqn (11) mul-
tiplied by the ratio between diffuse illuminance, dh,
calculated from eqn (7), and the same quantity ob-
300
Model 2
200 [
100 —
~ 100
-200 [
dn 4
~300 fen
0 2 4 6 8 10 12 14
300 +
Model 4
200 F
-—100 [
a
rs 4. a ra rT i. 3
00
0 2 4 6 9 10 12 14
SKY CLEARNESS
Fig. 16. Relative difference between measured and modeled luminance at four points in the sky dome
(Model 1: eqn (11) + measured zenith luminance input; Model 2: eqn (11) + horizontal diffuse irradiance
input; Model 3: Isotropic Sky; Model 4: Anisotropic sky equivalent luminance). Data from five
New York sites.


Modeling daylight availability and irradiance components from direct and global irradiance 287
Table 9. Validation performance summary for luminance distribution models
ee ee ee ee ee ee ee 2 ee 2 er
LUMINANCE
SITE DIRECTION
maw
wee eee eee eee MODEL ERROR (cd/m2) -------
NO. OF MEAN MODEL 1 MODEL 2 MODEL 3 MODEL 4
EVENTS (cd/m?) RMSE MBE RMSE MBE RMSE MBE RMSE MBE
ee ee ee eee ee eee ee ee eee ee eee eee eee er ee ee eee
Albany N.
Albany E.
Albany 5S.
Albany W.
Farmin. N.
Farmin. N.
Farmin. S$
G. Fis.
G. Fis.
mm
Oswego
Oswego
Oswego
wows
Queens N
Queens E.
Queens §
. 45°
459
. 45°
-157) 1008 -226 1683 642 1650 832
“481 = 1581 -558 2466 -400 1934 497
-785 2831 -870 4278-2282 2958 +86
-368 1200 -427 1532 -311 1796 822
+225) 1126 -274 «691885 536 1801 759
-290 1904 -274 3076 -472 2331 651
-616 2452 -628 4249-2169 2864 100
-459 946 -449 1311 733 1160 768
-116 891 -104 1319 279 2068 1637
-358 859 -354 1290 458 1016 342
-562 1451 -554 1778 -360 1581 504
-835 2559 -842 3735-2032 2462 -18
-51 1080 -13 1865 856 1944 1210
+466 1999 -385 3438 -697 2419 655
-862 2645 -791 4555-2346 2691 89
ee oe ee ee ee ee eee
Model 1: Equation 11 with measured zenith luminance input
Model 2: Equation 11 with diffuse irradiance input (through equation 7)
Model 3: Isotropic sky
Model 4: Equivalent luminance, anisotropic sky
ee aed er)
tained by integration of the luminance points calculated quantities relevant to the design and optimization of
from eqn (11).
4. CONCLUSIONS
solar energy systems and building structures and com-
ponents. All models share a common operating meth-
odology in the sense that (1) they are designed to span
This paper has presented a set of models designed all conditions from overcast to clear, and (ii) they rely
to generate a comprehensive array of energy/daylight on the same input data and insolation conditions pa-
Table 10. Luminance model RMS and mean bias error as a function of orientation
and insolation conditions in Farmingdale
ee ee ee
SOLAR ZENITH
ANGLE
RANGE
Ce
ee ey
MBE RMSE mean
cd/m? cd/m? ed/m2
ee i oe
ee ee
MBE, RMSE mean MBE RMSE mean
ed/m* ed/m2 ¢g/m2 cd/m? cd/m2 cd/m2
ee ee ee ee
i i ee es
995 3170 8575 -102 940 «3548
-150 1854 6577 “160 927 2599
-437 1390 4429 -292 598 2154
“4355 895 3085 -219 «381-1780
432 572 #1774 -272 «(338 «1241
-178 1703 4729 +230 644 2161
—— EOE OHO Oe me Om
0°.35°
35°-50°
50°.65°
659.759
759.g5°
ee ee ee ee ee es
722 «3024 12344 210 #1970 5480
-245 3023 9041 +7 1382 4011
-995 3245 6524 46 1215 3325
-1506 2854 4951 218 906 2704
-804 1331 2357 *13 497 «1808
-677 2850 6838 86 1215 5046
edit tee a aie’
ee
50°-65°
659-759
759.g5°
~1843 4199 21224 289 2418 10279
-1892 4708 15329 542 1786 6272
+2891 5267 10952 5319 1514 5684
“1129 2344 5238 297) 827) 3383
-411 633 1993 -68 233 1487
-1752 3957 10359 339 1441 5046


288 R. PEREZ et al.
rameterization—input is compatible with currently
available data and with that likely to be provided by a
new generation of low cost/low maintenance instru-
ments.
The models have been extensively validated using
data representative from various climatic environ-
ments. These range from maritime to high altitude de-
serts for the irradiance models and from temperate
maritime to continental for the daylight availability
models. For each model, a noticeable performance
improvement is found over existing methods that ac-
complish the same task.
The experimental /statistical approach used to de-
rive the models can be considered both as an asset and
a liability. On the asset side, the experimental approach
allows for simply delineating particular configurations,
which are far from straightforward in terms of radiation
transfer calculations: The delineation of intermediate
cases between very clear and totally overcast extremes
is an example (e.g., the combined effect of surface dew
point and atmospheric clearness effects on direct beam
luminous efÏcacy ); the observation of well-character-
ized continuity between thin/scattered clouds and high
turbidity events is another. On the liability side, ques-
tions may be raised because (i) model validity should
be limited to the domain covered by experimental data,
and (ii) the models may carry possible instrumentation
limitations (e.g., calibration). Concerning the first
point, the validation domain covers a wide climatic /
seasonal range, even for the davlight availability mod-
els. Further validation /development is, of course, rec-
ommended, particularly for drastically different envi-
ronments—the proposed CIE’s International Day-
lighting Year[41] should provide an excellent basis to
address these questions. Concerning the second res-
ervation, the authors believe that, given the care and
scrutiny used for instrumentation characterization and
cross-calibration, resulting imprecision should be small
(this should be of most concern for luminous efÏcacy
models, which are crucially dependent on instrument
absolute calibration; in this case it is believed that
overall instrumentation-induced model bias should not
exceed 3%.
Beyond this first comprehensive set of operational
models, further model development yielding enhanced
accuracy and/or extended validation is needed and
likely to occur in the future as more data becomes
available, particularly with respect to skylight angular
distribution. Based on their experience, the authors
recommend the highest possible care in data and in-
strumentation quality monitoring if future data are to
fulfil this expectation.
Acknowledgments—The work presented in this paper is the
result of research efforts sponsored, respectively, by:
|. The Fond National Suisse de la Recherche Scientifique
(grant no. 2000-5.314) and the U.S. National Science
Foundation (grant no. INT8712462): Research cooper-
ation between the Universities of Geneva, Switzerland,
and Albany, NY).
2. The New York State Energy Research and Development
Authority (contract no. 724CONDCS85 }: New York State
daylight availability resource assessment program.
3. Sandia National Laboratories (contract no. 56-5434, U.S.
Dept. of Energy): Diffuse irradiance model development.
4. The Ernst and Lucie Schmidheiny Foundation, The Societe
Academique de Geneve and Geneva's Department of
Public Economy: U. of Geneva'’s Radiation Model De-
velopment Program.
The authors are grateful to W. Berkheiser [II and K. Webster
of the ASRC, the staff of Sandia National Labs, the Florida
Solar Energy Center, SUNY Buffalo, Adirondack Community
College, Queens College and New York Polytechnic Institute
for their assistance in data acquisition and analysis, to A. Ze-
lenka of the Swiss Meteorological Institute for his comments,
to Ted Cannon of SERI for his assistance in instrumentation
characterization and to J. Wright and T. Guertin who con-
tributed to elements of this research through their Master’s
theses.
REFERENCES
1. M.R. Fontoynont, Simulation of complex window com-
ponents using a photon-tracing simulation program, ISES
Solar World Congress 1987, Paper 8.7.01. Hamburg, FRG
(1987).
2. New York State Energy Research and Development Au-
thority (1989): Daylight Availability Resource Assessment
Program: Phase IV Preparation of a Climatological Day-
light Availability Data Base, NYSERDA 724-CON-BCS-
85, NYSERDA, Albany, NY (1989).
3. DOE 2.1¢ Simulation Program, DOE 2 Engineering
Manual, Energy and Environment Division, Building
Energy Simulation Group, Lawrence Berkeley Laboratory
(LBL), University of California, Berkeley (1985).
4. Commission Internationale de l'Eclairage, Standardization
of Luminous EfÏcacy Distribution on Clear Skies, Pub.
no. 222, CIE, Paris, France (1973).
5. P. Moon and D. Spencer, Hlumination from a nonuniform
sky, filuminating Engineering 37, 707-726 (1942).
6. Standardization of Luminous Distribution on Clear Skies,
CIE Publications No.22, Paris: International Conference
on Illumination (1973).
7. K. Matsuura, Luminance distributions of various reference
skies, CIE Technical Report of TC 3-09 (1987).
8. J. J. Michalsky, J. L. Berndt, and G. J. Schuster, A mi-
croprocessor-based rotating shadowband radiometer, So-
lar Energy 36, 465-470 (1986).
9. J.J. Michalsky, R. Perez, R. Stewart, B. A. LeBaron, and
L. Harrison, Design and development of a rotating sha-
dowband radiometer solar radiation/davlight network,
Solar Energy 41, 577-581 (1986).
10. R. Perez, R. Seals, A. Zelenka, and P. Ineichen, Climatic
evaluation of models that predict hourly direct irradiance
from hourly global irradiance—-Prospects for performance
improvements, Solar Energy 44(2), 99-108 (1989).
11. A. Kasten, A new table and approximate formula for rel-
ative optical air mass, Arch. Meteorol. Geophys. Biokli-
matol. Ser. B, 14, 206-223 (1966).
12. C. H. Reitan, Surface dew point and water vapor aloft.
J. Appl. Meteor. 2, 776-778 (1963).
13. J. Wright, R. Perez, and J. J. Michalsky, Luminous efÏcacy
of direct irradiance: Variations with insolation and mois-
ture conditions, Solar Energy 42, 387-394 (1989).
14. J. F. Orgill and K. G. Hollands, Correlation equation for
hourly diffuse radiation on a horizontal surface, Solar
Energy 19, 357-359 (1977).
15. A. P. Brunger, The magnitude, variability, and angular
characteristics of the shortwave sky radiance at Toronto,
Doctoral Dissertation in Mechanical Engineering, Uni-
versity of Toronto, Canada (1987).
16. R. Perez. R. Seals, P. Ineichen, R. Stewart, and D. Men-
icucci, A new simplified version of the Perez diffuse ir-
radiance model for tilted surfaces, Solar Energy 39, 221-
231 (1987).
17. R. Perez, R. Stewart. R. Seals, and T. Guertin, Devel-
opment and validation of the Perez diffuse radiation


Modeling daylight availability and irradiance components from direct and global irradiance
model, Sandia National Labs Report no. SAND88 /7030,
250 pp. SNLA. Albuquerque, NM (1988).
. R. Perez, Daylight resource availability. Phase 17 Report
(200 pp). New York State Energy Research and Devel-
opment Authority, Albany, NY (1987).
. T. Cannon, Personal communication, SERI, Golden, CO
(1986).
. R. Perez. R. Seals, J. Michalsky, W. Berkheiser III, R.
Stewart, and K. Webster, Daylight resource availability.
Final report (85 pp) (1988).
. P. J. Littlefair, The luminous efÏcacy of daylight, 2nd
International Daylighting Conference, Long Beach, CA
(1986).
. G. Gillette and S. Treado, Correlation of solar irradiance
and daylight illuminance for building energy analysis.
ASHRAE Transactions 91( 1A), 180-192 (1985).
. M. Navvab, M. Karayei, E. Ne’eman, and S. Selkowitz,
Analysis of luminous efÏcacy for daylight calculations,
2nd International Daylighting Conference, Long Beach,
CA (and ASHRAE transactions) (in press).
. P. Ineichen, Mesures d’Ensoleillement a Geneve (6 /86-
5/87), Groupe de Physique Appliquee, Universite de
Geneve, Switzerland (1988).
. R. Perez. K. Webster, R. Stewart, and J. Barron, Varia-
tions of the luminous efÏcacy of global and diffuse radia-
tion and zenith luminance with weather conditions, Solar
Energy 38(1), 33-44 (1987).
26. P. J. Littlefair, Measurement of the luminous efÏcacy of
30.
31.
33.
34.
36.
37.
38.
39.
daylight. Lighting Research Technology (in press).
. P.R. Tregenza, Guide to recommended practice of day-
light measurement—General class stations, Supplement
to CLE Journal 6(2), (1987).
. M. Navvab, M. Karayel, E. Ne‘eman, and S. Selkowitz,
Analysis of atmospheric turbidity for daylight calculations,
First International Daylighting Conference, Phoenix, AZ.
and Energy and Building 6(3). (1983).
. S. Aydinli, Uber die Berechnung der zur Verfugung Ste-
henden Solar-energie und des Tageslichtes, Ductoral Dis-
sertation, Tech University of Berlin, Federal Republic of
Germany (1981).
P. Ineichen, R. Perez, and R. Seals. The importance of
correct albedo determination for adequately modeling
energy received by tilted surfaces, Solar Energy 39, 221-
232 (1987).
D. F. Menicucci, J. P. Fernandez. User’s manual for
PVFORM: A photovoltaic system simulation program
for stand-along and grid-interactive applications, Report
no. SAND85-0376-UC-276, Sandia National Laborato-
ries, Albuquerque, NM (1988).
. Daylighting—Lumen method calculation, In: [ES lighting
handbook reference volume, (Ch, 7), [Humination En-
gineering Society (IES). New York, (1981).
R. Perez, R. Stewart, C. Arbogast, R. Seals, and J. Scott,
An anisotropic hourly diffuse radiation model for sloping
surfaces—Description performance validation, site de-
pendency evaluation, Solar Energy 36, 481-498 (1986).
International Energy Agency Solar Heating and Cooling
Programme, Task IX B (Validation of Solar Irradiance
Simulation Models), IEA, Paris (1987).
. National Science Foundation International Programs
Project no. INT8712462 NSF, Washington, DC, 2.
K. Y. Kondratyev, Radiation in the atmosphere. Aca-
demic Press, New York (1969).
J. E. Hay and J. A. Davies, Calculation of the solar ra-
diation incident on an inclined surface, Proc. First Ca-
nadian Solar Radiation Workshop, Hay & Won, Toronto,
Ont., Canada (1980).
R, Dogniaux, Variations quantitatives et qualitatives des
composantes du rayonnement solaire sur une surface
horizontale per ciel serain en fonction du trouble at-
mospherique, Pub. 1RM-B-62, Royal Meteorological In-
stitute, Bruxelles, Belgium (1970).
M. Karayel, M. Navvab, E. Ne’eman, and S. Selkowitz,
40.
41.
42.
43.
44.
45.
46.
moog MOISE
Dh
De
XC
Xh
Luz
Lve
L'
289
Zenith luminance and sky luminance distribution for
daylighting calculations, Energy and Buildings 6(3).
(1983).
M. Perraudeau, Luminance models, National Lighting
Conference and Daylighting Colloquium, Robinson Col-
lege, Cambridge, England (1988).
Commission Internationale de l'Eclairage, Announcement
by President H. W. Bodmann of International Daylight
Measurements Year 1991, managed by TC 3-07 (1987-
12-18).
P. Ineichen, Mesures de rayonnement a Geneve. Groupe
de Physique Appliquee, Universite de Geneve. Geneva,
Switzerland (1988).
Direction de la Meteorologie, Service Meteorologique
Metropolitain, Stations #260 and #874, ONM., Paris
(1979-1981).
USDOE’s Solar Energy Meteorological Research and
Training Sites Region II, Atmospheric Sciences Research
Center, Albany, NY (1980-1982).
New York State Daylight Availability Resource Assess-
ment Program, NYSERDA contract 724-CONBCS85
Atmospheric Sciences Research Center, Albany, NY
(1986-1988),
Sandia National Laboratories’ Measurement Program for
Radiation Modeling Contract no. 56-5434, SNLA Al-
buquerque, NM (1986).
NOMENCLATURE
solar zenith angle (rads., unless otherwise specified)
Tilted plane slope angle (rads.)
Solar incidence angle on tilted plane (rads.)
Elevation angle for luminance direction in the sky dome
( rads.)
Solar elevation angle (rads.)
¢ Angle between direct beam and considered luminance
direction ( rads.)
Relative optical air mass
Atmospheric precipitable water (cm)
Surface dew point temperature (°C)
Global horizontal irradiance (W/m?)
Global horizontal luminance (Lux)
Normal incidence direct irradiance (W/m7*)
Extraterrestrial normal incidence irradiance (W/m?)
Normal incidence direct illuminance (Lux)
Horizontal diffuse irradiance (W/m*)
Horizontal diffuse iduminance (Lux)
Diffuse irradiance on a tilted plane (W/m?)
Diffuse illuminance on a tilted plane (Lux)
Generic term for both diffuse irradiance and illumi-
nance on a tilted plane
Genencc term for both horizontal diffuse irradiance and
illuninance
Luminance at the sky’s zenith (Cd/m7?)
Luminance at a given position in the sky (Cd/m7)
Normalized luminance at a given position in the sky
(Cd/m?)
Global luminous efÏcacy (Lm/W)
Diffuse luminous efÏcacy (Lm/W)
Direct luminous efÏcacy (Lm/W)
Zenith luminance “Pseudo-efÏcacy” Luz/Dh (Cd/W)
é Atmospheric clearness parameter (dimensionless )
Atmospheric brightness parameter (dimensionless)
Circumsolar brightening coefÏcient (dimensionless )}
Horizon brightening coefÏcient (dimensionless)
¥ Ratio between sky luminance at a given point in the
sky and zenith luminance
Same as above—CIE overcast sky formulation
Same as above—CIE intermediate sky formulation
~~ a&®N
dh
de
vc
vcs Same as above—ClE clear sky formulation
¥rs Same as above—CIE clear-turbid sky formulation
