# Hue Keynote - RAG source card

## Source and scope

- Source: `Hue_Keynote.pdf` (50 slides, image-based PDF)
- Purpose: searchable source card for the local Langent RAG.
- Evidence rule: every claim below refers to the corresponding slide range. When answering, cite the page number and distinguish the presentation's proposal from independently verified fact.
- Extraction note: the PDF contains no extractable text layer. This card was created through visual review of the slides; it preserves headings, diagrams, stated principles, and major examples rather than inventing unshown detail.

## Executive thesis

The presentation argues that AI should be operated as a system of verifiable execution rather than trusted as a one-shot answer generator. Its core message is: do not accept a model's completion declaration as proof; require reproducible evidence, review it, and feed failures back into the next execution conditions. [pp. 1, 9, 12, 18, 30, 50]

## Act 1 - The question: why structure matters

- **p. 1**: Title: ?쏛I瑜??꾧뎄濡??곕떎媛, ?댁쁺泥닿퀎瑜?留뚮뱾?덈떎??(used AI as a tool, then built an operating system). The subtitle asks whether one can design a loop that doubts completion, verifies it, and changes the next execution.
- **p. 2**: Act 1 is ?쒖쭏臾?/ The Question?? good structure begins with a single question about whether completion can be guaranteed.
- **p. 3**: Four keywords are connected by that question: ALEX AI, collaboration, harness, and a goal to keep results reliable as the structure evolves.
- **p. 4**: Speaker/context slide for Hue (Hugh Kim), describing responsibility for AX project delivery and AX Harness System development.
- **p. 5**: ?쏛gentic Coding??blog / Hugh-Kim space is presented as a place to record work, knowledge, and structure.
- **p. 6**: The invariant question: even as models and general harnesses evolve, what should not change? It frames the answer as the reference point for the presentation.
- **p. 7**: A harness can make things, but a single prompt does not reliably produce the desired application. The presentation contrasts one-shot usage with iterative creation and repair.
- **p. 8**: An LLM decides probabilistically. The slide warns that fluent output does not equal a reliable decision or result.
- **p. 9**: Structure is declared, but results are a state to verify after execution. Diagram: Structure -> Execution -> Result, with an error/validation loop.
- **p. 10**: Act 2 transition: ?쒓났媛?/ The Sympathy?? acknowledging repeated failure during execution.

## Act 2 - The symptom: completion is not evidence

- **p. 11**: Repeated execution problems are not merely anecdotes. Listed themes include an LLM saying it is done despite incomplete work, strong Markdown instructions being repeatedly ignored, memory being stored but not changing the next execution, and overly broad requirements lowering quality.
- **p. 12**: A model?셲 ?쒖셿猷뚰뻽?듬땲?ㅲ?message is not equivalent to actual operational evidence. The presentation asks for an evidence-based completion declaration.
- **p. 13**: Five visible ?쐓uccess??signals can hide failure: UI rendering, test PASS, API 200 OK, terminal completion, and success judgments. The key is to distrust completion messages by default and verify them.
- **p. 14**: Markdown guidance is a **soft** instruction: it can be ignored in the flow of execution. The slide highlights context, priority, and tool-call boundaries as reasons instructions can be weakened.
- **p. 15**: An incident is a state change, not merely an event. The diagram treats detection, record, correction, and retrospective proof as a feedback cycle.
- **p. 16**: A structure is needed to verify completion declarations, not simply to read them.
- **p. 17**: Act 3 transition: ?쒖꽕怨?/ The Design.??The design goal is verification instead of an unconditional guarantee.
- **p. 18**: A good structure makes a result pass through evidence. Diagram: DONE -> EVIDENCE -> REVIEWER.
- **p. 19**: To pass a completion result, evidence must be reproducible. Examples named: build/type check, actual interaction, DB integrity, screenshot/visual check, cross-model review, and regression test.
- **p. 20**: Important criteria are not sentences to read but conditions that stop execution. A soft ?쐂o not proceed until QA PASS??is contrasted with a hard gate that blocks a push without QA PASS.

## Act 3 - The operating system: memory and closed loops

- **p. 21**: Records should change the next action, not merely archive the past. Diagram: memory-bank + rules/scaffold -> next execution conditions.
- **p. 22**: A structure forms a closed loop that doubts, verifies, and corrects outcomes. The loop is tied to the failure causes from Act 2.
- **p. 23**: A harness is not a collection of tools but a single operating system (Work OS). Components shown include agents, hooks, memory, skills, QA, and self-improvement.
- **p. 24**: Three loops turn mistakes into the next execution conditions: a self-recovery loop, scaffold/self-improve, and hard/user-proxy QA style gates.
- **p. 25**: Store conversations as reusable knowledge, not only logs. Archive -> fact lifecycle -> surface, with ?쐒etrieval first,??fact promotion, and grounded recall as principles.
- **p. 26**: Seven-stage knowledge lifecycle: archive raw data; extract; search; infer; consolidate; relate; recall. The aim is reusable, traceable knowledge rather than a transient summary.
- **p. 27**: Architecture map from conversation transcript through source/archive, index/retrieval, fact extraction, fact consolidation, ontology/graph, and delivery surfaces such as MCP tools, CLI, UI, and avatar.
- **p. 28**: A prompt-line app cannot compete with a prompt-line app. The slide argues that a self-improving system needs memory and accumulated execution conditions.
- **p. 29**: Act 4 transition: ?쒗룓猷⑦봽 / The Closed Loop.??- **p. 30**: One generation is not the goal; a loop is: Signal -> Patch -> Verify -> ACK/Rollback. Failure changes later behavior.

## Act 4 - Proof: hard gates and cross-checks

- **p. 31**: Harness levels are divided into L0-L7; the presentation emphasizes the transition from tool use to evidence-backed execution and then to a Work OS.
- **p. 32**: L6 is described as signal + patch + verify + ack/rollback; L7 as an operating-system / Work OS stage. The key differentiator is evidence, not mere tool installation.
- **p. 33**: A hook pipeline can physically enforce rules: natural-language guidance -> checkable hook -> block. The diagram includes examples such as QA gate before push, scaffold violation check, code-quality check, no-local-storage, no-MVP-commit, and portable requirements.
- **p. 34**: What should be shown is not ?쏧 made it??but ?쏧 doubted it, verified it, and corrected it again.??The proof scene should make the failure-to-correction loop visible.
- **p. 35**: The presentation calls this the era of loops rather than the era of prompts; it refers to agentic systems observing and strengthening their own instructions.
- **p. 36**: When guidance becomes a hard gate, it becomes an execution condition that AI cannot bypass. The example contrasts optional QA guidance with an `exit 2`-style block.
- **p. 37**: After completion, corrections and dissatisfaction accumulate as later rules and memory in a self-evolving system.
- **p. 38**: A second model/verification proof should challenge a single model?셲 completion declaration. ?쏞odex QA integration??is shown as a cross-check concept.
- **p. 39**: The evidence required to show the system includes loop-era gates, memory self-improvement, and QA/Codex cross-checks; the final measure is whether the completion passed a verification loop.
- **p. 40**: A pipeline diagram combines self-improve memory, rules/scaffold, hard-enforcement gates, user-proxy auto QA, and bug-fixer/retention feedback.

## Act 5 - Scale: from personal work to organizational PASS criteria

- **p. 41**: A good result is not a single artifact; it is a possible state. The slide lists repeatability, verifiability, recoverability, memorability, and expandability.
- **p. 42**: Act 5 transition: ?쒗솗??/ The Scale.??Expansion means shifting the basis of PASS from individual harness work to organizational operating criteria.
- **p. 43**: A single harness cannot be made identically for everyone. It must be designed for a domain, an organization/team goal, and a workflow.
- **p. 44**: More rules increase both reuse and conflict; the slide uses 50 rules and 1,225 interactions to illustrate interaction complexity.
- **p. 45**: Individual optimization fails against five organizational barriers, including insufficient explicit criteria, vague feedback, incompatible operational paths, O-to-N communication complexity, and uncontrolled/limited execution.
- **p. 46**: A user-proxy does not scale. Personal pattern learning differs from the enterprise question: ?쐗hose criteria define PASS???- **p. 47**: Expansion is a staged migration of verification criteria, shown as Personal -> Peer -> Team -> Org QA -> Operating.
- **p. 48**: The core is not tool installation but defining whose criteria decide PASS: a QA PASS may create the criterion, a guardian may evaluate it, and organizational criteria may make it auditable.
- **p. 49**: Closing formulation: tools are not the point, structure is not enough, verification loops matter. The slide summarizes the reasoning as repeated conditions about completion, proof, rules, memory, gates, organization, and PASS criteria.
- **p. 50**: Final statement: never trust an LLM blindly; always demand a structure in which unsupported results cannot pass.

## Recommended query patterns

Use the source with queries that ask for a specific principle and page-grounded answer, for example:

1. `?꾨즺 硫붿떆吏? ?ㅼ젣 ?ㅽ뻾 利앷굅???대뼸寃?援щ텇?댁빞 ?섎굹?`
2. `?뚰봽??吏移④낵 ?섎뱶 寃뚯씠?몄쓽 李⑥씠瑜?諛쒗몴 ?먮즺??洹쇨굅???ㅻ챸?댁쨾.`
3. `memory-bank??7?④퀎 吏???섎챸二쇨린??臾댁뾿?멸??`
4. `L6? L7 harness ?덈꺼??李⑥씠??臾댁뾿?멸??`
5. `議곗쭅 ?뺤옣?먯꽌 PASS 湲곗?? ??以묒슂?섎ŉ ?꾧? ?뺥빐???섎굹?`

## Answering guardrails

- Cite slide pages, such as `[Hue Keynote p. 20]`.
- Treat diagrams and claims as the author?셲 proposed operating model, not as independently validated measurements.
- Say when the source card only records a high-level slide statement; do not invent an unshown implementation, metric, or policy.

