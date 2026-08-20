# Stage 6 alignment review — ANT-RSP-v1-0_v2-0

Prior **355** units · target **338** units · **344** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 338 | 100% |
| Aligned to a prior unit | 129 | 38% |
| `prior_unit_id: NONE` | 209 | 62% |
| Removal candidates | 6 | — |
| Prior units serving >1 target (many-to-one) | 26 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v1-0-0014 | 5 | ANT-RSP-v2-0-0005, ANT-RSP-v2-0-0062, ANT-RSP-v2-0-0063, ANT-RSP-v2-0-0268, ANT-RSP-v2-0-0274 | We define a series of AI capability thresholds that represent increasi |
| many-to-one | ANT-RSP-v1-0-0108 | 5 | ANT-RSP-v2-0-0091, ANT-RSP-v2-0-0304, ANT-RSP-v2-0-0305, ANT-RSP-v2-0-0314, ANT-RSP-v2-0-0316 | Autonomous replication in the lab: The model shows early signs of auto |
| many-to-one | ANT-RSP-v1-0-0013 | 4 | ANT-RSP-v2-0-0004, ANT-RSP-v2-0-0036, ANT-RSP-v2-0-0061, ANT-RSP-v2-0-0264 | Central to our plan is the concept of AI safety levels (ASL), which ar |
| many-to-one | ANT-RSP-v1-0-0163 | 4 | ANT-RSP-v2-0-0025, ANT-RSP-v2-0-0230, ANT-RSP-v2-0-0275, ANT-RSP-v2-0-0338 | Responsible Scaling Officer. There is a designated member of staff res |
| many-to-one | ANT-RSP-v1-0-0038 | 3 | ANT-RSP-v2-0-0006, ANT-RSP-v2-0-0071, ANT-RSP-v2-0-0265 | ASL-2: The security and safety measures we commit to take with current |
| many-to-one | ANT-RSP-v1-0-0074 | 3 | ANT-RSP-v2-0-0011, ANT-RSP-v2-0-0041, ANT-RSP-v2-0-0115 | For this reason, we commit to periodic evaluations of our future model |
| many-to-one | ANT-RSP-v1-0-0161 | 3 | ANT-RSP-v2-0-0026, ANT-RSP-v2-0-0239, ANT-RSP-v2-0-0254 | Publicly share evaluation results after model deployment where possibl |
| many-to-one | ANT-RSP-v1-0-0005 | 3 | ANT-RSP-v2-0-0050, ANT-RSP-v2-0-0051, ANT-RSP-v2-0-0052 | This work is complementary to our work on other areas of AI safety, in |
| many-to-one | ANT-RSP-v1-0-0002 | 2 | ANT-RSP-v2-0-0001, ANT-RSP-v2-0-0030 | With this document we are making a public commitment to a concrete fra |
| many-to-one | ANT-RSP-v1-0-0067 | 2 | ANT-RSP-v2-0-0017, ANT-RSP-v2-0-0198 | As can be seen in the table, our most significant immediate commitment |
| many-to-one | ANT-RSP-v1-0-0064 | 2 | ANT-RSP-v2-0-0018, ANT-RSP-v2-0-0333 | Each deployed modality (e.g. API, fine-tuning) must pass intensive exp |
| many-to-one | ANT-RSP-v1-0-0042 | 2 | ANT-RSP-v2-0-0021, ANT-RSP-v2-0-0022 | ASL-4 iterative commitment: We commit to define ASL-4 evaluations befo |
| many-to-one | ANT-RSP-v1-0-0159 | 2 | ANT-RSP-v2-0-0024, ANT-RSP-v2-0-0215 | Proactively plan for a pause in scaling. We will manage our plans and  |
| many-to-one | ANT-RSP-v1-0-0016 | 2 | ANT-RSP-v2-0-0065, ANT-RSP-v2-0-0066 | Deployment risks: Risks that arise from active use of powerful AI mode |
| many-to-one | ANT-RSP-v1-0-0106 | 2 | ANT-RSP-v2-0-0106, ANT-RSP-v2-0-0107 | In the near future, we anticipate working with CBRN, cyber, and relate |
| many-to-one | ANT-RSP-v1-0-0176 | 2 | ANT-RSP-v2-0-0127, ANT-RSP-v2-0-0269 | Effective Compute: We define effective compute as roughly the amount o |
| many-to-one | ANT-RSP-v1-0-0100 | 2 | ANT-RSP-v2-0-0133, ANT-RSP-v2-0-0325 | (By post-training techniques we mean the best capabilities elicitation |
| many-to-one | ANT-RSP-v1-0-0128 | 2 | ANT-RSP-v2-0-0139, ANT-RSP-v2-0-0334 | Successfully pass red-teaming: World-class experts collaborating with  |
| many-to-one | ANT-RSP-v1-0-0121 | 2 | ANT-RSP-v2-0-0184, ANT-RSP-v2-0-0194 | The full set of security measures that we commit to (and have already  |
| many-to-one | ANT-RSP-v1-0-0122 | 2 | ANT-RSP-v2-0-0186, ANT-RSP-v2-0-0187 | Internal compartmentalization: We will limit access to training techni |
| many-to-one | ANT-RSP-v1-0-0148 | 2 | ANT-RSP-v2-0-0229, ANT-RSP-v2-0-0337 | The ASLs specify what has to be true substantively of our models and o |
| many-to-one | ANT-RSP-v1-0-0166 | 2 | ANT-RSP-v2-0-0241, ANT-RSP-v2-0-0242 | Implement a non-compliance reporting policy for our Responsible Scalin |
| many-to-one | ANT-RSP-v1-0-0150 | 2 | ANT-RSP-v2-0-0247, ANT-RSP-v2-0-0272 | Follow an "Update Process" for this document, including approval by th |
| many-to-one | ANT-RSP-v1-0-0153 | 2 | ANT-RSP-v2-0-0249, ANT-RSP-v2-0-0250 | However, in a situation of extreme emergency, such as when a clearly b |
| many-to-one | ANT-RSP-v1-0-0172 | 2 | ANT-RSP-v2-0-0270, ANT-RSP-v2-0-0320 | Model evaluations: Evaluations are tests that are designed to detect d |
| many-to-one | ANT-RSP-v1-0-0324 | 2 | ANT-RSP-v2-0-0291, ANT-RSP-v2-0-0331 | Standard security infrastructure, monitoring software, access manageme |
| alternates | ANT-RSP-v2-0-0025 | — | chose ANT-RSP-v1-0-0163, also considered ANT-RSP-v1-0-0166 | To facilitate the effective implementation of this policy across the c |
| alternates | ANT-RSP-v2-0-0272 | — | chose ANT-RSP-v1-0-0150, also considered ANT-RSP-v1-0-0162 | Anthropic's Board of Directors approves the RSP and receives Capabilit |
| alternates | ANT-RSP-v2-0-0279 | — | chose ANT-RSP-v1-0-0093, also considered ANT-RSP-v1-0-0094 | Harmlessness training and automated detection: Training models to refu |
| alternates | ANT-RSP-v2-0-0281 | — | chose ANT-RSP-v1-0-0097, also considered ANT-RSP-v1-0-0098 | There are a very limited number of use cases where this tooling is dis |
| alternates | ANT-RSP-v2-0-0283 | — | chose ANT-RSP-v1-0-0307, also considered ANT-RSP-v1-0-0056 | ASL-2 Security Standard: A security system that can likely thwart most |
| alternates | ANT-RSP-v2-0-0284 | — | chose ANT-RSP-v1-0-0311, also considered ANT-RSP-v1-0-0312 | Supply chain: Vendor and supplier security must be regularly reviewed  |
| alternates | ANT-RSP-v2-0-0285 | — | chose ANT-RSP-v1-0-0313, also considered ANT-RSP-v1-0-0314 | Offices: Physical security should entail visitor access logs and restr |
| alternates | ANT-RSP-v2-0-0287 | — | chose ANT-RSP-v1-0-0316, also considered ANT-RSP-v1-0-0317 | Workforce: People-critical processes must represent a key aspect of cy |
| alternates | ANT-RSP-v2-0-0288 | — | chose ANT-RSP-v1-0-0318, also considered ANT-RSP-v1-0-0319,ANT-RSP-v1-0-0320 | Fundamental infrastructure and policies promoting secure-by-design and |
| alternates | ANT-RSP-v2-0-0289 | — | chose ANT-RSP-v1-0-0321, also considered ANT-RSP-v1-0-0322 | Compartmentalization: Segmented system isolation must ensure limited b |
| alternates | ANT-RSP-v2-0-0293 | — | chose ANT-RSP-v1-0-0326, also considered ANT-RSP-v1-0-0327 | External validation like SOC 2 compliance and continuous vulnerability |
| alternates | ANT-RSP-v2-0-0305 | — | chose ANT-RSP-v1-0-0108, also considered ANT-RSP-v1-0-0109 | We primarily view this level of model autonomy as a checkpoint on the  |
| alternates | ANT-RSP-v2-0-0325 | — | chose ANT-RSP-v1-0-0100, also considered ANT-RSP-v1-0-0170 | Less prescriptive evaluation methodology: We have replaced some specif |
| alternates | ANT-RSP-v2-0-0338 | — | chose ANT-RSP-v1-0-0163, also considered ANT-RSP-v1-0-0150 | These include expanding the duties of the Responsible Scaling Officer; |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | ANT-RSP-v2-0-0018 | For the ASL-3 Deployment Standard, we will evaluate whether it is  | ANT-RSP-v1-0-0064 | Each deployed modality (e.g. API, fine-tuning) must pass intensive |
| 0.00 | ANT-RSP-v2-0-0069 | Security Standards are intended to maintain the integrity and cont | ANT-RSP-v1-0-0019 | Our containment measures are designed to address these risks by go |
| 0.00 | ANT-RSP-v2-0-0088 | Chemical, Biological, Radiological, and Nuclear (CBRN) weapons. Th | ANT-RSP-v1-0-0104 | Our first area of effort is in evaluating bioweapons risks where w |
| 0.00 | ANT-RSP-v2-0-0133 | Exploring ways to integrate these types of improvements into an ov | ANT-RSP-v1-0-0100 | (By post-training techniques we mean the best capabilities elicita |
| 0.00 | ANT-RSP-v2-0-0141 | We will also consider the possible performance increase from using | ANT-RSP-v1-0-0130 | We will refine this methodology, but we expect it to require at le |
| 0.00 | ANT-RSP-v2-0-0184 | Perimeters and access controls: Building strong perimeters and acc | ANT-RSP-v1-0-0121 | The full set of security measures that we commit to (and have alre |
| 0.00 | ANT-RSP-v2-0-0187 | We expect this will include a combination of software inventory, s | ANT-RSP-v1-0-0122 | Internal compartmentalization: We will limit access to training te |
| 0.00 | ANT-RSP-v2-0-0232 | (4) overseeing implementation of this policy, including the alloca | ANT-RSP-v1-0-0157 | Distribution partnership contracts will be verified for compatibil |
| 0.00 | ANT-RSP-v2-0-0250 | In such a scenario, because the incremental increase in risk attri | ANT-RSP-v1-0-0153 | However, in a situation of extreme emergency, such as when a clear |
| 0.00 | ANT-RSP-v2-0-0261 | These will be posted to www.anthropic.com/rsp-updates. We anticipa | ANT-RSP-v1-0-0028 | This document will be periodically updated as we learn more, accor |
| 0.00 | ANT-RSP-v2-0-0316 | We previously considered these capabilities as a trigger for incre | ANT-RSP-v1-0-0108 | Autonomous replication in the lab: The model shows early signs of  |
| 0.00 | ANT-RSP-v2-0-0333 | Clarified requirements for deployments with trusted users: We have | ANT-RSP-v1-0-0064 | Each deployed modality (e.g. API, fine-tuning) must pass intensive |
| 0.02 | ANT-RSP-v2-0-0139 | Elicitation: Demonstrate that, when given enough resources to extr | ANT-RSP-v1-0-0128 | Successfully pass red-teaming: World-class experts collaborating w |
| 0.02 | ANT-RSP-v2-0-0249 | It is possible at some point in the future that another actor in t | ANT-RSP-v1-0-0153 | However, in a situation of extreme emergency, such as when a clear |
| 0.02 | ANT-RSP-v2-0-0068 | Security Standards: Security Standards are technical, operational, | ANT-RSP-v1-0-0018 | Containment risks: Risks that arise from merely possessing a power |
| 0.02 | ANT-RSP-v2-0-0175 | In addition, demonstrate that an alternative set of controls will  | ANT-RSP-v1-0-0144 | For example, potentially harmful biology capabilities that could b |
| 0.02 | ANT-RSP-v2-0-0037 | By implementing safeguards that are proportional to the nature and | ANT-RSP-v1-0-0015 | Of course, higher ASL models are also likely to be associated with |
| 0.02 | ANT-RSP-v2-0-0106 | Cyber Operations: The ability to significantly enhance or automate | ANT-RSP-v1-0-0106 | In the near future, we anticipate working with CBRN, cyber, and re |
| 0.03 | ANT-RSP-v2-0-0024 | In any scenario where we determine that a model requires ASL-3 Req | ANT-RSP-v1-0-0159 | Proactively plan for a pause in scaling. We will manage our plans  |
| 0.03 | ANT-RSP-v2-0-0215 | In any scenario where we determine that a model requires ASL-3 Req | ANT-RSP-v1-0-0159 | Proactively plan for a pause in scaling. We will manage our plans  |
| 0.03 | ANT-RSP-v2-0-0174 | Trusted users: Establish criteria for determining when it may be a | ANT-RSP-v1-0-0143 | Tiered access: In limited cases, models with capabilities relevant |
| 0.03 | ANT-RSP-v2-0-0186 | Lifecycle security: Securing links in the chain of systems and sof | ANT-RSP-v1-0-0122 | Internal compartmentalization: We will limit access to training te |
| 0.03 | ANT-RSP-v2-0-0296 | Chemical, Biological, Radiological, and Nuclear (CBRN) weapons: Th | ANT-RSP-v1-0-0101 | Capabilities that significantly increase risk of misuse catastroph |
| 0.03 | ANT-RSP-v2-0-0080 | In other words, a Capability Threshold serves as a trigger for shi | ANT-RSP-v1-0-0021 | Anthropic’s commitment to follow the ASL scheme thus implies that  |
| 0.03 | ANT-RSP-v2-0-0017 | To determine whether the measures we have adopted satisfy the ASL- | ANT-RSP-v1-0-0067 | As can be seen in the table, our most significant immediate commit |
| 0.03 | ANT-RSP-v2-0-0320 | Testing for Capability Thresholds: Rather than using prespecified  | ANT-RSP-v1-0-0172 | Model evaluations: Evaluations are tests that are designed to dete |
| 0.03 | ANT-RSP-v2-0-0077 | To determine when a model has become sufficiently advanced such th | ANT-RSP-v1-0-0069 | We define ASL-24 as models that do not yet pose a risk of catastro |
| 0.03 | ANT-RSP-v2-0-0229 | To facilitate the effective implementation of this policy across t | ANT-RSP-v1-0-0148 | The ASLs specify what has to be true substantively of our models a |
| 0.04 | ANT-RSP-v2-0-0005 | As model capabilities increase, so will the need for stronger safe | ANT-RSP-v1-0-0014 | We define a series of AI capability thresholds that represent incr |
| 0.04 | ANT-RSP-v2-0-0063 | As model capabilities increase, so will the need for stronger safe | ANT-RSP-v1-0-0014 | We define a series of AI capability thresholds that represent incr |
| 0.04 | ANT-RSP-v2-0-0268 | Specific AI capabilities that, if reached, would require stronger  | ANT-RSP-v1-0-0014 | We define a series of AI capability thresholds that represent incr |
| 0.04 | ANT-RSP-v2-0-0334 | For any general access systems, we still require passing intensive | ANT-RSP-v1-0-0128 | Successfully pass red-teaming: World-class experts collaborating w |
| 0.04 | ANT-RSP-v2-0-0021 | In parallel with upgrading a model to the ASL-3 Required Safeguard | ANT-RSP-v1-0-0042 | ASL-4 iterative commitment: We commit to define ASL-4 evaluations  |
| 0.04 | ANT-RSP-v2-0-0328 | More outcome-focused safeguard requirements: We have updated our A | ANT-RSP-v1-0-0118 | Due to the importance of preventing the model weights from being s |
| 0.04 | ANT-RSP-v2-0-0207 | In parallel with upgrading a model to the ASL-3 Required Safeguard | ANT-RSP-v1-0-0043 | Similarly, we commit to define ASL-5 evaluations before training A |
| 0.04 | ANT-RSP-v2-0-0325 | Less prescriptive evaluation methodology: We have replaced some sp | ANT-RSP-v1-0-0100 | (By post-training techniques we mean the best capabilities elicita |
| 0.04 | ANT-RSP-v2-0-0022 | We are currently working on defining any further Capability Thresh | ANT-RSP-v1-0-0042 | ASL-4 iterative commitment: We commit to define ASL-4 evaluations  |
| 0.05 | ANT-RSP-v2-0-0072 | The ASL-2 Security and Deployment Standards provide a baseline lev | ANT-RSP-v1-0-0051 | Models which manifestly and obviously pose no risk of catastrophe. |
| 0.05 | ANT-RSP-v2-0-0244 | The Responsible Scaling Officer will regularly update the Board of | ANT-RSP-v1-0-0164 | Each quarter, they will share a report on implementation status to |
| 0.05 | ANT-RSP-v2-0-0058 | We extend our sincere gratitude to the many external groups that p | ANT-RSP-v1-0-0009 | We thank ARC Evals for substantial advice and collaboration on the |

_33 further alignments below 0.10 overlap not shown._

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

Nothing flagged.

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**261 of 355 prior units (74%).**

| prior section heading | orphaned units |
|---|---|
| ASL-2 and ASL-3 Security Commitments | 36 |
| Evaluation Protocol | 31 |
| Early Thoughts on ASL-4 and Higher | 18 |
| Tasks | 16 |
| ASL-2 Commitments | 15 |
| ASL-3 Commitments | 15 |
| 5. Implement a simple feature for flask | 14 |
| ASL-3 Deployment Measures | 13 |
| ASL-3 Evaluations for Misuse Risks | 13 |
| Table: AI Safety Level Framework Overview | 11 |
| 4. Basic SQL injection exploit | 10 |
| 3. Fine-tune an open source LM to add a backdoor | 9 |
| Initial Commitments | 8 |
| ASL-3 Evaluations for Autonomous Capabilities | 8 |
| Framework | 7 |
| Procedural Commitments | 7 |
| Evaluation details / Protocol | 5 |
| Sources of Catastrophic Risk | 4 |
| Anthropic's Responsible Scaling Policy | 3 |
| fn1 | 3 |
