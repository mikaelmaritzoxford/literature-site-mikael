Energy Conversion and Management 89 (2015) 608–614

Contents lists available at ScienceDirect

## Energy Conversion and Management

journal homepage: www.elsevier.com/locate/enconman

# Determination of photovoltaic modules parameters at different operating conditions using a novel bird mating optimizer approach

a,⇑, Leandro dos Santos Coelho b Alireza Askarzadeh a Department of Energy Management and Optimization, Institute of Science and High Technology and Environmental Sciences, Graduate University of Advanced Technology, Kerman, Iran b Industrial and Systems Engineering Graduate Program, Pontifical Catholic University of Parana, and Department of Electrical Engineering, Federal University of Parana, Curitiba, PR, Brazil

# article info abstract

# Article history: The main goal of this paper is to provide a framework to accurately estimate the electrical equivalent

# Received 10 August 2014

circuit parameters of photovoltaic arrays by use of an efficient heuristic technique. Owing to the non-

# Accepted 9 October 2014

linearity of the current vs. voltage (I–V) characteristics of PV modules, using a superior optimization tech-

# Available online 30 October 2014

nique helps to effectively find the real electrical parameters. Inspired by the mating process of different bird species, bird mating optimizer (BMO) is a new invented search technique which has shown superior Keywords: performance for solving complex optimization problems. In this paper, the original BMO algorithm is Photovoltaic modules simplified and used to estimate the electrical parameters of the module model for an amorphous silicon Parameter estimation PV system at different operating conditions. The simplified BMO (SBMO) eliminates tedious efforts of Simplified bird mating optimizer parameter setting in original BMO and also modifies some rules. The usefulness of the proposed algorithm is investigated by comparing the obtained results with those found by two particle swarm optimization (PSO) variants, two harmony search (HS) variants as well as seeker optimization algorithm (SOA). Based on the investigated situations of this paper, SBMO yields more accurate results than the other studied methods. 2014 Elsevier Ltd. All rights reserved.

# 1. Introduction

Solar energy offers a clean, climate-friendly, very abundant, and in-exhaustive energy resource to mankind. Solar power generation by PV technology is an active area which is studied worldwide from various aspects such as modeling and control [1], combina- tion with other renewable sources [2], power forecasting [3], max- imum power point (MPP) tracking [4] and parameter optimization [5]. In order to understand the characteristics, evaluate the perfor- mance and consequently optimize photovoltaic (PV) systems, an accurate mathematical model is a key tool for researchers. Modeling includes the mathematical description of the non-linear behavior of current vs. voltage (I–V) characteristics. A number of mathematical models have been represented to clarify the behavior of PV system under different operating condi- tions. They vary from models with simple assumptions to advanced models accompanied with many physical variables. However, the single and double diode models are the most

⇑ Corresponding author. Tel./fax: +98 342 6233176. E-mail addresses: a.askarzadeh@kgut.ac.ir, askarzadeh_a@yahoo.com (A. Askarzadeh). [http://dx.doi.org/10.1016/j.enconman.2014.10.025](http://dx.doi.org/10.1016/j.enconman.2014.10.025) 0196-8904/ 2014 Elsevier Ltd. All rights reserved.

common models which are used in practice [6]. Though the double diode model slightly yields more accurate results than the other one, the ability of providing a good compromise between simplicity and accuracy causes the single diode model becomes more popular [7]. By the optimum value of the parameters, the model results can fit the experimental data as well as possible. Various techniques have been used to extract the optimum parameters. In some Refs. [8–11], conventional methods have been employed. Because of their global search ability, metaheuristic algorithms can be appropriate choices to conquer the difficulty of the problem. In recent years, metaheuristic optimization algorithms such as genetic algorithm (GA) [6], simulated annealing (SA) [12], pattern search (PS) [6], differential evolution (DE) [7], harmony search (HS) [13] and artificial bee swarm optimization (ABSO) [14] have been used to solve the parameter estimation issue. The main differences between this paper and the recently published papers by the author [13,14] are (1) In [13,14], an opti- mization framework has been developed to find the parameters of a single solar cell while in this paper the formulation has been extended to a PV array consisting a number of series and parallel solar cells, (2) In [13,14], only one operating condition has been considered while here, parameter identification is conducted at

A. Askarzadeh, L. dos Santos Coelho / Energy Conversion and Management 89 (2015) 608–614
Fig. 1. The single diode model of PV cell under illumination.

different operating conditions, (3) In [13,14], the parameter esti- mation is conducted for a commercial silicon solar cell while this paper studies an amorphous silicon PV system. Recently, a heuristic technique named bird mating optimizer (BMO), has been developed based on the idea of mimicking the breeding process in birds’ society. BMO belongs to the category of evolutionary algorithms (EAs) which borrows some idea from the other heuristic techniques. Though BMO has been successfully applied to the engineering optimization problems [15,16] in com- parison with a variety of optimization techniques, it suffers from some drawbacks. The main disadvantages of the original BMO are (1) numerous numbers of adjustable parameters and (2) numerous types of birds. In order to cope with the mentioned drawbacks, this paper proposes a simplified BMO algorithm, named SBMO, which reduces the types of the birds and eliminates tedious and experience-requiring parameter assigning efforts. In fact, these modifications make a user friendly optimization technique. The ultimate aim of this paper is to propose an efficient meth- odology to estimate the electrical equivalent circuit parameters of photovoltaic modules. The solar system considered in this paper is an amorphous silicon module which is an attractive solar cell for PV researchers. For this system, parameter identification is con- ducted at different operating conditions. Operating conditions affect the model parameters and so, in each operating condition parameter identification is necessary. In order to evaluate the search power of the proposed algorithm, the performance of SBMO is compared with the results found by some well-known heuristic techniques.

# 2. Problem formulation

## 2.1. Module model

PV systems are broadly characterized by circuit-based approaches. For modeling a PV system under the illumination, the simplest way is to consider a current source in parallel to a diode. Consequently, three unknown parameters, namely, photo- generated current (Iph), diode saturation current (Isd) and diode ide- ality factor (n), make the parameters of the equivalent circuit model. For considering the PV cell metal contacts and the semicon- ductor material bulk resistance, an improved model, called R s -model, takes into account a series resistance (Rs) to the model. Though Rs-model is more accurate, it shows serious deficiencies under high temperature variations since it does not account for the open circuit voltage coefficient. In addition, Rs-model is suit- able for crystalline PV cell and leads to significant inaccuracy when it is applied to the thin-film technology. Another modification was suggested by adding a shunt resistance (Rsh) to the diode to con- sider the partial short circuit current path near the cell’s edges resulted from the semiconductor impurities and non-idealities. This type of the model is known as the single diode model (or R sh-model). In the single diode model, shown in Fig. 1, the terminal current, I t, can be formulated as follows [17,18]: I t ¼ IphIdIshð1Þ where Idis the diode current and Ishdenotes the shunt resistor current. By use of Shockley equation for the diode current and substitut- ing the shunt resistor current, Eq. (1) is rewritten as given in the following equation [17,18]: ≥ ~ <u>qV</u> ðÞ<u>tþ R Is tVtþ R Is t</u> I t ¼ IphIsdexp ð2Þ nkT Rsh

where Isdis the diode saturation current, Vtis the terminal voltage, q is the electronic charge, k denotes the Boltzmann constant, n is the diode ideality factor and T (K) is the cell temperature. When insola- tion drops, short-circuit current of cell drops in direction proportion. A PV module consists of series and parallel PV cell combina- tions. If we consider a PV module with Nscells connected in series and Npstrings connected in parallel, the mathematical formulation of a PV module can be formulated by Eq. (3) [17,18]. ≥ ~ <u>qV=Nt sþ R I =Ns t p</u> I t ¼ NpIphNpIsdexp 1 nkT NpVt=Nsþ RsIt R sh ð3Þ

The equivalent circuit parameters of the single diode model which needs to be determined are photo-generated current, series resistance, shunt resistance, diode saturation current and diode ideality factor (Iph, Rs, Rsh, Isd, and n). Due to the fact that irradiance and temperature strongly affect the behavior of a PV module, it is necessary to determine all the model parameters simultaneously. This aim can be achieved by the help of a superior optimization technique.

## 2.2. Fitness function

In order to quantify the difference between the model results and the experimental data, root mean square error (RMSE) is used as the fitness function. For this aim, all the terms of Eq. (3), are moved to one side and the value of f is calculated for each pair of the experimental data by Eq. (4). Indeed, f denotes the error whose value is zero if the optimal values of the parameters are put into the right side. In this equation, Itand Vtare the experimental data obtained from the PV system:

fV ðÞt; It; ~x ¼ ItNpIphþ NpIsd ≥ ~ qVt=Nsþ RsIt=Np exp nkT 1 <u>N V =Np t sþ R Is t</u> þ ð4Þ R sh where f is the value of the homogeneous form of Eq. (3), ~x =[RsRsh I I n] is the vector of decision variables and M is the number of ph sd the experimental data.

So, we can define the optimization problem by: v uffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi u <u>1</u> X M 2 Min: RMSE ¼ tMðÞ fiðÞ Vt; It;~x i¼1 subject to R min sRsR max sð5Þ min max R shRshRsh min max I phIphIph I min sdIsdI max sd min max n n n

The optimization algorithm tries to minimize the fitness func- tion value with respect to the parameters range [13]. The optimiza- tion algorithm successively adjusts the parameters until the stopping criterion is reached. Because there is no information about the precise values of the parameters, any decrease in RMSE value is noteworthy since it leads to improvement in the knowl- edge about the real values of the parameters.

Type 1: the birds of this type are called females whose fitness values are better than those of the other birds of the society. Number of these birds (N₁) is determined by the following equation: ~ <u>N</u> N₁ ¼ round 10 ð6Þ

where round rounds to the nearest integer and N is the population size. Type 2: the birds of this type are male birds that are interested in mating with one female bird. Number of these birds is deter- mined by the following equation: ~ 7 N N₂ ¼ round ð7Þ 10 Type 3: the birds of this type are male birds that are interested in mating with two female birds. Number of these birds is deter- mined by the following equation: N₃ ¼ N N₁ N₂ ð8Þ Step 5: Breeding Each bird produces a brood by a specific pattern. Different spe- cies make use of the following patterns for breeding: Type 1: female birds use the following expression for breeding: for i ¼ 1 : d if randð0; 1Þ > randð0; 1Þ <u>randð0; 1Þðrandð0; 1Þrandð0; 1ÞÞ</u>

|x ðiÞ¼x|ðiÞþ|x ðiÞ;|
|---|---|---|
|else|||
|x ðiÞ¼x|ðiÞ;||

new old 10 old ð9Þ new old end end where ~xoldand ~xneware the vectors related to the bird and its brood and rand (0, 1) is a uniformly distributed random number between 0 and 1. It is worthwhile to mention that the random numbers are dif- ferent. This type of the reproduction is known as parthenogenesis in the nature. This idea has been used in evolutionary algorithms before in a few papers [20–22]. Type 2: male birds of type 2 use Eq. (10) for breeding. ~ x new¼ ~xoldþ randð0; 1Þð~xs~xoldÞð 10Þ where ~xsis the interesting mate of the male bird which is randomly selected among the female birds. Type 3: male birds of type 3 use Eq. (11) for breeding. ~ x new¼ ~xoldþ randð0; 1Þð~xs;1~xoldÞþrandð0; 1Þð~xs;2 ~ x oldÞð 11Þ where ~xs;1and ~xs;2are the interesting mates of the male bird which are randomly selected among the female birds. In order to effectively probe the search space, an optimization algorithm should be able to provide a good compromise between exploitation and exploration. In the proposed SBMO algorithm the birds included in type 1 search their vicinity to provide exploi- tation. On the other hand, in order to provide exploration, the other birds (type 2 and 3) of the society move through the search space with respect to memory and randomness. The difference between

# 3. Simplified bird mating optimizer (SBMO)

Inspired by mating strategies of different bird species, bird mating optimizer (BMO) was originally proposed by Askarzadeh and Rezazadeh [19]. The effectiveness of this algorithm has been confirmed by efficiently solving complex optimization problem. However, it is clear that efficiency is not the only feature of an algorithm for being selected by a user. In addition to effi- ciency, a popular optimization algorithm should be user friendly (easy to implement and few parameters to adjust). Due to the fact that the original version of BMO includes some drawbacks, especially for novice users, the authors have decided to intro- duce a new version of this algorithm to be more popular than the former. The steps of the proposed user-friendly BMO algorithm (SBMO) are as follows:

Step 1: Initialization

A society of random feasible birds is produced. Each bird is defined by a vector (~x) with the length of d (number of decision variables).

Step 2: Fitness evaluation

The decision variables related to each bird are put into the fit- ness function and the corresponding value is calculated.

Step 3: Ranking

The birds are ranked based on their fitness values so that the bird with the best fitness is placed at the first rank.

Step 4: Birds classification

According to their ranks, the birds are classified into three types

|||||type|2 and|type 3 is that|in type|3 the information|of more|
|---|---|---|---|---|---|---|---|---|---|
|Rank 1|2 …..|N₁ N₁+1|N₁+2 …..|N₁+N₂|N₁+N₂+1|N₁+N₂+2|….. N₁+N₂+N₃|||
|Type|Type 1|Fig. 2. Classification of the birds of the society.|Type 2|||Type 3||||

as Fig. 2.

Fig. 3. Brief overview of steps 4 and 4.

value, are returned as the optimal values of the parameters. Otherwise, Steps 3–6 are repeated.

Fig. 4 indicates the pseudocode of the proposed SBMO

algorithm. In this version of BMO, only two parameters of N and t maxneed to be adjusted. Considering this point that population size and maximum number of iterations are two adjustable param- eters in most of population-based heuristic techniques, it can be said that in SBMO there is no specific parameter to adjust. On the other hand, the steps mentioned above, reveal that SBMO can be easily implemented by a novice user.

solutions is used to produce a new one. This way may result in providing more exploration. In differential evolution (DE) algo- rithm there is mutation factor which is used to expand the search space. Usually, based on this factor, for each member of the popu- lation, three distinct members are randomly selected and a donor vector is made by adding the weighted difference of two of the members to the third. Then, each element of the donor vector is used for producing the corresponding element of the new solution by a probability. In comparison with DE, in SBMO, birds of type 2 and 3 randomly move toward the elite bird(s) from all dimensions.

Fig. 3 shows the brief overview of steps 4 and 5.

Step 6: Replacement

The fitness value of each brood is calculated and is compared with that of the corresponding bird. The brood is added to the soci- ety and the bird is eliminated if the brood produces better fitness. Otherwise, it is removed.

Step 7: Checking the stopping criterion

The algorithm is terminated if the stopping criterion is reached. In this case, the birds of the society are evaluated and the decision variables related to the bird with the minimal fitness function

# 4. Results and discussion

SBMO-based parameter estimation method is used to obtain the optimum parameters of the PV module model at different operating conditions for a real amorphous silicon solar cell. This system has the area of 1.31 1.10 m² in which 160 PV cells have been connected in series. The I–V test of this system is conducted in an advanced PV-lab which has an AAA class solar simulator. The spectrum of the solar simulator is very close to the solar spectrum. To extract the experimental data, the solar radiation and module temperature are fixed at their values and the I–V curve is measured.

Fig. 4. Pseudocode of BMO algorithm.

Table 1

The statistical results of fitness function values over 30 runs obtained by SBMO and the other studied algorithms on case 1.

|Index|PSO-w|PSO-cf|IGHS|GGHS|SOA|SBMO|
|---|---|---|---|---|---|---|
|Mean|0.1602420|0.2485330|0.0174631|0.0190022|0.0148198|0.0073349|
|Std|0.15805|0.24779|0.00568|0.00416|0.00487|0.0021812|
|Best|0.0076107|0.0288260|0.0057271|0.0079010|0.0065674|0.0056741|
|Worst|0.7370739|1.1150854|0.0240636|0.0238538|0.0252346|0.0154996|

Index PSO-w PSO-cf IGHS GGHS SOA SBMO

Table 2

The result of two-tailed t-test between SBMO and the other algorithms on case 1 over 30 runs (star sign means the performances are different). <u>Index</u> PSO-w <u>PSO-cf IGHS GGHS SOA</u> t 5.2985⁄5.3313⁄9.1175⁄13.6049⁄7.6828⁄

Parameter estimation is done at the following operating condi- tions: 40.01 C 1014.46 W/m² (case 1), 25.01 C 1004.63 W/m² (case 2), 55.09 C 1007.21 W/m² (case 3), 25 C 204.53 W/m² (case

4) and 35 C 203.22 W/m² (case 5). MATLAB environment is used to code and execute the proposed method. For studying the effectiveness of the proposed approach, the parameter estimation problem is also solved by the other metaheuristic algorithms and the results are compared. In all the investigated algorithms, the population size and maximum num- ber of iterations which have been set by trial and error are 30 and 2000, respectively. Setting of population size and maximum number of iterations is highly problem dependent (number of vari- ables and complexity of the search space). These parameters are usually set by trial and error. In this paper, a relatively small value
was considered for the population size and increased until the ideal value was found. Based on the convergence process of the algorithm, maximum number of iterations was set so that the algorithm can be able to be converged to the solution. The investigated algorithms are as follows: Particle swarm optimization (PSO) with adaptive inertia weight (PSO-w): learning rate c₁ = c₂ = 2; inertia weight linearly decreases from 0.9 to 0.4. PSO with constriction factor (PSO-cf): c₁ = c₂ = 2.01. Innovative global HS (IGHS): number of elite harmonies is set to 5; HMCR = 0.95; PARmax= 0.7; PARmin= 0.1; bwmax=1; bwmin= 0.0001. Grouping-based global HS (GGHS): HMCR = 0.95; PARmax= 0.7; PARmin= 0.1; bwmax=1; bwmin= 0.0001. Seeker optimization algorithm (SOA): wmax= 0.9; wmin= 0.1; lmax= 0.95; lmin= 0.0111.

Table 1 summarizes the statistical results of fitness function

values obtained over 30 independent runs. The results include the mean (Mean), the standard deviation (Std), the best (Best), and the worst (Worst) values on case 1. The results have been com- pared with those found by the other algorithms. Comparison of the

Table 3

The results obtained by SBMO and the other studied algorithms over 30 runs on case 2. Index PSO-w PSO-cf IGHS

|Index|PSO-w|PSO-cf|IGHS|GGHS|SOA|SBMO|
|---|---|---|---|---|---|---|
|Mean|0.6040925|1.1412444|0.0225511|0.0224065|0.0198860|0.0148394|
|Std|0.94118|1.67998|0.00433|0.00825|0.01047|0.0230804|
|Best|0.0541714|0.0807811|0.0084553|0.0072267|0.0126907|0.0071863|
|Worst|3.5571989|7.1429160|0.0278189|0.0487573|0.0729016|0.1144409|

Table 4

The results obtained by SBMO and the other studied algorithms over 30 runs on case 3.

|Index|PSO-w|PSO-cf|IGHS|GGHS|SOA|SBMO|
|---|---|---|---|---|---|---|
|Mean|0.0227540|0.0785677|0.0165562|0.0175014|0.0139666|0.0080271|
|Std|0.01441|0.06350|0.00594|0.00383|0.00384|0.0012568|
|Best|0.0067695|0.0082140|0.0066148|0.0091111|0.0076290|0.0061124|
|Worst|0.0821154|0.2801122|0.0254743|0.0220965|0.0200880|0.0123665|

Index PSO-w PSO-cf IGHS

Table 5

Case Conditions Rs(O) Rsh(O) 1 T = 25.01 C 0.10472 5.13413

GGHS SOA SBMO

GGHS SOA SBMO

I ph(A) Isd(lA) n RMSE

1.0729 0.04008 1.9998 0.0071863
The optimal parameters of the module model at different operating conditions related to the best performance of SBMO algorithm.

|1|T = 25.01|C|0.10472|5.13413|1.0729|0.04008|1.9998|0.0071863|
|---|---|---|---|---|---|---|---|---|
||G = 1004.63 W/m²||||||||
|2|T = 40.01 G = 1014.46 W/m²|C|0.07937|5.19247|1.0950|0.20948|1.9996|0.0056741|
|3|T = 55.09 G = 1007.21 W/m²|C|0.06925|5.39098|1.0842|0.94257|1.9957|0.0061124|
|4|T =25 C G = 204.53 W/m²||0.17716|12.2156|0.21389|0.02954|1.9999|0.0029154|
|5|T =35 C G = 203.22 W/m²||0.12332|12.9721|0.21105|0.08620|2|0.0021009|

0.25
Experimental -Case 4 Model -Case 4

0.2
1.2
Experimantal -Case 1 1 Model -Case 1

0.8
0.6
**Current (A)**

0.4
0.2 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 5. Comparison between the experimental data and the model results (case 1).

1.2
Experimantal -Case 2 Model -Case 2 1

0.8
0.6
**Current (A)**

0.4
0.2 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 6. Comparison between the experimental data and the model results (case 2).

0.15
**Current (A)**

0.1
0.05 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 8. Comparison between the experimental data and the model results (case 4).

0.25
Experimental -Case 5 Model -Case 5

0.2
0.15
**Current (A)**

0.1
0.05 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 9. Comparison between the experimental data and the model results (case 5).

t crit, is obtained ± 2.0017. This implies that if |t| > 2.0017, the per- formances of two algorithms are statistically different with 95% certainty. Table 2 represents the results of the two-tailed t-test. It can be seen that SBMO significantly outperforms all the algorithms. Tables 3 and 4 lists the SBMO results in comparison with the results obtained by the other algorithms on case 2 and case 3, respectively. It is seen that the SBMO performance is more prom- ising than the others. Considering case 4, the indexes obtained by SBMO are Mean = 0.0029766, Std = 0.0001111, Best = 0.0029154 and Worst = 0.0033310. For case 5, the value of Mean, Std, Best and Worst is 0.0022711, 0.0004266, 0.0021009 and 0.0039356, respec- tively. On cases 5 and 6, SBMO outperforms the other studied algorithms.

Table 5 shows the optimum value of the parameters of the mod-

ule model related to the best performance of SBMO algorithm for different cases. In real world, when insolation drops, short-circuit current of cell drops in direct proportion. If we compare the results of case 1 and case 5 where the temperature is equal and the ratio of insolation is close to 5, the ratio of Iphis close to 5 as well. More- over, it can be drawn that the diode ideality factor is independent on temperature and solar irradiance. In order to observe the quality of the fitting, the optimum parameters found by SBMO algorithm are returned to the module model and the I–V characteristic is reconstructed. This is simply performed by applying Newton method when Itis unknown while V tis known. Figs. 5–9 show the I–V characteristics at different operating conditions. It is clear that the model results are in

1.2
Experimantal -Case 3 1 Model -Case 3

0.8
0.6
**Current (A)**

0.4
0.2 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 7. Comparison between the experimental data and the model results (case 3).

results reveals that the performance of SBMO is quite promising. SBMO produces the best results in terms of all the indexes. On this case, the search power of the algorithms in terms of the Mean index can be ordered as SBMO > SOA > IGHS > GGHS > PSO- w > PSO-cf. In terms of the Best index, the best performance with the value of 0.0056741 belongs to SBMO and the other ranks belong to IGHS, SOA, PSO-w, GGHS and PSO-cf. To determine whether the results found by SBMO are statisti- cally different from the results of the other algorithms, two-tailed t-test with the level of significance set at a = 0.05 is investigated. In this case, the degree of freedom is 58 and hence, a critical value,

1.2
Experimental -Case 2 Model -Case 2 1

0.8
0.6
**Current (A)**

0.4
0.2 0 0 20 40 60 80 100 120 140
**Voltage (V)**

Fig. 10. Comparison between the I–V characteristics obtained by the experimental

data and the module model when considering only three pairs.

accordance with the experimental data. The successful perfor- mance of SBMO in finding the optimum parameters can be explained by this fact that it employs distinct patterns to move through the search space. So, it is more flexible than those algo- rithms which employ one pattern to update the position of theirs individuals. Seeking a search space with different patterns increases the probability of providing a good balance between exploration and exploitation and therefore finding the optimum solution. The experimental data used in the estimation process must cover all the region of system working. Using sufficient experimen- tal data leads to obtaining better fitness. To show this, the estima- tion process of case 2 is conducted using only 3 pairs of the experimental data, namely, the initial, knee and end points of the characteristic. As Fig. 10 indicates, the extracted model has high degree of accuracy at the used points and describes the system per- formance inadequately at the other points. It can be drawn that for obtaining high degree of accuracy, sufficient experimental data at the whole period of working must be used to discover the opti- mum values of the parameters.

# 5. Conclusion

In this paper, a recently invented population-based optimiza- tion algorithm, bird mating optimizer (BMO), is simplified and applied to solve the parameters estimation problem of PV modules model. The proposed SBMO modifies parameter setting and some rules of the original BMO. On the investigated case studies, simula- tion results reflect the superiority of SBMO in terms of accuracy when it is compared with the tested optimization algorithms. This means that SBMO has more global search ability. From the results, it can be drawn that when insolation drops, short-circuit current of cell drops in direct proportion and the diode ideality factor is inde- pendent on the temperature and solar irradiance. Moreover, the

promising performance of SBMO makes it an ideal method when dealing with optimization problems related to PV modules.

# Acknowledgement

Special thank is made from Mr. Jinqing Peng for providing the data.

# References

[1] Vatau Doru, Musuroi Sorin, Barbulescu Constantin, Babescu Marius. PV systems modelling and optimal control. Energy Convers Manage 2014;84:448–56. [2] Karami Nabil, Moubayed Nazih, Outbib Rachid. Energy management for a PEMFC–PV hybrid system. Energy Convers Manage 2014;82:154–68. [3] Almonacid F, Pérez-Higueras PJ, Fernández Eduardo F, Hontoria L. A methodology based on dynamic artificial neural network for short-term forecasting of the power output of a PV generator. Energy Convers Manage [4] Liu Yali, Ming Li Xu, Ji Xi Luo, Wang Meidi, Zhang Ying. A comparative study of 2014;85:389–98. the maximum power point tracking methods for PV systems. Energy Convers Manage 2014;85:809–16. [5] Ismail MS, Moghavvemi M, Mahlia TMI. Characterization of PV panel and global optimization of its model parameters using genetic algorithm. Energy [6] Convers Manage 2013;73:10–25 AlRashidi MR, AlHajri MF, El-Naggar. KM, Al-Othman AK. A new estimation approach for determining the I–V characteristics of solar cells. Sol Energy 2011;85:1543–50. [7] Ishaque K, Salam Z. An improved modeling method to determine the model parameters of photovoltaic (PV) modules using differential evolution (DE). Sol Energy 2011;85:2349–59. [8] Easwarakhanthan T, Bottin J, Bouhouch I, Boutrit C. Nonlinear minimization algorithm for determining the solar cell parameters with microcomputers. Sol [9] Energy 1986;4:1–12 Chan DSH, Phillips JR, Phang JCH. A comparative study of extraction methods. for solar cell model parameters. Solid-State Electron. 1986;29:329–37. [10] Jian A, Kapoor A. Exact analytical solutions of the parameters of real solar cells [11] using Lambert W-function. Sol Energy Mater Sol Cells 2004;81:269–77 Saleem H, Karmalkar S. An analytical method to extract the physical. parameters of a solar cell from four points on the illuminated J–V curve. IEEE Electron Device Lett 2009;30:349–52. [12] El-Naggar KM, AlRashidi MR, AlHajri MF, Al-Othman AK. Simulated annealing algorithm for photovoltaic parameters identification. Sol Energy 2012;86:266–74. [13] Askarzadeh A, Rezazadeh A. Parameter identification for solar cell models [14] using harmony search-based algorithms. Sol Energy 2012;86:3241–9 Askarzadeh A, Rezazadeh A. Artificial be swarm optimization algorithm. for parameter identification of solar cell models. Appl Energy 2013;102:943–9. [15] Askarzadeh A, Rezazadeh A. A new heuristic optimization algorithm for modeling of proton exchange membrane fuel cell: bird mating optimizer. Int J Energy Res 2012. <u>[http://dx.doi.org/10.1002/er.2915](http://dx.doi.org/10.1002/er.2915)</u>. [16] Askarzadeh A, Rezazadeh A. Artificial neural network training using a new efficient optimization algorithm. Appl Soft Comput 2013;13:1206–13. [17] Chegaar M, Ouennoughi Z, et al. A new method for evaluating illuminated solar cell parameters. Solid-State Electronics 2001;45(2):293–6. [18] Villalva MG, Gazoli JR, et al. Comprehensive approach to modeling and simulation of photovoltaic arrays. IEEE Trans Power Electron [19] 2009;24(5):1198–208 Askarzadeh A. Bird mating optimizer: an optimization algorithm inspired by. bird mating strategies. Commun Nonlinear Sci Simulat 2014;19(4):1213–28. [20] Katayama K, Narihisa H. On fundamental design of parthenogenetic algorithm for the binary quadratic programming problem. In: Proceedings of congress on evolutionary computation. vol. 1; 2001. [21] Barukcˇic´ M, Nikolovski S, Jovic´ F. Hybrid evolutionary-heuristic algorithm for capacitor banks allocation. J Electrical Eng 2010;61(6):332–40. [22] Wu J, Wang H. A parthenogenetic algorithm for the founder sequence reconstruction problem. J Comput 2013;8(11):2934–41.
