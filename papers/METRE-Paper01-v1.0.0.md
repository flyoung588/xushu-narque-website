---
title: "Recursive Productive Capacity: An Intergenerational Evidence Framework for Autonomous Machine Economies"
author: "Fei Yang"
date: "14 October 2026"
lang: en-US
---

**Article type:** Conceptual and methodological research article.  
**JEL classification:** D81, O33, O41, C61.  
**Keywords:** recursive productive capacity; intergenerational reproducibility; autonomous production; science–production feedback; joint-service feasibility; probabilistic viability; evidence-based economic decisions; organizational permissions.

# Abstract

Machine-operated production and research may eventually alter not only the quantity of present output but also the productive services that subsequent systems can reproduce. Existing economic models address capital reproduction, endogenous innovation, production networks and automated research feedback; formal methods address stochastic viability and multiobjective certificates. This paper contributes a domain-specific **intergenerational evidence framework** that connects those established mechanisms for a distinct measurement task: deciding whether a *joint* configuration of services can be delivered and renewed across at least two production generations under a single admissible, observation-adapted policy. The framework separates one-time output, physical capital renewal, independently qualified scientific methods, organizational execution rights and economic valuation. It specifies time-indexed energy, materials, equipment, permission and risk records; supplies two elementary counterexamples showing why separate feasible services and coarse current-output accounts cannot certify joint renewal; and illustrates a two-renewal synthetic schedule with explicit falsification cases. A five-stage investment example distinguishes serial conditional probabilities from latent marginal probabilities and shows that unknown dependence can reverse both certification and investment decisions. A fully informed Bellman benchmark reproduces the same optimal policy, ruling out any claim of intrinsic optimization superiority. The paper's distinct output is therefore a transparent cross-domain *measurement contract*, not a new growth theorem, stochastic-control algorithm or empirical proof of autonomous industrial reproduction. It specifies an equal-information, full-cost evaluation that could establish—or reject—the protocol's practical value. The result is a bounded foundation for cumulative economic investigation of physically and scientifically recursive production.

# Introduction — From Producing Output to Producing Future Producers

A production system can enlarge future opportunity by producing equipment, improving its design and expanding scientific knowledge. Economists have long analyzed capital-producing sectors, endogenous technological change and production-network adaptation (von Neumann, 1945; Romer, 1990; Acemoglu and Azar, 2020). More recent work addresses the macroeconomics of automated physical production and automated research (Trammell and Korinek, 2026; Davidson et al., 2026). None of these phenomena becomes new merely because machines perform them. A useful foundational contribution must specify a sharper analytical or measurement problem and place it honestly against these precedents.

Consider a machine-operated production system with installed tools, energy and material rights, a laboratory, a fixed sponsor objective and a constrained financing envelope. It may conduct experiments, validate recipes, manufacture replacement equipment and delegate installation or procurement decisions. A profitable plant can nevertheless lose its essential production capability if it depends on a sole replacement component or cannot lawfully transfer a qualified design to a factory before a deadline. Conversely, a system with lower current output might preserve alternative renewal routes. These states differ even if present accounting values look identical.

The central question is **which joint productive services a successor system can actually deliver and renew**, over specified generations, with admissible information, time, resources, independent scientific qualification and organizational authority. The question concerns the economic state transmitted to future production, not merely present output or the existence of a scientific idea. A one-off prototype and a renewable production system are not interchangeable observations.

This paper proposes *recursive productive capacity* (RPC) as a common evidence and comparison contract for this task. The contribution is integrative and operational. First, a policy-indexed, probability-qualified correspondence distinguishes jointly sustainable successor configurations from one-time possibilities. Second, a pair of production/science transformations separates genuine research-method improvement, accepted knowledge and physically maintainable implementation. Third, dated material and machine accounts, permissions and renewal triggers define what a feasible witness would have to contain. Fourth, the framework links capability judgments to economic decisions without conflating feasibility with welfare or claiming to surpass an equally informed dynamic optimizer. The two formal counterexamples, one complete synthetic schedule and a strong matched Bellman control supply consistency checks, not new general economic laws.

The integration may matter in multidisciplinary research and investment decisions where required information is dispersed among engineering records, scientific validations, supply contracts and organizational approvals. Its practical incremental value is a **testable hypothesis**, not an observed result. We specify an equal-information, full-verification-cost design to prevent favorable comparisons with deliberately weak baselines. The paper's seven sections address the economic object, physical and scientific recursion, dynamic feasibility, growth diagnostics, organization, controlled economic cases and the scope of the resulting contribution. This is a foundation for later sector-specific theory and evidence, not a claim to have solved all questions about autonomous machine economies.

# 1. The Economic Object: Productive Capacity That Can Change Its Successors

## 1.1 Output, assets, one-shot feasibility, and reproduction

*Current output* is the flow delivered during a dated period. *Productive assets* include operational machines, physical facilities, methods with enforceable usage rights, qualified research capabilities, stocks of resources, and the complementary infrastructure permitting their application. *One-shot feasibility* means a specified output can be completed at least once, not necessarily repeated after maintenance or component replacement. *Reproductive capability* means a defined essential service can be renewed across declared replacement cycles under explicit external dependencies. *Recursive productive capacity* means current productive and scientific actions alter which qualified, maintainable configurations the future system can itself construct, operate, and renew.

A factory may produce a sophisticated component once with imported machine tooling and still lack the ability to replace that tooling when it fails. Conversely, a less technically advanced facility may sustain a broad set of service functions because it can make substitutes or lawfully obtain replacement inputs from independent suppliers. The term *reproduction* concerns relevant economic functions and their renewal witnesses, not the manufacture of a bitwise clone of a particular robot or software instance. No argument requires that every input become autarkically sourced.

A patent, proof, candidate recipe, or AI-generated design should enter a versioned knowledge register; it does not enter installed operational capital merely by being produced. Scientific capability is demonstrated by quality-controlled performance on appropriate research tasks, not by the budget spent on computing or the number of text outputs. Capital reproduction, qualified knowledge, and scientific-method improvement therefore remain distinct observations.

## 1.2 One central successor-capability correspondence

Let decision time be $t_0$ and physical time be $u\in[t_0,t_0+T]$. Specify before intervention: the starting controlled state $s_{t_0}$; common service vocabulary $Q_0$; essential service floor $v$; a typed cumulative resource/financing ceiling $B$; lawful and contractual external dependency boundary $D$; time horizon $T$; number of renewal events $g\ge 2$; minimum duration and service requirements for each renewal; and threshold $0<p\le 1$. The service vocabulary includes units, throughput windows, quality, reliability, required complementary services, permissible external deliveries, and capacity obligations. New services require an independently reviewable service specification before cross-system comparison.

The contract fixes renewal checkpoints $\tau_1,\ldots,\tau_g$. They may be deterministic calendar dates or stopping times generated by **predeclared** wear/failure triggers; their stopping rule, ordering, permitted duration intervals $[\underline\Delta_i,\overline\Delta_i]$, and monitoring windows may not be selected retrospectively. They satisfy $t_0<\tau_1<\cdots<\tau_g\le t_0+T$ whenever the renewal event succeeds. For constant fixed generation length $\Delta$, feasibility demands $T\ge g\Delta$; heterogeneous equipment need not share a single $\Delta$. A generation refers to renewal of the contracted *service network*, not a cosmetic model update or a single component swap.

Work on a controlled path space $(\Omega,\mathcal F)$ with observations $o_u$ and information $\mathcal G_u=\sigma(o_z,\text{recorded actions and authorized receipts up to }z\le u)$. A policy $\pi=(\pi_u)$ is adapted to $\mathcal G_u$ and cannot use a future research discovery or failure realized after the action date. The system's transition law and the given policy induce a probability measure $\mathbb P_{s_{t_0}}^{\pi}$. Its actions must satisfy lawful and safety-critical permissions on every admissible hidden state consistent with the observation (the conservative robust-admission rule below); operational failure probabilities belong inside the specified service-reliability event. No unknown permit is silently assumed valid.

For a **joint** service configuration $c$ (not a menu of separately deliverable outputs), define $E_{T}^{(g)}(c;Q_0,B,v,D,\pi)$ as the event that the *same* policy $\pi$, without retroactive branch selection, (i) respects material, energy, fiscal, security, and rights constraints throughout the entire dated path; (ii) maintains the essential floor $v$ in its declared service windows and checkpoints; (iii) completes $g$ independently specified renewal events within $T$ and prescribed deadlines; and (iv) delivers all simultaneous or overlapping services in $c$ **together**, using one feasible time-indexed allocation, while preserving the required subsequent renewal route. Then the single central object is

**Equation (1): joint, policy-indexed successor capability.** Let the policy-specific event probability be

$$
\rho(c,\pi):=\mathbb P_{s_{t_0}}^{\pi}\big[E_T^{(g)}(c;Q_0,B,v,D,\pi)\big].
$$

$$
\mathcal C_{T,p}^{(g)}:=\{c:\exists\pi\in\Pi_{\mathrm{adm}},\ \rho(c,\pi)\ge p\},\quad g\ge2.\qquad\text{(1)}
$$

Here $\Pi_{\mathrm{adm}}$ abbreviates the adapted/admissible policy class and $\mathcal C_{T,p}^{(g)}$ retains the common fixed argument list $(s_{t_0};Q_0,B,v,D,T)$ defined immediately above. Both $\pi$ and its probability law refer to the same policy on the same history-dependent event; the shorthand removes only typesetting redundancy.

The policy $\pi$ appears in **both** admissibility and the measured event, and it induces the probability law. This prevents an empty existential policy qualifier independent of an unrelated random event. The quantifiers describe distinct achievable configurations under possibly different policies; they **do not** claim that the full set $\mathcal C$ can be delivered simultaneously. Within any one configuration, however, the services have a joint deliverability witness; individually feasible services cannot be added to claim a bundle the system lacks capacity to produce.

A *one-shot* comparison is separately defined with the same starting state and admissibility vocabulary but no successor-renewal condition:

**Equation (1a): one-shot feasible service.** Define $\rho_{\mathrm{one}}(q,\pi)=\mathbb P_{s_{t_0}}^{\pi}[E_T^{\mathrm{one}}(q;Q_0,B,D,\pi)]$. Then

$$
\mathcal O_{T,p}:=\{q:\exists\pi\in\Pi_{\mathrm{adm}},\ \rho_{\mathrm{one}}(q,\pi)\ge p\}.\qquad\text{(1a)}
$$

The one-shot policy class and event share the preregistered start state, external boundary, horizon and budget, but do not require $g$ subsequent renewals.

A one-shot service may qualify for $\mathcal O$ under an ex ante chance statement yet fail to qualify for $\mathcal C$; observing a lucky prototype alone establishes neither ex ante certification. These objects have different contractual meanings and should never be interchanged in conclusions or data tables. Neither is a scalar measure of welfare or investment value. **Operational-status rule:** a mathematical lower bound verified inside a synthetic model is a *model-conditional certificate*, not a field-qualified claim. Field certification requires independently checked transition estimates, safety rights, metrology/quality records, and an uncertainty classification. A missing critical datum returns **UNKNOWN / NOT CERTIFIED**; it is never silently replaced by a favorable model assumption.


## 1.3 Joint service certificates, partial orders, and new service classes

A **configuration certificate** binds named service units, rate and quality limits, service-time overlaps, shared input and machine allocations, physical renewal obligations, operating permissions, a budget, observed system state, and an ex ante risk estimate with uncertainty. It must identify a single preregistered **observation-contingent admissible policy** and a joint feasible schedule on each realized successful path; it is not a fixed hindsight-picked schedule. Merely listing individually successful tests is an invalid joint certificate. **Counterexample:** one machine can perform A or B for one full hour, and both customers demand the same one-hour deadline. Each service is individually feasible, but the bundle $(A=1,B=1)$ is not; the union of separate certificates must not be reported as a jointly attainable configuration.

For configurations over a common preregistered vocabulary $Q_0$, an optional partial-order report states $c_A\succeq_{Q_0,B,v,D,T,p}c_B$ only when every *jointly feasible service requirement* that the comparison protocol certifies for $c_B$ is matched by $c_A$ within the same budget, deadline, quality, essential-floor, and renewal constraints. This is a comparison of certified envelopes, not a claim that one individually successful output dominates another on aggregate. Where no such verified matching relation exists, use **INCOMPARABLE** rather than forcing a ranking. A technology may improve one throughput coordinate while degrading renewable reliability or imposing extra resource costs. A new activity $q_{\mathrm{new}}$ first receives a new public service specification and a separate evidence certificate; it is not silently pooled into $Q_0$ or assigned an arbitrary numerical value.

The protocol distinguishes capability inclusion, cash value, and normative desirability. A configuration with more technically feasible services may still be a worse choice under financing constraints, externalities, changing prices, or distributional objectives. A feasible set is a question about **can**; an objective and explicit valuation are required for **should**.

## 1.4 Operational autonomy is a measured condition, not a moral category

Machine autonomy is multidimensional. Define an observed profile $A=(a_D,a_P,a_R,a_O)$: decision delegation, replacement/renewal independence, resource-sourcing independence, and organizational/permission independence over the frozen horizon. Each coordinate must be tied to a denominator: permitted choices actually made without continuing discretionary human approval; fraction of essential renewal services completed within $D$; share of essential inputs available through lawful replaceable sources; and proportion of required research-to-factory handoffs completed by valid delegated control. An illustrative $a_D=1$ means routine decisions within a given mandate are automated, **not** that the machine invented the mandate, bears legal personhood, or deserves an ultimate-purpose status.

This profile alone does not identify an economic *causal* effect. A corporation can grant extensive decision rights to human managers, and a human-run automated scheduler can make the same timely production choice as an AI agent. The potentially machine-specific regime concerns the measured scale, speed, replication, availability, and operating cost of delegated decision and discovery processes. Its distinct contribution requires a matched intervention changing these operating attributes while holding mandate, resource endowment, permissions, informational access, and baseline optimization fixed. Machine-versus-human branding is not a treatment variable. We do not infer superior growth, survival, or social welfare from autonomy scores.

## 1.5 Boundary counterexample: equal current output, unequal renewal

Two workshops report identical quarterly output and comparable nominal capital. Workshop A can build and inspect its critical replacement spindle and has two authorized substitute suppliers; Workshop B depends on an exclusive supplier and possesses a qualified substitute blueprint but lacks time-valid legal permission to deploy it. On the day of a common supplier failure, their output histories are the same and their multi-generation service-renewal possibilities differ. This is an illustration of a missing state variable, not a new identification theorem. An appropriately specified classic dynamic production-network model would discover exactly the same difference. Whether collecting the additional repair and authorization evidence is worth its cost remains empirical.

# 2. Two Interacting Recursions: Physical Production and Scientific Discovery

## 2.1 Physical-production recursion

Physical-production recursion means a productive configuration can use its current capabilities to maintain, repair, replace, and potentially change its successor's productive instruments, infrastructure, or enabling services. Raw materials, machine hours, transport, energy, measurements, spare parts, and installation labor are scarce inputs, regardless of whether decisions are made by robots, AI software, or human operators. A productive sequence is recursive only when the activities of an earlier generation causally change the renewability or feasible production of a later one, rather than merely adding one copy of an existing product.

This is a complementarity problem. An automated machine tool is useful only with suitable power, controls, feedstocks, coolant, calibration, fixtures, maintenance methods, and enforceable access rights. The relevant object is therefore a network of typed input-output hyperedges and time-dependent constraints, not the count of machines described as autonomous. A high-performance replacement may introduce an irreplaceable sensor or rare input; an older tool may be more robust when it can be serviced from widely available parts. Every proposed self-replacement must be evaluated against real production receipts and outside dependencies, rather than a narrated cycle on a diagram.

The reproduction pathway can be recorded as

$$
K_t\;\xrightarrow[\mathrm{resources,\ time,\ rights}]{\mathrm{fabricate/maintain/replace}}\;K_{t+1}\quad\text{with service-floor and renewal checks.}\qquad\text{(P)}
$$

An installed unit count is not a proxy for functional reproduction. Failed and retired equipment must be tracked separately, and evidence of a fabricable component alone is insufficient where complementary tools, system integration, or future recurring inputs are missing. Physical reproduction can be purchased partly from external independent providers: the boundary $D$ declares the permitted trade, human labor, external science, imported components, and utility access. Calling a system 'self-reproducing' without stating $D$ is uninformative.

## 2.2 Scientific-technological recursion

Scientific recursion refers to improvements in the capacity to produce *future independently qualified knowledge*, not simply an increase in scientific expenditures, generated papers, or benchmark scores obtained by changing the task mix. A research method is productive only when its measured improvement survives difficulty-matched, held-out scientific tasks, reproducibility checks and appropriate independent evaluation. Novel ideas, qualified results, deployed research tools, and improvements to subsequent research capability are separate typed states. A proof may be correct without a feasible engineering implementation; a physical measurement method may become more powerful without producing a new industrial recipe during the observation window.

The provisional scientific chain is

$$
H_t\;\longrightarrow\;\text{candidate hypotheses}\;\longrightarrow\;\Theta_{t+1}^{\mathrm{qualified}}\;
\longrightarrow\;\text{validated method / recipe},\qquad\text{(S)}
$$

where $H_t$ is a *task- and domain-calibrated latent capability profile*, $\Theta^{\mathrm{qualified}}$ is a versioned register of independently qualified knowledge and usable methods, and the arrows involve experiment time, budgets, access rights and possible failure. A measured improvement in $H$ requires a registered evaluation design: frozen problem distribution/difficulty, computational and laboratory budgets, blinded or otherwise contamination-controlled held-out problems, false positive/failure audit, transfer tests, calibration error, and retained negative results. Publication status or the mere existence of an impressive result cannot substitute for those controls.

Improved research methods can change the yield, speed and reliability of later inquiry; they can also increase qualification bottlenecks, rely on scarce instruments, or produce more unimplementable possibilities. Recombinant growth and research-sector feedback are established modeling themes (Weitzman, 1998; Davidson et al., 2026). The METRE question is how these phenomena enter a traceable physical production and successor-renewal decision, without claiming first discovery of science improving science.

## 2.3 The two directions and their qualification boundary

The *science-to-production conversion* is $H\rightarrow\Theta^{\mathrm{qualified}}\rightarrow$ technically implementable design $\rightarrow$ installed, serviceable $K$. The *production-to-science conversion* is an installed $K$ that fabricates or improves instruments, experiment throughput, metrology, computational hardware or physical test environments, thereby raising independently measured future $H$. A feedback mechanism must identify **both** directed interventions on a matched base and distinguish any intermediate one-time scientific or physical output from a repeatable effect on subsequent research or production generations.

![Figure 1. Physical renewal and scientific capability conversion across successive generations. Every arrow is an unverified conditional mechanism, not an empirical claim.](METRE_Paper01_Figure1_Recursion.png){ width=88% }

**Observable qualification gates for Figure 1:**

**Physical renewal ($K_t\to K_{t+1}$).** Requires fabricated, installed and maintainable assets plus dated renewal evidence; a single fabricated part or design proposal is insufficient.

**Research ($H_t\to\Theta_{t+1}$).** Requires held-out method evaluation and independently qualified discoveries; more hypotheses, easier tasks or publication count do not qualify.

**Science to production ($\Theta_{t+1}\to K_{t+1}$).** Requires engineering qualification, real installation and a complete maintenance route; valid but stranded knowledge is not operational capacity.

**Production to science ($K_{t+1}\to H_{t+1}$).** Requires matched future research-performance uplift enabled by a specific physical instrument; hardware ownership alone is not research ability.

**Repeated coupling ($K_t\to H_{t+1}\to\Theta_{t+1}\to K_{t+1}\to H_{t+2}$).** Requires repeated, separately qualified feedback effects; the Section 6.1 AND-gate is not evidence of this full cycle.

The arrows represent costly and failure-prone conversions. Their coupling may be beneficial, negative, or negligible. A research team can occupy a machine that otherwise produces replacement parts. New instruments can create new calibration obligations. A manufacturing upgrade can improve physical output yet degrade the next generation's ability to fabricate its own essential tooling. No free, optional, strictly superior technique can itself shrink the feasible choice set when all previous feasible actions remain available; deterioration requires a stated irreversible conversion, resource reallocation, lost complement, or additional obligation.

## 2.4 Switch-off interventions and the meaning of complementarity

A clean test fixes the common initial state, objective, external boundary, legal rights, spending and time ceilings, uncertainty model, and the target qualified successor service. Interventions disable *one specific conversion edge* rather than removing all useful activity of one subsystem. Let $C^{P}$ denote a physical-only successor evaluation where existing knowledge is allowed but further research discovery of the target recipe is disabled; $C^{S}$ a research-only evaluation where discovery remains permitted but additional manufacturing of the target is disabled; and $C^{PS}$ a coupled evaluation permitting both. A target $q_N$ may be absent in the first two and attainable in the third. That implies the specified project needs both conversions under the stipulated treatment; it does **not** prove that physical assets improve future research, that feedback accelerates growth, or that either standalone subsystem has no other valuable output.

To identify genuinely reciprocal feedback, add a second treatment that varies the **instrument/experimental capability produced by physical capital** and measures a future $H$ on matched research tasks, followed by a new qualified recipe and a further $K$. A minimally informative paired comparison records $\Delta H^{K\to H}$, $\Delta K^{H\to K}$, their costs, bottlenecks and final multi-generation service reliability, with interventions and measurements registered before observing outcomes. Section 6 gives an explicitly stipulated illustrative design; real identification remains undone.

## 2.5 Sequence, delay, and weak links

Research and manufacture are not interchangeable stages in a cyclic system. If a qualified recipe arrives after an indispensable existing machine retires, the new capability is not yet attainable. If a robot finishes fabrication before the necessary metrology protocol is approved, output cannot be called qualified. Parallel paths may raise service continuity but can increase joint failure risk when they share the same utility, single supplier, model, or verifier. The proper accounting is dated, stochastic, and typed; a connected network graph alone cannot certify that production completes before a deadline.

A separate implication concerns weak links. An AI method can improve dramatically while the deployment chain remains constrained by high-reliability sensors, cooling, materials, or regulatory approval. A small improvement in a complementary bottleneck can affect more future production options than a large advance in a nonbinding research task. These are recognized themes in the economics of complementarities and AI (Jones, 2026). The framework seeks to report their effect on the reproducible successor configuration, not to rebrand complementarity as a new physical law.

# 3. A Common Dynamic Framework of Recursive Productive Capacity

## 3.1 State, observations, and admissible actions

At a resolution adequate for a particular experiment, let

$$
s_u=(K_u,H_u,\Theta_u,R_u,X_u,M_u,L_u,Z_u),\quad u\in[t_0,t_0+T],\qquad\text{(2)}
$$

where $K$ is the typed condition-aware installed capital inventory, $H$ the calibrated research-method capability, $\Theta$ the knowledge/recipe evidence ledger, $R$ available lawful materials and energy rights, $X$ declared external suppliers/components/services, $M$ prevailing organization/permissions/information policy, $L$ obligations, and $Z$ dated observations and evidence about queues, experiments, and physical installations. Rights to obtain an outside input are not the same thing as physical possession; qualified methods are not installed productive units; observations are not future realizations.

Actions include manufacture, repair, retirement, scientific experiment, qualification, physical installation, procurement, delegation, reorganization, financing, and pause/reject. The true state determines a physical and legal admissibility set $U(s_u)$. However a partially observing decision-maker chooses $a_u=\pi_u(h_u^{\mathrm{obs}})$, with $h_u^{\mathrm{obs}}$ measurable relative to $\mathcal G_u$. These two statements are jointly meaningful only with an information-safe admission rule. Our baseline is

$$
\pi_u(h)\in\bigcap_{s\in\operatorname{Supp}(b_u(\cdot\mid h))}U_{\mathrm{hard}}(s),
\qquad \mathbb P^{\pi}[E_T^{(g)}]\ge p,\qquad\text{(3a)}
$$

where $b_u$ is the policy's versioned belief distribution on hidden states and $U_{\mathrm{hard}}$ is the subset respecting never-violate legal, safety, and rights constraints. If a permit cannot be shown valid in every relevant state of support, the action is rejected until stronger evidence arrives. Reliability/failure events *within* authorized operations are handled by the probabilistic event and expected losses rather than being mislabeled as lawful permission to violate safety. In applications where support-wide admission is unreasonably conservative, a different regulator-approved chance-constrained rule must be written and cannot be substituted silently.

The transition/observation model is

$$
s_{u+1}\sim P(\cdot\mid s_u,a_u),\quad o_{u+1}\sim O(\cdot\mid s_{u+1},a_u),\quad a_u=\pi_u(h_u^{\mathrm{obs}}).\qquad\text{(3)}
$$

The use of a discrete $u+1$ is for notation; time-indexed physical tasks may be embedded in finer event steps. The model must record what information was genuinely available when a decision was made, including any failed probes or delayed supplier quotes. A policy chosen after seeing the winning research outcome is an illegal hindsight reconstruction. Organizational change $M_{u+1}=\Psi(M_u,a_u^M,Z_{u+1})$ requires an authorized change action with actual transaction costs and time. Merely allowing $M$ to vary in a state vector is **not** an economic equilibrium model of emergent institutions.

## 3.2 Dated production hypergraph and resource feasibility

Each production recipe $j$ is a hyperedge combining inputs, capabilities, evidence conditions and access rights. It declares typed input vector $a_j$, output vector $b_j$, start time $\sigma_j$, completion time $\phi_j\ge\sigma_j+\ell_j$, machine reservations $\kappa_{jm}$, physical energy demand, qualification version $\theta_j$, failure/repair rules and authorization requirements. Material outputs become available only after their completion and successful quality release. A recipe cannot spend parts that a later event will eventually fabricate, even when a one-year input-output spreadsheet balances.

Let $\{t_k\}$ contain every production start, completion, supply delivery, consumption and failure time. Resource stocks $r_k$ have consistent physical units. A necessary ledger, evaluated at each *ordered* event, is

$$
r_{k+1}=r_k+e_k+\sum_{j:\phi_j=t_k}b_jx_j-\sum_{j:\sigma_j=t_k}a_jx_j-w_k\ge 0,\qquad\text{(4)}
$$

where $e_k$ is actual admissible dated inflow, and $w_k$ excludes inputs already included in $a_j$. An event at a common timestamp is ordered so an output cannot finance its own earlier input. A path is admissible only if **every prefix** satisfies this nonnegativity test and the required types/grades of material actually match. Cumulative end-period nonnegativity is weaker and not sufficient.

Time-indexed machine reservations and power delivery add, for all machine classes $m$ and physical instants $u$,

$$
\sum_{j:\sigma_j\le u<\phi_j}\kappa_{jm}x_j\le\overline K_m^{\mathrm{operational}}(u),\qquad
0\le P_{\mathrm{use}}(u)\le P_{\mathrm{authorized}}(u),\qquad\text{(4a)}
$$

and $\int P_{\mathrm{use}}(u)\,du$ must satisfy energy-supply or stored-energy accounts separately from the instantaneous power constraint. Transport latency, staff or robot availability, metrology, safety, queue times and deadline constraints must likewise be included before calling a physical schedule feasible. Equations (4)–(4a) are an **audit template**, not a claim to have specified all industrial constraints for every sector; site-specific flow models remain necessary.

**Counterexample — annual balance versus dated feasibility.** A process requires one part at day 1 and completes installation on day 2. Its supplier manufactures that part on day 3. An annual material account shows one delivered and one consumed part, net zero, but no legal time-indexed schedule can supply the day-1 production start. The candidate production edge is reachable in a static graph and infeasible in the stipulated physical experiment. A capability certificate must therefore include time-resolved delivery receipts, not just totals.

## 3.3 Equipment state identities without double-counted failure

Economic depreciation, declining service quality and physical retirement require disjoint event semantics. For a homogeneous equipment class, partition each asset into mutually exclusive operational, failed-but-repairable, and permanently retired states. Let $n_u^{\mathrm{op}},n_u^{\mathrm{fail}},n_u^{\mathrm{ret}}$ denote their counts, and let $I$ be newly installed operating assets; $F$ newly failed from operating; $\mathrm{Rep}$ returned from failed after verified repair; $D_{\mathrm{op}}$ permanently retired directly from operation; and $D_{\mathrm{fail}}$ permanently retired from the failed inventory. Then

**Equation (5): mutually exclusive asset transition identities.**

$$
n_{u+1}^{\mathrm{op}}=n_u^{\mathrm{op}}+I_u+R_u-F_u-D_{\mathrm{op},u}.\qquad\text{(5a)}
$$

$$
n_{u+1}^{\mathrm{fail}}=n_u^{\mathrm{fail}}+F_u-R_u-D_{\mathrm{fail},u}.\qquad\text{(5b)}
$$

$$
n_{u+1}^{\mathrm{ret}}=n_u^{\mathrm{ret}}+D_{\mathrm{op},u}+D_{\mathrm{fail},u}.\qquad\text{(5c)}
$$

All event sets are disjoint by origin state and each asset transition has one immutable identity and timestamp. A failed tool that is later scrapped leaves $n^{\mathrm{op}}$ exactly once, then leaves $n^{\mathrm{fail}}$ once; it is not subtracted twice from operating capital. If equipment is acquired/sold/transferred outside the modeled boundary, declare additional explicit inventory events instead of burying them as depreciation. Condition/quality $q_{j,u}$ changes effective service rates $K_{j,u}=\varphi_j(n_{j,u}^{\mathrm{op}},q_{j,u},\Theta_u,R_u)$ without automatically changing the number of units. Financial book depreciation is a separate valuation account and does not physically produce or destroy machines.

A simple test starts with one operating mill, fails it, subsequently retires it, and installs a verified replacement: operating count goes $1\to0\to0\to1$, failed count $0\to1\to0\to0$, retired count $0\to0\to1\to1$. There is one operational mill at the end, not two. Replacing control software on an installed mill may change performance or a usable method record without adding a second physical unit.

## 3.4 Qualified knowledge and physical deployment ledgers

Keep the append-only history $\Theta_u^{\mathrm{qual}}$ of independently accepted claims, methods and retractions; maintain $\Theta_u^{\mathrm{usable}}$ as its time-dependent subset with valid rights, scope, and deployment constraints. A qualified proof enters the evidence ledger at its actual acceptance time; a method improvement requires independent held-out performance before updating $H$; only an installed, calibrated and serviceable facility affects $K$. Revoking an obsolete method changes its current usability status and does not delete its historical receipt. Organizational transfers have separate permission receipts. This prohibits collapsing the path *research expenditure → patent → industrial capability* into one unsupported growth step.

The smallest repeatability certificate must include: versioned service definition, starting asset and condition ledger, $g$ renewal checkpoints, dated real input and power accounts, shared-machine capacity, qualified methods, service-floor outcome measurements, external dependencies, legal/organizational authority, and the joint event estimator with calibration and correlation assumptions. When any of these is unknown, the appropriate output is **UNKNOWN / NOT CERTIFIED**, not an invented PASS.

## 3.5 RPC-CP01 comparison and feasibility audit protocol

RPC-CP01 is a preregistered reporting contract: (i) freeze the economic objective and who bears externalities; (ii) fix common named services, essential floors and target configurations; (iii) fix $B,D,T,g,p$ and the observable information/authority boundary; (iv) register permitted policies and safe-state admission; (v) record every dated industrial, financial and information decision; (vi) independently qualify new scientific claims and method improvements; (vii) verify the **joint** physical renewal certificate, including losses and hidden dependencies; (viii) publish inclusion, incomparability, calibrated probability bounds, and remaining Unknowns; and (ix) only then calculate investment value and compare against the strongest feasible baseline.

The protocol must report assumptions that materially affect certification, including correlations across stages, stale qualifications, external supplier dependence, financing limits, sensitivity to $p$, time horizon and service vocabulary, and the cost of collecting evidence. If a complete dynamic production model with the same state and information yields the same decision, that agreement must be reported; the procedural value of RPC-CP01 is not a new optimization theorem. This is a measurement-and-communication standard proposal. Adoption or actual superiority remains untested.

## 3.6 Identification limits of aggregate output and separate service menus

**Proposition 1 (separate feasibility does not compose into a bundle).** Let a resource-constrained, two-renewal controlled system admit two policies $\pi_a$ and $\pi_b$ such that service $a$ and service $b$, respectively, are each individually renewed with probability one. It does **not** follow that there exists any single admissible policy that renews the joint bundle $(a,b)$ with positive probability. **Proof by construction:** each two-generation path has one indivisible operating machine with one work slot at each renewal checkpoint. Policy $\pi_a$ reserves this sole slot for $a$ at both renewals; $\pi_b$ reserves it for $b$ at both. The slot cannot be shared or duplicated within the fixed budget, so each service is individually feasible at probability one, while the joint predicate cannot hold on any path. $\square$

The proposition is elementary constrained scheduling/multi-objective feasibility—not a new stochastic-control theorem. Its economic use is to block the common but incorrect practice of presenting a list of individually possible factory services as one jointly available production frontier. A qualification dossier must therefore identify the *same policy* and the dated joint resource allocation used to support a claimed production bundle.

**Proposition 2 (aggregate-state nonidentification).** Suppose an evaluator observes only the tuple $Z=($present net output, book equipment value, equipment count, contemporaneous service rate$)$ and must give a binary answer to whether a specified service is renewable through two deadlines under a declared boundary. There can exist two physically admissible models with exactly the same $Z$, one satisfying and the other failing the two-renewal contract. **Proof by construction:** hold installed equipment, observed services, prices, maintenance expenditure and all components of $Z$ fixed. In model $S_{\mathrm{valid}}$, a pre-existing license permits fabrication of replacement tooling before both renewal deadlines. In model $S_{\mathrm{invalid}}$, the otherwise identical license expires before the first fabrication. The action is permitted in $S_{\mathrm{valid}}$ but prohibited in $S_{\mathrm{invalid}}$. No cash, book-value or current-output datum in $Z$ differs. Thus the renewal indicator differs although $Z$ is the same. Any deterministic binary rule based only on $Z$ must be wrong in at least one of the two worlds. $\square$

With equal prior weight on these constructed worlds and equal loss $L$ for an incorrect binary assessment, the minimum expected classification loss from $Z$ alone is $L/2$. If the binding rights fact can be perfectly verified before choice at *total* cost $c$, the maximum *net* improvement in this construction is $L/2-c$; verification is worthwhile iff $c<L/2$. These inequalities follow from the stipulated binary decision and are standard value-of-information logic. They do **not** establish that an RPC-specific evaluator outperforms a fully informed conventional optimizer: the latter makes the identical decision once given the same verified license.

**Qualification boundary.** The propositions are deliberately narrow counterexamples and cannot establish a universally minimal evidence schema or claimed mathematical priority. In particular, prior work already develops stochastic viability by dynamic programming and machine-checkable certificates for multiobjective MDP queries (Doyen and De Lara, 2010; Funke, Jantsch and Baier, 2020; Chatterjee et al., 2025; Baier, Chau and Klüppelholz, 2025). The proposed cross-domain extension is the *specific observation/measurement contract* for scientifically qualified, physically renewable, legally executable productive services, and its net value is an empirical question.

# 4. Growth Mechanisms: From Reproduction to Expansion of Possibility

## 4.1 Four diagnostic states, not four proven equilibria

Four analytically useful observations form a taxonomy, **not** a theorem of growth. In *maintenance*, the essential floor is met and qualified services can be renewed under the declared boundary, but no improvement of the contracted successor profile is established. In *scale expansion*, additional throughput or copies of known qualified services are feasible but do not, by themselves, establish more advanced self-renewal or a new qualified production service. In *capability expansion*, a service dimension or new service class can be jointly delivered and renewed at the declared $T,g,p$ and resource boundary. In *recursive capability expansion*, a verified effect on *a further generation's* ability to discover, fabricate, or renew productive capabilities goes beyond a single upgraded product.

These states need not form a complete mutually exclusive chronology. A system can increase scale in service A while losing reproducibility in service B; shorter renewal horizons can pass while longer ones fail; a new qualified service may be incomparable to an existing configuration. Revenue increases due to market prices, changes in stock market valuations, a one-time copy, or the publication of a paper are not sufficient evidence for any physical recursive-capacity improvement. The protocol reports the relevant service family and time/risk/boundary coordinates rather than a single maturity badge.

## 4.2 Necessary conditions and conditional thresholds

A successor configuration has to be reachable under some admissible strategy, yet reachability alone is not a feasibility certificate. A full renewal path requires correctly typed and timely physical inputs, sufficient equipment/energy capacity, physical reliability, qualified knowledge, legitimate rights, cash/credit solvency and controlled information available in time to act. For a coupled scientific route, a discovery arriving after a critical tool failure cannot be treated as available at the earlier start date. The event in Equation (1) combines those requirements rather than treating them as separable afterthoughts.

Several conditional exclusion statements follow. If an essential input becomes irretrievably unavailable before the only replacement route can run, an admissible policy for that service may not exist; then the target fails the corresponding multi-generation event, even though it may have been manufactured once. If a replacement input has an authorized substitute with measured lead time and capacity, the certificate can include it without imposing autarky. If the system can physically renew a service for two generations at some stated risk, it has **not** established indefinite survival, exponentially rising output or long-run social desirability. Indefinite claims require global resource conditions, reachable state invariance, repeated research-qualification distributions, correlated failure structure and durable institutional rights.

A stationary local production approximation can yield matrices with eigenvalues above one; interpreting the largest eigenvalue as an industrial growth rate requires a positive-stock production meaning, dated resource feasibility and a valid domain of approximation. A local unstable deviation from an equilibrium is not evidence of sustained positive physical capital growth. This caution is not novel mathematics; it prevents the paper from mistaking a familiar linear calculation for a general machine-growth law. Recent growth models already consider feedback among automated production and innovation (Trammell and Korinek, 2026; Davidson et al., 2026), so any claimed new comparative static would need explicit assumptions and an irreducibility check against those models.

## 4.3 Irreversible investments and preservation of future options

A sponsor can allocate scarce effort and capital to immediate goods, replacement capacity, metrology, alternate materials, discovery methods, research software, or redundancy. A high-throughput system can be fragile if its renewals require an imported component whose supply cannot be secured; a more modest system can preserve alternative productive paths. But the mere presence of a new, costless, optional technology cannot shrink the feasible choice set when all earlier methods remain feasible. Negative effects require irreversibility, actual diversion of scarce resources, maintenance burdens, changed legal obligations, or loss of complements.

Real-option reasoning already examines decisions to wait, preserve substitute routes and exercise irreversibly costly investments under uncertainty (Dixit and Pindyck, 1994). RPC adds no claim of priority for this logic. It asks the measurement team to identify whether the option is **executable across successor generations**: can a machine actually obtain material inputs, lawfully authorize installation, re-qualify a method and renew the service before its deadline? The option's monetary value remains an objective-dependent and evidence-intensive estimate, not the number of branches in a speculative technology graph.

An important inference can run against technological enthusiasm: producing more experiments or more equipment models may reduce economic welfare when the additional facilities impose expensive future obligations. The frontier and its expected value are separate observables. Costs of verification, maintenance and downstream risk must be assigned to a real payer; internal machine-to-machine payments cannot be counted repeatedly as new final value.

## 4.4 Growth without an autonomous final consumer or a universal market

An externally sponsored industrial program can reinvest its operating surplus into research tools and replacement factories without each generation finding an entirely new customer. This is a production and allocation economy even if one company owns the assets and records intermediate movements internally. A market economy is a possible institution, not a definitional requirement of physical recursion. A machine can produce economic services on behalf of a human-set purpose and thereby generate machine-origin instrumental and capital demands without possessing terminal preferences or any moral status.

Nor do internal prices or machine-to-machine transfer volumes establish growth of final welfare. An economy may show expanding gross transactions while net useful output stalls or falls. In a production network, value added, intermediate input use, environmental costs, obligations, and the actual external beneficiary must be distinguished. The paper studies **positive feasibility and decision mechanisms**, not an ethical proposition that autonomous expansion is always desirable.

## 4.5 What would falsify the stronger growth narrative?

Resource depletion, rising experiment difficulty, slow metrology throughput, correlated tool failures, insufficient energy delivery, financing constraints and permission delays can all stop expansion. Research may become better at generating ideas without making subsequent industrial qualification cheaper. Factories may manufacture new tools without being able to build the instruments required to validate them. A company may reinvest surplus yet decrease true reproducible capacity. Such negative outcomes belong to the theory as potential empirical refutations, not anomalies requiring an ad hoc story to rescue optimism.

A credible growth research program would therefore report stalled, contracting, fragile and incomparable cases under the same observation contract used for apparent success. It would compare industrial cohorts at matched initial capital, input boundary, risk horizon and service definition, including groups where a stronger AI method was available but failed physical deployment. Until repeated evidence or a nontrivial theorem distinguishes regimes beyond established models, the four labels remain diagnoses of possible histories, not predicted universal economic trajectories.

# 5. Economic Organization as a Part of Productive Recursion

## 5.1 Institutions change what actions are legally and physically executable

Organization $M$ governs who observes particular information, holds permission to purchase material or install equipment, accesses research assets, approves a technical method, bears liability, resolves conflicts and authorizes changes in production rules. A physically adequate material supply and a correctly qualified scientific recipe do not yield an executable deployment path if the handoff violates the actual access regime or occurs after the deadline. Conversely, delegated permissions and portable evidence may enable a previously blocked action without fabricating a single additional machine.

In Equations (2)–(3), organization affects the action set, the observation channel, coordination cost, and response delays. The economic object remains the successor-capability correspondence: a change in authorization may affect current output or the long-run range of renewable service configurations. The causal treatment is a **specific permissions or information intervention**, not the word 'market,' 'hierarchy,' 'federation,' or 'decentralization.' An institutional comparison that grants one regime earlier knowledge, extra resources, or free legal permissions has not isolated organization.

A full intergenerational record should specify who may issue and revoke a mandate, approve a replacement recipe, update knowledge qualifications, sign supply contracts, fund public verification and bear a loss after a process failure. Technical identity continuity and cryptographic receipts can support traceability but cannot by themselves create recognized legal title, insurance capacity or public authority. A machine can exercise extensive routine decision autonomy while a real company or person remains the legal obligor.

## 5.2 Central planning, markets and federation are all contingent candidates

One integrated planner may coordinate strongly complementary inputs more efficiently than a fragmented market, especially when qualified research and physical installation require rapid joint resource commitments. Independent production units may perform better when local conditions change quickly, spare capacity is widely distributed, errors are less correlated or competing scientific methods can be explored in parallel. Hierarchies can protect investment specificity; markets can improve supplier substitution; federations can separate liability and local experimentation. Which arrangement is more effective depends on information costs, product modularity, delay, incentives, the cost of verifying remote actions and the physical coupling among inputs.

Classical organizational economics already models knowledge costs, hierarchy and adaptation (Garicano, 2000; Siggelkow and Levinthal, 2003; Alonso, Dessein and Matouschek, 2015). More recent work studies how AI changes the cost of using dispersed local knowledge (Brynjolfsson and Hitzig, 2026). We cannot claim that a machine economy necessarily decentralizes, spontaneously creates markets or evolves toward a universal federation. More capable AI may make some centrally coordinated decisions faster and more complete than before, while cheap verification may permit others to become modular and exchangeable.

The correct comparison freezes a sponsor objective, true technology, starting equipment, environmental law, uncertainty, resource pricing and independent test data. It varies a specified institutional rule—such as the number of lawful signatories needed to approve a qualified recipe, the availability of a fallback authority, or the latency of information transfer—and observes success probability, costs, renewal and total net value. Section 6's 0.75 approval factor is a constructed illustration of this mechanism, **not** an empirical property of federated organizations and **not** a model of equilibrium formation.

## 5.3 Institutions across generations: rights, memory and replacement authority

Long-lived production creates obligations that survive a particular physical host. A factory can fail while its warranty, safety responsibilities, customer service obligations and resource debts continue; a successor machine may inherit a production process only if its rights and obligations can be transferred lawfully. Repeatable capacity includes these execution constraints. A nominal backup machine that lacks permission to process customer data or run a patented method cannot count as a qualified fallback even if its hardware is otherwise suitable.

Organization also determines how a qualified discovery becomes usable knowledge for a factory. A laboratory's internal validation may not satisfy an external buyer, regulator or factory owner. Trust and evidence can be portable, but an audit log's integrity is not the same as the truth of the scientific result or lawful acceptance of its claims. These are additional production qualifications, not mystical properties of machine identity. Every service contract must mark the responsibility owner and whether a permit is an operating constraint, a contingent risk, or an unresolved hard blocker.

The long-run effect can go in either direction. An integrated organization may maintain a common set of tooling specifications across generations; a distributed set of independent suppliers may preserve alternative production paths after correlated local failures. A dynamic enterprise may change organizational form after receiving a new manufacturing method because the method alters modularity and verification cost. All these are candidate mechanisms for comparing successor feasible sets; none has been proven to be the unique economic institution for autonomous production.

## 5.4 Organizational transition is modeled conditionally, not solved as an equilibrium

The minimal organization transition is

$$
M_{u+1}=\Psi(M_u,a^M_u,Z_{u+1}),\qquad
\text{cost}(a^M_u)\le B^{M}_{\mathrm{available}},\quad a^M_u\in U^M(s_u).\qquad\text{(M)}
$$

The operator records time, legal authority, bargaining or integration cost, observed information and which productive permissions change. This establishes that organizational change **can enter** the recursive production process. It does not establish that private agents find a stable or welfare-maximizing $M$ under decentralized incentives. An endogenous organizational equilibrium would need actors, information sets, utility/claims, contracts, strategic choices, legal enforcement, entry/exit and stationary or time-evolving equilibrium conditions. No such system is solved in this paper. Where the paper uses a fixed sponsor, the organization is a policy variable of that sponsor, not an emergent political-economic order.

For an explicit opposing example to a 'centralization always wins' narrative, suppose two lawfully independent approval paths can each clear a research-to-factory handoff with probability 0.92 and failures are independent. If either is enough, the probability of timely clearance is $1-(1-0.92)^2=0.9936$, compared with a single clearance route of 0.75. Applied to the **same** technical chain in Section 6, the additional approval survival factor becomes $0.9936$, raising qualified success probability to about 0.6005 (subject to unchanged resources and the independence stipulation). But two approval paths may consume duplicated legal, security and verification budgets, and shared suppliers can correlate their failures. The inference is that a well-designed federation *can* reverse a specific authorization bottleneck, not that it necessarily beats integration on total economic value.

## 5.5 A falsifiable organization–technology coevolution hypothesis

The hypothesized feedback is $M_t\to$ admissible scientific/physical search $\to\Theta_{t+1},K_{t+1}\to$ changes in information, modularity and contracting costs $\to M_{t+1}$. It is not enough to observe that organizational charts changed while automation increased. A valid test must establish a temporal ordering, control initial task/resource conditions, distinguish exogenous platform policy changes from endogenous firm choice and account for selection of organizations into different workloads.

Two particularly useful null hypotheses are: (i) conditional on complete physical and scientific state, access policies do not affect the jointly renewable service set beyond time/cost effects already present in classical organization models; (ii) changing machine decision speed or replication cost does not change institution choice after controlling for those same state variables and incentives. Rejecting either would require a measured and preferably preregistered comparison. The present foundation raises these as research obligations, not as findings.

# 6. What the Framework Changes for Research, Production, and Capital Allocation

## 6.1 An auditable investment comparison: complementarity, certification, and value

Consider the original an earlier model constructed example, now with the certification and economic contracts made explicit. A sponsor makes a time-zero choice between two mutually exclusive machine-operated production plans. Both begin with the same budget of 100 abstract units, comparable existing machines, an identical legal/physical boundary, a common essential service and a two-renewal horizon. For that essential service, each stipulated renewal succeeds with probability 0.94, independently, yielding $0.94^2=0.8836$. Both meet a **separate** essential-service availability requirement of 0.80 in this hypothetical case. **Joint-event convention:** the two 0.94 renewal gates for the incremental $q_N$ in Plan B are the *same shared platform-renewal events* used to assess essential-service availability, **not an additional independent pair**. Plan A faces the same platform-renewal events but has no stipulated route to $q_N$. Real industrial systems may have different dependencies; that joint structure would require measurement. All reported current net values are net of the same initial committed budget. They are stipulated for the illustration, not inferred from business records. They exclude a shared essential-service value that cancels across plans.

Plan A prioritizes short-run cash-generating work and produces present net value $Y_A=130$. Plan B devotes more of its identical initial budget to research-method improvement, recipe discovery, independent qualification, installation, and future renewal tooling, producing current net value $Y_B=105$. It can additionally create a new qualified manufacturing service $q_N$ with net terminal value $V_N=50$ **conditional on the full successful chain**. The sponsor chooses a single already-composed terminal discount factor $d=0.90$ for the two-period horizon; **this 0.90 is not applied twice**. Neither plan receives additional credit or permission in the constructed base case.

Five serial technical events are required for $q_N$: research-method improvement $H$ with probability 0.90; recipe qualification with probability 0.80; installed physical implementation with probability 0.95; first renewal with probability 0.94; and second renewal with probability 0.94. The operational model for this calculation is a **sequential conditional-stage model** under a *single fixed*, non-anticipative policy: write $H_{i-1}$ for the history in which all previous required stages succeeded and $q_i=P(G_i=1\mid H_{i-1},\pi)$ for the corresponding reached-stage conditional probability. Their values are the five stipulated numbers. The product follows from the **probability chain rule**, not from an unneeded assertion that the serial observed stages are unconditionally independent. Estimating these conditional probabilities and their transport across policies or failure domains remains unaddressed empirically. Thus

$$
p_{N,\mathrm{int}}=0.90\times0.80\times0.95\times0.94^2
=0.6043824.\qquad\text{(6)}
$$

The successor-capability **reporting rule** is: enter $q_N$ in the certified two-generation capability correspondence only if the ex ante evidence package justifies $p_N\ge p_{\mathrm{report}}=0.60$ under the declared dependency structure. Under the synthetic, sequential conditional-gate calculation, Plan B *barely* meets the **model-conditional** reporting threshold for $q_N$; A does not possess a route to $q_N$ on this horizon. An observed lucky prototype does not by itself meet this probabilistic requirement; the contract calls for both renewals and a non-hindsight strategy.

A separate **revenue-admission rule** is essential. For the example, lawful sale and delivery of the new service are permitted after actual quality and installation acceptance even if its *ex ante* probability is below the reporting standard $p_{\mathrm{report}}=0.60$. The $0.60$ number governs classification in the capability report, not a license, customer warranty, or ban on revenue. Monetary expectation therefore includes realized revenue on successful paths that were not certified at the 0.60 threshold. If a regulator or customer instead requires an ex ante $p\ge0.60$ contract before any sale, then a fragmented or adverse-correlation version must recalculate revenue using that stricter rule, potentially assigning no new-service sales in this toy model. The same threshold must never silently play both roles.

Under this explicitly stated *report-only certification* contract, the sponsor's expected discounted net objectives are

$$
J_A=130,\qquad J_B=105+d\,p_N\,V_N.
\qquad\text{(7)}
$$

Under integrated research-to-factory permission, $J_B=105+0.90(0.6043824)(50)=132.197208>130$. A current-net-value-only rule favors A, whereas the fully specified expected future-value rule favors B. This comparison does **not** prove that established economics would choose incorrectly. A full-information conventional dynamic optimizer with the same states, probabilities and preferences also chooses B, as Section 6.4 shows.

Now change only a concrete organizational clearance condition: a necessary handoff before the physical installation deadline succeeds with an additional stipulated conditional probability $q_M=0.75$ on reached histories and without extra resource advantages. Then

$$
p_{N,\mathrm{gate}}=0.75p_{N,\mathrm{int}}=0.4532868,\quad
J_{B,\mathrm{gate}}=105+0.90(0.4532868)(50)=125.397906<130.\qquad (8)
$$

In this version Plan B fails the $0.60$ *reporting* standard and loses the **expected monetary** comparison, even though a successful realized route could still legally earn the stipulated net payoff under the example's revenue contract. This demonstrates how time-valid permissions can affect the physical implementation of qualified knowledge. It establishes nothing about the average economic performance of markets versus central planners; the 0.75 number is invented, not estimated.

The minimum conditional terminal payoff supporting Plan B is $V_{N,\mathrm{crit}}=(130-105)/(d\,p_N)$: about 45.96 with the integrated permission path and about 61.28 with the additional clearance gate. A claimed new capability whose genuine conditional value is 30 is not the preferred investment under the integrated example despite the existence of a physically broader successor option. This makes the difference between set inclusion and economic valuation explicit.

**Comparison summary (same initial budget and sponsor objective).** Plan A: no $q_N$ route, success probability 0, expected net value 130, not certified. Plan B physical-only switch-off for the new recipe: probability 0, value 105, not certified. Plan B scientific-only switch-off for the installation route: probability 0, value 105, not certified. Coupled Plan B with stipulated conditional technical stages: probability 0.6043824, value 132.197208, **nominally certified** at 0.60. Coupled Plan B with an additional 0.75 timely-clearance gate: probability 0.4532868, value 125.397906, **not certified** at 0.60.

For the two switch-offs, zero applies **only** to the incremental manufactured service $q_N$ and its associated incremental payoff. Existing production, experimental insight, known scientific knowledge and other useful outputs are not assumed to become valueless. The committed base budget is held in place rather than reoptimized when a causal edge is disabled; a full dynamic decision evaluation allowing reallocation would compare different counterfactual investment policies and is a separate analysis.

## 6.2 Full dependence, sequential conditional probabilities, and robust choice

There are **two distinct probabilistic objects** that cannot be interchanged. **Model S (serial conditional transitions)**, selected for the explicit five-stage controlled path in Section 6.1, assigns

$$
q_i:=P(G_i=1\mid H_{i-1},\pi),\qquad H_i:=H_{i-1}\cap\{G_i=1\},\quad P(H_5\mid\pi)=\prod_{i=1}^{5}q_i=0.6043824.\qquad (9)
$$

The $G_i$ for $i>1$ are observed only on histories where the stage is reached. The chain rule is an identity for *those conditional probabilities*, regardless of an informal claim about 'independence'. Changing organization, weather, quality monitoring or policy may change the conditioned histories and probabilities. None is empirically estimated here. Reporting a nonzero lower reliability bound in a live industrial case would require validated conditional estimates with their uncertainty and applicability scope.

**Counterexample to a common misuse.** For $P(G_1)=0.90$, $P(G_2\mid G_1)=0.80$, $P(G_3\mid G_1,G_2)=0.95$, the reached three-stage probability is $0.684$. The unobserved counterfactual $G_{2,\mathrm{pot}}$ on failed-$G_1$ histories is a **different potential-event variable**: its unconditional probability can range from $0.72$ to $0.82$ without changing the reached-stage data. Consequently a Fréchet bound applied to the number $0.80$ as though it were the unconditional $P(G_{2,\mathrm{pot}})$ is not an identification analysis for Model S.

**Model M (separate latent-marginal stress test).** In a different, explicitly counterfactual model, stipulate five potential success events $G_{1,\mathrm{pot}},\dots,G_{5,\mathrm{pot}}$ defined even on paths where the production sequence would normally stop. Suppose their **unconditional marginals** (not Model S's $q_i$) are fixed at $(0.90,0.80,0.95,0.94,0.94)$ and their joint law is otherwise unknown. The sharp Boole–Fréchet interval is

$$
\max\!\left(0,\sum_{i=1}^{5}P(G_{i,\mathrm{pot}})-4\right)=0.53
\ \le\ P\!\left(\bigcap_{i=1}^{5}G_{i,\mathrm{pot}}\right)\ \le\
\min_i P(G_{i,\mathrm{pot}})=0.80.\qquad (10)
$$

The sharpness is independently verified by linear programming over all $2^5=32$ joint outcomes with a probability simplex and five marginal constraints; separate feasible distributions achieve both extremes. If only the last two potential renewal events are stipulated mutually independent, their joint chance is $0.94^2=0.8836$, but dependence between this pair and the first three remains unrestricted: the corresponding sharp bounds become $[0.5336,0.80]$. Neither interval is an interval estimate for an actual machine nor can its elements be substituted into Model S without adding an explicit potential-event model.

Under the **separate** constructed monetary contract $J_A=130$, $J_B=105+0.90(50)p_N=105+45p_N$, the investment indifference probability is

$$
p_{\mathrm{crit}}=\frac{130-105}{0.90(50)}=\frac59\approx0.555556.\qquad (11)
$$

Hence the full latent-marginal stress interval permits $J_B\in[128.85,141.00]$, straddling $J_A=130$: the risk-neutral ranking is **not identified** by those five marginals. Under a maximin policy *over this declared ambiguity set only*, Plan A wins ($130>128.85$); other ambiguity preferences, priors or bounds can choose B. This maximin observation is not a recommendation for industrial investment.

**Separate uncertainty sources.** A serial conditional model may instead place justified bounds on each reached-history $q_i$, producing a chain-product interval only if the individual bounds hold uniformly under the same policy and admissible histories. For illustrative uncalibrated envelopes $q_{\mathrm{low}}=(0.85,0.72,0.90,0.90,0.90)$ and $q_{\mathrm{high}}=(0.93,0.85,0.98,0.96,0.96)$, the corresponding products are $0.446148$ and $0.713954304$. They are *not* statistical confidence intervals. With no qualified transition evidence or missing permissions, the frontier outcome remains **UNKNOWN / NOT FIELD CERTIFIED** regardless of the favorable point estimate. The $0.60$ reporting threshold does not by itself prohibit economically realized cash flow, unless a distinct contractual sale constraint is preregistered.

**A robust decision classification.** For any fully specified pair of plans with $J_A=a$ and $J_B=b+\delta Vp$, where $\delta V>0$ and the admissible joint success probability is known only to satisfy $p\in[p_L,p_U]$, Plan B dominates throughout the ambiguity set if $b+\delta Vp_L>a$; Plan A dominates throughout if $b+\delta Vp_U<a$; otherwise the ordinal choice is not identified by the supplied probability information. This follows immediately from monotonicity of the affine objective in $p$ and is a decision-theoretic identity, not a new theorem of probability. In the illustrative case $a=130$, $b=105$, $\delta=0.90$, $V=50$, $p_L=0.53$, $p_U=0.80$, both rankings are admissible. The criterion for certification $p\ge0.60$ is distinct from the criterion for economic preference $p>5/9$. A model claiming either without identifying its probability semantics is incomplete.

## 6.3 Two-way physical–scientific recursion: a separate illustrative design, not an observed result

The preceding five-gate investment calculation has one research-to-physical installation route followed by two renewal checks. It is a **joint-necessity (AND-gate) example**. It does not contain an independently measured $K_{t+1}\to H_{t+1}$ change. A theoretical manuscript committed to two interacting recursions must make this limitation visible and specify an additional pathway where fabricated physical capability improves later *research method* and the improved method then changes future physical production.

A second, strictly constructed design illustrates the correct observation logic without pretending that its probabilities come from a real laboratory. Start with $K_0$ and a fixed research task distribution. With stipulated probability 0.80, $K_0$ fabricates and calibrates an experimental instrument $I_1$. If $I_1$ is valid, the method's independently qualified success probability on matched held-out tasks is stipulated as 0.75; without it, that probability is 0.50. These are **different $H_1$-performance conditions**, not two numbers of research papers. Under the fixed planned budget and an assumed no-reallocation diagnostic treatment, the average first-stage method success probability is $0.80(0.75)+0.20(0.50)=0.70$, versus 0.50 when the physical-to-research uplift edge is disabled.

Conditional on qualified first-stage research, a new process recipe is accepted with probability 0.80, the corresponding physical service $K_1$ is installed with probability 0.90, and its two prespecified renewal events each succeed with probability 0.94. If all these subsequent stages are independent conditional on the stated parent events, the joint success probabilities are

**Equation (11): first-generation physical-to-science conversion (synthetic).** Write

$$
\alpha_1=0.80(0.75)+0.20(0.50)=0.70.\qquad\text{(11a)}
$$

$$
p_{q_1,\mathrm{on}}=\alpha_1(0.80)(0.90)(0.94^2)=0.4453344.\qquad\text{(11b)}
$$

$$
p_{q_1,\mathrm{off}}=0.50(0.80)(0.90)(0.94^2)=0.3180960.\qquad\text{(11c)}
$$

Here $\mathrm{on}$ and $\mathrm{off}$ refer only to enabling versus disabling the instrument-to-research *uplift*, not to whether the research subsystem exists.

The difference $0.1272384$ is a **constructed model implication** conditional on all fixed input assumptions. It is not a measured effect of instrument building and does not identify a general feedback parameter. Both numbers fall below a 0.60 certification threshold, so this example must not be mixed with the threshold-PASS language of Section 6.1. Its purpose is to display the missing causal link and quantify what a matched edge-switch-off would compare.

A second direction completes the temporal loop in the proposed *design*. Conditional on reaching installed and renewed $K_1$, that physical system fabricates a further research instrument $I_2$ with probability 0.80. If $I_2$ works, the next research-method evaluation succeeds at 0.70; otherwise, **the baseline method can still succeed at 0.55**. These are hypothetical conditional probabilities, not measured rates. A subsequent qualified recipe is accepted at 0.80, a $K_2$ service is installed at 0.90, and the second successor service passes two additional renewal checks at $0.94^2$. Under conditional independence, the probability of the full two-round event with both physical-to-research uplifts is

**Equation (12): second-round conditional method and full path (synthetic).**

$$
\alpha_2=0.80(0.70)+0.20(0.55)=0.67.\qquad\text{(12a)}
$$

$$
p_{q_2,\mathrm{on}}=0.4453344(0.67)(0.80)(0.90)(0.94^2)
=0.189823182345216.\quad\text{(12b)}
$$

Disabling only the *second* instrument-to-research uplift gives method success 0.55 whether or not $I_2$ was built, and yields $0.155825000432640$ for the full path. Disabling both physical-to-research uplifts, while retaining otherwise admissible baseline research and physical installation, gives $0.111303571737600$. All three values retain the same subsequent qualification (0.80), installation (0.90), and two renewal (0.94 each) probabilities. Multiplying $0.80\times0.70$ alone would incorrectly discard instrument-failure paths that still have baseline research success 0.55; the correct conditional average is $0.80(0.70)+0.20(0.55)=0.67$. These numbers are deliberately transparent and artificial. A four-renewal-cycle $q_2$ interpretation must set $T$ long enough to include both round-specific two-renewal sequences, instrument fabrication, method tests, qualification and installation deadlines; $T$ may not be inherited unchanged from the two-renewal example in Section 6.1.

The causal arrows in this constructed design are now genuinely bidirectional in the assumed transition mechanism, but **the bidirectionality has not been observed or estimated**. Real research would need a matched intervention in which improvements to instruments and physical experimental throughput are recorded separately from added computing, easier scientific tasks, new human expertise, extra monetary budgets and evaluator leakage. It must show a validated $K_1\to H_2$ uplift, not infer it from installed hardware. It must subsequently verify an incremental, physically maintainable $K_2$, account for failures correlated across experiments and suppliers, and compare net economic value after instrument, verification and opportunity costs. The only warranted conclusion today is that the framework can *represent and preregister* this experiment.

## 6.4 A strong dynamic baseline that reproduces the constructed choice

A rigorous test of RPC's proposed practical value cannot compare it only with a rule that ranks current cash flows and ignores the future. Give a standard finite-horizon dynamic optimization model exactly the same technology, probability law, rights, scientific-method states, budget, risk convention, terminal payoff and observation information used above. Let actions choose A or B at the initial node, and let later observations update the state according to the same serial success gates; there is no salvage/reallocation value from a failed stage in this minimalist toy case because none was stipulated in the source decision problem. The Bellman evaluation at time zero is then

$$
V_0(s_0)=\max\{130,\;105+0.90\,\Pr(q_N\mid s_0,\pi_B)\,50\},\qquad\text{(13)}
$$

with the same risk and revenue contracts. It chooses B for $p_N=0.6043824$ and A for $p_N=0.4532868$. This is **exact equality of choices**, not a disadvantage of dynamic optimization. A state-rich production-network model or appropriately specified real-options optimizer can encode the same option, renewal and authorization constraints. No decision-theoretic superiority of RPC-CP01 is established by the toy inversion against the thinner current-only benchmark.

Three baselines should therefore be distinguished in empirical follow-up. A *thin operational* baseline records current yield, capacity and expected short-run cost but omits successor renewal and qualification. A *state-rich dynamic* baseline uses the same observed states, conditional distributions, instruments, constraints and objective as RPC-CP01. A *realistic decision-process* baseline captures what an actual team can measure and afford under fixed acquisition effort, including missing inputs, latent correlations, late legal information and verification overhead. The fully informed baseline provides the logical equivalence check; the realistic baseline, under equal information and decision cost accounting, tests whether a common protocol reduces actual omissions or improves calibration.

A fair randomized or matched comparison would fix decision cases, participant expertise, access to source evidence, numerical solver, allowed time, and observed data, then compare: unrecognized successor failures; false qualification; probability calibration error; net realized choice value; time-to-decision; and fully loaded evidence collection/review cost. If the protocol needs more expensive evidence to reach the same decision, that cost must count against its benefit. If the comparator uses less detail by design, its disadvantage must be attributed to omitted state, **not** to an inability of existing economic mathematics to represent it. An actual strong-baseline empirical study has **not** been run.

## 6.5 A decision protocol for an autonomous research or industrial manager

A manager optimizing future productive capability should keep five accounting layers separate: qualified physical capital and renewal receipts; research capability $H$ on held-out difficulty-matched tasks; independently accepted knowledge $\Theta$; the dated path from knowledge to installed production; and organizational permissions/obligations. The manager should first assess the common sponsor objective and opportunity cost. A research project can have high long-run option value even if its first output cannot yet be installed, but it may not be counted as installed renewal capacity until physical engineering and resource gates pass. Conversely, pressing all effort into immediate production may reduce future feasible options by consuming sole-source tooling or experiment windows.

For physical production, the protocol asks whether an output is one-time, repeatable, repairable or replaceable; whether necessary materials can be lawfully delivered at the right time; whether the next generation retains sufficient tooling and knowledge; and how correlated failures limit the use of redundant supply. For capital allocation, it asks whether spending produces usable productive capital, supports a qualified option, or merely finances an internal transfer. The expected financial return can be different from the physical option frontier. A larger attainable set is neither an unconditional investment recommendation nor an unconditional social benefit.

An operational evidence package would record each event with timestamp, responsible actor, source measurement, verifier, system configuration, material flows, net cash flows, access rights, consent/version status, target service, relevant probability estimate, correlation group, and failed counterfactual. If a mechanism has not been observed, write **NOT OBSERVED** instead of drawing a future-effect arrow as established. If the risk bound is too weak to certify $p\ge p_{\mathrm{report}}$, report the interval and the failed gate. A method change can be scientifically credible yet economically unprofitable; both facts belong in the decision record.

## 6.6 Preregistered empirical protocol and stopping rules

A useful first empirical design is a matched two-configuration renewal comparison in one domain with accessible material bills and qualified scientific methods. Preregister: $Q_0$, essential service floor, supplier boundary, budgets and time, actual generation events and replacement criteria, source of calibrated joint probabilities, risk interval, autonomy treatment, organizational authority, data collection costs and intended dynamic comparator. Record positive and negative episodes, not just successful replacements. Include at least one time-infeasible but graph-reachable recipe and one individually feasible but jointly infeasible service bundle to test false-certification resistance.

A stronger two-way study varies a verifiably produced research instrument $I_1$ and measures downstream $H_1$ against matched held-out scientific tasks, then qualifies/install $K_1$, then tests a $K_1$-enabled $H_2$ and installed $K_2$. Controls must prevent larger compute budgets, task simplification, hidden external expertise, redefined service units or cherry-picked stopping times from being called an endogenous rise in scientific ability. The intervention should retain exactly the same resource boundary or explicitly account for the opportunity cost of the control allocation, and it should test correlation and negative transfer rather than only mean improvements.

Finally, the observation program should be allowed to fail. Abandon a specific mechanism when independent renewal cannot be demonstrated, the apparent uplift disappears under matched budget/difficulty, material or permitting bottlenecks block installation, a complete dynamic model subsumes the claimed result without remaining diagnostic value, or verification cost exceeds the expected decision benefit. These are case-specific stop conditions, not an automatic instruction to abandon the broader machine-economy research program.

## 6.7 A dated two-renewal *synthetic* joint-policy witness

A five-stage probability calculation by itself lacks the scheduled material, machinery and legal facts required by Equation (1). An executable **finite synthetic countermodel** therefore defines one fixed policy and a complete list of actions. This is a specification check, not a physical factory experiment. The contracted service network comprises essential service $e$ and newly qualified precision service $q_N$, both delivered jointly at two full-machine renewal checkpoints $t=3$ and $t=6$; $e$ is also delivered at $t=0$. It assumes an initially operational F0 and an independent laboratory, a single operating machine with two slots per period, manufacturing of F1 by F0 and F2 by F1, and time-limited operating/fabrication permits.

The dated execution ledger is recorded here as one step per line (material, energy, and cash units are kept separate):

- **t=0, F0:** deliver essential service $e$; use material 1, energy 1, cash 5.
- **t=1, LAB:** independently qualify research method and production recipe; use material 1, energy 1, cash 10.
- **t=2, F0:** fabricate complete successor F1; use material 3, energy 3, cash 20.
- **t=3, F1:** commission F1, retire F0, jointly deliver $e$ and $q_N$; use material 2, energy 3, cash 14.
- **t=5, F1:** fabricate complete successor F2; use material 3, energy 3, cash 20.
- **t=6, F2:** commission F2, retire F1, jointly deliver $e$ and $q_N$; use material 2, energy 3, cash 14.
- **Total:** material **12**, energy **14**, cash **83**.


The starting typed endowments are $(15\text{ material},17\text{ energy},103\text{ cash})$ and the program reserves $(3,3,20)$ at the end solely for a *possible next* manufacturing action. The later spare right and physical capacity are predeclared but **no third renewal is asserted**. Each action checks physical balance before consumption, production slots, operating machine lineage, knowledge qualification, permissions and deadlines. Necessary linked resources and costs are not hidden inside a scalar proxy. Negative runs independently revoke a fabrication permit, remove one unit of each escrow resource, reduce F1's two-slot capacity, shorten the deadline, or cancel the future fabrication right; all prevent certification. The same active production unit must deliver both services at each checkpoint. Conditional probability from the separately assumed five-stage transition model gives 0.6043824 for completing the constructed all-success path, but none of the event rates, material coefficients, equipment designs, legal rights or safety standards are measured industrial facts.

A legitimate **field certificate is therefore explicitly not issued**. Even a software-verified scheduled witness is *sound only relative to the input transition, physics and authority model*. Outside-support conditions and unresolved material/permit provenance return UNKNOWN. The witness demonstrates internal consistency under stipulated rules; it does not close the gap to actual industrial evidence.

## 6.8 A fair dynamic benchmark and a *costed* test of evidence acquisition

A separate five-stage finite-horizon synthetic decision (not the original 130/105 revenue case) permits a research program to stop after failed qualification, inspect a GOOD/BAD site signal, and choose NORMAL or HARDEN installation before two renewals. The discount-adjusted terminal reward is 126 and all costs, conditional probabilities, budget ceilings, salvage and site observation are supplied **identically** to both a conventional state-rich Bellman optimizer and an RPC-style assessor. Backward induction yields $V_B=35.27678656$, chooses NORMAL at a GOOD site and HARDEN at a BAD site, versus $V_A=30$. The fully informed conventional optimizer selects exactly the same policy. Hence there is **no mathematical optimization gain** to assign to the RPC name.

The candidate added contribution is deliberately limited to *how missing and contestable evidence is surfaced before a dynamic optimization*, not what an optimizer can express with complete information. A valid value claim must compare **equal evidence access** and **full acquisition/validation cost**. The following preregistration design is part of the proposed method, not a completed experiment:

1. Assemble independently verified cases with industrial service renewal, qualification, dated production inputs, rights and failure outcomes; classify missing data as UNKNOWN instead of treating absence as success. Establish data rights, confidentiality and an external ground-truth adjudication plan before any live testing.
2. Randomize or counterbalance review workflows across matched cases and assessors. Both arms receive identical source packets, query rights, general-purpose calculation tools, optimizer capabilities, processing time allowances and goal/risk definitions. The sole treatment is compulsory use of RPC-CP01's typed generation/qualification/permission checklist versus the assessor's strongest unrestricted standard review workflow.
3. Blind an independent external panel to the workflow, and adjudicate joint renewability only from verified physical and rights records. The primary endpoint is *false positive renewable-capability certifications per eligible adjudicated case*, with UNKNOWN coverage separately reported. Secondary endpoints are false negatives, prediction calibration, net decision value under the **same** objective, review hours, evidence acquisition/verification cost and auditability.
4. An analytical standard dynamic program with **the same complete states** is a parity control; comparisons against a weaker present-cash-only score are illustrative and cannot support superiority. Include the strongest existing viability/model-checking certificate workflow as a second technical comparator, not merely an unstructured spreadsheet.
5. Count all extra measurement, data licensing, human review, external verification, rework and opportunity costs. Preregister a net-value criterion and conservative uncertainty intervals; do not declare success for a trivial reduction in false certifications if the protocol's total verification cost exceeds expected avoided loss.
6. Stop or downgrade the specific RPC novelty claim if the strongest comparator is equal or better at lower total cost, if the observed agreement cannot be independently adjudicated, if case selection is contaminated, or if reviewers' competence/evidence differs. Sample size and statistical power must be determined from pilot base rates and a defined economically meaningful minimum effect, not invented ex ante from these toy calculations.

The protocol operationalizes an *economics-of-evidence* question specific to intergenerational physical-and-scientific production. Its effectiveness and academic distinctiveness **remain unmeasured**. Neither synthetic counterexamples nor verified arithmetic should be interpreted as evidence that this comparative field experiment has succeeded.

# 7. Academic Contribution, Limits and a Cumulative Research Programme

## 7.1 A bounded scholarly contribution and its relation to prior art

The contribution is a **specific measurement architecture** for the intergenerational renewal of *joint* productive services under coupled scientific, physical and organizational constraints. Its components are not claimed to be original in isolation. Von Neumann (1945) studies expanding systems of production; Romer (1990) models endogenous knowledge; Acemoglu and Azar (2020) study endogenous production networks; Trammell and Korinek (2026) and Davidson et al. (2026) directly analyze automated production and research feedback. Doyen and De Lara (2010) show stochastic viability can be computed through dynamic programming, and Baier, Chau and Klüppelholz (2025) provide checkable certificates for multiobjective MDP specifications. These works prevent claims to mathematical priority for recursion, viability, feedback networks or machine-checkable witnesses.

The proposed addition is the **economic unit of assessment and its evidence interface**: an intergenerational production *configuration* must be supported by a common adapted policy, simultaneous service obligations, generation-specific replacement, independent research qualification, real input and time ledgers, and enforceable permissions. Section 1 defines this object; Section 3 makes its evidence contract operational; Section 6 applies it to a reproducible example and explicit adverse cases. Proposition 1 documents a false inference from separate service feasibility to a joint feasible bundle; Proposition 2 documents a false inference from current accounting aggregates to intergenerational renewal. They apply familiar feasibility and information principles rather than introducing new foundational mathematical results.

The analytical output is **complete relative to its declared conceptual and synthetic scope**: a defined estimand, auditable data requirements, counterexamples, a falsifiable synthetic positive witness, dependence-sensitive decision bounds, and parity with a strong state-rich optimizer. The protocol does not claim to be a better optimizer or to have generated a real scientific discovery, a self-reproducing industrial system, or an empirically superior audit. A further practical contribution would require a comparative field study; the absence of such evidence limits what can be concluded here but does not invalidate a conceptual-methodological definition.

## 7.2 Operational boundaries and falsification conditions

No model here assumes machine consciousness, suffering, terminal preferences, legal personhood, self-generated objectives, autarkic production, universal markets or unlimited growth. A human sponsor may retain ultimate authority while an AI operates under a bounded delegation. Human-run organizations may make the same dynamic decisions with the same information. Likewise, centralized coordination, federated production and market exchange are competing institutional possibilities, not inevitable phases in machine evolution.

A growth inference fails when materials or energy cannot be supplied on time, complementary equipment cannot be renewed, scientific qualification does not survive blinded transfer tests, the organization cannot lawfully deploy a discovered process, the full opportunity cost overwhelms expected added value, or a model's alleged gain disappears against an equally informed dynamic baseline. A physical capability claim must report UNKNOWN when critical rights, safety or measurement records are unavailable. In particular, the synthetic witness does not establish a real factory's thermodynamic, metallurgical or safety feasibility.

Expanding a technical opportunity set need not improve welfare. The objective and valuation owner, distribution of benefits, environmental costs, concentrated power, safety, and human control must be evaluated separately. Gross internal machine-to-machine payments, patent counts, compute spending and financial asset-price gains are not physical additions to reproducible productive capital.

## 7.3 What belongs to later papers—and does not count as a result here

Deriving a sector-specific asymptotic growth law would require calibrated production functions, replacement times, complementarity and capital constraints. Identifying a true reciprocal $K	o H	o\Theta	o K$ effect would require matched experimental controls and independently confirmed physical implementation. Estimating machine-autonomy effects would require variation in decision frequency, latency, delegation, available information and costs while holding the underlying mandate fixed. Explaining endogenous organizations would require actors' incentives, entry/exit, rights, bargaining and a solved selection model. These are separate results, neither implied by the current framework nor prerequisites to presenting its bounded conceptual object.

## 7.4 The next empirical falsification test

To test the practical incremental value of RPC-CP01, investigators can compare it against the strongest available conventional multidisciplinary review and existing viability/model-checking workflows under **identical raw information, tools, optimizer access, authorizations, time and objectives**. Independent, blinded engineering adjudication must establish ground truth. The primary endpoint is false-positive two-renewal certification among adjudicated cases, accompanied by the UNKNOWN denominator. Secondary outcomes include false negatives, calibration, monetary decision regret, verification time and total data/measurement/expert cost. The RPC claim of practical superiority should be rejected if its benefit disappears after equal access and full costs, or if ground truth cannot be established. Such an experiment is proposed rather than reported. It permits the methods hypothesis to fail cleanly without reopening the conceptual definition indefinitely.

# Conclusion

When a machine-operated production system constructs, repairs or improves the capabilities available to its successors, current output alone is an incomplete description of its economic state. Yet capital reproduction, technological innovation and economic coordination are already subjects of extensive theory. The specific task addressed here is narrower and measurable: determine which productive **joint service configurations** can survive two or more actual renewals under a common observation-adapted plan, with dated real inputs, valid research methods and enforceable rights.

Recursive productive capacity is proposed as an intergenerational evidence contract for that task. Its outputs are separate from the one-shot feasibility set, present accounting wealth, scientific publication counts and final social desirability. The two counterexamples reveal what individual feasibility claims and aggregate accounts can conceal; the synthetic witness shows how a joint renewal certificate can be constructed and falsified inside a declared model. The investment example separates reached-history conditional probabilities from latent-event marginals and makes ambiguous economic choices visible when dependence is unknown. The equal-information Bellman benchmark reaches the same optimum, as a correct dynamic model should.

The conceptual foundation therefore supports a precise, defensible question rather than a new universal growth law. Its potential practical benefit is improving cross-disciplinary evidence and avoiding false intergenerational claims at acceptable cost. That benefit remains subject to external measurement; evidence against it would revise the recommended protocol, not justify overstating the result. Subsequent studies can build independently on the present definitions to investigate real material renewal, recursive science, organizational evolution, capital allocation and the broader machine economy.

# Research transparency and declarations

**Study type and data.** This article is conceptual and methodological. All numerical probabilities, prices, inventories and equipment recipes are synthetic. No human participants, personal records, animal subjects, commercial customer data or real industrial runs were collected for this study. The accompanying reproducibility code checks arithmetic and the declared finite synthetic models, not external industrial truth.

**Generative AI assistance.** OpenAI ChatGPT was used to support literature discovery, conceptual drafting, mathematical consistency checks, synthetic-code development and manuscript preparation. Generated material and references require verification by the named human author, who retains responsibility for the submitted work; AI tools are not authors.

**Code and reproducibility.** A separately provided computational supplement contains the formulas, finite test cases and numerical check outputs. Its execution does not imply scientific qualification of empirical model parameters.

# References

Baier, C., C. Chau, and S. Klüppelholz (2025). “Certificates and Witnesses for Multi-Objective Queries in Markov Decision Processes.” *Performance Evaluation* 168: 102482. https://doi.org/10.1016/j.peva.2025.102482.

Chatterjee, K., T. Quatmann, M. Schäffeler, M. Weininger, T. Winkler, and D. Zilken (2025). “Fixed Point Certificates for Reachability and Expected Rewards in MDPs.” *TACAS 2025*, LNCS 15697: 130–151. https://doi.org/10.1007/978-3-031-90653-4_7.

Doyen, L., and M. De Lara (2010). “Stochastic Viability and Dynamic Programming.” *Systems & Control Letters* 59(10): 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008.

Funke, F., S. Jantsch, and C. Baier (2020). “Farkas Certificates and Minimal Witnesses for Probabilistic Reachability Constraints.” *TACAS 2020*, LNCS 12078: 324–345. https://doi.org/10.1007/978-3-030-45190-5_18.

Puterman, M. L. (1994). *Markov Decision Processes: Discrete Stochastic Dynamic Programming*. John Wiley & Sons.

Acemoglu, D., and P. D. Azar (2020). “Endogenous Production Networks.” *Econometrica* 88(1): 33–82. https://doi.org/10.3982/ECTA15899.

Alonso, R., W. Dessein, and N. Matouschek (2015). “Organizing to Adapt and Compete.” *American Economic Journal: Microeconomics* 7(2): 158–187. https://doi.org/10.1257/mic.20130100.

Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser, Boston.

Brynjolfsson, E., and Z. Hitzig (2026). “AI’s Use of Knowledge in Society.” In *The Economics of Transformative AI*, University of Chicago Press / NBER chapter. https://www.nber.org/books-and-chapters/economics-transformative-ai/ais-use-knowledge-society.

Davidson, T., B. Halperin, T. Houlden, and A. Korinek (2026). “When Does Automating AI Research Produce Explosive Growth? Feedback Loops in Innovation Networks.” NBER Working Paper 35155. https://doi.org/10.3386/w35155.

Dixit, A. K., and R. S. Pindyck (1994). *Investment under Uncertainty*. Princeton University Press. https://doi.org/10.2307/j.ctt7sncv.

Garicano, L. (2000). “Hierarchies and the Organization of Knowledge in Production.” *Journal of Political Economy* 108(5): 874–904. https://doi.org/10.1086/317671.

Hordijk, W., S. Kauffman, and R. Koppl (2023). “Emergence of Autocatalytic Sets in a Simple Model of Technological Evolution.” *Journal of Evolutionary Economics* 33(5): 1519–1535. https://doi.org/10.1007/s00191-023-00838-2.

Jones, C. I. (2026). “AI and Our Economic Future.” *Journal of Economic Perspectives* 40(3): 3–22. https://doi.org/10.1257/jep.20261505.

Romer, P. M. (1990). “Endogenous Technological Change.” *Journal of Political Economy* 98(5, Part 2): S71–S102. https://doi.org/10.1086/261725.

Siggelkow, N., and D. A. Levinthal (2003). “Temporarily Divide to Conquer: Centralized, Decentralized, and Reintegrated Organizational Approaches to Exploration and Adaptation.” *Organization Science* 14(6): 650–669. https://doi.org/10.1287/orsc.14.6.650.24840.

Trammell, P., and A. Korinek (2026). “Economic Growth Under Transformative AI.” *Annual Review of Economics* 18: 589–611. https://doi.org/10.1146/annurev-economics-051624-061002.

von Neumann, J. (1945). “A Model of General Economic Equilibrium.” *The Review of Economic Studies* 13(1): 1–9. https://doi.org/10.2307/2296111.

Weitzman, M. L. (1998). “Recombinant Growth.” *The Quarterly Journal of Economics* 113(2): 331–360. https://doi.org/10.1162/003355398555595.

**Reference-status note:** The 14 inherited references plus five direct methodological comparators are tracked by source/DOI; a full-text theorem-by-theorem and implementation-level equivalence audit has **not** been completed. The RT-20/review item 15 literature gate remains open.

# Appendix A. Formal Object and Claim Register

**RPC-C01 — Successor-capability correspondence.** Equation (1) is a policy-indexed, at-least-two-generation probability-qualified candidate definition with a common joint service witness. Its existence and properties have not been established by a general theorem.

**RPC-O01 — One-shot feasibility.** Equation (1a) makes a single delivered output distinguishable from renewable productive configurations.

**RPC-E01 — Dated event.** The event $E_T^{(g)}$ requires predeclared renewal checkpoints, essential-service viability, common policy, resources, permissions and joint feasibility. A successful hindsight path does not prove ex ante qualification.

**RPC-P01 — Physical accounting.** Equations (4), (4a) and (5) distinguish flow feasibility, machine capacity and mutually exclusive asset states. They are not a complete industrial simulator.

**RPC-S01 — Research evidence.** Calibrated research ability $H$, qualified knowledge $\Theta$ and installed physical assets $K$ are separate evidence classes; candidate hypotheses are not physical production.

**RPC-I01 — Mechanism identification.** The five-gate illustrative investment chain is an AND-gate; a real two-way feedback claim requires a measured instrument-to-science and science-to-capital cycle.

**RPC-M01 — Institutions.** Permissions, information and transition costs may alter $U$ and $\Psi$; their presence does not demonstrate endogenous equilibrium.

**RPC-R01 — Reporting and revenue gates.** The $0.60$ reporting criterion is not a default legal sales restriction or revenue-recognition rule.

**RPC-B01 — Strong baseline.** A full-information dynamic optimizer with identical payoff and state chooses the same plan in the constructed case.

**RPC-X01 — Reciprocal research design.** Equation (11)–(12) describes a stipulated two-way mechanism, not observed machine research or productivity compounding.

# Appendix B. Reproducible Numerical Audit

**Investment-case inputs.** Five reached-history *conditional* event probabilities: 0.90, 0.80, 0.95, 0.94 and 0.94. The serial joint probability by the chain rule is 0.6043824 (without requiring unconditional independence). Timely clearance is 0.75, reducing joint success to 0.4532868. Current net values A = 130 and B = 105; conditional terminal net value 50 and **total two-period terminal discount** 0.90. Exact expected values are 132.197208 and 125.397906. Conditional-value indifference thresholds are about 45.96060007336 and 61.28080009781 respectively.

**Alternative latent-event marginal sensitivity; not the selected serial model.** Hypothetical method and recipe *unconditional potential-event* marginals 0.90 and 0.80 imply an admissible joint range 0.70 to 0.80, not necessarily 0.72. Keeping later gates independent, joint success of the full service ranges 0.587594 to 0.671536. Its nominal 0.60 **report qualification** therefore fails the robust lower-bound check. Corresponding expected monetary objectives under the report-only contract range 131.44173 to 135.21912. These are bounding calculations under stipulated marginals, not confidence intervals from data.

**Two-way hypothetical path.** A first physical instrument succeeds at 0.80, changing held-out research success from 0.50 to 0.75 when available. The first qualified production path with downstream probabilities 0.80, 0.90 and $0.94^2$ has modeled success 0.4453344, versus 0.3180960 if that instrument's research uplift is disabled. A second physical instrument with success 0.80 improves further research from 0.55 to 0.70, followed by 0.80 recipe qualification, 0.90 installation and $0.94^2$ renewal. Full second-round success is **0.189823182345216**; disabling only the second research uplift yields **0.155825000432640**; disabling both yields **0.111303571737600**. These are constructed and require the stipulated conditional independence. The second-stage instrument failure branch is *not* assigned zero research success: its baseline is 0.55, so the correct weighted method success is $0.80(0.70)+0.20(0.55)=0.67$. A separate script in the revision package verifies all decimal operations.

**Equipment-state check.** One working mill fails (moves OP → FAILED), then is retired (FAILED → RETIRED), while a replacement is installed (NEW → OP). At completion only one operational mill exists, not two; accounting depreciation does not cause an additional count reduction.

# Appendix C. Minimum Measurement Contract

**Baseline.** Register the sponsor objective, true initial machine inventory and condition, research-task difficulty, materials and power availability, finances, external supplier boundary, service specification, verification ownership and dates.

**Time and physical witness.** Record ordered input and output availability at each physical event; part grades and delivery time; instantaneous power and total energy; machine reservation and maintenance windows; renewal-event timestamps; service-floor and failure receipts.

**Scientific witness.** Record blinded or contamination-controlled held-out tasks and budgets, independently validated method performance, accepted claims, retractions, ability transfer, actual instrument improvements, installation receipts, and negative tests.

**Institutional and economic witness.** Record what the operator could observe at decision time, permissions and obligations, legal actor, actual contract and revenue rules, cross-organizational handoff delays, common-cause failures and real cost of duplicate verification.

**Comparators and stopping.** Use a matched state-rich dynamic optimizer and an actually available constrained practical baseline. Measure false certification, risk calibration, net decision value and evidence cost. A failed renewal or a method uplift erased by matched controls must remain a negative result. External independent mathematical and bibliographic review remains outstanding.

# Appendix D. Prior-Art Comparison and Claim Boundaries

The following comparisons state the closest *conceptual* precedents and the narrower additional measurement work proposed here. They are not a claim of a complete systematic review or theorem-level priority search.

**Capital reproduction and innovation.** Von Neumann (1945) and Romer (1990) address expanding productive systems and endogenous technological knowledge. This paper does not claim discovery of either mechanism; it specifies a joint, dated successor-service renewal test with independent research qualification.

**Production networks and automated growth.** Acemoglu and Azar (2020) analyze endogenous production networks. Trammell and Korinek (2026) and Davidson et al. (2026) directly treat automated production, research feedback and economic growth. This article neither derives a new explosive-growth threshold nor claims to be first to identify two feedback loops. Its narrower contribution is the separation of scientific qualification, material implementation, joint service renewal and economic value.

**Viability and dynamic choice.** Puterman (1994) and Doyen and De Lara (2010) supply established stochastic dynamic programming and probabilistic viability methods. The paper's use of a policy-dependent successor event is an application, not a new Bellman procedure. The additional output is a field-oriented evidence interface, including explicit UNKNOWN classifications.

**Checkable stochastic certificates.** Funke, Jantsch and Baier (2020), Chatterjee et al. (2025), and Baier, Chau and Klüppelholz (2025) already develop machine-checkable reachability and multiobjective certificates. This paper proposes a combined physical, scientific, contractual and organizational evidence contract rather than inventing formal verification certificates or multiobjective witnesses.

**Knowledge costs and organizational rights.** Garicano (2000), Alonso, Dessein and Matouschek (2015), and Brynjolfsson and Hitzig (2026) analyze coordination costs and alternative allocations of decision rights. Our framework treats these rights as time-indexed feasibility conditions; it does not claim a new market-emergence equilibrium or that decentralized production always wins.

The comparison rests on the cited works and verified bibliographic identities, with varying levels of access to full underlying texts. Editorial review may identify closer equivalents or request empirical evidence; neither completeness nor originality is asserted by bibliographic listing alone.

# Appendix E. Field Audit Template

An actual RPC claim can be evaluated by recording one row per relevant event with these minimum fields: `case_id`, `service_contract_version`, `policy_id`, `state_observed_at_decision`, `time`, `generation_id`, `service_id`, `required_service_overlap`, `material_in`, `material_out`, `energy_in`, `energy_out`, `equipment_identity`, `repair_or_retirement_event`, `experiment_id`, `independent_method_qualification`, `rights_and_permit_status`, `provider_and_failure_domain`, `cash_commitment`, `verifier_id`, `failure_reason`, `terminal_certification_status` and `unknown_fields`.

The minimal terminal states are `CERTIFIED_WITHIN_MODEL`, `NOT_CERTIFIED`, `UNKNOWN_CRITICAL_EVIDENCE` and `FIELD_VERIFIED` (the last only with real independently qualified records). A field-verification claim must not be inferred from the first three. This typed schema is a proposed reporting contract and can be adapted to sector-specific metrology and safety requirements.