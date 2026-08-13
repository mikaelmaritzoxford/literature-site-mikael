## Matrix method for thin film optics

### Leandro N. Acquaroli

Department of Engineering Physics, Ecole Polytechnique Montreal

P.O. Box 6079, Station Centre-Ville, Montreal (QC) H3C 3A7, Canada
September 21, 2018

Review of a matrix method used in optics of thin films for the calculation of reflectance, transmittance, absorptance, the electric field distribution inside the stack and the photonic dispersion considering the stack as perfect unidimensional crystals —Distributed Bragg mirrors—. We emphasizes the discussion on transfer matrices and give an alternative approach with scattering matrices for the propagation of light as plane waves through a homogeneous layered system.

**Fig. 1:** Scheme of a multilayer stack comprising *j* = 1*,..,M*

layers —media—, where *dj* is the geometrical thickness of each layer, *θj* is the angle of incidence in the medium normal to the surface, *N₀* is the index of refraction of the incident medium, *Nj* is the index of refraction of each layer, and *NM*+1 is the index *±* of refraction of the substrate. *F~l*indicates the vector field —electric for a p-wave (TM) and magnetic for a s-wave (TE)— measured before and after crossing interface *l*, that travels *′* towards *±x*. The symbol indicates those quantities located (12) behind —after crossing the interface— the optical surfaces.

Thin films are present in diverse applications due to the effective control provided by advanced deposition and electrochemical techniques in the synthesis processes. Func- tional multilayer stacks offer a broad range of flexibility for their use in optical filters, antireflection coatings and Fabry-Pèrot interferometers (1–4). The transfer matrix method —TMM— reviewed here aims to help predicting the behavior of multilayer thin films structures in a given configuration. The TMM al- lows analyzing different thin film designs such as single films (5,6), Bragg mirrors —crystals—, quasycristals —e.g. Fibonacci or Thue-Morse structures— according to reflec- tion, transmission, absorption and electromagnetic field distribution (7,8). It proved to be useful to calculate the photonic dispersion —bands structure— for perfect crystals and to model porosity and thickness gradients

(9). Optoflu-
idic techniques also take advantage of TMM studying the imbibition dynamics inside thin film nanostructures (10,11). We focus on transfer matrices and discuss alternative equa- tions with scattering matrix. We present the thin film optical theory by steady state Maxwell’s equations for the propagation of light through a system of multilayers, assuming the following hypothe- sis (12) :

- An optically isotropic medium describes the mass of a thin film, characterized by an index of refraction *N ∈* C.
- A plane separates two consecutive media with different index of refraction.
- The variation of the index of refraction occurs in the direction normal to the multilayer structure —normal inhomogeneity—.
- Two planes define a layer in the propagation axis. The other dimensions of the layer extend to infinity.
- The magnitud of the thickness of a layer is in the order of the wavelength of the incident light.
- The incident wave is plane, monochromatic and linearly polarized (p or s) respect to the plane of incidence. Consider the following physical aspects that the TMM
(12) ignore, but they exists :

- Dispersion of absorption of light caused by polycrys- talline structures of evaporated thin films.
- The roughness of the substrate and planes —interfaces— dividing the layers.
- Anisotropy due to internal structures of the material.
- Temporal dependence of the index of refraction and thickness —e.g. aging effects—. To study the reflection and transmission of the elec-
tromagnetic radiation of a multilayer stack, we consider one-unidimensional structures alternating layers with differ- ent indexes of refraction in any order —Fig.1—. Assuming a wave traveling from *−x* to +*x* reflecting at each inter- face and refracting at each layer of a system composed by *M* layers, where the wave pass through the last layer experimenting refraction only. These conditions define the dielectric structure as follows:  *N₀, x < x₁,*      *N ,*1*x₁ < x < x₂,* *N* (*x*) = *··· ···* (1)     *NM, xM −< x < xM,*   *NM*+1*, xM< x,*

where *xl*is the position at interface *l*. Maxwell’s equations

1 of6

# arXiv:1809.07708v1 [physics.optics] 20 Sep 2018

*L. N. Acquaroli. **Matrix method for thin film optics**.*
**Fig. 2:** Orientation of the coordinates system, electromagnetic

(12) field and its propagation.

**Fig. 3:** Scheme of the fields’ projections of s- and p-wave. *n*ˆ is

the normal vector. *n*ˆ is the vector normal to the surface given by interface *l*, *~q* = *uq*ˆ is the wavevector, *u*ˆ is a unitary vector in (12) the direction of propagation and *θ* is the angle of incidence. for a linear, non-dispersive, homogeneous, isotropic and without free charges medium read (13)

<u>∂E</u> <u>~</u> *∇×* *~ H~* = *ε, ∇~ **·** H~* = 0*,* *∂t* <u>∂H</u> <u>~</u> *∇×* *~ E~* = *−µ, ∇~ **·** E~* = 0*,* *∂t*

||+|−|′+|′−|
|---|---|---|---|---|
|l|l|l|l|l|
|l|l+|l−|l′+|l′−|

where *ε* and *µ* are the electric permittivity and magnetic permeability of the material, respectively —for dielectric media, *µ* = 1—. We can write the plane wave solution¹ to these equations as follow (15,16) :

*F* *~* = *F~* exp[*i*(*~q **·**~r − ωt*)]*,* (2)

*~ ~* where *F~* is the amplitud of the field *F* —*F* = *E~* for p- *~* waves (TM) or *H* for s-waves (TE)—, *~q* = *xq*ˆ*x*+ *zq*ˆ*z*is the wavevector propagation in the medium and *~r* = *xx* ˆ +*yy*ˆ +*zz*ˆ 2 2 2 is the position vector. The wavevector *qx,j*= *q − qz*=

|||||||~|~|
|---|---|---|---|---|---|---|---|
|2 2|2 2|2|2|2|j|||
|j j|j|||||||
||(6) + + l l −|− x,j x,j|l l||(15)|+ l l ′+ j l + j ′+ j+1 l|− l l ′− l − ′− j+1 l|

2 2 2 2 2 2 2 *q −* <u>q</u> sin *θ* = *q* (1 *−* sin *θ*) = *q* cos *θ*, where *qj*= *√* *q₀ ε µ* = *q₀N*, and *q₀* = *ω/c* = 2*π/λ* is the wavevector in free space. For a steady state problem, we can simplify Eq. (2) as a linear combination of waves traveling to *−x* —regressive waves— and to +*x* —progressive waves— :

*F* *~* (*x*) = *F~* (*x*) + *F~* (*x*) (3)

### = F~ exp[iq (x − x)]+

### F~ exp[−iq (x − x)]. (4)

We orient the set {*E~*, *H~*, *~q*} for the incident and reflected waves in such a way that for normal incidence both polar-

|+|− ′+|′−||
|---|---|---|---|
|l|l l|l||
|+|−|′+|′−|
|j l j|l j+1|l j+1|l|

ization produce the same results respect to the phase vector *E~* (12) : a change in the axis containing *H~*, keeping the axis containing *E~* unchanged after reflection. The orientation of the set remains unaltered in the refracted wave respect to the incident wave —Fig.2—. The optical theory of multilayers consists in repeating the boundary conditions of a simple plane dividing two media, coherently coupling the consecutive boundaries affected by the phase changes applied to the progressive and regressive waves. We can write the boundary conditions taking the tangential components of the electromagnetic fields, *H~*tan= *H* *~* y *E~* tan= *E* *~*, since they conserve at each side of an

|tan|+|−|′+|′−|
|---|---|---|---|---|
|(15,17)|j l|j l|j+1 l|j+1 l|
|Different authors define it adopting j = −i|l+|l−|l′+ l′−||

interface, employing progressive and regressive waves.

(12,14).

The boundary conditions for an interface *l* establish the conservation of the tangential fields at each side of the interface (12) : *~ ~ ~ ~ ~* *E* = *E* + *E* = *E* + *E* (5a)

*H* *~* = *H~* + *H~* = *H~* + *H~.* (5b)

We define the admittance of a medium *ζ* = √*ε/µ*. Ac- cording to Fig.3, the electric field is perpendicular to the surface of incidence, thus, *E~* = *E~*, while the magnetic field relates to the tangential component as *u*ˆ*× H~* cos*θ* = *n*ˆ*× H~*, where *u*ˆ is the unitary vector in the direction of the wavevec- tor *~q*. The relation between the tangential components of the fields for a s-wave is then

*n*ˆ *× H~* = *−ζ E* cos*θ* = *−s E,* (6)

where the parameter *s* = *ζ* cos*θ*. Taking the cross vector of *n*ˆ by (5b) and using (6) we have:

*~ ~ ~* *n*ˆ *× Hl*= ˆ*n × H* + ˆ*n × H*

= ˆ*n × H~* + ˆ*n × H~*

### = s E~ − s E~

= *s E~ − s E~.* (7)

Then, substituting Eq. (7) in (5b), the system rearranges as follow:

*E* *~* + *E~* = *E~* + *E~* (8a)

*s E~ − s E~* = *s E~ − s E~.* (8b)

Performing the same analysis for the p-wave with the mag- *~ ~* netic field normal to the surface of incidence, *H* = *H*. Hence, the relation between the electric field with tis tan- *~ ~* gential component is *n*ˆ *× E* = ˆ*u × E* cos*θ*. Then,

*n*ˆ *× E~* = <u>1</u> *H* *~* cos*θ* = *s H, ~* (9) *ζ*

where *s* = cos*θ/ζ*. Taking the cross vector of *n*ˆ by (5a) and using (9), the new system reads: + *− ′*+ *′−* *s H~ − s H~* = *s H~ − s H~* (10a)

*H* *~* + *H~* = *H~* + *H~,* (10b)

2 of6

where the negative sign of the last equation is due to that *H* *~* relates to *E~* through *−n*ˆ for the regressive character of the wave. We define the characteristic matrix of a layer *j* by [] 1 1 *Γj*= s-wave*,* (11a) *s* *j−sj* [] *s* *j−sj* *Γj*= p-wave*,* (11b) 1 1

where *ΓjΓj−* 1 = *I*, the identity matrix. Thus, systems (8) and (10) in matricial form read: [ +] [ *′*+] *F~* *l−* *F~* *l′−* *Γj−*1 *~* = *Γj* *~* (12) *F* *l* *F* *l* or [] [] *F~* *l* + *F~* *l* *′*+ *−*1 *−*= *∆j−*1*,j ′−, ∆j−*1*,j*= *Γj−*1*Γj.* (13) *F~jF~* *l*

Equation (13) describes the relation between the incoming and outgoing fields at the interface *j*, where *∆* is the transfer (15) matrix —also called transformation or refraction ma- (12) trix —, that satisfies the relation det*{∆j−*1*,j}* = *sj/sj−*1. After crossing the interface *l* the wave propagates certain distance until the next interface *l*+1. The distance between these two consecutive interfaces equals the thickness of the layer *j*, *dj*. The progressive and regressive waves, according to (4), are:

*F~* *l* + (*xl*= 0) = *F~* *l* + (14a)

*F~* *l* *−* (*xl*= 0) = *F~* *l* *−* (14b)

*F~* *l* + +1 (*xl*+1= *dj*) = *F~* *l* + +1 exp(*iqx,jdj*) (14c)

*F~* *l* *−* +1 (*xl*+1= *dj*) = *F~* *l* *−* +1 exp(*−iqx,jdj*)*.* (14d)

Combining (14a) with (14c) and (14b) with (14d) we have:

*F~* *l* +

(0) = *F~* *l* + +1
(*d*) exp(*−iqx,jdj*) (15)
*F~* *l* *−*

(0) = *F~* *l* *−* +1
(*d*) exp(*iqx,jdj*)*.* (16)
A general expression results writing the previous equations in matricial form: [ *′*+] [ *−iϕ*] [ +] [ +] *F~* *l* *ej*0 *F~l*+1*F~l*+1 *′−*=*iϕj −*= *Υj −,* (17) *F~* *l* 0 *e F~* *l*+1 *F~* *l*+1

where <u>2π</u> *ϕj*= *qxdj*= *Njdj*cos*θj*(18) *λ* is the phase shift angle experimented by the wave after

(6) (12)
crossing the layer *j*. *Υj*is the propagation or phase matrix, which is unimodular: det*{Υj}* = 1. Merging the matrices relating the fields at both sides of the interface and the propagation through a layer, we can compute the total matrix of a multilayer structure, using (12) Eqs. (13) and (14) for a total number of *M* layers : [ +] *F~*1 *−*= *∆*0*,*1*Υ₁∆*1*,*2*Υ₂ ···* *F~*1 [] *F~M* *′*+ +1 *··· ∆M −,MΥM∆M,M*+1 *~′−*

*.* (19)
*FM*+1

Taking the product of the r.h.s. of the last expression previous to the column vector, we define the total transfer matrix of the system, *Ω*, as follow:

[]*j*=*M*[] [] *F~* + ∏ *F~* *′*+ *F~* *′*+ 1 *−*= *∆j−*1*,jΥj∆j,j*+1 *M* *′−* +1 = *Ω* *M* *′−* +1 *.* *F~ F~ F~* 1 *j*=1 *M*+1 *M*+1

(20)

The matrix *Ω* relates the tangential components of the fields + and *−* at the extremes of the multilayer. We define the interference matrix *Φ* for both polarization as (6,15,18) *j* [ cos*ϕ −*(*i/s*) sin*ϕ*] *Φj*= *ΓjΥjΓ* *−*1 = *j j j*

*.* (21)
*j* *−isj*sin*ϕj*cos*ϕj*

*Φ* is unimodular and it relates to the transfer matrix of the system *Ω* as follow (12,6) :   *j*=*M* *−*1 ∏ *−*1 *Ω* = *Γ₀*  *Φj* *ΓM*= *Γ₀ ΨΓM*+1*.* (22) *j*=1

where *Ψ* is the interference matrix of the system and es- tablish the transformation of the incoming and outgonig tangential total fields in the system, [] [] *E* *~* 1*E* *~* *M*+1 *~* = *Ψ* *~*

*.* (23)
*H₁ HM*+1

We can further use the matrix theory described until now to calculate the reflection, transmission and absorption spectra of the multilayer structure in terms of the transfer and the interference matrices. Expanding Eq. (20)

*F* *~*+= *ω F~′*++ *ω F~′−*(24a) 1 1*,*1 *M*+1 1*,*2 *M*+1 *F* *~−*= *ω F~′*++ *ω F~′−,* (24b) 1 *M*+1 *M*+1 2*,*1 2*,*2

the reflection *r*˜ and transmission *t*˜ Fresnell coefficients for both directions of incident light can be determined. Con- sider first the progressive waves, *F~M* *′−* +1= 0, i.e. after crossing the last layer, the wave does not undergoes any reflection. Then,

<u>~</u>*−* +<u>F₁ ω₂,1</u> *r*˜ = = (25) *F~*1+*ω₁,*1 + <u>F</u> *~* <u>1</u> *t* ˜ + = <u>M+1</u> =*.* (26) *F~* +*ω₁* *,*1 1

For regressive waves, *F~*1 + = 0, then

<u>F</u> *~′−* *r*˜ *−* = <u>M+1</u> = *−* <u>ω₁,2</u> (27) *~′*+ *FM*+1*ω₁,*1

*−F~*1 *−* <u>1</u> *t* ˜ = = det*{Ω}.* (28) *F~* *′−ω₁* *,*1 *M*+1 *Ω* results from the product of *∆* and *Υ*, thus, det*{*Ω*}* = *s s* *−*1, leading to the important relation (12) : *M*+1 0

*t* ˜ *−* = <u>s</u> <u>M+1</u> *t* ˜ +

*.* (29)
*s₀*

According to Eq. (22) we can relate the elements of *Ω*

3 of6

### with those of Ψ

### ω₁,= (s₀ψ₁,+ ψ₂,+

*s₀sM*+1*ψ₁,*+ *sM*+1*ψ₂,*) (30a) <u>1</u> *ω₁,*2= (*s₀ψ₁,*1+ *ψ₂,*1*−* 2 *s₀sM*+1*ω₁,*2*− sM*+1*ψ₂,*2) (30b) <u>1</u> *ω₂,*1= (*s₀ψ₁,*1*− ψ₂,*1+ 2 *s₀sM*+1*ψ₁,*2*− sM*+1*ψ₂,*2) (30c) <u>1</u> *ω₂,*2= (*s₀ψ₁,*1*− ψ₂,*1*−* 2 *s₀sM*+1*ψ₁,*2*− sM*+1*ψ₂,*2)*.* (30d)

and then calculate the reflection and transmission coeffi- cients as follow (12,17) :

+<u>s₀ψ₁,1− ψ₂,1+ s₀sM+1ψ₁,2− sM+1ψ₂,2</u> *r*˜ =*,* *s₀ψ₁,*1+ *s₀sM*+1*ψ₁,*2+ *ψ₂,*1+ *sM*+1*ψ₂,*2 (31) <u>2</u> *t* ˜ + =*.* (32) *s₀ψ₁,*1+ *s₀sM*+1*ψ₁,*2+ *ψ₂,*1+ *sM*+1*ψ₂,*2

The expression for the reflectance and transmittance from the coefficients derived are:

*R* = ˜*r* *±* (˜*r* *±* ) *∗* (33) ˜ *±*˜*± ∗* *T* = *s₀sM*+1*t* (*t*)*,* (34)

where *∗* denotes the complex conjugate. Cisneros *et. al* explain that (34) is valid when the last medium is non- (15) absorbent, although, a more general expression is pro-

(2)
posed taking the real part, *ℜ*[*sM*+1]. We do not include the absorptance in terms of the matrix elements, as it is (15) simply calculated by *A* = 1 *− T − R*. There exists a direct relation between the absorption and the intensity of the field at any point inside the multilayer structures. Computing the electromagnetic field distribu- tion allows to analyze important effects such as the damage induced by a laser radiation on the layers, in which the ab- (14,19–22) sorption transforms into incident heat energy. The enhancement of the field inside Fabry-Pèrot type cavities provoque an increase in the FTIR and Raman signals, which is useful to study intrinsically weak vibrational modes (23). We define normalized field distribution as follow (14)

<u>|F~(x)|</u> 2 *I* = + *,* (35) *|F~*1*|*2

where *F~*(*x*) is the total field at the position *x* inside the multilayer, and *F~*1+is the incident field of the progressive wave, where *x* = 0 is the origin of the first layer in the stack. Since the wave travels towards +*x*, Eq. (24a) establish that *F~M* *′−* +1= 0, then *F~*1 + = *ω₁,*1*F~M* *′*+ +1for the first interface. The next step is to calculate the field as a function of the position *x*. A simple approach to do this is taking the *−*1 product between the total matrix *Ψ* by *Ξ* = *Φ* : [] cos*ϑ‘*(*i/s‘*) sin*ϑ‘* *Ξ‘*=*,* *is‘*sin*ϑ‘*cos*ϑ‘*

where the elements varies for each position inside the mul-

tilayer through the phase shift angle *ϑ‘*: ( <u>π</u> ) *ϑ‘*= *N‘d‘*cos*θ‘.* *h λ*

The constant *h* is the number of times we divide the phase shift angle to compute the electromagnetic field at the position *x ∈* [0*,h · M*]. Taking the product of *Ξ* times the total *Ψ*, ( ∏ *x* )

*G*(*x*) = Ξ*‘Ψ ,* *‘* determines the field at each position through

*F~*(*x*) = [*g* (*x*) + *g* (*x*) *s*]*F~* *′*+ *,* 1*,*1 1*,*2 *M*+1 *M*+1

where *g* are the elements of the matrix *G*. The intensity ratio —Eq. (35)— takes the final form: 2 <u>|g₁,1(x) + g₁,2(x) sM+1|</u> *I*(*x*) =*.* (36) *|γ₁,*1*|*2

A wave in a periodic system travels similarly to electrons in a crystalline solid. Hence, we can borrow the mathemat- ical formulation for the band theory in solids and apply it to the electromagnetic propagation in periodic media, along with the concepts of Bloch waves, Brillouin zone and band-gaps. A binary —alternates two media with different index of refraction— periodic system resembles an unidi- mensional lattice invariant to translation operation. The relation between the waves amplitudes in a unit cell of a periodic multilayer is

(9) :
[ +] [ +] *F* *~ F~* *l* = ∆*j,j*+1Υ*j*+1∆*j*+1*,j*+2Υ*j*+2 *l*+2 *F~* *−* *F~* *−* *l l*+2 [ *~*+] *F* *l−*+2 = *U,* (37) *F* *~* *l*+2

where *U* is the translation operator in the unit cell. Ac- cording to Bloch’s —Floquet— theorem a wave propagates in a periodic system in the form of (14)

*~ ~* *FK*(*x,z*) = *FK*(*x*) exp (*iKx*) exp (*iq zz*) (38)

where *F~K*is periodic with period Λ, where Λ —unit cell— results from adding the thicknesses of the two layers with different indexes of refraction gives the period: *~ ~* *FK*(*x* + Λ) = *FK*(*x*)*.* (39)

The quantity to determine is the constant *K*, the Bloch wavevector. Rewriting condition (39) in terms of Eq. (4), results in [] [ +] + *F~* *l* *F~* *l*+2 *F~* *−*= exp (*−iK*Λ) *F~* *−.* (40) *l l*+2

Combining Eqs. (39) and (40) we note that the Bloch wave satisfies the following eigenvalue equation: [ +] [ +] *F~ F~* *U* *l* = exp (*iK*Λ) *l*

*.* (41)
*F~* *−* *F~* *−* *l l* The phase factor is the eigenvalue of the translation operator

4 of6

**Fig. 4:** (a) Incoming and outgoing waves at an interface.

(b) Scattering of incoming waves in terms of the scattering
++ *−−* *−*+ +*−* coefficients *t*, *t*, *r* and *r*.

*U*, given by

*±iK*Λ<u>1</u> *e* = (*u₁,*1+ *u₂,*2)*±* 2 { [] }1*/*2 2 <u>1</u> *i* 1 *−* (*u₁,*1+ *u₂,*2)*.* (42) 2

Equation (41) allows to calculate the corresponding eigen- vectors as follow, [ +] [] *F~*1*u₁,*2 *−*=*.* (43) *F~*1exp (*−iK*Λ) *− u₁,*1 (14) multiplied by an arbitrary constant. The Bloch waves (43) are the eigenvectors of the translation oper- ator with eigenvalues exp (*±iK*Λ) given by (42). Both eigenvalues are inverse to each other since the matrix *U* is unimodular. Equation (42) describes the relation disper- sion between the frequency *$*, the wavevector *qz*and the Bloch vector *K* for the Bloch wave function: <u>1</u> *K*(*$,qz*) = arccos [tr(*U*)] Λ [] <u>1 1</u> = arccos (*u₁,*1+ *u₂,*2)*.* (44) Λ 2

Three regimes arise from Eq. (44). When *|*1*/*2(*u₁,*1+ *u₂,*2)*| <* 1, *K* is real and the Bloch wave propagates, while if *|*1*/*2(*u₁,*1+ *u₂,*2)*| >* 1, then *K* = *mπ/*Λ + *iKi*has an imaginary component and the Bloch wave is evanescent. These last waves represent forbidden band-gaps in a peri- odic system. The edges of the bands locate in the regime where *|*1*/*2(*u₁,*1+ *u₂,*2)*|* = 1. An alternative expression for the dispersion relation expanding (44) results as follow,

<u>1</u> cos(*K*Λ) = [2 cos*ϕ₁* cos*ϕ₂* 2] <u>(s²1+ s²2)</u> *−* sin*ϕ₁* sin*ϕ₂,* (45) *s₁s₂*

where *ϕ* is the phase shift angle from (18). An alternative approach to the TMM formalism which is the scattering matrices method, defined as *X* matri- ces (13,24). The base of this method is to express the out-

going waves from a scattering center as a function of the incoming waves —Fig.4—. The scattering relations require the amplitudes to satisfy

*F~* *l* *′*+ = *t* ++ *F~* *l* + + *r* +*−* *F~* *l* *′−* (46)

*F~* *l* *−* = *r* *−*+ *F~* *l* + + *t* *−−* *F~* *l* *′−*

*.* (47)
In matricial form the last equation reads: [ +*−*][ *′*+] [ ++][ +] 1 *−r F~* *l* *t* 0 *F~* *l* *−−*=*−*+*.* (48) 0 *t F~* *l′−* *−r* 1 *F~* *l−* Inverting the matrix on the left of Eq. (48), results [ *′*+] [ ++ +*− −− −*1 *−*+ +*− −− −*1][ +] *F~* *l* *t − r* (*t*) *r r* (*t*) *F~* *l* =*−− −*1 *−*+ *−− −*1 *F~* *l′−* *−*(*t*) *r* (*t*) *F~* *l−* (49) [ +] *F~* *l−* = *X* *~*

*.* (50)
*F* *l* The expressions relating the transfer matrix with the scat- tering matrix at an interface results from the combination of Eqs. (13) and (49): [ ++ +*− −− −*1 *−*+ +*− −− −*1]*−*1 *t − r* (*t*) *r r* (*t*) *∆* =*−− −*1 *−*+ *−− −*1(51) *−*(*t*) *r* (*t*) [ *−*1 *−*1]*−*1 *δ₁,*1*− δ₁,*2*δ₂,*1*δ₂,*2*δ₁,*2*δ₂,*2 *X* =*−,*1 *−,*1*.* (52) *−δ₂,*1*δ₂*2*δ₂*2

For a wave crossing an homogeneous layer the scattering matrix turns out to be: [ *−iϕ*] *e* 0 *X* =*−iϕ,* (53) 0 *e*

where *ϕ* is the phase shift angle. Notice that this equation differs from that expressed by *Υ* in Eq. (17). We can summarize the main characteristics of the TMM as follow:

- Efficiently calculates the optical spectra of arbitrary ordered multilayer systems.
- Handle complex index of refraction denoting the gain- ing or absorption for cases of negative or positive index of refraction. When the index is real it ideally behaves without dissipation of energy —lossless material—.
- The thicknesses of the layers can take any value. Al- though, we can expect incoherence effects.
- Suitable to calculate the distribution of the electric field throughout a multilayer stack.
- Assumes the plane perpendicular to the direction of propagation to be infinite, implicating that each layer extends infinitely in other dimensions. The incident and outgoing —substrate— media are semi-infinite.
- Calculates the fields in the structure propagating from one layer to the next one by matrix relations, making the computational cost dependable on the number of layers.
- Limited to waves traveling continuously without pulses of propagation, where finite difference techniques be- comes useful.
- Handle dispersion relations for perfect crystals or peri- odic binary systems.
5 of6

[1] J. A. Dobrowolski. Fundamentals, techniques, and design. In *Handbook of Optics*, volume 1, chapter 42. McGraw-Hill, New York, 2 edition, 1994. [2] H. A. Macleod. *Thin -Film Optical Filters*. Institute of Physics Publishing, 3 edition, 2001. [3] O. Bisi, E. Ossicini, and L. Pavesi. Porous silicon: A quantum sponge structure for silicon based optoelectronics. *Surface Science Reports*, 38:1–126, 2000. [4] W. Theiß. Optical properties of porous silicon. *Surface* *Science Reports*, 29(3–4):91–192, 1997. [5] P. Yeh, A. Yariv, and C. S. Hong. Electromagnetic propaga- tion in periodic stratified media. i. general theory. *Journal* *of the Optical Society of America*, 67(4):423, 1997. [6] J. A. Monsouri, R. A. Depine, and E. Silvestre. Porous silicon: A quantum sponge structure for silicon based op- toelectronics. *Journal of the European Optical Society -* *Rapid Publications*, 2:07002, 2007. [7] R. Urteaga, O. Marín, L. N. Acquaroli, D. Comedi, J. A. Schmidt, and R. R. Koropecki. Enhanced photoconduc- tivity and fine response tuning in nanostructured porous silicon microcavities. *Journal of Physics: Conference Series*, 167(1):012005, 2009. [8] L. N. Acquaroli, R. Urteaga, and R. R. Koropecki. Innova- tive design for optical porous silicon gas sensor. *Sensors* *and Actuators B: Chemical*, 149(1):189 – 193, 2010. [9] E. X. Pérez. *Design, fabrication and characterization of* *porous silicon multilayer optical devices*. PhD thesis, Uni- versitat Rovira I Virgili, Tarragona, 2007. [10] L. N. Acquaroli, R. Urteaga, C. L. A. Berli, and R. R. Koropecki. Capillary filling in nanostructured porous silicon. *Langmuir*, 27(5):2067–2072, 2011. [11] R. Urteaga, L. N. Acquaroli, R. R. Koropecki, A. San- tos, M. Alba, J. Pallarès, L. F. Marsal, and C. L. A. Berli. Optofluidic characterization of nanoporous mem- branes. *Langmuir*, 29(8):2784–2789, 2013.

[12] Z. Knittl. *Optics of Thin Films (An Optical Multilayer* *Theory)*. John Wiley & Sons, Czechoslovakia, 1976. [13] B. E. A. Saleh and M. C. Teich. *Fundamentals of photonics*. John Wiley & Sons, 2 edition, 2007. [14] O. Arnon and P. Baumeister. Electric field distribution and the reduction of laser damage in multilayers. *Applied* *Optics*, 19(11):1853, 1980. [15] J. I. Cisneros. *Ondas Eletromagnéticas. Fundamentos e* *aplicações*. Editora da UNICAMP, Campinas, SP Brasil,

2001.
[16] J. D. Jackson. *Classical Electrodynamics*. John Wiley & Sons, 3 edition, 1998. [17] F. J. Pedrotti and L. S. Pedrotti. *Introduction to Optics*. Prentice Hall, USA, 2 edition, 1992. [18] L. Plattner. *A Study in Biomimetics: Nanometer-scale,* *high-efficiency, dielectric diffractive structures on the wings* *of butterflies and in the silicon chip factory*. PhD thesis, University of Southampton, 2003. [19] J. H. Apfel. Electric fields in multilayers at oblique inci- dence. *Applied Optics*, 15(10):2339, 1976. [20] J. H. Apfel. Optical coating design with reduced electric field intensity. *Applied Optics*, 16(7):1880, 1977. [21] F. Demichelis, E. Mezzetti-Minetti, and E. Tresso. Opti- mization of optical parameters and electric field distribution in multilayers. *Applied Optics*, 23(1):165, 1984. [22] D. Patel, D. Schiltz, P. F. Langton, L. Emmert, L. N. Acquaroli, C. Baumgarten, B. Reagan, J. J. Rocca,

W. Rudolph, A. Markosyan, R. R. Route, M. Fejer, and
C. S. Menoni. Improvements in the laser damage behavior of Ta₂O₅/SiO₂ interference coatings by modification of the top layer design. *Proc. SPIE*, 8885:8885–1 – 8885–5, 2013.
[23] G. Mattei, G. Marucci, and V. A. Yakovlev. Splitting of porous silicon microcavity mode due to the interaction with si–h vibrations. *Materials Science and Engineering B*, 51(1–3):158, 1998. [24] J. B. Pendry. Waves in 1d disordered systems. *Advances* *in physics*, 43(4):461–542, 1995.

6 of6
